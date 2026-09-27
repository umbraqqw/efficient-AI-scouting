import sqlite3
import json

connection = sqlite3.connect("scouting.db")
cursor = connection.cursor()
print("complete")

cursor.execute("DROP TABLE IF EXISTS players")
cursor.execute("DROP TABLE IF EXISTS matches")



cursor.execute("""
     CREATE TABLE players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        position TEXT,
        club TEXT,
        
        -- In Possession
        progressive_passes REAL,
        pass_accuracy REAL,
        key_passes REAL,
        expected_assists REAL,
        
        -- Out of Possession
        tackles_won REAL,
        interceptions REAL,
        defensive_duels_win_pct REAL,
        aerial_duels_win_pct REAL,
        
        -- In Transition
        ball_recoveries REAL,
        top_speed REAL,
        high_regains REAL
    )
""")


with open ("mock_data.json", "r", encoding="utf-8") as file:
    all_players = json.load(file)


for players in all_players:
    cursor.execute("""
        INSERT INTO players(
            name, position, club,
            progressive_passes, pass_accuracy, key_passes, expected_assists,
            tackles_won, interceptions, defensive_duels_win_pct, aerial_duels_win_pct,
            ball_recoveries, top_speed, high_regains
        
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        players["name"],
        players["position"],
        players["club"],
        
        # In Possession
        players["in_possession"]["progressive_passes"],
        players["in_possession"]["pass_accuracy"],
        players["in_possession"]["key_passes"],
        players["in_possession"]["expected_assists"],
        
        # Out of Possession
        players["out_of_possession"]["tackles_won"],
        players["out_of_possession"]["interceptions"],
        players["out_of_possession"]["defensive_duels_win_pct"],
        players["out_of_possession"]["aerial_duels_win_pct"],
        
        # In Transition
        players["in_transition"]["ball_recoveries"],
        players["in_transition"]["top_speed"],
        players["in_transition"]["high_regains"]

    ))




connection.commit()
connection.close()

print("table complete")
