#!/usr/bin/node

/*
Write a JavaScript script that fetches the character name
from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
The name must be displayed in the HTML tag with id character.
*/
const fetchCharBtn = document.querySelector("#fetch_character");
const characterEl = document.querySelector("#character");

fetchCharBtn.addEventListener("click", () => {
  getCharacterName();
})
async function getCharacterName() {
  const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const character_json = await response.json()
    const characterName = character_json["name"];
    console.log(`Character Name: ${characterName}`);
    characterEl.textContent = characterName;
  } catch (error) {
    console.log(error.message);
  }
}

