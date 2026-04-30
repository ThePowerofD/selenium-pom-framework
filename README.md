# Selenium POM Framework

A Python + Selenium + pytest test automation framework demonstrating Page Object Model design, parameterized testing, and CI/CD integration.

## Tech stack
- Python 3.11
- Selenium 4
- pytest
- webdriver-manager
- GitHub Actions

## Setup

```bash
python -m venv venv
source venv/Scripts/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running tests

```bash
python -m pytest                          # all tests
python -m pytest -m smoke                 # only smoke tests
python -m pytest --headless               # headless mode locally
```

## Project structure

- `pages/` — Page Object classes
- `practice/` — test files
- `conftest.py` — pytest fixtures and CLI options
- `pytest.ini` — pytest configuration and markers
