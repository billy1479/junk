const express = require('express')
const app = express()

// This starts an app that listens on port 8090 for a URL that has the expression
// /users/:userId/books/:bookId and sends the variables users and books to the console
// i.e. http://localhost:8090/users/80/books/12 prints 80 and 12 to the page
app.get('/users/:userId/books/:bookId', function(req,resp) {
    resp.send(req.params)
})
app.listen(8090)
