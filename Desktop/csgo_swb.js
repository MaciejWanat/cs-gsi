var request = require('request');

http = require('http');
fs = require('fs');

port = 3000;
host = '127.0.0.1';

server = http.createServer(function(req, res) {
    console.log('Handling POST request...');

    var body = '';

    req.on('data', function (data) {
        body += data;
    });

    req.on('end', function () {
        console.log('POST payload: ' + body);
        console.log('Type: ' +  typeof body);
    
        request({
            'method': 'POST',
            'uri': 'http://10.100.6.255:3000',
            'body': body
        });

        res.end('');
    });
    
});

server.listen(port, host);
console.log('Listening at http://' + host + ':' + port);
