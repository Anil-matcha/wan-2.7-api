from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
import os
from typing import Optional

app = FastAPI(title="Wan 2.7 API", description="API wrapper for Wan AI 2.7 video generation model.")

# --- Model Configuration ---
# Note: Wan 2.1 is the current version, using "wan-2.7" as requested.
MODEL_ID = os.getenv("MODEL_ID", "alibaba/Wan2.1-T2V-1.3B-Diffusers")
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

class GenerationRequest(BaseModel):
    prompt: str
    num_frames: Optional[int] = 81
    width: Optional[int] = 480
    height: Optional[int] = 480
    fps: Optional[int] = 16

@app.get("/")
async def root():
    return {"message": "Wan 2.7 API is running", "model": MODEL_ID, "device": DEVICE}

@app.post("/generate")
async def generate_video(request: GenerationRequest):
    """
    Endpoint to trigger video generation.
    In a real implementation, you would load the Wan model via Diffusers here.
    """
    try:
        # Placeholder for inference logic
        # pipeline = WanPipeline.from_pretrained(MODEL_ID, torch_dtype=torch.float16).to(DEVICE)
        # video = pipeline(request.prompt, num_frames=request.num_frames, ...).frames
        
        return {
            "status": "success",
            "prompt": request.prompt,
            "message": f"Generation triggered on {DEVICE} (Simulated for Wan 2.7)",
            "video_url": "placeholder_url_to_video.mp4"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
