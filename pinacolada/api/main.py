from fastapi import FastAPI, HTTPException
from pinacolada.api.types import Providers, Products
from pinacolada.api.metadata import TAGS_METADATA

from pinacolada.providers.jokr.searcher import JokrSearcher
from pinacolada.providers.lysto.searcher import LystoSearcher

AVAILABLE_PROVIDERS = {
  'jokr': JokrSearcher,
  'lysto': LystoSearcher
}

app = FastAPI(
  title = "🍍 PiñaColada",
  descripton = "Search for all products, all at once, while drinking a cold piña colada.",
  openapi_tags = TAGS_METADATA
)

@app.get("/", include_in_schema=False)
async def root():
    return { "message": "Welcome to 🍍 Piña Colada. Docs at /docs" }

@app.get("/providers", response_model=Providers, tags=["providers"])
async def providers():
    return { "providers": list(AVAILABLE_PROVIDERS.keys()) }

@app.get("/search_products/{provider}/{search_term}", response_model=Products, tags=["products"])
async def get_products(provider: str, search_term: str, latitude: str, longitude: str):
    if not provider in AVAILABLE_PROVIDERS:
      raise HTTPException(status_code = 404, detail = f"Provider '{provider}' not found")

    provider = AVAILABLE_PROVIDERS[provider](latitude = latitude, longitude = longitude)

    return { "products": provider.get_products(search_term = search_term) }
