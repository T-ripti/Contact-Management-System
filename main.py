import sqlite3

def create_table():
    conn = sqlite3.connect("Contectfile.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS contacts(
        First text,
        Last text,
        Number text
        )
        """ 
        )
    conn.commit()
    conn.close()

def add_one(First, Last, Number):
    conn = sqlite3.connect("Contectfile.db")
    c=conn.cursor()

    c.execute(f"SELECt * FROM contacts WHERE first = '{First}' AND last = '{Last}' AND number = '{Number}'")
    result = c.fetchall()

    if len(result) == 0 and First!= "" and Last != "" and Number!= "":
        c.execute("INSERT INTO contacts VALUES (?, ?, ?)", (First, Last, Number))
    conn.commit()
    conn.close()

def show_all():
    conn = sqlite3.connect("Contectfile.db")
    c=conn.cursor()
    c.execute("SELECT rowid, * FROM contacts")

    result = c.fetchall()
    conn.commit()
    conn.close()
    return result


def delete(id):
    conn = sqlite3.connect("Contectfile.db")
    c=conn.cursor()
    c.execute(f"DELETE FROM contacts WHERE rowid ={id}")
    conn.commit()
    conn.close()


def update(id, First, Last, Number):
    conn = sqlite3.connect("Contectfile.db")
    c=conn.cursor()
    if First != "":
        c.execute(f"UPDATE contacts SET first = '{First}' WHERE rowid = {id}")

    if Last != "":
        c.execute(f"UPDATE contacts SET last = '{Last}' WHERE rowid = {id}")

    if Number != "":
        c.execute(f"UPDATE contacts SET number = '{Number}' WHERE rowid = {id}")
    conn.commit()
    conn.close()


create_table()
  


