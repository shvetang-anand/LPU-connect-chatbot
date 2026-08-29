function addMessage(text, className) {
    let chatBox = document.getElementById("chat-box");
    let div = document.createElement("div");
    div.className = className;
    div.textContent = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendQuestion() {
    let input = document.getElementById("input-user");
    let question = input.value.trim();

    if (question === "") {
        return;
    }

    addMessage(question, "user-message");
    input.value = "";

    try {
        let res = await fetch("/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question: question })
        });

        let data = await res.json();
        addMessage(data.answer, "bot-message");
    } catch (err) {
        addMessage("Sorry, something went wrong. Please try again.", "bot-message");
    }
}

// Send on Enter key
document.getElementById("input-user").addEventListener("keydown", function(e) {
    if (e.key === "Enter") {
        sendQuestion();
    }
});
