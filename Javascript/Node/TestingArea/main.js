const express = require('express');
const app = express();

app.get('/Javascript/Node/TestingArea/test1', function (req, resp) {
    document.getElementById('mainContainer1').innerHTML = 'hello this is working'
})

app.listen(5500)