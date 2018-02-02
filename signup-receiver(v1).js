var url = require('url')
var express = require('express')
var app = express()
var express2 = require('express')
var app2 = express2()
var http = require('http')
var mysql = require('mysql')
var io = require('socket.io')
var fs = require('fs')

app.use(express.static("Desktop"))

app.post("/sender", function (req, res) {
  res.sendfile("")
  function check() {
    var check = url.parse(req.url).query
    if (check !== null) {
    console.log("Received something")
    clearInterval(interval)
  }
  }
  var interval = setInterval(check, 200)
})

var server = app.listen(8089, function (){
  console.log("Listening")
})
