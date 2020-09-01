import mysql.connector


class Session:
    """Provides an abstraction that connects a MySQL session.

    """

    def __init__(self, host='127.0.0.1', port=3306, user='localhost', password='root', database='roncarati'):
        """Initialization method.

        Args:
            host (str): Connection host.
            port (int): Connection port.
            user (str): MySQL username.
            password (str): MySQL password.
            database (str): Database to be connected.

        """

        print('Initializing session ...')

        # Connects to a MySQL server
        self.session = mysql.connector.connect(host=host, port=port, user=user, 
                                               password=password, database=database)

        # Defines a cursor
        self.cursor = self.session.cursor()

        print('Session connected.')

    def close(self):
        """Closes the MySQL connection.

        """

        # Closes the session
        self.session.close()

        print('Session closed.')
