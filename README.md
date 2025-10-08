# Emotion Extractor for SillyTavern

## 功能
- 从 SillyTavern 获取原始文本
- 调用用户配置的 LLM API 自动识别文本情绪并打标签
- 将带情绪的文本发送到 IndexTTS 生成语音

## 安装
1. 克隆仓库：
```bash
git clone https://github.com/yourusername/emotion_extractor.git

	2.	进入 backend 并安装依赖：

cd emotion_extractor/backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt

	3.	运行 Flask 后端：

python app.py

	4.	在浏览器打开 frontend/index.html 配置 API URL、Key 和模型。

目录说明
	•	backend/ : Flask 后端，处理 LLM 调用和情绪分析
	•	frontend/ : SillyTavern 前端界面，配置 API 和选择模型
	•	.gitignore : 忽略 Python 缓存、虚拟环境、敏感配置
	•	README.md : 项目说明
