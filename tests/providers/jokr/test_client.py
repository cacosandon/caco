import pytest
from pinacolada.providers.jokr.client import JokrClient

class TestJokrClient:
  def setup_method(self):
    self.client = JokrClient()

  @pytest.mark.vcr
  def test_get_hub_id_by_coordinates(self):
    hub_id = self.client.get_hub_id_by_coordinates(latitude='-33.4054017', longitude='-70.56745')

    assert hub_id == 'SCL003'

  @pytest.mark.vcr
  def test_search_products(self):
    products = self.client.search_products(search_term='manzana', hub_id='SCL003')

    assert { 'sku': '1111111411111' } in products
    assert { 'sku': '7802200270022' } in products

  @pytest.mark.vcr
  def test_get_products_data(self):
    skus = ['1111111411111', '7802200270022']
    products_data = self.client.get_products_data(
      skus=skus,
      hub_id='SCL003'
    )

    assert len(products_data) == len(skus)
    assert products_data[0]['name'] == 'Manzana Fuji 1 und'
    assert products_data[0]['packshot1_front_grid']['url'].startswith('https://')
    assert products_data[0]['price']['amount'] == 466
