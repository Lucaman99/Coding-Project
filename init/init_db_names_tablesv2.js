var mysqldb = require('mysql')

//Database names can be added to this array when it is determined how the information will be stored.
var db_name_arr = ["User_Info", "Messages"]
//Table names can be added to this array when it is determined how the information will be stored.
var db_table_arr = [["user_info (email TEXT, username TEXT, password TEXT, firstname TEXT, lastname TEXT)"]]

function init_db(db_name, db_table) {

var connector = mysqldb.createConnection({host: "localhost", user: "root", password: "Password"})
connector.connect(function (err){
	if (err) throw err;
	var mysql = "CREATE DATABASE " + db_name
	connector.query(mysql, function (err, data) {
		if (err) throw err;
	})
	connector.end()
})
if (db_table !== undefined) {
	console.log(db_name)
	var connectortwo = mysqldb.createConnection({host: "localhost", user:"root", password: "Password", database: db_name})
	connectortwo.connect(function (err) {
	if (err) throw err;
	for (var v = 0; v < db_table.length; v++) {
		var mysqltwo = "CREATE TABLE " + db_table[v]
		connectortwo.query(mysqltwo, function (err, data){
			if (err) throw err;
		})
}
connectortwo.end()
})
}

}
if (db_name_arr.length > 0) {
	for (var i = 0; i < db_name_arr.length; i++) {
		init_db(db_name_arr[i], db_table_arr[i])
	}
	console.log("Databases/tables successfully created.")
}
else {
	console.log("No databases to query.")
}
