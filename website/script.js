const searchInput = document.getElementById("search-input");
const searchResults = document.getElementById("search-results");

const cardName = document.getElementById("card-name");
const cardRole = document.getElementById("card-role");
const viewProfileBtn = document.getElementById("view-profile-btn");

const modal = document.getElementById("profile-modal");
const closeModalBtn = document.getElementById("close-modal-btn");

let activePlayerData = null;

// Listen for typing in the sidebar
searchInput.addEventListener("input", async (e) => {
  const query = e.target.value.trim();

  if (query.length === 0) {
    searchResults.innerHTML = "";
    return;
  }

  try {
    const response = await fetch(`http://127.0.0.1:8000/search/${query}`);
    const players = await response.json();

    searchResults.innerHTML = "";

    if (players.length === 0) {
      searchResults.innerHTML = `<li class="player-item" style="cursor:default;">No players found</li>`;
      return;
    }

    players.forEach((player, index) => {
      const id = `player-${index}`;

      const li = document.createElement("li");

      // Uses player-radio and player-item elements matching your CSS
      li.innerHTML = `
        <input type="radio" name="selected_player" id="${id}" class="player-radio">
        <label for="${id}" class="player-item">
          ${player.name}
          <span class="subtext">${player.position} · ${player.club}</span>
        </label>
      `;

      li.querySelector("input").addEventListener("change", () => {
        loadPlayerPreview(player.name);
      });

      searchResults.appendChild(li);
    });
  } catch (err) {
    console.error("Error fetching search results:", err);
  }
});

// Fetch player data and update teaser card
async function loadPlayerPreview(playerName) {
  try {
    const response = await fetch(`http://127.0.0.1:8000/player/${playerName}`);
    if (!response.ok) return;

    activePlayerData = await response.json();

    cardName.textContent = activePlayerData.name;
    cardRole.textContent = `${activePlayerData.position} · ${activePlayerData.club}`;

    viewProfileBtn.disabled = false;
  } catch (err) {
    console.error("Error loading player profile:", err);
  }
}

// Populate and open the full profile modal
viewProfileBtn.addEventListener("click", () => {
  if (!activePlayerData) return;

  document.getElementById("modal-player-name").textContent = activePlayerData.name;
  document.getElementById("modal-player-sub").textContent = `${activePlayerData.position} · ${activePlayerData.club}`;

  // In Possession
  const pos = activePlayerData.in_possession;
  document.getElementById("m-prog-passes").textContent = `${pos.progressive_passes} /90`;
  document.getElementById("m-pass-acc").textContent = `${pos.pass_accuracy}%`;
  document.getElementById("m-key-passes").textContent = `${pos.key_passes} /90`;
  document.getElementById("m-xa").textContent = pos.expected_assists;

  // Out of Possession
  const def = activePlayerData.out_of_possession;
  document.getElementById("m-tackles").textContent = `${def.tackles_won} /90`;
  document.getElementById("m-interceptions").textContent = `${def.interceptions} /90`;
  document.getElementById("m-def-duels").textContent = `${def.defensive_duels_win_pct}%`;
  document.getElementById("m-aerial-duels").textContent = `${def.aerial_duels_win_pct}%`;

  // In Transition
  const tr = activePlayerData.in_transition;
  document.getElementById("m-recoveries").textContent = `${tr.ball_recoveries} /90`;
  document.getElementById("m-top-speed").textContent = `${tr.top_speed} km/h`;
  document.getElementById("m-high-regains").textContent = `${tr.high_regains} /90`;

  modal.classList.remove("hidden");
});

// Modal close listeners
closeModalBtn.addEventListener("click", () => modal.classList.add("hidden"));

window.addEventListener("click", (e) => {
  if (e.target === modal) {
    modal.classList.add("hidden");
  }
});