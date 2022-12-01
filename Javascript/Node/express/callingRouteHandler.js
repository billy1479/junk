// This uses the await function to call the webpage that is defined in one of the express handler functions and stores the response in the variable

let recipeKeys = await fetch('127.0.0.1:8090/recipes');
recipe_content.innerHTML = recipeKeys;


// Or:

async function loadRecipes() {
    let recipe_content = document.getElementById('recipe_results');
    let recipeKeys = await fetch('127.0.0.1:8090/recipes');
    recipe_content.innerHTML = recipeKeys;
}
document.addEventListener('DOMContentLoaded', loadRecipes)

// The above loads the recipes like the top lines of code via an async function which waits for the response to load before moving onto the next function