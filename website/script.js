const searchInput = document.getElementById("player-search");
const resultsList = document.querySelector("#sidebar ul");

async function loadPlayerCard(playerName){
    const response = await fetch("http://127.0.0.1:8000/player/" + playerName);
    const data = await response.json();

    document.getElementById("player-name").innerText = data.name;
    document.getElementById("avg-speed").innerText = data.avg_speed;
    document.getElementById("avg-cross").innerText = data.avg_cross;
    document.getElementById("avg-shot").innerText = data.avg_shot;
}

    
searchInput.addEventListener("input", async (event) => {
  const query = event.target.value;

  // Don't search if the box is empty
  if (query.trim() === "") {
    resultsList.innerHTML = "";
    return;
  }

  try {
    // 3. Fetch matching names from our new backend search route
    const response = await fetch(`http://127.0.0.1:8000/search/${query}`);
    const data = await response.json();

    // 4. Clear old results
    resultsList.innerHTML = "";

    // 5. Loop through matching names and build <li> items dynamically
    data.results.forEach((name, index) => {
      const li = document.createElement("li");
      
      // Inject your styled radio + label structure
      li.innerHTML = `
        <input type="radio" name="player-select" id="p-${index}" class="player-radio">
        <label for="p-${index}" class="player-item">${name}</label>
      `;

      // 6. When clicked, load this player's stats onto the card!
      li.addEventListener("click", () => {
        loadPlayerCard(name);
      });

      resultsList.appendChild(li);
    });

  } catch (error) {
    console.error("Search error:", error);
  }
});
