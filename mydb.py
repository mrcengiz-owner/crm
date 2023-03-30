#Öncelikle My SQL Sistemde kurulu olması gerekmektedir.
# https://dev.mysql.com/downloads/installer/ bu adres üzerinden indirme sağlayabilirsiniz. Daha sonra Sırasıyla
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

#yukarıdaki adımları uygulayın


import mysql.connector

dataBase=mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    passwd= 'Murat1993.',

)
#bir Cursor nesnesi hazırlama
cursorObject=dataBase.cursor()

#Veritabanı oluşturma

cursorObject.execute("CREATE DATABASE CRMRT")
print("Tüm işlemler TAMAM!")