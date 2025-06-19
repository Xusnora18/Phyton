
import sqlite3

# Connect to a new in-memory database
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# 1. Create the Roster table
cursor.execute("""
CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# 2. Insert data into the table
cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
])

# 3. Update the name from Jadzia Dax to Ezri Dax
cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

# 4. Select Name and Age where Species is Bajoran
cursor.execute("""
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran'
""")
results = cursor.fetchall()
for row in results:
    print(row)

# Save and close the connection
conn.commit()
conn.close()
