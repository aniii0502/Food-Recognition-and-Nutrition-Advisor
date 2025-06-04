import React, { useState } from 'react';

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setResult(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return alert("Please select an image");

    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://localhost:8000/predict/", {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      setResult(data);
    } catch (err) {
      alert("Error: " + err.message);
    }
    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 600, margin: "auto", padding: 20, fontFamily: "Arial" }}>
      <h1>Smart Grocery Assistant</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" accept="image/*" onChange={handleFileChange} />
        <button type="submit" disabled={loading} style={{ marginLeft: 10 }}>
          {loading ? "Predicting..." : "Predict"}
        </button>
      </form>

      {result && (
        <div style={{ marginTop: 20 }}>
          <h2>Prediction:</h2>
          <p><strong>Label:</strong> {result.prediction}</p>
          <p><strong>Confidence:</strong> {(result.confidence * 100).toFixed(2)}%</p>

          {result.nutrition ? (
            <>
              <h3>Nutrition Info (per serving):</h3>
              <ul>
                <li>Calories: {result.nutrition.calories}</li>
                <li>Protein: {result.nutrition.protein_g} g</li>
                <li>Fat: {result.nutrition.fat_g} g</li>
                <li>Carbs: {result.nutrition.carbs_g} g</li>
              </ul>
            </>
          ) : (
            <p>No nutrition info available.</p>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
