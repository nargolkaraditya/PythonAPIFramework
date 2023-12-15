# Python API Automation Framework

Hybrid Custom Framework to test the REST APIs

## Tech Stack
1. Python version 3.11
2. Requests HTTP Requests
3. PyTest Testing Framework
4. Reporting - Allure Report, PyTest html
5. Test Data - CSV, Excel, JSON
6. Parallel Execution - x distribute

### How to install packages
... pip install requests pytest pytest-html faker allure-pytest jsonschema 
 
### To Freeze your package version
... pip freeze > requirements.txt

### To install freeze version
... pip install -r requirements.txt

### To run your test cases parallel
pip install pytest-xdist

pytest -n auto tests/Parrallel/test_parallel.py
pytest -n auto tests/integration_test/test_create_booking.py

