async function sendMessage() {
  let inputField = document.getElementById("userInput");
  let userText = inputField.value.trim();
  if (userText === "") return;

  displayMessage(userText, "user");
  inputField.value = "";

  let response = await fetch("/get", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: userText })
  });

  let data = await response.json();
  displayMessage(data.reply, "bot");
}

function displayMessage(text, sender) {
  let chatbox = document.getElementById("chatbox");
  let msg = document.createElement("div");
  msg.className = "message " + sender;
  msg.innerText = text;
  chatbox.appendChild(msg);
  chatbox.scrollTop = chatbox.scrollHeight;
}
