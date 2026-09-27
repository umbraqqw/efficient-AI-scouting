import sqlite3
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection():
    conn = sqlite3.connect("scouting.db")
    # This allows accessing database columns by name (dict-like)
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/search/{search_term}")
def search_players(search_term: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Query matching player names along with position and club
    cursor.execute("""
        SELECT name, position, club FROM players
        WHERE name LIKE ?
        LIMIT 10
    """, (f"%{search_term}%",))
    
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]

@app.get("/player/{player_name}")
def get_player_profile(player_name: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM players WHERE name = ?", (player_name,))
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        raise HTTPException(status_code=404, detail="Player not found")
    
    p = dict(row)
    
    # Structure database row into nested JSON matching our generator schema
    return {
        "id": p["id"],
        "name": p["name"],
        "position": p["position"],
        "club": p["club"],
        "in_possession": {
            "progressive_passes": p["progressive_passes"],
            "pass_accuracy": p["pass_accuracy"],
            "key_passes": p["key_passes"],
            "expected_assists": p["expected_assists"]
        },
        "out_of_possession": {
            "tackles_won": p["tackles_won"],
            "interceptions": p["interceptions"],
            "defensive_duels_win_pct": p["defensive_duels_win_pct"],
            "aerial_duels_win_pct": p["aerial_duels_win_pct"]
        },
        "in_transition": {
            "ball_recoveries": p["ball_recoveries"],
            "top_speed": p["top_speed"],
            "high_regains": p["high_regains"]
        }
    }