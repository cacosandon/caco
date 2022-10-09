from abc import ABC, abstractmethod
from typing import Callable, List, Union
import requests
from bs4 import BeautifulSoup
from pinacolada.constants import SUCCESS_STATUS_CODE

class BaseHtmlScraper(ABC):
  REQUEST_HEADERS = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit"\
                  "/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
  }

  def __init__(self, search_url_builder: Callable[[str], str]):
    self.search_url_builder = search_url_builder

  def get_html_soup(self, search_term: str):
    search_url = self.search_url_builder(search_term)

    response = requests.get(search_url, headers=BaseHtmlScraper.REQUEST_HEADERS)
    if response.status_code != SUCCESS_STATUS_CODE:
      return

    return BeautifulSoup(response.text, 'html.parser')

  @abstractmethod
  def get_products_data(self, search_term: str) -> List[dict[str, Union[str, int]]]:
    """
      Uses the get_html_soup function to get the HTML parsed using BeautifulSoup4,
      and retrieves list of products in JSON format
    """
