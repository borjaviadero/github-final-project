# ==========================================
# AUTOMATED UNIT TESTS FOR EMOTION DETECTION
# ==========================================
from emotion_detection import analyze_emotion

def test_happy_emotion_detection():
    """Test if the script correctly identifies happy keywords."""
    sample_text = "I am feeling very happy and glad today!"
    assert analyze_emotion(sample_text) == "happy"

def test_angry_emotion_detection():
    """Test if the script correctly identifies angry keywords."""
    sample_text = "This customer service is bad, I am completely mad!"
    assert analyze_emotion(sample_text) == "angry"

def test_neutral_emotion_detection():
    """Test if the script correctly defaults to neutral."""
    sample_text = "The package arrived at the main station."
    assert analyze_emotion(sample_text) == "neutral"

def test_empty_input_validation():
    """Test if the script handles empty string validation correctly."""
    assert analyze_emotion("") == "invalid"
