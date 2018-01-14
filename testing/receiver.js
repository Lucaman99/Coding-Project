var express = require('express')
var app = express()
var url = require('url')
var http = require('http')
var fs = require('fs')
var mysql = require('mysql')

var con = mysql.createConnection({host: 'localhost', user: 'root', password: 'Password', database: "testing"})

con.connect(function (err){
	if (err) throw err;
})

function one() {

	var sql = "SELECT * FROM test"
   con.query(sql, function(err, data){
   	if (err) throw err;


   	console.log(decodeURI(data[data.length - 1].value2))
   	var base = data.length

   	function send() {
	var sql = "SELECT * FROM test"
   con.query(sql, function(err, data){
   	if (err) throw err;
   	if (base !== data.length) {
   		console.log("New transmission")
   		one()
   	}
   	else {
   		setTimeout(send, 1000)
   	}
   })

}
send()

   })

}
one()
