from pinacolada.base_searcher import BaseSearcher
from pinacolada.providers.lysto.scraper import LystoScraper
from pinacolada.utils import deep_get

class LystoSearcher(BaseSearcher):
  """
    Lysto searcher that use the same interface as all searchers, using the scraper for parsing
    the HTML from Lysto webpage
  """

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.scraper = LystoScraper()

  def get_products(self, search_term: str):
    products_data = self.scraper.get_products_data(search_term = search_term)

    return list(map(self.__parse_product_data, products_data))

  def __parse_product_data(self, product_data: dict[str, str]):
    return {
      'name': product_data['name'],
      'image_url': product_data['image'],
      'price_amount': float(deep_get(product_data, 'offers', 'price'))
    }
