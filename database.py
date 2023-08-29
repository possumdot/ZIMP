import sqlite3


class Database:

    def create_tables(self):
        db_connection = sqlite3.connect("ZIMP.db")
        db_cursor = db_connection.cursor()
        try:
            db_cursor.execute("""CREATE TABLE items(
                                name STRING PRIMARY KEY NOT NULL,
                                item BLOB)""")
        except sqlite3.OperationalError:
            pass
        try:
            db_cursor.execute("""CREATE TABLE tiles_indoor(
                                name STRING PRIMARY KEY NOT NULL,
                                tile BLOB)""")
        except sqlite3.OperationalError:
            pass

        try:
            db_cursor.execute("""CREATE TABLE tiles_outdoor(
                                    name STRING PRIMARY KEY NOT NULL,
                                    tile BLOB)""")
        except sqlite3.OperationalError:
            pass

        try:
            db_cursor.execute("""CREATE TABLE dev_cards(
                                    name STRING PRIMARY KEY NOT NULL,
                                    dev_card BLOB)""")
        except sqlite3.OperationalError:
            pass

    def add_item_to_table(self, items):
        db_connection = sqlite3.connect("ZIMP.db")
        db_cursor = db_connection.cursor()

        db_cursor.execute("INSERT INTO items VALUES(?, ?)", items)
        db_connection.commit()

    def get_item_from_table(self, key):
        db_connection = sqlite3.connect("ZIMP.db")
        db_cursor = db_connection.cursor()

        result = db_cursor.execute("SELECT (?), item FROM items", key)
        result = result.fetchone()
        return result
