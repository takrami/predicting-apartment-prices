from sklearn import tree, preprocessing
import mysql.connector

# You should change this based on your config
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='learn')

cursor = cnx.cursor()

x = []
y = []

query = 'SELECT * FROM apartment;'
cursor.execute(query)
for line in cursor:
    x.append(line[1:4])
    y.append(line[4])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

# You can change data to predict new apartment price
new_data = [['10', '150', '1380']]
answer = clf.predict(new_data)
print(answer)
