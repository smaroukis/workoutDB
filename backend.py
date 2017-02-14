import sqlite3

# To add columns to sql table do `alter table <tblname> add <colname> <datatype>;`
# To check columns use `.schema <tblname>`

def connect():
    conn=sqlite3.connect("workouts.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS workout (id INTEGER PRIMARY KEY, type TEXT, duration INTEGER, intensity TEXT, description TEXT, tags TEXT)")
    conn.commit()
    conn.close()

def insert(type, duration, intensity, description, tags):
    conn=sqlite3.connect("workouts.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO workout VALUES (NULL, ?, ?, ?, ?, ?)",(type, duration, intensity, description, tags))
    # Note we pass NULL to create the id automatically
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("workouts.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM workout")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(type="", duration="", intensity="", description="", tags=""):
    conn=sqlite3.connect("workouts.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM workout WHERE type=? OR duration=? OR intensity=? OR description=? OR tags=?", (type, duration, intensity, description, tags))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("workouts.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM workout WHERE id=?", (id,)) # comma for sqlite
    conn.commit()
    conn.close()

def update(id, type, duration, intensity, description, tags):
    conn=sqlite3.connect("workouts.db")
    cur=conn.cursor()
    cur.execute("UPDATE workout SET type=?, duration=?, intensity=?, description=?, tags=? WHERE id=?", (type, duration, intensity, description, tags, id))
    conn.commit()
    conn.close()
