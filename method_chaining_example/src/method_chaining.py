

class SimpleSQLStatementExample(object):

    def __init__(self):
        self._statement = None
        self._select = "SELECT\r\n"
        self._from = None
        self._where = None

    def select(self, *args):
        select_sql = []
        for v in args:
            select_sql.append(v)

        self._select += "\r\n".join(["   " + select_sql[0]] + ["  ," + item for item in select_sql if item != select_sql[0]])

        return self

    def source(self, from_table):
        self._from = from_table

        return self

    def where(self, **kwargs):
        where_sql = []
        for k, v in kwargs.iteritems():
            where_sql.append("{0}='{1}'".format(k, v))

        if len(where_sql) > 0:
            self._where = "WHERE "
            self._where += "\r\n".join(["" + where_sql[0]] + ["  AND " + item for item in where_sql if item != where_sql[0]])

        return self

    def execute(self):
        print self._select + "\r\nFROM " + self._from + "\r\n" + self._where


if __name__ == '__main__':
    s = SimpleSQLStatementExample()
    s.select("make", "model").source("cars").where(make="ford", model="taurus").execute()