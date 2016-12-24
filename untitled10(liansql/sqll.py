#coding=utf-8
import MySQLdb

conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db="mysql")

cur = conn.cursor()

cur.execute("select version();")
data = cur.fetchone()

print "DataBase version: %s" % data