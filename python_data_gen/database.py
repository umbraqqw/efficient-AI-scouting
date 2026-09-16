import sqlite3
import json

connection = sqlite3.connect("scouting.db")
cursor = connection.cursor()
print("complete")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS players(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        position TEXT
    )


""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS matches(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_name TEXT,
        match_id INTEGER,
        top_speed REAL,
        cross_successrate INTEGER,
        shot_on_target INTEGER,
        shot_off_target INTEGER,
        shot_accuracy REAL
    )
""")


with open ("mock_data.json", "r") as file:
    all_players = json.load(file)


for player in all_players:
    cursor.execute("""
        INSERT INTO players (name, position)
        VALUES (?, ?)
    
    """, (player["name"], player["position"]))

    for match in player["matches"]:
        cursor.execute("""
            INSERT INTO matches (player_name, match_id, top_speed, cross_successrate, shot_on_target, shot_off_target, shot_accuracy)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (player["name"], 
              match["match_id"], 
              match["top_speed"], 
              match["cross_successrate"], 
              match["shot_on_target"], 
              match["shot_off_target"], 
              match["shot_accuracy"]
              ))




connection.commit()


print("table complete")
connection.close()
