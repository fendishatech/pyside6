import sqlite3
from typing import List, Dict

class Database:
    def __init__(self, db_file:str)-> None:
        self._db = sqlite3.connect(self.db_file)
        self._cursor = self._db.cursor()
    def execute(self, query: str, params: tuple = ()) -> List[Dict[str, str]]:
        """
        Executes an SQL query on the database.

        Args:
            query (str): The SQL query to execute.
            params (tuple, optional): The parameters to pass to the query. Defaults to ().

        Returns:
            List[Dict[str, str]]: A list of dictionaries, where each dictionary represents a row in the result set.
        """
        self._cursor.execute(query, params)
        rows = self._cursor.fetchall()
        columns = [column[0] for column in self._cursor.description]
        items = []
        for row in rows:
            item = {columns[i]: row[i] for i in range(len(columns))}
            items.append(item)
        return items


    def commit(self):
        self._db.commit()

    def close(self):
        self._db.close()