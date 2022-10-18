from pinacolada.base_clients import GraphqlClient
from pinacolada.utils import deep_get
from typing import Union, List

JOKR_BASE_URL = "https://api-prd-cl.jokrtech.com"

class JokrClient(GraphqlClient):
  """
    Client for getting Jokr App products information, retrieved via GraphQL.
  """

  def __init__(self):
    super().__init__(base_url = JOKR_BASE_URL)

  def get_hub_id_by_coordinates(self, latitude: str, longitude: str) -> str:
    """
      Gets Hub ID (kind of location area code)
    """

    query = """
      query HubByCoordinates($lat: String!, $lng: String!) {
        hubByCoordinates(lat: $lat, lng: $lng) {
          id
        }
      }
    """
    variables = { "lat": latitude, "lng": longitude }

    response = self.run(query, variables)
    return deep_get(response, 'data', 'hubByCoordinates', 'id')

  def search_products(self, search_term: str, hub_id: str) -> List[dict[str, str]]:
    """
      Searches products by a search string term and the Hub ID.
    """

    query = """
      query SearchProducts($searchTerm: String!, $hubId: String) {
        searchProducts(searchTerm: $searchTerm, hubId: $hubId) {
          products {
            sku
          }
        }
      }
    """

    variables = { "searchTerm": search_term, "hubId": hub_id }

    response = self.run(query, variables)
    return deep_get(response, 'data', 'searchProducts', 'products')

  def get_products_data(self, skus: List[str], hub_id: str) -> List[dict[str, Union[str, int]]]:
    """
      Gets products data based on SKUs and the Hub ID.
    """

    query = """
      query GetProductsData($productsSkus: [String!], $hubId: String!) {
        products(where: { sku_in: $productsSkus }) {
          name
          packshot1_front_grid {
            url
          }
          price(hubId: $hubId) {
            amount
          }
        }
      }
    """
    variables = { "productsSkus": skus, "hubId": hub_id }

    response = self.run(query, variables)
    return deep_get(response, 'data', 'products')
