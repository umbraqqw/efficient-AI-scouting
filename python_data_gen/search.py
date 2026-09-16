import sqlite3

connection = sqlite3.connect("scouting.db")
cursor = connection.cursor()

search_speed = 33.0

cursor.execute("""
    SELECT player_name, top_speed FROM matches WHERE top_speed > ?
""", (search_speed,))


results = cursor.fetchall()

print(f"Found {len(results)} matches matching your criteria:")
for row in results:
    print(row)


connection.close()