import sqlite3

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS vinylia(id INTEGER PRIMARY KEY, sinthetis text, stixourgos text, orxistra text, date integer, ekdotis text, matrix text, serial_number text)")
        self.conn.commit()
    
    def insert(self, sinthetis,stixourgos,orxistra,date,ekdotis,matrix,serial_number):
        self.cur.execute("INSERT INTO vinylia VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)",
                        (sinthetis, stixourgos, orxistra, date, ekdotis, matrix, serial_number))
        self.conn.commit()


    def remove(self,id):
        self.cur.execute("DELETE FROM vinylia WHERE id=?", (id,))
        self.conn.commit()


    def fetch(self,query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows


    def __del__(self):
        self.conn.close()