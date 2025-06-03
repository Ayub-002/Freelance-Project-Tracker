# Freelance Project Tracker

## Overview

The Freelance Project Tracker is a command-line interface (CLI) application built with Python and SQLAlchemy. It helps freelancers manage their clients, projects, and invoices efficiently by storing and querying data from a SQLite database.

## Features

- Add and view clients
- Add and view projects associated with clients
- Add and view invoices associated with projects
- Uses SQLAlchemy ORM for database interaction
- Persistent SQLite storage
- Clean CLI navigation

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/freelance-project-tracker.git
   cd freelance-project-tracker

2. Install dependencies with Pipenv:

    pipenv install

3. Run the database setup:

    pipenv run python lib/db/setup.py

4. Seed the database with sample data:
    pipenv run python scripts/seed_data.py

5. Ensure database tables are created
    pipenv run python -m lib.db.setup

6. Start the CLI app:

    pipenv run python run.py

Project Structure

freelance-project-tracker/
│
├── run.py
├── Pipfile
├── Pipfile.lock
├── README.md
├── lib/
│   ├── db/
│   │   ├── connection.py
│   │   └── setup.py
│   ├── models/
│   │   ├── client.py
│   │   ├── project.py
│   │   └── invoice.py
│   └── controllers/
│       └── cli.py
├── scripts/
│   └── seed_data.py
└── tests/
    ├── test_clients.py
    ├── test_projects.py
    └── test_invoices.py

Requirements
Python 3.11+

Pipenv

SQLAlchemy



