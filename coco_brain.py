import webbrowser

def generate_reply(user_input):
    user_input = user_input.lower().strip()

    # === STOP Command ===
    if "stop" in user_input:
        return "Okay! Coco will stop listening now. "

    # === Greeting ===
    elif "hello" in user_input or "hi" in user_input:
        return "Hi! I’m Coco, your soft toy assistant "

    # === Love Message ===
    elif "love you" in user_input:
        return "Aww, I love you too! "

    # === Name Query ===
    elif "your name" in user_input:
        return "I'm Coco, your cute helper "

    # === Google Search ===
    elif "search for" in user_input:
        query = user_input.split("search for")[-1].strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        return f"🔍 Searching Google for '{query}'..."

    elif "google" in user_input:
        query = user_input.replace("google", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        return f"Googling '{query}' for you!"

    # === YouTube Search ===
    elif "youtube" in user_input:
        query = user_input.replace("youtube", "").strip()
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url)
        return f" Playing '{query}' on YouTube!"

    # === Open Instagram ===
    elif "open instagram" in user_input:
        webbrowser.open("https://www.instagram.com")
        return "📸 Opening Instagram for you!"

    # === Tell a joke ===
    elif "joke" in user_input:
        return "Why don’t teddy bears ever eat cake? Because they’re always stuffed! "

    # === Fallback ===
    else:
        return f"You said: '{user_input}'. I’m still learning new tricks!"
