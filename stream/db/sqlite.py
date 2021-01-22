import sqlite3
import login.config as config


## OPEN CONNECTION___________________________
conn = sqlite3.connect(config.DB_PATH)

c = conn.cursor()


## CREATE TABLE_______________________________
# c.execute("""CREATE TABLE trades (
#             id integer,
#             sym text,
#             price real,
#             quantity integer
#             )""")


## DEFINE FUNCTIONS __________________________
def insert_trade(t):
    with conn:
        c.execute("INSERT INTO trades VALUES (:id, :sym, :price, :quantity)", {'id': t['id'], 'sym': t['sym'], 'price': t['price'], 'quantity': t['quantity']})


def get_trade():
    c.execute("SELECT * FROM trades")
    return c.fetchall()


def remove_trade(t):
    with conn:
        c.execute("DELETE from trades WHERE id = :id",
                  {'id': t})

##### TEST ROW_______________________________
# trade1 = {
#     'id': 1234,
#     'sym': 'symballs',
#     'price': 23.5,
#     'quantity':3
# }

# insert_trade(trade1)
# print(get_trade())



# conn.close()









