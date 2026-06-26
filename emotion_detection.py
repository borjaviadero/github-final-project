def analyze_emotion(text):
    if not text:
        return "invalid"
    
    text_lower = text.lower()
    if "happy" in text_lower or "glad" in text_lower or "good" in text_lower:
        return "happy"
    elif "angry" in text_lower or "mad" in text_lower or "bad" in text_lower:
        return "angry"
    else:
        return "neutral"
