function sendMessage() {
  // Get the user's message from the input field
  var message = document.getElementById("message-input").value;

  // Get the selected model from the dropdown menu
  var selectedModel = "text-davinci-002";


  // Create a new XMLHttpRequest object
  var xhr = new XMLHttpRequest();

  // Set the HTTP method and URL
  xhr.open("POST", "/generate_text");

  // Set the Content-Type header
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

  // Define the function to be called when the server responds
  xhr.onload = function() {
    if (xhr.status === 200) {
      // Parse the JSON response from the server
      var response = JSON.parse(xhr.responseText);

      // Display the chatbot's response in the chat window
      var chatWindow = document.getElementById("chat-window");
      chatWindow.innerHTML += "<div class='message bot'>" + response.generated_text + "</div>";
      chatWindow.scrollTop = chatWindow.scrollHeight;
    } else {
      console.log("Error: " + xhr.status);
    }
  };

  // Create a URL-encoded string with the user's message and selected model
  var data = "prompt=" + encodeURIComponent(message) + "&gptmodel=" + encodeURIComponent(selectedModel);

  // Send the message to the server
  xhr.send(data);

  // Clear the input field
  document.getElementById("message-input").value = "";

  // Display the user's message in the chat window
  var chatWindow = document.getElementById("chat-window");
  chatWindow.innerHTML += "<div class='message user'>" + message + "</div>";
  chatWindow.scrollTop = chatWindow.scrollHeight;
}
