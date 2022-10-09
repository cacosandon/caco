import json
from typing import List, Union
from pinacolada.base_scrapers import BaseHtmlScraper

class LystoScraper(BaseHtmlScraper):
  def __init__(self):
    base_url = "https://www.lysto.cl/products?keywords="

    super().__init__(search_url_builder=lambda search_term: base_url + search_term)

  def get_products_data(self, search_term: str) -> List[dict[str, Union[str, int]]]:
    html_soup = self.get_html_soup(search_term = search_term)
    if not html_soup:
      return

    ld_json_contents = html_soup.find("script", {"type":"application/ld+json"}).contents
    joined_unparsed_jsons = "".join(ld_json_contents)

    return json.loads(joined_unparsed_jsons)
