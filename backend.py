import sqlite3

def connect():
    conn=sqlite3.connect("workouts.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS workout (id INTEGER PRIMARY KEY, type TEXT, duration INTEGER, intensity TEXT, description TEXT)")
    conn.commit()
    conn.close()

def insert(type, duration, intensity, description):
    conn=sqlite3.connect("workouts.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO workout VALUES (NULL, ?, ?, ?, ?)",(type, duration, intensity, description))
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

def search(type="", duration="", intensity="", description=""):
    conn=sqlite3.connect("workouts.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM workout WHERE type=? OR duration=? OR intensity=? OR description=?", (type, duration, intensity, description))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("workouts.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM workout WHERE id=?",(id,)) # comma for sqlite
    conn.commit
    conn.close()

def update(id, type, duration, intensity, description):
    conn=sqlite3.connect("workouts.db")
    cur=conn.cursor()
    cur.execute("UPDATE workout SET type=?, duration=?, intensity=?, description=?", (id, type, duration, intensity, description))
    conn.commit()
    conn.close()

connect()
