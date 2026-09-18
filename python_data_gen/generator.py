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

match_history =[]

for name in name_list:
  player_profile = {
    "name": name,
    "position": "left_wing",
    "matches": []
  }


  for match_id in range (1, 41):
    on_target = random.randint(1, 10)
    off_target = random.randint(1, 10)

    total_shots = on_target + off_target
    accuracy = (on_target / total_shots)*100

    match_data ={
      "match_id" : match_id,
      "top_speed": round(random.uniform(28.0, 34.0), 1),
      "cross_successrate": random.randint(60, 85),
      "shot_on_target": on_target,
      "shot_off_target": off_target,
      "shot_accuracy": round(accuracy, 1)
    }

    player_profile["matches"].append(match_data)

  all_players.append(player_profile)

  with open("mock_data.json", "w") as file:
    json.dump(all_players, file, indent=4)

  print("mock_data.json is generated")

    