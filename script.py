#! /usr/bin/env python
import MySQLdb

host = "YourHost"
passwd = "YourPasswd"
user = "YourUser"
dbname = "YourDb"

db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=dbname)
cursor = db.cursor()

cursor.execute("ALTER DATABASE `%s` CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci'" % dbname)

sql = "SELECT DISTINCT(table_name) FROM information_schema.columns WHERE table_schema = '%s'" % dbname
cursor.execute(sql)

results = cursor.fetchall()
for row in results:
  try:
    sql = "ALTER TABLE `%s` convert to character set DEFAULT COLLATE DEFAULT" % (row[0])
    cursor.execute(sql)
  except:
    cursor.execute("DESC `%s`" % (row[0]))
    desc = cursor.fetchall()
    for elem in desc:
      if "varchar" in elem[1]: #data type of the columns
        cursor.execute("ALTER TABLE `%s` MODIFY `%s` VARCHAR(191) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci" % (row[0], elem[0]))
db.close()
