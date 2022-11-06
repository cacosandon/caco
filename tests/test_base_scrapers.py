import pytest
from bs4 import BeautifulSoup
from typing import Callable, List, Union


from pinacolada.base_scrapers import BaseHtmlScraper

class TestBaseHtmlScraper:
  def setup_method(self):
    class SomeHtmlScraper(BaseHtmlScraper):
      def get_products_data(self, search_term: str) -> List[dict[str, Union[str, int]]]:
        return super().get_products_data(search_term)

    self.scraper = SomeHtmlScraper(
      search_url_builder=lambda query: f"https://example.com?q={query}"
    )

  @pytest.fixture(autouse=True)
  def mock_requests_response(self, requests_mock):
    requests_mock.get("https://example.com?q=apple", text="some large html!", status_code=200)
    requests_mock.get("https://example.com?q=lettuce", text="some error html!", status_code=500)

  def test_get_html_soup_correct_response(self):
    soup = self.scraper.get_html_soup(search_term='apple')

    assert isinstance(soup, BeautifulSoup)
    assert str(soup) == 'some large html!'

  def test_get_html_soup_incorrect_response(self):
    soup = self.scraper.get_html_soup(search_term='lettuce')

    assert soup == None # bc, who really likes lettuce?
