def test_db_conection():
    import postgresql
    db = postgresql.open('pq://user:password@host:port/database')
    r = db.execute("SELECT * FROM Foo")
    print(r)
