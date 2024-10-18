def mood_response(mood):
    mood = mood.lower()  # Convert mood to lowercase for easier matching
    if mood == "happy":
        return "I'm glad to hear you're happy! 😊"
    elif mood == "sad":
        return "I'm sorry you're feeling sad. I'm here if you need someone to talk to. 😔"
    elif mood == "angry":
        return "It's okay to feel angry sometimes. Take a deep breath and try to relax. 😡"
    elif mood == "excited":
        return "That's awesome! What's making you so excited? 🎉"
    elif mood == "tired":
        return "You should get some rest. Take care of yourself! 😴"
    else:
        return "I'm not sure how to respond to that, but I hope you're doing well! 🙂"