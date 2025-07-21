from flask import Flask, render_template, request, jsonify
import webbrowser

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_message = data.get('message', '')
    reply = generate_response(user_message)
    return jsonify({'reply': reply})

def generate_response(message):
    message = message.lower()

    # === Search Only If User Says "search"
    if "search" in message:
        if "youtube" in message:
            query = message.split("search", 1)[-1].replace("on youtube", "").strip()
            if query:
                webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
                return f"Searching '{query}' on YouTube."
        
        elif "google" in message:
            query = message.split("search", 1)[-1].replace("on google", "").strip()
            if query:
                webbrowser.open(f"https://www.google.com/search?q={query}")
                return f"Searching '{query}' on Google."

    # === Open Websites Only If User Says "open"
    elif "open youtube" in message:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    elif "open instagram" in message:
        webbrowser.open("https://www.instagram.com")
        return "Opening Instagram."

    elif "open google" in message:
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    # === Fun Replies
    elif "hi" in message or "hello" in message:
        return "Hi! I'm Coco, your assistant."

    elif "who are you" in message:
        return "I'm Coco, your AI assistant!"

    elif "joke" in message:
        return "Why don’t robots ever get tired? Because they recharge!"

    return "I'm not sure what you mean. Try saying 'search songs on YouTube' or 'open Instagram'."

if __name__ == '__main__':
    app.run(debug=True)
