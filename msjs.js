    $(document).ready(function(){
        $("#nav2 i").click(function(){
            $(".nav2").slideToggle()
        })

        var saved_lists = new Object()

        var list_names = []

        function outgoing() {
            var value = document.getElementById('tx').value
        var bubble = document.createElement("DIV");
        var textp = document.createElement("P")
        var text = document.createTextNode(value)
        textp.appendChild(text)
        bubble.appendChild(textp)
        $(bubble).addClass("outgoing")
        document.getElementById("wn").appendChild(bubble)

            if (value.search("Listbot") >= 0) {
                  
                  var searching_expression = value.substring(value.search("Listbot") + 7, value.length)
                  
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
                    var final_message = "Beep boop beep boop....Sorry, I don't recognize that statement. Please try again."
                  }
                  
                  else {
                
                  
                  switch (overall) {
                    case 0:
                      var final_message = "Beep boop beep boop....Sorry, I don't recognize that statement. Please try again."
                      break;
                    case 1:
                      if (string_array_total.length > 1) {
                        var final_message = "Beep boop beep boop....Sorry, I don't recognize that statement. Please try again."
                      }
                      else {
                      var message = string_array_total[0].join("")
                      list_names.push(message)
                      saved_lists[message] = [];
                      var final_message = "The list " + message + " has been created!"
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
                        var final_message = "Beep boop beep boop....Sorry, I can't seem to find that list. Please try again"
                      }
                      else {
                        for (var t = 0; t < string_array_total.length; t++) {
                          var message = saved_lists[list]
                          saved_lists[list].push(string_array_total[t].join(""))
                        }
                        var final_message = "Awesome! The list " + list + " has been updated."
                      }
                      break;
                    case 3:
                     if (string_array_total.length > 2) {
                        var final_message = "Beep boop beep boop....Sorry, I don't recognize that statement. Please try again."
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
                          var final_message = "Beep boop beep boop....Sorry, I don't recognize that statement. Please try again."
                        }
                        else {
                          if (string_array_total.length === 0) {
                            var final_message = "The list " + list + " has been deleted!"
                            delete saved_lists[list]
                          }
                          if (string_array_total.length === 1) {
                            saved_lists[list].splice(saved_lists[list].indexOf(string_array_total[0].join("")), 1)
                            var final_message = "Aye aye captain! The list " + list + " has been updated."
                          }
                          
                        }
                      }
                      break;
                    case 4:
                      if (string_array_total.length > 1) {
                        var final_message = "Beep boop beep boop....Sorry, I don't recognize that statement. Please try again."
                      }
                      if (string_array_total.length === 1) {
                        var list = false
                      for (var v = 0; v < string_array_total.length; v++) {
                        for (var i = 0; i < list_names.length; i++) {
                          if (string_array_total[v].join("").toLowerCase() === list_names[i].toLowerCase()) {
                          var list = list_names[i]
                          string_array_total.splice(v, 1)
                          }
                        }
                      }
                      if (list !== false) {
                        var final_message = "Coming right up!"
                        var message = saved_lists[list]
                      }
                      else {
                        var final_message = "Beep boop beep boop....Sorry, I don't recognize that statement. Please try again."
                      }
                      }
                      break
                      
                    default:
                      var final_message = "Beep boop beep boop....Sorry, I don't recognize that statement. Please try again."
                  }
                  }

                  var bubblea = document.createElement("DIV");
                        var mes = document.createTextNode(final_message)
                        bubblea.appendChild(mes)


                            if (overall === 4) {
                                var breaking1 = document.createElement('BR')
                                var breaking2 = document.createElement('BR')
                                bubblea.appendChild(breaking1)
                                bubblea.appendChild(breaking2)
                                if (message.length === 0) {
                                var list_text = document.createTextNode(" \n \n Sorry, there is no data to display")
                                bubblea.appendChild(list_text)
                                }
                                else {
                           var over_list = document.createElement('UL')
                           for (var v = 0; v < message.length; v++) {
                           var list_elements = document.createElement('LI')
                           var list_text = document.createTextNode(message[v])
                           list_elements.appendChild(list_text)
                           over_list.appendChild(list_elements)
                           bubblea.appendChild(over_list)
                           }
                       }
                         }

                        $(bubblea).addClass("incoming")
                        document.getElementById("wn").appendChild(bubblea);
            }



          
        }
        
        $("#bu").click(function(){
        outgoing()
    })
    })
