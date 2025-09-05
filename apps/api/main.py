from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "DigitalMarkPro AI API is running!"}
