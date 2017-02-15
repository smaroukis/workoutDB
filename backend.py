import sqlite3

# To add columns to sql table do `alter table <tblname> add <colname> <datatype>;`
# To check columns use `.schema <tblname>`

class Database:
# need to pass `self` to all methods of a class

    def __init__(self, db):
        self.conn=sqlite3.connect("workouts.db")
        self.cur=self.conn.cursor() # now we can use the cursor in other methods
        self.cur.execute("CREATE TABLE IF NOT EXISTS workout (id INTEGER PRIMARY KEY, type TEXT, duration INTEGER, intensity TEXT, description TEXT, tags TEXT)")
        self.conn.commit()

    def insert(self, type, duration, intensity, description, tags):
        self.cur.execute("INSERT INTO workout VALUES (NULL, ?, ?, ?, ?, ?)",(type, duration, intensity, description, tags))
        # Note we pass NULL to create the id automatically
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM workout")
        rows=self.cur.fetchall()
        return rows

    def search(self, type="", duration="", intensity="", description="", tags=""):
        self.cur.execute("SELECT * FROM workout WHERE type=? OR duration=? OR intensity=? OR description=? OR tags=?", (type, duration, intensity, description, tags))
        rows=self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM workout WHERE id=?", (id,)) # comma for sqlite
        self.conn.commit()

    def update(self, id, type, duration, intensity, description, tags):
        self.cur.execute("UPDATE workout SET type=?, duration=?, intensity=?, description=?, tags=? WHERE id=?", (type, duration, intensity, description, tags, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
