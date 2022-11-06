import pytest
from pinacolada.base_clients import GraphqlClient

class TestGraphQlClient:
  def setup_method(self):
    self.query = 'query BlaBlah'
    self.variables = { 'some_param': 'hey!' }
    self.base_url = 'https://test.com'
    self.client = GraphqlClient(base_url=self.base_url)

  @pytest.fixture(autouse=True)
  def mock_requests_response(self, requests_mock):
    requests_mock.post(
      self.base_url,
      json={ 'products': ['hehe', 'haha'] },
      status_code=200
    )

  def test_json_reponse(self):
    json_response = self.client.run(query=self.query, variables=self.variables)

    assert json_response == { 'products': ['hehe', 'haha'] }