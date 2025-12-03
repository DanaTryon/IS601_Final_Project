
# Assignment 14 – FastAPI Application with CI/CD

This project is a FastAPI-based web application containerized with Docker and integrated with GitHub Actions for continuous integration, security scanning, and deployment.  
It includes automated testing (unit, integration, and end-to-end), database migrations with Alembic, and frontend testing with Playwright.

---

## 🚀 Features
- FastAPI backend with authentication and calculation models
- PostgreSQL database integration
- Alembic migrations for schema management
- Unit, integration, and E2E tests with pytest
- Frontend automation with Playwright
- CI/CD pipeline: testing, security scanning (Trivy), and Docker deployment

---

## 🐳 Docker Hub Repository
The latest image is available on Docker Hub:  
[danatryon/assignment14](https://hub.docker.com/r/danatryon/assignment14)

Pull the specific image used in CI/CD:
```bash
docker pull danatryon/assignment14:da8ffd226d2a9f5b68cb09f4fd4058214eef9f2a
```

---

## ⚙️ Running the Application Locally

### 1. Clone the repository
```bash
git clone https://github.com/DanaTryon/assignment14.git
cd assignment14
```

### 2. Set up environment variables
Create a `.env.development` file in the project root:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/fastapi_db
```

### 3. Start services with Docker Compose
```bash
docker-compose up --build
```

The application will be available at:
```
http://localhost:8000
```

---

## 🧪 Running Tests Locally

### 1. Prepare the test database
Create a `.env.test` file in the project root:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/mytestdb
```

Reset and migrate the test database:
```bash
export DATABASE_URL=postgresql://user:password@localhost:5432/mytestdb
alembic upgrade head
```

### 2. Run pytest
```bash
pytest
```

You can also run subsets:
```bash
pytest tests/unit
pytest tests/integration
pytest tests/e2e
```

---

## 📦 CI/CD Pipeline
- **Tests**: Unit, integration, and E2E tests run automatically in GitHub Actions.
- **Security**: Trivy scans the Docker image for vulnerabilities.
- **Deployment**: Images are built and pushed to Docker Hub on successful runs.

