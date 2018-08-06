# import pandas as pd
import sqlite3 as lite


conn = lite.connect('wine.db')

# df = pd.read_csv('data/wine-reviews/winemag-data_first150k.csv')
# df = pd.read_csv('data/wine-reviews/winemag-data-130k-v2.csv')
# print(df.head(2))
# df.to_sql('reviews', conn, if_exists='append', index=False)
# sym = query
# create a function that takes what user requires as argument and substitute
# that in the sql query using variable. this way we have one query for multiple
# options
# wine is going to remain in the query surely since he may ask something about
# the wine
# what will change is the description or price etc according to the wine name.
# For now - create a query that gives all the information about a wine brand
# def get_items(self, owner):
# stmt = "SELECT description FROM items WHERE owner = (?)"
# args = (owner, )
# return [x[0] for x in self.conn.execute(stmt, args)] # replace this
# accordingly?


def getAnswer(variety):
    # symbol = '*'
    sql = ("SELECT DISTINCT country FROM reviews WHERE country IS NOT NULL "
           "AND variety like (?) ORDER BY points DESC limit 1")
    args = (variety,)

    cur = conn.execute(sql, args)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.close()


getAnswer("Pinot Noir")
