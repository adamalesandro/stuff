var express = require('express');
var app = express();

app.use(express.static('templates'));

app.listen(3000, function () {
    console.log('Running on http://localhost:3000');
});