import sqlite3


class DatabaseConnection:

    #initializes the connection
    def __init__(self, host):
        self.connection = None
        self.host = host

    #opens the connection and returns it
    def __enter__(self):
        self.connection = sqlite3.connect('data.db')
        return self.connection

    #commits and closes the connection
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type or exc_value or exc_tb:
            self.connection.close() #avoid commiting to databse if there is an error; values are not None
        else:
            self.connection.commit()
            self.connection.close()   

