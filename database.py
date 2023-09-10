import sqlite3


class Database:

    def create_tables(self):
        db_connection = sqlite3.connect("ZIMP.db")
        db_cursor = db_connection.cursor()
        try:
            db_cursor.execute("""CREATE TABLE save_games(
                                save_name STRING PRIMARY KEY NOT NULL,
                                save_game BLOB NOT NULL)""")
            db_connection.close()
        except sqlite3.OperationalError:
            pass

    def add_save_game_to_table(self, save_info):
        try:
            db_connection = sqlite3.connect("ZIMP.db")
            db_cursor = db_connection.cursor()
            sql = "INSERT INTO save_games(save_name, save_game) VALUES(?, ?)"

            db_cursor.execute(sql, save_info)
            db_connection.commit()
            db_connection.close()
        except sqlite3.IntegrityError:
            print("This save game already exists. Please choose another name.")

    def get_save_game_from_table(self, save_name):
        db_connection = sqlite3.connect("ZIMP.db")
        db_cursor = db_connection.cursor()

        sql = 'SELECT save_game FROM save_games WHERE save_name = ?'

        result = db_cursor.execute(sql, (save_name,))
        result = result.fetchall()
        db_connection.close()
        return result
