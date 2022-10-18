from pinacolada.base_searcher import BaseSearcher
from pinacolada.providers.jokr.client import JokrClient
from pinacolada.utils import deep_get

class JokrSearcher(BaseSearcher):
  """
    Jokr searcher that use the same interface as all searchers, using the client for parsing
    the data
  """

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.client = JokrClient()

  def get_products(self, search_term: str):
    hub_id = self.client.get_hub_id_by_coordinates(
      latitude = self.latitude,
      longitude = self.longitude
    )

    if not hub_id:
      return []

    products = self.client.search_products(search_term = search_term, hub_id = hub_id)
    products_skus = list(map(lambda product: product['sku'], products))

    products_data = self.client.get_products_data(skus = products_skus, hub_id = hub_id)

    return list(map(self.__parse_product_data, products_data))

  def __parse_product_data(self, product_data: dict[str, str]):
    return {
      'name': deep_get(product_data, 'name'),
      'image_url': deep_get(product_data, 'packshot1_front_grid', 'url'),
      'price_amount': deep_get(product_data, 'price', 'amount')
    }
