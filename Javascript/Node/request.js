const http = require('http')

http.createServer((request, response) => {
    const { headers, method, url } = request;
    let body = [];
    request.on('error', (err) => {
        console.log(err);
    }).on('data', (chunk) => {
        body.push(chunk);
    }).on('end', () => {
        body = Buffer.concat(body).toString();

        response.on('error', (err) => {
            console.log(err)
        })

        response.writeHead(200, {'Content-type': 'application/json'})

        let billy = 'hi';
        const responseBody = { headers, method, url, body, billy };

        response.write(JSON.stringify(responseBody))
        response.end();
    })
}).listen(8080)
