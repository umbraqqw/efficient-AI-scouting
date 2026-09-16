async function loadPlayerCard(playerName){
    const response = await fetch("http://127.0.0.1:8000/player/" + playerName);
    const data = await response.json();

    document.getElementById("player-name").innerText = data.name;
    document.getElementById("avg-speed").innerText = data.avg_speed;
    document.getElementById("avg-cross").innerText = data.avg_cross;
    document.getElementById("avg-shot").innerText = data.avg_shot;
}

loadPlayerCard("Mikkelsen");