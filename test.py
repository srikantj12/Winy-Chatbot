from dbHelper import getAnswer

query = "Chardonnay"

response = getAnswer(query)

print("price, winery = {}".format(response))

#print("price = ", price)
#print("winery = ", winery)