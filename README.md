# Python Backend & FastAPI Applications 🚀

This repository contains two complete FastAPI applications along with custom Pydantic data validation schemas, machine learning pipeline integration, and a Streamlit web frontend.

---

## 📁 Repository Directory Structure

```text
Backend-Python/
├── main.py                   # Patient Management System (FastAPI CRUD API)
├── patients.json             # Persistent JSON Database for Patient Records
├── app.py                    # ML Insurance Premium Prediction API (FastAPI)
├── frontend.py               # Streamlit Web User Interface for ML Predictions
├── model.pkl                 # Trained Machine Learning Model Pipeline (scikit-learn)
├── fastapi_ml_model.ipynb    # Jupyter Notebook for Model Training & Export
├── insurance.csv             # Dataset used for Training the ML Model
├── Pydantic/                 # Pydantic v2 Mastery Lessons & Concepts
│   ├── 01_pydantic_why.py
│   ├── 02_field_validator.py
│   ├── 03_model_validator.py
│   ├── 04_computed_field.py
│   ├── 05_nested_model.py
│   └── 06_serialization.py
├── requirements.txt          # Project Dependencies
└── README.md                 # Project Documentation
```

---

# SECTION 1: Patient Management System API 🏥

The **Patient Management System API** (`main.py`) provides a full-featured CRUD (Create, Read, Update, Delete) RESTful service for managing patient records stored persistently in a `patients.json` file.

### Key Features & Data Validations
- **Pydantic Model Enforcements (`Patient`)**: Validates patient metadata including age constraints (`gt=0, lt=120`), gender literals (`Male`, `Female`, `Other`), positive height, and weight.
- **Dynamic Computed Fields**:
  - `@computed_field bmi`: Calculates Body Mass Index automatically using `weight / (height^2)`.
  - `@computed_field verdict`: Dynamically evaluates BMI health category (`Underweight`, `Normal`, `Overweight`, `Obese`).
- **Partial Update Logic (`PatientUpdate`)**: Supports updating selective fields without overwriting unmodified values (`exclude_unset=True`) while automatically recalculating BMI and verdict.
- **Dynamic Sorting**: Filter and sort patients by physical parameters (`height`, `weight`, `bmi`) in ascending or descending order.

---

### 📡 API Endpoints Specification

| Method | Endpoint | Description | Request Payload / Params | Response |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/` | Root Welcome Endpoint | None | `{"message": "hello world"}` |
| `GET` | `/about` | Platform Information | None | `{"message": "campusX is an education platform..."}` |
| `GET` | `/view` | View All Patients | None | Full dictionary of patient records |
| `GET` | `/patient/{patient_id}` | View Specific Patient | Path Param: `patient_id` (e.g. `P001`) | Single patient data or `404 Not Found` |
| `GET` | `/sort` | Sort Patient Records | Query Params: `sort_by` (`height`/`weight`/`bmi`), `order` (`asc`/`desc`) | Sorted list of patient objects |
| `POST` | `/create` | Create New Patient | Request Body: `Patient` model JSON | `201 Created` status with confirmation |
| `PUT` | `/edit/{patient_id}` | Update Patient Info | Path Param: `patient_id`, Request Body: `PatientUpdate` model | `200 OK` status with updated fields |
| `DELETE` | `/delete/{patient_id}`| Delete Patient Record | Path Param: `patient_id` | `200 OK` status with deletion message |

---

### 💡 Example Requests

#### Creating a Patient (`POST /create`)
```json
{
  "id": "P005",
  "name": "Sarah Connor",
  "city": "Mumbai",
  "age": 29,
  "gender": "Female",
  "height": 1.65,
  "weight": 58.0
}
```
*Calculated Response Stored:* `bmi: 21.3, verdict: "Normal"`

#### Sorting Patients (`GET /sort?sort_by=bmi&order=desc`)
Returns all patients ordered from highest to lowest BMI.

---

### 🚀 Running the Patient Management System

1. Ensure dependencies are installed and activate virtual environment:
   ```bash
   .\myvenv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Start the FastAPI Uvicorn development server:
   ```bash
   uvicorn main:app --reload
   ```

3. Access interactive API docs at:
   - **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

# SECTION 2: ML Insurance Premium Prediction API & Frontend 🤖

The **ML Insurance Premium Prediction System** (`app.py` & `frontend.py`) utilizes a trained scikit-learn machine learning pipeline (`model.pkl`) to predict a user's insurance premium risk category based on demographic, lifestyle, and health data.

### Key Features & Model Preprocessing
- **Automated Feature Engineering via Pydantic (`UserInput`)**:
  - `bmi`: Calculated automatically from user `height` and `weight`.
  - `lifestyle_risk`: Derived from `smoker` status and `bmi` threshold (`high`, `medium`, `low`).
  - `age_group`: Segmented into `young` (<25), `adult` (<45), `middle_aged` (<60), and `senior` (>=60).
  - `city_tier`: Maps input city name to Tier 1, Tier 2, or Tier 3 classification.
- **Model Output & Confidence**: Returns the predicted category along with prediction confidence percentage and exact class probability breakdown.
- **Interactive Streamlit Web Interface**: A visual frontend for users to enter health data and receive instant ML predictions without manual API calling.

---

### 📡 API Endpoints Specification

| Method | Endpoint | Description | Request Payload | Response Structure |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/` | API Health Check | None | `{"message": "Insurance Premium Prediction API is running..."}` |
| `POST` | `/predict` | Predict Insurance Premium Category | Request Body: `UserInput` JSON | `predicted_category`, `confidence`, `class_probabilities` |

---

### 💡 Request & Response Example

#### Endpoint: `POST /predict`
**Request Payload**:
```json
{
  "age": 35,
  "weight": 75.0,
  "height": 1.75,
  "income_lpa": 12.5,
  "smoker": false,
  "city": "Bangalore",
  "occupation": "private_job"
}
```

**Response Output**:
```json
{
  "predicted_category": "Medium",
  "confidence": 0.8425,
  "class_probabilities": {
    "High": 0.0512,
    "Medium": 0.8425,
    "Low": 0.1063
  },
  "response": {
    "predicted_category": "Medium",
    "confidence": 0.8425,
    "class_probabilities": {
      "High": 0.0512,
      "Medium": 0.8425,
      "Low": 0.1063
    }
  }
}
```

---

### 🖥️ Streamlit Web Interface (`frontend.py`)

The project includes an interactive web interface built with **Streamlit** that seamlessly connects to the FastAPI ML backend.

- User inputs details (Age, Height, Weight, Income, Smoker status, City, Occupation) using custom numeric sliders and selectboxes.
- Sends payload to `http://127.0.0.1:8000/predict`.
- Displays real-time prediction result, model confidence score, and JSON chart of class probabilities.

---

### 🚀 Running the ML Prediction System & Frontend

1. **Start the ML FastAPI Backend**:
   ```bash
   uvicorn app:app --reload --port 8000
   ```

2. **Start the Streamlit UI Frontend** (in a separate terminal):
   ```bash
   streamlit run frontend.py
   ```

3. Open your browser at [http://localhost:8501](http://localhost:8501) to interact with the web app!

---

## 🛠️ Summary & Quick Commands Reference

| Application | Server Command | Access URL |
| :--- | :--- | :--- |
| **Patient Management API** | `uvicorn main:app --reload` | [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) |
| **ML Prediction API** | `uvicorn app:app --reload` | [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) |
| **Streamlit Web UI** | `streamlit run frontend.py` | [http://localhost:8501](http://localhost:8501) |
