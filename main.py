from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from rembg import remove
from io import BytesIO

# 👇 هذا السطر مهم لتفعيل /docs
app = FastAPI(docs_url="/docs", redoc_url="/redoc", openapi_url="/openapi.json")

@app.post("/remove")
async def remove_bg(file: UploadFile = File(...)):
    input_image = await file.read()
    output_image = remove(input_image)
    return StreamingResponse(BytesIO(output_image), media_type="image/png")

@app.get("/")
def root():
    return {"message": "🎉 Rembg FastAPI server is live!"}
