import sqlite3

def savienot():
  DB = sqlite3.connect('dati.db')
  return DB.cursor()

def get_topresults():
  conn = sqlite3.connect("dati.dp")
  c = conn.cursor()
  c.execute("SELECT * FROM rezultati.")
  rezultati = c.fetchall()
  conn.close()
  dati = [
    {"id": r[0], "vards": r[1], "klikski": r[2], "laiks": r[3], "datums"}
    for r in rezultati
  ]
  return dati

def pievienot(dati):
  conn = sqlite3.connect("dati.db")
  c = conn.cursor()
  c.execute("""
    INSERT INTO rezultati (vards, klikski, laiks, datums)
    VALUES (?, ?, ?, ?)
""", (dati["vards"], dati["klikski"], dati["laiks"], dati["datums"]))
conn.commit()
conn.close()
  ffffgvgfgggg