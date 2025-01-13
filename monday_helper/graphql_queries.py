class GraphQLQueries:
    @staticmethod
    def get_board_details(board_id: str) -> str:
        """
        Retrieves the groups of a specified board.

        Args:
            board_id (str): board id where the group is located

        Returns: 
            dict: response data containing the groups id,name
        """
        return f"""
        {{
            boards (ids: {board_id}) {{
                id
                name
                groups {{
                    id
                    title
                }}
            }}
        }}
        """
        
    @staticmethod
    def get_item_details(board_id: str, 
                         group_id: str, cursor: str) -> str:
        """_summary_

        Args:
            board_id (str): _description_

        Returns:
            str: _description_
        """
        
        return f"""
        {{
            boards (ids: {board_id}) {{
                groups (ids: "{group_id}") {{
                    id
                    items_page (limit: 500, cursor: {f'"{cursor}"' if cursor else 'null'}) {{
                        cursor
                        items {{
                            id
                            name
                            column_values {{
                                ... on LocationValue {{
                                    address
                                    city
                                    city_short
                                    country
                                    country_short
                                    street_number
                                    street_number_short
                                    lat
                                    lng
                                    text
                                }}
                                ... on FileValue {{
                                    id
                                    files
                                }}
                                ... on MirrorValue {{
                                    id
                                    display_value
                                }}
                                ... on PeopleValue {{
                                    id
                                    text
                                    persons_and_teams {{
                                        id
                                    }}
                                }}
                                column {{
                                    id
                                    title
                                }}
                                id
                                text
                                value
                                type
                            }}
                            updates {{
                                id
                                created_at
                                creator {{
                                    id
                                    name
                                }}
                                item_id
                                body
                            }}
                        }}
                    }}
                }}
            }}
        }}
        """