const express = require('express');
const app = express();
app.use(express.static('client'));
const recipes = 
{
"carbonara": "text2",
"bolognese": "test2"
}
app.get('/recipes', function(req,resp) {
    const recipe = req.query.recipe;
    let recipeKeys = Object.keys(recipes);
    resp.send(recipeKeys)
})
app.listen(8091)