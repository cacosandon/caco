import requests
from json.decoder import JSONDecodeError

class GraphqlClient:
  """
    GraphQL client for performing graphql queries.
  """

  def __init__(self, base_url: str):
    self.base_url = base_url

  def run(self, query: str, variables: dict() = {}, headers: dict() = {}):
    """
      Returns GraphQL response from query.
    """

    response = requests.post(
      self.base_url,
      json={
        "query": query,
        "variables": variables
      },
      headers=headers
    )

    try:
        return response.json()
    except JSONDecodeError:
        return {}