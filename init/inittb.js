var mysqldb = require('mysql')

//Database names can be added to this array when it is determined how the information will be stored.
var db_name_arr = ["user_info", "messages", "information"]
//Table names can be added to this array when it is determined how the information will be stored.
var db_table_arr = [["sign_in (email TEXT, username TEXT, password TEXT, firstname TEXT, lastname TEXT)", "friends (current_friends TEXT, friend_requests TEXT)"], ["messaging (sender TEXT, receiver TEXT, message TEXT, info TEXT, time_stamp TEXT)"], ["online (status TEXT, other_info TEXT)"]]

function init_tb(db_name, db_table) {

if (db_table !== undefined) {
	var connectortwo = mysqldb.createConnection({host: "localhost", user:"root", password: "Lucaman"})
	console.log(db_table)
	connectortwo.connect(function (err) {
	if (err) throw err;
	for (var v = 0; v < db_table.length; v++) {
		var mysqltwo = "CREATE TABLE " + db_name+"."+db_table[v]
		console.log(mysqltwo)
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
		init_tb(db_name_arr[i], db_table_arr[i])
	}
	console.log("Tables successfully created.")
}
else {
	console.log("No databases to query.")
}
