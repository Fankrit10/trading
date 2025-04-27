
---

## Documentation

- The API documentation is available at:  
  [https://trading-d0gedfexhtbxbfad.canadacentral-01.azurewebsites.net/docs](https://trading-d0gedfexhtbxbfad.canadacentral-01.azurewebsites.net/docs)

---

## Development and Deployment

- Initially intended for deployment on **Google Cloud**, but encountered a payment error (`CBAT-23`).
- Related issue documented here:  
  [https://support.google.com/googleplay/thread/267532884/error-compra-or-cbat-23?hl=es](https://support.google.com/googleplay/thread/267532884/error-compra-or-cbat-23?hl=es)
- **Deployment was completed on Azure** due to Google Cloud payment issues.
- Deployment uses **Docker** and **docker-compose**.
- `.env` file required. Particularly, a correct `MONGO_URL` must be supplied for correct operation.

---

## Key Highlights

- **Architecture:** MVCD (Model - View - Controller - Database).
- **Database:** MongoDB (both for logging signals and calculating cumulative returns).
- **Endpoints:**
  - `POST /signal`: Send new trading signal
  - `GET /performance`: Retrieve current cumulative return
  - `GET /history`: Retrieve trading history
- **Unit Tests and Quality Analysis:**
  - `pytest` for unit testing
  - `flake8` for code style checking
  - `pylint` for advanced code analysis
  - `bandit` for security checks
  - `Postman / Newman` for API tests with expected outputs automated.
- **CI/CD:**
  - Azure Pipelines integrated for:
    - Build
    - Tests
    - Static code analysis
    - Security analysis
    - Docker build and push
    - Automated deployment to Azure Web App.
- **Vault Integration:**
  - Hardcoded variables were used for practical demonstration.
  - However, the Azure pipeline includes pointers to retrieve secrets from **Azure Key Vault** in production.

- **Logs:**
  - A database is created to record application logs and maintain traceability.
---

## Deployment Instructions

### Requirements

- `docker-compose` installed
- `.env` file with `MONGO_URL` provided (check your email for the connection string).

### Run locally

Create .ENV previously

```bash
docker-compose up --build
