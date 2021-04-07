import sqlite3

# connect
conn = sqlite3.connect('ch_14_sqlite/music.sqlite3')
# obtain cursor
cursor = conn.cursor()

# run commands
cursor.execute('DROP TABLE IF EXISTS Tracks')
cursor.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')


cursor.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )',
               ('Thunderstruck', 20))
cursor.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )',
               ('My Way', 15))

# commit commands
conn.commit()

# read from db
print('Tracks:')
cursor.execute('SELECT title, plays FROM Tracks')

for row in cursor:
    print(row)

# delete from db
cursor.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()

# close cursor
cursor.close()

# close db
conn.close()
