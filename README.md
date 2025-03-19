# Car Insurance Premium Simulator

## Installation

To perform the installation, you must have docker installed on your machine.

With docker installed on your machine, run the following commands:


### Rename the file _.env.sample_ to _.env_
```
Windows (Command Prompt ou PowerShell)
ren .env.sample .env

Mac (Terminal)
mv .env.sample .env
```

### Edit, if desired, the initial values ​​contained in the _.env_ file, these values ​​must respect the following rules:
```
CAR_MAKE: string
CAR_MODEL: string
CAR_YEAR: int
CAR_VALUE: float
DEDUCTIBLE_PERCENTAGE: float
BROKER_FEE: float
ADDRESS_STREET: string
ADDRESS_NUMBER: string
ADDRESS_NEIGHBORHOOD: string
ADDRESS_CITY: string
ADDRESS_STATE: string
ADDRESS_COUNTRY: string
ADDRESS_POSTAL_CODE: string
```

### Build the container of our application
```
docker-compose build
```

### Run the created container of our application
```
docker-compose up -d
```

### To run the unit tests, run the command below:
```
pytest -v -s
```

### After running our container, the url below will be available to access the documentation of our routes
```
http://localhost:8000/docs
```

---

## Project Description

As a product owner, I want a backend service that calculates car insurance premiums based on a car's age, value, deductible percentage and a broker's fee. This ensures users receive an accurate and configurable insurance premium calculation. The service must be implemented using **FastAPI**, containerized with **Docker**, and designed following **Domain-Driven Design (DDD), S.O.L.I.D., and Clean Architecture** principles. The domain model should clearly distinguish between **value objects, entities, aggregates, services, and events**.

---

## Core Requirements and Calculation Logic

Everything must be **parameterized** to allow future modifications in the configuration **without requiring code changes**. These values should be **configurable via environment variables or a configuration file**. If using a code generation tool, ensure that: All functions and parameters are written in alphabetical order.

### 1. **Dynamic Rate Calculation**

- For every year since the car was produced, **add 0.5% to the rate**.
- For every **$10,000 of the car’s value, add another 0.5%** to the rate.
- **Example:** A 10-year-old car valued at **$100,000** would have a rate of:
  - **5%** (from age) + **5%** (from value) = **10%** total rate.

### 2. **Premium Calculation**

- **Base Premium** = `car value * applied rate`
- **Deductible Discount** = `base premium * deductible percentage`
- **Final Premium** = `Base Premium - Deductible Discount + Broker’s Fee`

### 3. **Policy Limit Calculation**

- **Base Policy Limit** = `car value * coverage percentage (default 100%)`
- **Deductible Value** = `base policy limit * deductible percentage`
- **Final Policy Limit** = `base policy limit - deductible value`

### 4. [Optional Bonus Task] GIS Adjustment

If a **registration location** is provided, integrate with a **Geographic Information System (GIS)** to adjust the derived rate based on geographic risk factors.

- Suggested approach: Apply an additional rate variation between **-2% and +2%** depending on the risk associated with the location.

## Interface Contracts

### **Input Interface**

- **Car Details:**
  - `make` _(string)_, e.g., `"Toyota"`
  - `model` _(string)_, e.g., `"Corolla"`
  - `year` _(integer)_, e.g., `2012`
  - `value` _(float)_, e.g., `100000.0`
- `deductible_percentage` _(float)_, e.g., `0.10` for **10%**
- `broker_fee` _(float)_, e.g., `50.0`
- `registration_location` _(optional, Address)_

### **Output Interface**

- **Car Details:** _(Echoed from input)_
- `applied_rate` _(Final calculated rate after adjustments)_
- `policy_limit` _(Final policy limit after deductible application)_
- `calculated_premium` _(Final premium after deductible and broker fee adjustments)_
- `deductible_value` _(Monetary value calculated from the original policy limit and deductible percentage)_

---

## Project Structure
```
shandryll-car-insurance-premium-simulator/
├── .env.sample                                           # Sample environment variables file
├── .gitignore                                            # Git ignore file
├── docker-compose.yml                                    # Docker Compose configuration file
├── Dockerfile                                            # Docker configuration file
├── pyproject.toml                                        # Python project configuration file
├── README.md                                             # Project README file
├── requirements.txt                                      # Python dependencies file

├── .vscode/                                              # VS Code configuration folder
│   ├── settings.json                                     # VS Code settings

├── src/                                                  # Source code folder
│   ├── __init__.py                                       # Package initializer
│   ├── config.py                                         # Configuration settings
│   ├── main.py                                           # Main application entry point
│   ├── server.py                                         # Server setup

│   ├── application/                                      # Application layer
│   │   ├── __init__.py                                   # Package initializer

│   │   ├── dto/                                          # Data Transfer Objects
│   │   │   ├── __init__.py                               # Package initializer
│   │   │   ├── insurance_dto.py                          # DTO for insurance

│   │   ├── services/                                     # Service layer
│   │   │   ├── __init__.py                               # Package initializer
│   │   │   ├── config_check.py                           # Configuration check service
│   │   │   ├── health_check.py                           # Health check service

│   │   ├── use_cases/                                    # Use cases
│   │   │   ├── __init__.py                               # Package initializer

│   │   │   ├── factories/                                # Factories for creating use cases
│   │   │   │   ├── __init__.py                           # Package initializer
│   │   │   │   ├── make_calculate_dynamic_rate.py        # Factory for dynamic rate calculation
│   │   │   │   ├── make_calculate_policy_limit.py        # Factory for policy limit calculation
│   │   │   │   ├── make_calculate_premium.py             # Factory for premium calculation

│   │   │   ├── insurance/                                # Insurance related use cases
│   │   │   │   ├── __init__.py                           # Package initializer
│   │   │   │   ├── calculate_dynamic_rate.py             # Use case for dynamic rate calculation
│   │   │   │   ├── calculate_dynamic_rate_test.py        # Tests for dynamic rate calculation
│   │   │   │   ├── calculate_policy_limit.py             # Use case for policy limit calculation
│   │   │   │   ├── calculate_policy_limit_test.py        # Tests for policy limit calculation
│   │   │   │   ├── calculate_premium.py                  # Use case for premium calculation
│   │   │   │   ├── calculate_premium_test.py             # Tests for premium calculation

│   ├── domain/                                           # Domain layer
│   │   ├── __init__.py                                   # Package initializer

│   │   ├── entities/                                     # Data entities
│   │   │   ├── __init__.py                               # Package initializer
│   │   │   ├── address.py                                # Address model
│   │   │   ├── car.py                                    # Car model

│   │   ├── repositories/                                 # Data repositories
│   │   │   ├── __init__.py                               # Package initializer
│   │   │   ├── insurance_repository.py                   # Insurance domain repository

│   ├── infrastructure/                                   # Infrasctruture layer
│   │   ├── __init__.py                                   # Package initializer

│   │   │   ├── controllers/                              # Infrastructure controllers
│   │   │   │   ├── __init__.py                           # Package initializer

│   │   │   │   ├── insurance/                            # Insurance related controllers
│   │   │   │   │   ├── __init__.py                       # Package initializer
│   │   │   │   │   ├── calculate.py                      # Insurance calculation logic
│   │   │   │   │   ├── routes.py                         # API routes for insurance

│   │   │   ├── repositories/                             # Data repositories
│   │   │   │   ├── __init__.py                           # Package initializer
│   │   │   │   ├── insurance_repository.py               # Insurance infrasctruture repository

│   ├── utils/                                            # Utilities folder
│   │   ├── __init__.py                                   # Package initializer
│   │   ├── handler.py                                    # Monetary value handler
```