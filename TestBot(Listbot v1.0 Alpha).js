//Listbot v1.0 Alpha (Testing)
var saved_lists = {"Groceries":["Eggs", "Milk", "Baking Soda", "Lemons", "Brown Sugar"], "To-Do":["Clean the kitchen", "Do the laundry"]}

var list_names = ["Groceries", "To-Do"]

var expression = "Listbot get rid of the list 'Groceries'"

if (expression.search("Listbot") >= 0) {
      
      var searching_expression = expression.substring(expression.search("Listbot") + 7, expression.length).toLowerCase()
      
      var create_array = ["create", "make", "start"]
      var open_array = ["open", "display", "show"]
      var add_array = ["add", "append", "insert", "write", "put"]
      var delete_array = ["delete", "remove", "rid"]
      
      var split_array = searching_expression.split("")
      
      string_array_total = []
      
      for (var v = 0; v < split_array.length; v++) {
      if (split_array[v] === "'") {
      var lower_bound = v
      split_array.splice(lower_bound, 1)
      var upper_bound = split_array.indexOf("'")
      split_array.splice(upper_bound, 1)
      var string_array = split_array.slice(lower_bound, upper_bound)
      split_array.splice(lower_bound, upper_bound - lower_bound)
      string_array_total.push(string_array)
      }
        
      }
      
      var other_data = split_array.join("").split(" ")
      var counting_key = 0
      
      var overall = 0
      for (var v = 0; v < create_array.length; v++) {
        for (var i = 0; i < other_data.length; i++) {
          if (create_array[v] === other_data[i]) {
            var overall = 1
            counting_key++
          }
        }
      }
      

      for (var v = 0; v < add_array.length; v++) {
        for (var i = 0; i < other_data.length; i++) {
          if (add_array[v] === other_data[i]) {
            var overall = 2
            counting_key++
          }
        }
      }
      

      for (var v = 0; v < delete_array.length; v++) {
        for (var i = 0; i < other_data.length; i++) {
          if (delete_array[v] === other_data[i]) {
            var overall = 3
            counting_key++
          }
        }
      }
      

      for (var v = 0; v < open_array.length; v++) {
        for (var i = 0; i < other_data.length; i++) {
          if (open_array[v] === other_data[i]) {
            var overall = 4
            counting_key++
          }
        }
      }
      
      if (counting_key > 1) {
        var message = "Beep boop beep boop....Sorry, I don't recognize that statement. Please try again."
      }
    
      
      switch (overall) {
        case 0:
          var message = "Beep boop beep boop....Sorry, I don't recognize that statement. Please try again."
          break;
        case 1:
          if (string_array_total.length > 1) {
            var message = "Beep boop beep boop....Sorry, I don't recognize that statement. Please try again."
          }
          else {
          var message = string_array_total[0].join("").charAt(0).toUpperCase() + string_array_total[0].join("").substring(1, string_array_total[0].join("").length)
          saved_lists[message] = [];
          }
          break;
        case 2:
          var list = false
          for (var v = 0; v < string_array_total.length; v++) {
            for (var i = 0; i < list_names.length; i++) {
              if (string_array_total[v].join("").toLowerCase() === list_names[i].toLowerCase()) {
              var list = list_names[i]
              string_array_total.splice(v, 1)
              break
              }
            }
          }
          if (list === false) {
            var message = "Beep boop beep boop....Sorry, I can't seem to find that list. Please try again"
          }
          else {
            for (var t = 0; t < string_array_total.length; t++) {
              var message = saved_lists[list]
              saved_lists[list].push(string_array_total[t].join(""))
            }
          }
          break;
        case 3:
         if (string_array_total.length > 1) {
            var message = "Beep boop beep boop....Sorry, I don't recognize that statement. Please try again."
          }
          else {
          var list = false
          for (var v = 0; v < string_array_total.length; v++) {
            for (var i = 0; i < list_names.length; i++) {
              if (string_array_total[v].join("").toLowerCase() === list_names[i].toLowerCase()) {
              var list = list_names[i]
              string_array_total.splice(v, 1)
              break
              }
            }
          }
            if (list === false) {
              var message = "Beep boop beep boop....Sorry, I don't recognize that statement. Please try again."
            }
            else {
            delete saved_lists[list]
            }
          }
          break;
        case 4:
          if (string_array_total.length > 1) {
            var message = "Beep boop beep boop....Sorry, I don't recognize that statement. Please try again."
          }
          else {
            var message = saved_lists[string_array_total[0].join("")]
          }
        default:
          var message = "Beep boop beep boop....Sorry, I don't recognize that statement. Please try again."
      }
      console.log(overall)
      console.log(saved_lists)
      console.log(message)

}
