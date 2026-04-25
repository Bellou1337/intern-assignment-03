# Tests

## Environment Setup

```bash
pip install pytest requests allure-python-commons pytest-allure
```

## Start Test Server

```bash
docker compose up -d --build postgres backend
```

Wait for readiness:

```bash
curl http://localhost:8080/health
# Expected: {"status":"ok"}
```

## Run Tests

### Single test
```bash
pytest tests/autotests/api/smoke/test_tc_1_health_check.py -v
```

### All API tests
```bash
pytest tests/autotests/api/ -v
```

### With Allure report
```bash
pytest tests/autotests/api/ --alluredir=tests/allure-results/run_$(date +%Y-%m-%d_%H-%M-%S) -v
allure serve tests/allure-results/
```

## Mobile Tests

```bash
./gradlew :feature:allTests
./gradlew :app:detekt :feature:detekt :model:detekt
```
