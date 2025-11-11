# CNPJ Lookup

A simple Python + Streamlit application that retrieves company data by CNPJ using BrasilAPI.

## About

This project provides a minimal web interface to search for CNPJ (Brazilian company tax ID) information by querying the public BrasilAPI. The interface accepts a CNPJ (formatted or plain numbers) and displays returned data such as corporate name, trade name, address, partners, and activities.

## Features

- Enter a CNPJ (accepts formatted CNPJ with dots, slash and dash or only digits).
- Automatic formatting of CNPJ and CEP for display.
- Displays: corporate name, trade name, share capital, opening date, phone numbers, address, CEP, email, registration status, tax regime, partners, and activities.
- Uses BrasilAPI (no API key required).

## Requirements

- Python 3.8 or newer
- Internet connection (queries BrasilAPI)

Main dependencies:

- streamlit
- requests

## Installation (Windows - cmd.exe)

1. Create and activate a virtual environment (recommended):

```cmd
python -m venv venv
venv\Scripts\activate
```

2. Upgrade pip and install dependencies:

```cmd
pip install --upgrade pip
pip install streamlit requests
```

You can also create a `requirements.txt` containing `streamlit` and `requests` and install with `pip install -r requirements.txt`.

## How to run

Run Streamlit pointing to the main file (`main.py`):

```cmd
streamlit run main.py
```

This will open the web interface in your browser (usually at http://localhost:8501). On the page, enter the CNPJ in the field and click "Search".

## Usage

- Enter the full CNPJ (e.g., `12.345.678/0001-90` or `12345678000190`).
- If the CNPJ is valid and present in BrasilAPI's database, the data will be displayed.
- Error messages will appear if the CNPJ is invalid (not 14 digits) or if there is a problem connecting to the API.

## Project structure

- `main.py` — Streamlit application that performs the lookup and renders the interface.
- `pyproject.toml` — project metadata (optional).
- `README.md` — this file.

## Notes

- The application depends on BrasilAPI availability. If the API is down or changes, some information may stop being returned.
- No authentication handling is included because the BrasilAPI used here does not require an API key.

## Contributions

Contributions are welcome. Open an issue or a pull request describing the proposed change.
// ...existing code...
```// filepath: c:\Users\hugod\Desktop\ANALYTICS ENGINEER\estudos\projetos\api_cnpj\README.md
// ...existing code...
# CNPJ Lookup

A simple Python + Streamlit application that retrieves company data by CNPJ using BrasilAPI.

## About

This project provides a minimal web interface to search for CNPJ (Brazilian company tax ID) information by querying the public BrasilAPI. The interface accepts a CNPJ (formatted or plain numbers) and displays returned data such as corporate name, trade name, address, partners, and activities.

## Features

- Enter a CNPJ (accepts formatted CNPJ with dots, slash and dash or only digits).
- Automatic formatting of CNPJ and CEP for display.
- Displays: corporate name, trade name, share capital, opening date, phone numbers, address, CEP, email, registration status, tax regime, partners, and activities.
- Uses BrasilAPI (no API key required).

## Requirements

- Python 3.8 or newer
- Internet connection (queries BrasilAPI)

Main dependencies:

- streamlit
- requests

## Installation (Windows - cmd.exe)

1. Create and activate a virtual environment (recommended):

```cmd
python -m venv venv
venv\Scripts\activate
```

2. Upgrade pip and install dependencies:

```cmd
pip install --upgrade pip
pip install streamlit requests
```

You can also create a `requirements.txt` containing `streamlit` and `requests` and install with `pip install -r requirements.txt`.

## How to run

Run Streamlit pointing to the main file (`main.py`):

```cmd
streamlit run main.py
```

This will open the web interface in your browser (usually at http://localhost:8501). On the page, enter the CNPJ in the field and click "Search".

## Usage

- Enter the full CNPJ (e.g., `12.345.678/0001-90` or `12345678000190`).
- If the CNPJ is valid and present in BrasilAPI's database, the data will be displayed.
- Error messages will appear if the CNPJ is invalid (not 14 digits) or if there is a problem connecting to the API.

## Project structure

- `main.py` — Streamlit application that performs the lookup and renders the interface.
- `pyproject.toml` — project metadata (optional).
- `README.md` — this file.

## Notes

- The application depends on BrasilAPI availability. If the API is down or changes, some information may stop being returned.
- No authentication handling is included because the BrasilAPI used here does not require an API key.

## Contributions

Contributions are welcome. Open an issue or a pull request describing the proposed change.
