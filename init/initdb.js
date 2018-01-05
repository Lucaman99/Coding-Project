var mysqldb = require('mysql')

//Database names can be added to this array when it is determined how the information will be stored.
var db_name_arr = ["user_info", "messages", "information"]
//Table names can be added to this array when it is determined how the information will be stored.
var db_table_arr = [["sign_in (email TEXT, username TEXT, password TEXT, firstname TEXT, lastname TEXT)", "friends (current_friends TEXT, friend_requests TEXT)"], ["messaging (sender TEXT, receiver TEXT, message TEXT, info TEXT, time_stamp TEXT)"], ["online (status TEXT, other_info TEXT)"]]

function init_db(db_name) {

var connector = mysqldb.createConnection({host: "localhost", user: "root", password: "Lucaman"})
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
