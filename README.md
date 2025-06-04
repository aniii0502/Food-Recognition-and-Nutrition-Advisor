
# Food Recognition and Nutrition Advisor

This project is a **Deep Learning-based Food Recognition and Nutrition Advisor** web application.  
It allows users to upload images of fruits or vegetables, predicts the food type using a trained model, and fetches nutrition information from a real-world API.

---

## 🚀 Project Structure


FoodRecognition_and_NutritionAdvisor/

├── frontend/      # React.js app (UI)    
├── backend/       # Flask API (prediction + Nutrition API)  
├── notebook/      # Jupyter notebook for model training  
├── README.md      # Project instructions

---

## 📦 Dataset

This project uses the [Fruits 360 dataset (100x100)](https://github.com/fruits-360/fruits-360-100x100) for training the food classification model.

> **Note:** The dataset is **NOT included** in this repository due to size constraints.  
> Please download it separately from the official repo:  
> 📁 `https://github.com/fruits-360/fruits-360-100x100`

---

## 🧠 Model Training

The training code is located in the `notebook/` directory.

1. Clone/download the Fruits 360 dataset and extract images.
2. Train the CNN model using the provided Jupyter notebook.
3. Save the trained model as `food_classifier.h5` and the class label mapping as `class_indices.json`.
4. Place both files inside `backend/model/`.

---

## ✅ Prerequisites

- Python 3.8+
- Node.js and npm
- Git

---

## 🛠 Backend Setup (Flask)

1. Navigate to the backend directory:

   ```bash
   cd backend

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate  # For Windows

3. Install dependencies:

   ```bash
   pip install -r requirements.txt

4. Set your Nutritionix API credentials in `main.py`:

   ```python
   NUTRITIONIX_APP_ID = "your_app_id_here"
   NUTRITIONIX_APP_KEY = "your_app_key_here"

5. Run the Flask backend server:

   ```bash
   python main.py
   
The API will run at: [http://localhost:8000](http://localhost:8000)

---

## 💻 Frontend Setup (React)

1. Navigate to the frontend directory:

   ```bash
   cd frontend

2. Install dependencies:

   ```bash
   npm install

3. Replace the contents of `src/App.js` with the custom UI for:

   * Image upload

   * Displaying prediction result

   * Showing nutrition info via API call

   > ⚠️ Make sure the React app is connected to the Flask backend at `http://localhost:8000`.

4. Run the React development server:

   ```bash
   npm start

5. Visit the app in your browser:
   👉 [http://localhost:3000](http://localhost:3000)

---

## 🧪 Usage

1. Upload an image (fruit or vegetable).
2. The model predicts the item using the trained classifier.
3. Nutrition information is fetched and displayed from the Nutritionix API.

---

