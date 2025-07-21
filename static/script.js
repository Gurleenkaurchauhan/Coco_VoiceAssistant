
let recognizing = false;
const output = document.getElementById("output");

function startListening() {
    if (!('webkitSpeechRecognition' in window)) {
        output.innerText = "Your browser doesn't support speech recognition.";
        return;
    }

    const recognition = new webkitSpeechRecognition();
    recognition.lang = "en-US";
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.start();
    recognizing = true;
    output.innerText = "Listening...";

    recognition.onresult = function(event) {
        const userInput = event.results[0][0].transcript;
        output.innerText = "Processing...";
        fetch("/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userInput })
        })
        .then(res => res.json())
        .then(data => {
            output.innerText = "Coco: " + data.reply;
            speak(data.reply);
        })
        .catch(() => {
            output.innerText = "Could not connect to the assistant.";
        });
    };

    recognition.onerror = function(event) {
        output.innerText = "Error: " + event.error;

        if (event.error === "not-allowed") {
            output.innerText += "\nPlease allow microphone access in your browser.";
        }
        if (event.error === "no-speech") {
            output.innerText += "\nNo speech detected. Try speaking louder or check your microphone.";
        }
    };
}

function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.pitch = 1.2;
    utterance.rate = 1;
    utterance.voice = speechSynthesis.getVoices().find(v => v.name.includes("Google UK English Female")) || null;
    speechSynthesis.speak(utterance);
}
