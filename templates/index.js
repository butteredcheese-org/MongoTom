function sendMessage() {
    // Get the user's message from the input field
    var message = document.getElementById("message-input").value;
  
    // Create a new XMLHttpRequest object
    var xhr = new XMLHttpRequest();
  
    // Set the HTTP method and URL
    xhr.open("POST", "/generate_text");
  
    // Set the Content-Type header
    xhr.setRequestHeader("Content-Type", "application/json");
  
    // Define the function to be called when the server responds
    xhr.onload = function() {
      if (xhr.status === 200) {
        // Parse the JSON response from the server
        var response = JSON.parse(xhr.responseText);
  
        // Display the chatbot's response in the chat window
        var chatWindow = document.getElementById("chat-window");
        chatWindow.innerHTML += "<div class='message bot'>" + response.generated_text + "</div>";
      } else {
        console.log("Request failed.  Returned status of " + xhr.status);
      }
    };
  
    // Create a JSON object with the user's message
    var data = JSON.stringify({"prompt": message});
  
    // Send the message to the server
    xhr.send(data);
  
    // Clear the input field
    document.getElementById("message-input").value = "";
  }
  