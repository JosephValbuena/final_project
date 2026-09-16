from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, request, render_template

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    emotions = emotion_detector(text_to_analyze)

    return '''For the given statement, the system response is 'anger''''
