#! usr/bin/env python
# -*- coding:utf:8 -*-

import MySQLdb
import _mysql_exceptions

HOST = 'localhost'
USER = 'root'
PASS = '288paq03'
DBASE = 'qunlimited'

class Base:
    def __init__(self):
        try:
            self.conn = MySQLdb.connect(host=HOST, user=USER, passwd=PASS,db=DBASE)
            self.cursor = self.conn.cursor()
        except _mysql_exceptions.DatabaseError, e:
            print 'Error'

    def query(self, query=None):
        if query == None:
            return 0
        else:
            self.cursor.execute(query)
            return 1

    @property
    def fetchALL(self):
        return self.cursor.fetchall()


    @property
    def fetchONE(self):
        return self.cursor.fetchone()


    def desconectar(self):
        if self.conn:
            if self.cursor:
                print 'Cerrando cursor...'
                self.cursor.close()
            print 'Desconectar DB'
            self.conn.close()

    '''def __del__(self):
        if self.conn:
            print 'Desconectar'
            self.conn.close()'''


'''if __name__ == '__main__':
    conex= Base()
    conex.query('SELECT `id_sch`, `name_sch`, `state_sch`, `city_sch`, `add_sch`, `tel_sch`, `contact_sch` FROM `school` ')
    print conex.fetchONE
    conex.desconectar()'''

#file = open('../resource/NewQ2Macros.txt','r')
#print file.readlines()


