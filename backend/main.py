from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import json
import requests
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Load model and class indices
model = tf.keras.models.load_model("../model/food_classifier.h5")

with open("../model/class_indices.json", "r") as f:
    class_indices = json.load(f)

# Reverse mapping from index to class name
idx_to_class = {v: k for k, v in class_indices.items()}

def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((100, 100))
    image_array = np.array(image) / 255.0
    return np.expand_dims(image_array, axis=0)

# Nutritionix API credentials (replace with your actual keys)
NUTRITIONIX_APP_ID = "your_app_id_here"
NUTRITIONIX_APP_KEY = "your_app_key_here"

def get_nutrition_info(food_name):
    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_APP_KEY ,
        "Content-Type": "application/json"
    }
    data = {
        "query": food_name,
        "timezone": "US/Eastern"
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        res_json = response.json()
        if "foods" in res_json and len(res_json["foods"]) > 0:
            food_data = res_json["foods"][0]
            nutrition = {
                "calories": food_data.get("nf_calories"),
                "protein_g": food_data.get("nf_protein"),
                "fat_g": food_data.get("nf_total_fat"),
                "carbs_g": food_data.get("nf_total_carbohydrate")
            }
            return nutrition
    return None

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    img = preprocess_image(image_bytes)

    preds = model.predict(img)
    class_id = np.argmax(preds)
    confidence = float(np.max(preds))

    label = idx_to_class[class_id]

    nutrition_info = get_nutrition_info(label)

    return JSONResponse(content={
        "prediction": label,
        "confidence": confidence,
        "nutrition": nutrition_info
    })

@app.get("/")
async def root():
    return {"message": "Smart Grocery Assistant API is running"}
