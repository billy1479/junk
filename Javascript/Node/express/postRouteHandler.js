const express = require('express');
const app = express();
app.use(express.static('client'));

app.post('/new', function(req,resp){
    resp.send('hello')
})
app.listen(8090)