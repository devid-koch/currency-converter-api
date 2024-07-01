# Currency Converter API

This project provides a simple API to convert currency amounts using live exchange rates from an external API.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Configuration](#configuration)

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Django 3.x or later
- `requests` library

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/currency-converter-api.git
    cd currency-converter-api
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate    # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your environment variables:**

    Create a `.env` file in the root of your project and add your Exchange Rates API key:

    ```env
    EXCHANGE_RATE_API_KEY=your_api_key_here
    ```

5. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The project will be available at `http://127.0.0.1:8000/`.

## Usage

[text](http://127.0.0.1:8000/api/convert/?amount=100&from=EUR&to=USD)



## Endpoints

### `GET /api/convert/`

Converts an amount from one currency to another using live exchange rates.

#### Parameters

- `amount` (float): The amount of money to convert.
- `from` (string): The currency code to convert from.
- `to` (string): The currency code to convert to.

#### Response

```json
{
    "amount": 100,
    "from": "EUR",
    "to": "USD",
    "converted_amount": 118.50
}


Configuration
The following environment variable is required:

EXCHANGE_RATE_API_KEY: Your API key for the Exchange Rates API.
Add this variable to your .env file in the root of your project.