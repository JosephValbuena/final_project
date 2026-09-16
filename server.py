from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, request, render_template

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    emotions = emotion_detector(text_to_analyze)

    return f"""For the given statement, the system response is
    'anger': {emotions['anger']}, 
    'disgust': {emotions['disgust']}, 
    'fear': {emotions['fear']} 
    'joy': {emotions['joy']}
    and 'sadness': {emotions['sadness']}. 
    The dominant emotion is {emotions['dominant_emotion']}
    """
@app.route('/')
def main():
    return render_template(index.html)


if __name__ == "__main__":
    app.run(debug=True)