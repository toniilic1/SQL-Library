from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///library.db', echo = False)
meta = MetaData()

books = Table(
    'Books', meta,
    Column('id', Integer, primary_key = True),
    Column('title', String),
    Column('year', Integer),
)
meta.create_all(engine)

book_id = input("Enter book id: ")
book_title = input("Enter book title: ")
book_year = input("Enter book year: ")

query = books.insert().values(id = book_id, title = book_title, year = book_year)

query2 = books.select()

conn = engine.connect()
r1 = conn.execute(query)
result = conn.execute(query2)

for row in result:
    print("Title: {} | Year: {}".format(row[1], row[2]))