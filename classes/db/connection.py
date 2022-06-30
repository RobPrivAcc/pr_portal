import pymssql


class Connection:

    def __init__(self, string):
        self._login = string['login']
        self._shop_name = string['shopName']
        self._password = string['password']
        self._ip = string['external_IP']
        self._db = string['dbName']
        self._internal_ip = string['internal_IP']
        self._cursor = None
        self._connection = None

        self._connect()

    def _connect(self):
        try:
            self._connection = pymssql.connect(self._ip, self._login, self._password, self._db, port=1317)
            self._cursor = self._connection.cursor()
        except BaseException as e:
            print(e)
            print(f"Trying {self._shop_name} under {self._internal_ip}.")
            try:
                self._connection = pymssql.connect(self._ip, self._login, self._password, self._db, port=1317)
                self._cursor = self._connection.cursor()
            except BaseException as e:
                print(e)
                print(f"Can't connect to {self._shop_name.title()} under {self._internal_ip}. Breaking program.")
                exit(0)

    def get_cursor(self):
        return self._cursor

    def commit(self):
        self._connection.commit()

    def close(self):
        self._cursor.close()


class SqlQuery(Connection):

    def __init__(self, string):
        super().__init__(string)

    def query_execute(self, query):
        executed_query = self.get_cursor()
        executed_query.execute(query)
        return executed_query.fetchall()

    def query_update(self, query):
        self._cursor.execute(query)
        self.Con.commit()

    def query_insert(self, query, values=""):
        executed_query = self.get_cursor()
        executed_query.execute(query)
        self.commit()