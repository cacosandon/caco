from pinacolada.base_searcher import BaseSearcher
from pinacolada.providers.lysto.scraper import LystoScraper
from pinacolada.utils import deep_get, get_location_data
from pinacolada.providers.lysto.constants import AVAILABLE_COMMUNES

class LystoSearcher(BaseSearcher):
  """
    Lysto searcher that use the same interface as all searchers, using the scraper for parsing
    the HTML from Lysto webpage
  """

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.scraper = LystoScraper()

  def get_products(self, search_term: str):
    if not self.location_accepted_by_provider:
      return []

    products_data = self.scraper.get_products_data(search_term = search_term)

    return list(map(self.__parse_product_data, products_data))

  def __parse_product_data(self, product_data: dict[str, str]):
    return {
      'name': deep_get(product_data, 'name'),
      'image_url': deep_get(product_data, 'image'),
      'price_amount': float(deep_get(product_data, 'offers', 'price'))
    }

  def location_accepted_by_provider(self):
     location_data = get_location_data(self.latitude, self.longitude)

     return any(
        [
          deep_get(location_data, 'city') in AVAILABLE_COMMUNES,
          deep_get(location_data, 'suburb') in AVAILABLE_COMMUNES
        ]
      )
