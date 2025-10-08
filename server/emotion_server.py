from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok", "msg": "Emotion server running."})

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get("text", "")
    # 简单规则判断（以后可以替换成 AI 模型）
    if "!" in text or "开心" in text:
        emotion = "happy"
    elif "生气" in text:
        emotion = "angry"
    elif "难过" in text:
        emotion = "sad"
    else:
        emotion = "neutral"
    return jsonify({"emotion": emotion})

if __name__ == "__main__":
    print("🧠 Emotion Extractor Server running at http://127.0.0.1:8090")
    app.run(host="127.0.0.1", port=8090)