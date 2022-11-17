http = require("http")
http.createServer(function (request, response) {
    response.writeHead(200, );
    response.end('Hello World\n')
}).listen(8080)

var express = require('express')
var app = express()

app.get('/', function (req, resp) {
    resp.send('Hello world')
})

app.listen(8090)

app.get('/random/:max', function(req, resp){
    max = parseInt(req.params.max)
    rand = Math.floor(Math.random()*max) +1
    console.log('Max via url is ' + max + ' rand is ' + rand)
    resp.send('' + rand)
})

app.get('/r', function(req, resp){
    max = parseInt(req.query.max)
    rand = Math.floor(Math.random()*max) +1
    console.log('Max via query is ' + max + ' rand is ' + rand)
    resp.send('' + rand)
})

app.listen(8090)