import json
import random

all_players= []
name_list = [
    "Garcia", "Rodriguez", "Gonzalez", "Kim", "Lopez",
    "Martinez", "Perez", "Sanchez", "Muller", "Fernandez",
    "Schneider", "Silva", "Jones", "Yilmaz", "Hernandez",
    "Diaz", "Smith", "Williams", "Camara", "Hansen",
    "Ramirez", "Torres", "Schmidt", "Pereira", "Santos",
    "Traore", "Brown", "Diallo", "Alvarez", "Romero"
]

club_list = [
  "Rosenborg", "IK Start", "Molde", "Brann", "Bodø/Glimt", "Viking",
  "Tromsø", "Lillestrøm", "Fredrikstad", "Sarpsborg 08", "KFUM",
  "Sandefjord", "Vålerenga", "Hamkam", "Aalesund", "Kristiansund",
]

player_positions = [
  "LB", "CB", "RB"
  "CM", "LW", "RW" , "ST",
]

match_history =[]

for name in name_list:
  player_profile = {
    "name": name,
    "position": random.choice(player_positions),
    "club": random.choice(club_list),

    "in_possession": {
      "progressive_passes": round(random.uniform(1.5, 7.5), 1),
      "pass_accuracy": round(random.uniform(72.0, 91.0), 1),
      "key_passes": round(random.uniform(0.4, 3.2), 1),
      "expected_assists": round(random.uniform(0.05, 0.40), 2) 
    },

    "out_of_possession": {
      "tackles_won": round(random.uniform(1.0, 4.2), 1),
      "interceptions": round(random.uniform(0.5, 2.8), 1),
      "defensive_duels_win_pct": round(random.uniform(48.0, 78.0), 1),
      "aerial_duels_win_pct": round(random.uniform(35.0, 72.0), 1)
    },

    "in_transition": {
      "ball_recoveries": round(random.uniform(3.0, 9.5), 1),
      "top_speed": round(random.uniform(28.5, 35.2), 1),
      "high_regains": round(random.uniform(0.4, 2.5), 1)
    }
  }

  all_players.append(player_profile)

with open("mock_data.json", "w", encoding="utf-8") as f:
    json.dump(all_players, f, indent=4, ensure_ascii=False)

print("mock_data.json is generated")

    