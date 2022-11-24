const express = require('express')
const app = express()

// This will start an app that listens on port 8090 and goes through the 3 responses
// NOTE - you can only have a response where you want it to end. If you put a response before the final .get then it will terminate there


app.get('/next', function(req, resp, next) {
    console.log('response 1')
    next()
}, (req, resp, next) => {
    console.log('response 2')
    next()
}, (req, resp) => {
    resp.send('This is callback 3')
})

app.listen(8090)