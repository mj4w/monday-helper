"""
This module contains the MondayAPIClient class to interact with the Monday.com API.
"""

from typing import Dict, Any
from monday_helper.graphql_queries import GraphQLQueries
import requests

class MondayAPIClient:
    
    """
    A class to interact with the Monday.com API.
    """

    def __init__(self, api_key: str, api_url: str = "https://api.monday.com/v2"):
        """
        Initializes the API client for Monday API.
        """
        self.api_key = api_key
        self.api_url = api_url

    def get_headers(self) -> Dict[str, str]:
        """
        Returns headers required for Monday API.
        """
        return {"Authorization": self.api_key, "API-Version": "2023-10"}

    def make_request(self, query: str, variables: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Makes a request to the Monday API with a GraphQL query.
        """
        if variables is None:
            variables = {}

        headers = self.get_headers()
        response = requests.post(
            self.api_url,
            json={"query": query, "variables": variables},
            headers=headers,
            timeout=10,
        )
        response.raise_for_status()
        return response.json()

    def get_group(self, board_id: str) -> Dict[str, Any]:
        """
        Queries group by ID and name.
        """
        query = GraphQLQueries.get_board_details(board_id)
        response = self.make_request(query)
        return response

    def get_items(self, board_id: str):
        """
        Queries items from a board.
        """
        query = GraphQLQueries.get_item_details(board_id)
