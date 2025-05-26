#!/usr/bin/node

const request = require('request');

// Get movie ID from command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Star Wars API URL for films
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to fetch character data
function fetchCharacter (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`HTTP ${response.statusCode}`));
      } else {
        try {
          const character = JSON.parse(body);
          resolve(character.name);
        } catch (parseError) {
          reject(parseError);
        }
      }
    });
  });
}

// Main function to get film and characters
request(filmUrl, async (error, response, body) => {
  if (error) {
    console.error('Error fetching film:', error.message);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Error: HTTP ${response.statusCode}`);
    process.exit(1);
  }

  try {
    const film = JSON.parse(body);
    const characterUrls = film.characters;

    // Fetch all characters in order
    for (const characterUrl of characterUrls) {
      try {
        const characterName = await fetchCharacter(characterUrl);
        console.log(characterName);
      } catch (fetchError) {
        console.error('Error fetching character:', fetchError.message);
      }
    }
  } catch (parseError) {
    console.error('Error parsing film data:', parseError.message);
    process.exit(1);
  }
});
