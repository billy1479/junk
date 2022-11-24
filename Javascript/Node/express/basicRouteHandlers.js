const express = require('express')
const app = express()

// This will print hello world to the page when the website is loaded at port 8090
// This will print hello to the console when the port is browsed too with /hello at the end
app.get('/', function(req, resp) {
    resp.send('Hello World')
}).get('/hello', function(req, resp){
    resp.send('hello')
}).get('/hellothere', function(req, resp){
    resp.send('you get the point')
})
app.listen(8090)

