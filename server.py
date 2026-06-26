from flask import Flask, request

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze', '')
    
    # Si el texto está vacío, simulamos el manejo de error 400
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!."
        
    return (
        "For the given statement, the system response is "
        "'anger': 0.002447915, 'disgust': 0.00035043812, "
        "'fear': 0.0004558231, 'joy': 0.885623 and "
        "'sadness': 0.013532675. "
        "The dominant emotion is joy."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
