from abc import ABC, abstractmethod

class BaseSearcher(ABC):
  """
    Searcher that implements the interface for all stores searchers.
  """

  def __init__(self, latitude: str, longitude: str):
    self.latitude = latitude
    self.longitude = longitude

  @abstractmethod
  def get_products(self, search_term: str):
    """
      Get products that matches with the query 'search_term'. It returns a list of products, with
      the following interface:

      [
        {
          name: 'Some Product',
          image_url: 'some_image_url.xyz',
          price_amount: 9999
        }
      ]
    """

    pass
