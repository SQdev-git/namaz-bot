import sqlite3 as db

class SQdb:
    __error = 'Произошла ошибка -({})'
    def __init__(self, database):
        self.__database = database
    def excom(self, sql):
        self.__con = db.connect(self.__database)
        self.__cur = self.__con.cursor()
        try:
            self.__cur.execute(sql)
        except Exception as e:
            print(self.__error.format(e))
        finally:
            self.__con.commit()
            self.__con.close()
    def exfetchall(self, sql):
        self.__con = db.connect(self.__database)
        self.__cur = self.__con.cursor()
        try:
            self.__result = self.__cur.execute(sql).fetchall()
        except Exception as e:
            self.__result = None
            print(self.__error.format(e))
        finally:
            self.__con.close()
        if not (self.__result is None):
            return self.__result
    def exfetchone(self, sql):
        self.__con = db.connect(self.__database)
        self.__cur = self.__con.cursor()
        try:
            self.__result = self.__cur.execute(sql).fetchone()
        except Exception as e:
            self.__result = None
            print(self.__error.format(e))
        finally:
            self.__con.close()
        if not (self.__result is None):
            return self.__result
    """def execute(self, sql):
        self.__con = db.connect(self.__database)
        self.__cur = self.__con.cursor()
        try:
            self.__result = self.__cur.execute(sql)
        except Exception as e:
            self.__con.close()
            print(self.__error.format(e))
            self.__result = None
        if not (self.__result is None):
            return self.__result"""