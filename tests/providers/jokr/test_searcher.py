import pytest
from pinacolada.providers.jokr.searcher import JokrSearcher

class TestJokrSearcher:
  @pytest.mark.vcr
  def test_get_products_for_available_location(self):
    searcher = JokrSearcher(latitude='-33.4054017', longitude='-70.56745')

    products = searcher.get_products(search_term='papas')
    assert products[0]['name'] == 'Papas Fritas Marco Polo Rústicas Sal de Mar 185g'
    assert products[0]['image_url'].startswith('https://')
    assert products[0]['price_amount'] == 2270

  @pytest.mark.vcr
  def test_get_products_for_unavailable_location(self):
    searcher = JokrSearcher(latitude='-40.4054017', longitude='-20.56745')

    products = searcher.get_products(search_term='papas')
    assert products == []
