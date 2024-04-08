function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    if (userInput.trim() !== "") {
        addUserMessage(userInput);
        // Call your chatbot backend API here to get the bot's response
        // For demonstration, let's assume a simple response from the bot
        setTimeout(function() {
            addBotMessage("Sorry, I'm just a demo chatbot!");
        }, 500);
    }
}

function addUserMessage(message) {
    var chatBox = document.getElementById("chat-box");
    var userMessage = document.createElement("div");
    userMessage.className = "chat-message user-message";
    userMessage.textContent = message;
    chatBox.appendChild(userMessage);
    document.getElementById("user-input").value = "";
    chatBox.scrollTop = chatBox.scrollHeight;
}

function addBotMessage(message) {
    var chatBox = document.getElementById("chat-box");
    var botMessage = document.createElement("div");
    botMessage.className = "chat-message bot-message";
    botMessage.textContent = message;
    chatBox.appendChild(botMessage);
    chatBox.scrollTop = chatBox.scrollHeight;
}