# Python Backend & FastAPI Course 🚀

Welcome to the **Backend-Python** repository! This repository tracks the complete learning roadmap for Python backend development, focusing on **Pydantic v2** and **FastAPI**.

---

## 📌 Repository Status

| Module | Status | Description |
| :--- | :--- | :--- |
| **Pydantic v2** | ✅ **Completed** | Full data validation, custom/model validators, computed fields, nested models, and serialization |
| **FastAPI** | 🚧 **In Progress / Remaining** | Fundamental GET endpoints & parameter validation covered; CRUD, request bodies, schemas & advanced topics remaining |

---

## 📁 Directory Structure

```text
Backend-Python/
├── Pydantic/                        # ✅ COMPLETED
│   ├── 01_pydantic_why.py          # Motivation, BaseModel, Field constraints & metadata
│   ├── 02_field_validator.py       # Custom field-level validators (@field_validator)
│   ├── 03_model_validator.py       # Multi-field & root model validators (@model_validator)
│   ├── 04_computed_field.py        # Dynamically calculated fields (@computed_field)
│   ├── 05_nested_model.py          # Nested BaseModel schema composition
│   └── 06_serialization.py         # Dict/JSON serialization (model_dump, model_dump_json, exclude)
├── main.py                         # 🚧 IN PROGRESS - FastAPI endpoints (Path & Query parameter validation)
├── patients.json                   # Sample JSON dataset for FastAPI API operations
└── README.md                       # Repository documentation
```

---

## ✅ Module 1: Pydantic Mastery (Completed)

### 1. Data Validation & Metadata (`01_pydantic_why.py`)
- **Why Pydantic?**: Replaces repetitive, manual `if`/`else` type and range checks with declarative schema enforcement.
- **`BaseModel` & `Field`**: Adding field boundaries (`gt`, `max_length`), default values, descriptions, and custom titles.
- **Type Annotations**: Utilizing `EmailStr`, `AnyUrl`, `Annotated`, and `Optional` lists/dictionaries.

### 2. Custom Field Validators (`02_field_validator.py`)
- **`@field_validator`**: Creating custom validation logic for individual attributes.
- **Validation Modes**: Using `mode='after'` (or default) to format input values (e.g. converting names to title case or validating email domains).

### 3. Model & Cross-Field Validators (`03_model_validator.py`)
- **`@model_validator(mode='after')`**: Validating dependencies between multiple fields across the model instance.
- **Use Case**: Enforcing rules across attributes (e.g., verifying emergency contacts are present if patient `age > 60`).

### 4. Computed Fields (`04_computed_field.py`)
- **`@computed_field`**: Defining derived values dynamically calculated on access and included during model serialization.
- **Use Case**: Calculating Body Mass Index (BMI) automatically from `weight` and `height`.

### 5. Nested Models (`05_nested_model.py`)
- **Composition**: Defining reusable schema components (e.g., `Address` model) embedded inside higher-level schemas (e.g., `Patient` model).

### 6. Model Serialization (`06_serialization.py`)
- **`model_dump()`**: Converting Pydantic model instances into Python native dictionaries.
- **`model_dump_json()`**: Exporting models directly to JSON strings.
- **Filtering**: Using `exclude` and `include` sets/dicts to filter out sensitive or unnecessary fields during serialization.

---

## 🚧 Module 2: FastAPI Development (In Progress / Remaining)

### Currently Implemented (`main.py`)
- **Endpoints & Routing**: `@app.get("/")`, `@app.get("/about")`, `@app.get("/view")`, `@app.get("/patient/{patient_id}")`, `@app.get("/sort")`.
- **Parameter Validation**:
  - `Path(...)`: Path parameter validation with OpenAPI descriptions & example values.
  - `Query(...)`: Query parameter validation, field constraints, default values, and sorting logic (`asc`/`desc`).
- **Error Handling**: Raising structured `HTTPException` with status codes (`400`, `404`).

### ⏳ Remaining / Upcoming FastAPI Topics
- [ ] **POST, PUT, DELETE Endpoints**: Creating, updating, and deleting patient records.
- [ ] **Request Body Validation**: Integrating Pydantic `BaseModel` schemas for API payloads.
- [ ] **Response Models**: Defining response schemas with `response_model`.
- [ ] **CRUD Integration**: Updating local JSON storage or database persistent layer.
- [ ] **Dependency Injection**: Reusable dependencies (`Depends`).
- [ ] **Middleware & Authentication**: Security protocols, JWT tokens, and CORS configuration.

---

## 🛠️ How to Run

### Prerequisites
Make sure you have Python installed and set up your virtual environment:

```bash
# Activate virtual environment (Windows PowerShell)
.\myvenv\Scripts\activate

# Install required dependencies
pip install pydantic fastapi uvicorn email-validator
```

### Running Pydantic Examples (Completed)

Run any script individually to observe data validation and outputs:

```bash
python Pydantic/01_pydantic_why.py
python Pydantic/02_field_validator.py
python Pydantic/03_model_validator.py
python Pydantic/04_computed_field.py
python Pydantic/05_nested_model.py
python Pydantic/06_serialization.py
```

### Running FastAPI Server (In Progress)

Launch the development server using Uvicorn:

```bash
uvicorn main:app --reload
```

Access the interactive API documentation at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🎯 Summary

This repository tracks learning for Python backend development. **Pydantic v2** is fully wrapped up and completed. **FastAPI** is currently underway, starting with GET endpoints and parameter validation, with full CRUD, body validation, and advanced concepts to follow.
