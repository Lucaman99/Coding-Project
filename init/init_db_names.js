var mysqldb = require('mysql')

//Database names can be added to this array when it is determined how the information will be stored.
var db_name_arr = []

function init_db(db_name) {

var connector = mysqldb.createConnection({host: "localhost", user: "root", password: \\Password Here})
connector.connect(function (err){
	if (err) throw err;
	var mysql = "CREATE DATABASE " + db_name
	connector.query(mysql, function (err, data) {
		if (err) throw err;
	})
	connector.end()
})
}
if (db_name_arr.length > 0) {
	for (var i = 0; i < db_name_arr.length; i++) {
		init_db(db_name_arr[i])
	}
	console.log("Databases successfully created.")
}
else {
	console.log("No databases to query.")
}
