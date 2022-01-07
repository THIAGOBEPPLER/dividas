import mysql.connector


cnx = mysql.connector.connect(user='root', 
                                password='teste',
                                host='localhost',
                                database='Dividas')

cursor = cnx.cursor()

#query = (" INSERT INTO Teste (Nome) VALUES ('tetse2');")

# query = ("Select * from Usuario")


# cursor.execute(query)

# #cnx.commit()

# myresult = cursor.fetchall()

# for x in myresult:
#     print(x)


#cnx.close()

