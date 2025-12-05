

---

# IS601 Final Project – FastAPI Calculator Application

This project is a full‑stack FastAPI application that provides:

- User registration and authentication (JWT-based)
- CRUD operations for saved calculations
- Arithmetic operations (add, subtract, multiply, divide)
- New Feature Added -Least Common Multiple calculation with strict validation -
Finds the least common multiple of two positive integers.
- A frontend interface
- A complete automated test suite (unit, integration, E2E)
- Dockerized deployment with CI/CD via GitHub Actions

This repository represents the final project for IS601 and demonstrates production‑grade engineering practices including CI/CD, containerization, automated testing, and environment reproducibility.

---

## 🚀 Running the Application Locally

### **1. Clone the repository**
```bash
git clone git@github.com:DanaTryon/IS601_Final_Project.git
cd IS601_Final_Project
```

### **2. Create and activate a virtual environment**
```bash
python3.12 -m venv venv
source venv/bin/activate
```

### **3. Install dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### **4. Set environment variables**
Create a `.env` file or export manually:

```bash
export DATABASE_URL="postgresql://user:password@localhost:5432/mydb"
export SECRET_KEY="your-secret-key"
export ALGORITHM="HS256"
```

### **5. Start the FastAPI application**
```bash
uvicorn app.main:app --reload
```

The application will be available at:

```
http://127.0.0.1:8000
```

Interactive API docs:

```
http://127.0.0.1:8000/docs
```

---

## 🐳 Running with Docker

### **Pull the image from Docker Hub**
```bash
docker pull danatryon/is601_final_project:latest
```

Or pull the specific deployed version:

```bash
docker pull danatryon/is601_final_project:7457139acdbf7ef4bf5c78d5b71a3dc29d4c5d6e
```

### **Run the container**
```bash
docker run -p 8000:8000 danatryon/is601_final_project:latest
```

---

## 🧪 Running Tests Locally

This project uses:

- `pytest`
- `pytest-asyncio`
- `pytest-cov`
- `playwright` (for frontend tests)
- PostgreSQL (for integration tests)

### ✅ **Important:** Async tests must run *before* TestClient tests  
This avoids event‑loop conflicts.

### **1. Install Playwright browsers**
```bash
playwright install
```

### **2. Start PostgreSQL locally**
Using Docker:

```bash
docker run --name testdb \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=mytestdb \
  -p 5432:5432 -d postgres:14
```

### **3. Run async unit tests first**
```bash
pytest tests/unit/test_jwt.py tests/unit/test_redis.py -vv
```

### **4. Run the rest of the test suite**
```bash
pytest -vv --ignore=tests/unit/test_jwt.py --ignore=tests/unit/test_redis.py
```

### ✅ Or use the provided script:
```bash
./run_tests.sh
```

### **5. Generate coverage reports**
```bash
coverage combine
coverage report
coverage html
```

---

## 🐳 Docker Hub Repository

Published image is available here:

👉 **https://hub.docker.com/r/danatryon/is601_final_project**

Pull the latest image:

```bash
docker pull danatryon/is601_final_project:latest
```

---

## 📁 Project Structure

```
.
├── alembic.ini
├── app
│   ├── __init__.py
│   ├── __pycache__
│   ├── auth
│   ├── core
│   ├── database_init.py
│   ├── database.py
│   ├── main.py
│   ├── models
│   ├── operations
│   └── schemas
├── docker-compose.yml
├── Dockerfile
├── docs
├── htmlcov
├── init-db.sh
├── LICENSE
├── Makefile
├── migrations
│   ├── __pycache__
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
├── pytest.ini
├── readme.md
├── requirements.txt
├── run_tests.sh
├── static
│   ├── css
│   └── js
├── templates
│   ├── dashboard.html
│   ├── edit_calculation.html
│   ├── index.html
│   ├── layout.html
│   ├── login.html
│   ├── register.html
│   └── view_calculation.html
├── tests
│   ├── __init__.py
│   ├── __pycache__
│   ├── conftest_unit.py
│   ├── conftest.py
│   ├── e2e
│   ├── frontend
│   ├── integration
│   └── unit
└── venv
    ├── bin
    ├── include
    ├── lib
    └── pyvenv.cfg
```

---

## ✅ CI/CD Pipeline

GitHub Actions performs:

1. Install dependencies  
2. Run async unit tests first  
3. Reset and migrate the test database  
4. Run remaining unit tests  
5. Run integration tests  
6. Run E2E tests  
7. Merge coverage  
8. Run security scanning (Trivy)  
9. Deploy on successful checks
10. Build and push Docker images to Docker Hub 

---

## ✅ Final Notes

- The project is fully containerized and reproducible.
- The test suite covers backend logic, database interactions, and frontend behavior.
- The CI/CD pipeline ensures consistent quality and automated deployment.


