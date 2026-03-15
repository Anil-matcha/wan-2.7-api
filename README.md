# Wan 2.7 API

Python API wrapper for **Wan AI 2.7** video generation model. Built with FastAPI and designed for easy integration.

## Features
- **FastAPI-powered REST API**: High performance and easy integration.
- **Wan AI Support**: Compatible with Wan 2.1/2.7 architectures.
- **Flexible Configuration**: Supports custom resolution, frame count, and FPS.

## Getting Started

### Prerequisites
- Python 3.10+
- NVIDIA GPU with 12GB+ VRAM (Recommended for 1.3B model)
- [Hugging Face Access Token](https://huggingface.co/settings/tokens) (If required for weights)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Anil-matcha/wan-2.7-api.git
   cd wan-2.7-api
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
Run the API server:
```bash
python app.py
```

Generate a video:
```bash
curl -X POST "http://localhost:8000/generate" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "A futuristic city under a neon sunset, cinematic motion"}'
```

## Disclaimer
"Wan 2.7" is used as a target identifier. Currently, Wan AI 2.1/2.2 are the most widely available versions. This API defaults to `Wan2.1-T2V-1.3B` for efficiency.
