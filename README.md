# Weather API Test Automation Framework

## Overview
This framework provides automated tests for the **Weather API** (OpenWeatherMap), covering endpoints for current weather and forecast data.

---

## Technology Stack
- **Python 3.x** – Programming language  
- **Pytest** – Test framework  
- **Requests** – HTTP client for API calls  
- **PyYAML** – Configuration management  
- **Pytest-HTML** – HTML test reports  

---

## How to Run Tests

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt

1. **Run all tests with HTML report**
   ```bash
   python -m pytest -v --html=report.html
   