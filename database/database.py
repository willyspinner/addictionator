import sqlite3

class UserDB:
    def __init__(self, filepath:str):
        self.filepath = filepath
        self.columns = ['summoner_name', 'phone_number', 'phone_call_choice', 'text_message_choice']

    def add_user(self, data:dict = {}):
        """
        Input: 
            - data: key value pair with keys ('summoner_name', 'phone_number', 'phone_call_choice', 'text_message_choice')
        """

        self.conn = sqlite3.connect(self.filepath)
        self.conn.row_factory = sqlite3.Row

        # Checking if results exist
        cur = self.conn.cursor()
        cur.execute(
            """
            SELECT *
            FROM user_db
            WHERE summoner_name = ?
            """,
            (data.get('summoner_name'),)
            )
        
        results = cur.fetchone()
        if results is not None:
            print("summoner data already exists in database!")
        else:
            self.conn.execute(
                """
                INSERT INTO user_db (summoner_name, phone_number, phone_call_choice, text_message_choice)
                VALUES (?, ?, ?, ?)
                """,
                (
                    data.get('summoner_name'),
                    data.get('phone_number'),
                    data.get('phone_call_choice'),
                    data.get('text_message_chioce')
                )
            )
        
        self.conn.commit()
        self.conn.close()
    
    def query_user(self, summoner_name:str):
        """

        """

        self.conn = sqlite3.connect(self.filepath)
        self.conn.row_factory = sqlite3.Row

        cur = self.conn.cursor()
        cur.execute(
            """
            SELECT *
            FROM user_db
            WHERE summoner_name = ?
            """,
            (summoner_name,)
            )
        results = cur.fetchone()

        self.conn.commit()
        self.conn.close()
        return results

    def fetch_all_data(self):
        """

        """

        self.conn = sqlite3.connect(self.filepath)
        self.conn.row_factory = sqlite3.Row

        cur = self.conn.cursor()
        cur.execute(
            """
            SELECT *
            FROM user_db
            """
            )
        results = cur.fetchall()

        r = []
        for res in results:
            r.append(dict(zip(self.columns, res)))

        self.conn.commit()
        self.conn.close()
        return r
