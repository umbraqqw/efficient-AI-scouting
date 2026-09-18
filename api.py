from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

# This is a security bypass. It allows your local HTML file to talk to this API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# This creates the URL path: http://127.0.0.1:8000/player/NAME
@app.get("/player/{player_name}")
def get_player_averages(player_name: str):
    
    connection = sqlite3.connect("scouting.db")
    cursor = connection.cursor()
    
    # We group all of the player's matches together and calculate the average
    cursor.execute("""
        SELECT 
            player_name, 
            ROUND(AVG(top_speed), 1), 
            ROUND(AVG(cross_successrate), 1), 
            ROUND(AVG(shot_accuracy), 1)
        FROM matches 
        WHERE player_name = ?
        GROUP BY player_name
    """, (player_name,))
    
    result = cursor.fetchone() 
    connection.close()
    
    # Pack the result into a clean dictionary to send to the browser
    if result:
        return {
            "name": result[0],
            "avg_speed": result[1],
            "avg_cross": result[2],
            "avg_shot": result[3]
        }
    else:
        return {"error": "Player not found"}


# The {query} in the path will be whatever text the user typed in the search box
@app.get("/search/{query}")
def search_players(query: str):
    
    connection = sqlite3.connect("scouting.db")
    cursor = connection.cursor()
    
    # SQL 'LIKE' finds partial matches. 
    # Adding '%' before and after means: "find 'query' anywhere inside the string"
    search_term = f"%{query}%"
    
    # We SELECT distinct names, and LIMIT 10 so we never overload the site
    cursor.execute("""
        SELECT DISTINCT player_name 
        FROM matches 
        WHERE player_name LIKE ?
        LIMIT 10
    """, (search_term,))
    
    # fetchall() grabs every row that matched the query
    results = cursor.fetchall()
    connection.close()
    
    # Convert from list of tuples [('Jensen',), ('Mikkelsen',)] 
    # into a clean list of strings ['Jensen', 'Mikkelsen']
    player_list = [row[0] for row in results] if results else []    
    return {"results": player_list}