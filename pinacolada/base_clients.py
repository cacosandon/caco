import requests
from pinacolada.constants import SUCCESS_STATUS_CODE

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

    request = requests.post(
      self.base_url,
      json={
        "query": query,
        "variables": variables
      },
      headers=headers
    )

    if request.status_code == SUCCESS_STATUS_CODE:
      return request.json()

    raise Exception(f"Unexpected status code returned: {request.status_code}: {request.text}")
