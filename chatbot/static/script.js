const chatbotIcon = document.getElementById("chatbotIcon");
const chatPopup = document.getElementById("chatPopup");
const chatBody = document.getElementById("chatBody");
const userInput = document.getElementById("userInput");

chatbotIcon.onclick = () => {
    chatPopup.style.display = chatPopup.style.display === "flex" ? "none" : "flex";
};

function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    addMessage("You", message);
    userInput.value = "";

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    })
    .then(res => res.json())
    .then(data => addMessage("Bot", data.response));
}

function addMessage(sender, text) {
    const msg = document.createElement("div");
    msg.textContent = `${sender}: ${text}`;
    chatBody.appendChild(msg);
    chatBody.scrollTop = chatBody.scrollHeight;
}
