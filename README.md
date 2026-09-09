# Python Backend & Pydantic Mastery 🚀

Welcome to the **Backend-Python** repository! This project serves as a comprehensive hands-on learning guide covering core concepts of **Pydantic v2** data validation, serialization, nested data modeling, computed fields, along with foundational **FastAPI** REST API development.

---

## 📁 Directory Structure

```text
Backend-Python/
├── Pydantic/
│   ├── 01_pydantic_why.py       # Motivation for Pydantic, BaseModel, Field constraints & metadata
│   ├── 02_field_validator.py    # Custom field-level validators (@field_validator)
│   ├── 03_model_validator.py    # Multi-field & root model validators (@model_validator)
│   ├── 04_computed_field.py     # Dynamically calculated fields (@computed_field)
│   ├── 05_nested_model.py       # Nested BaseModel schema composition
│   └── 06_serialization.py      # Serialization to Dict/JSON (model_dump, model_dump_json, exclude)
├── main.py                      # FastAPI application with path/query validation & endpoints
├── patients.json                # Sample JSON dataset for FastAPI API operations
└── README.md                    # Repository documentation
```

---

## 🧠 Pydantic Concepts Covered

### 1. Data Validation & Metadata (`01_pydantic_why.py`)
- **Why Pydantic?**: Replaces repetitive, manual `if`/`else` type and range checks with declarative schema enforcement.
- **`BaseModel` & `Field`**: Adding field boundaries (`gt`, `max_length`), default values, descriptions, and custom titles.
- **Type Annotations**: Utilizing `EmailStr`, `AnyUrl`, `Annotated`, and `Optional` lists/dictionaries.

### 2. Custom Field Validators (`02_field_validator.py`)
- **`@field_validator`**: Creating custom validation logic for individual attributes.
- **Validation Modes**: Using `mode='after'` (or default) to format input values (e.g. converting names to title case or validating email domains like `@hdfc.com` / `@icici.com`).

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

## 🌐 FastAPI Fundamentals (`main.py`)

- **Endpoints & Routing**: `@app.get("/")`, `@app.get("/view")`, `@app.get("/patient/{patient_id}")`, `@app.get("/sort")`.
- **Parameter Validation**:
  - `Path(...)`: Validating path parameters with descriptions and examples in OpenAPI docs.
  - `Query(...)`: Validating query parameters, setting choices, and handling defaults.
- **Error Handling**: Raising structured `HTTPException` with appropriate status codes (`400`, `404`).

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

### Running Pydantic Examples

Run any script individually to observe data validation and outputs:

```bash
python Pydantic/01_pydantic_why.py
python Pydantic/02_field_validator.py
python Pydantic/03_model_validator.py
python Pydantic/04_computed_field.py
python Pydantic/05_nested_model.py
python Pydantic/06_serialization.py
```

### Running FastAPI Server

Launch the development server using Uvicorn:

```bash
uvicorn main:app --reload
```

Access the interactive API documentation at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🎯 Summary

This repository encapsulates the core pillars of backend development in Python using **Pydantic v2** and **FastAPI**, establishing solid practices for type safety, request validation, domain modeling, and API construction.
