import os, json
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

def load_config():
    if not os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump({"api_url": "", "api_key": "", "model": ""}, f, indent=4)
        return {"api_url": "", "api_key": "", "model": ""}
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

@app.route("/get_config", methods=["GET"])
def get_config():
    return jsonify(load_config())

@app.route("/save_config", methods=["POST"])
def save_config_route():
    data = request.get_json(force=True)
    save_config(data)
    return jsonify({"status": "ok"})

@app.route("/get_models", methods=["GET"])
def get_models():
    config = load_config()
    headers = {"Authorization": f"Bearer {config.get('api_key', '')}"}
    resp = requests.get(f"{config.get('api_url', '')}/models", headers=headers)
    return jsonify(resp.json())

@app.route("/emotion", methods=["POST"])
def analyze_emotion():
    """
    接收文本，调用用户配置的 LLM API 返回带情绪标签的文本
    """
    config = load_config()
    data = request.get_json(force=True)
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "文本不能为空"}), 400

    headers = {
        "Authorization": f"Bearer {config.get('api_key', '')}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": config.get("model", ""),
        "input": text
    }
    resp = requests.post(f"{config.get('api_url', '')}/analyze_emotion", headers=headers, json=payload)
    return jsonify(resp.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9880)