# Employee Management System (EMS)

A Django REST API Project with Data Visualization

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Architecture](#architecture)
- [API Endpoints](#api-endpoints)
- [Data Visualization](#data-visualization)
- [Authentication & Authorization](#authentication--authorization)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Development & Testing](#development--testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Environment Management](#environment-management)
- [Key Files & Directories](#key-files--directories)

---

## Overview

The Employee Management System (EMS) is a Django-based web application for managing employee records, attendance, performance reviews, and department data. It provides a secure RESTful API for CRUD operations and interactive dashboards for visualizing workforce metrics. Built with Django, Django REST Framework, and PostgreSQL, EMS is designed for scalability, security, and ease of integration.

---

## Features

- **Employee CRUD**: Add, update, view, and delete employee records.
- **Department Management**: Organize employees by department.
- **Attendance Tracking**: Record and analyze employee attendance (Present, Absent, Late).
- **Performance Reviews**: Track employee performance ratings over time.
- **Data Visualization**: Interactive dashboards using Chart.js for analytics.
- **Authentication**: Token-based authentication for secure API access.
- **Role-Based Access Control**: Restrict access to sensitive endpoints.
- **API Documentation**: Swagger and Redoc auto-generated docs.
- **Database Seeding**: Populate with realistic test data using Faker.
- **Extensible**: Easily add new models, endpoints, or visualizations.

---

## Technology Stack

- **Backend**: Django 5.2.5, Django REST Framework
- **Database**: PostgreSQL
- **Frontend**: HTML, Chart.js
- **API Docs**: drf-yasg (Swagger, Redoc)
- **Testing**: pytest, Django TestCase
- **Other**: Faker (for seeding), Docker (optional)

---

## Architecture

- **Monolithic Django Project**:
  - `EMS/EMS/`: Project settings and root URLs
  - `EMS/myapp/`: Main app with models, views, serializers, templates
  - `EMS/myapp/templates/`: HTML dashboards (`index.html`, `attendance_chart.html`)
  - `EMS/myapp/management/commands/seed_data.py`: Seed script for test data
  - `EMS/myapp/migrations/`: Database migrations
  - `EMS/tests/`: API and integration tests (`test_apis.py`)
  - `.env`: Environment variables for database and settings

---

## API Endpoints

All endpoints are prefixed with `/api/` (see [`EMS/EMS/urls.py`](EMS/EMS/urls.py)).

### Employee Management

- `POST /api/employees/` — Create employee
- `GET /api/employees/` — List employees (filter/search/order supported)
- `GET /api/employees/{id}/` — Retrieve employee by ID
- `PUT /api/employees/{id}/` — Update employee
- `DELETE /api/employees/{id}/` — Delete employee

### Department Management

- `GET /api/departments/` — List departments
- `POST /api/departments/` — Create department

### Attendance

- `GET /api/attendance/` — List attendance records
- `POST /api/attendance/` — Add attendance

### Performance

- `GET /api/performance/` — List performance reviews
- `POST /api/performance/` — Add review

### Analytics & Visualization

- `GET /api/employees-per-department/` — Employees count per department (for pie chart)
- `GET /api/attendance-chart/` — Monthly attendance overview (for bar chart)
- `GET /api/dashboard/` — Main dashboard page

### API Documentation

- `/swagger/` — Swagger UI
- `/redoc/` — Redoc UI

---

## Data Visualization

- **Pie Chart**: Employees per department ([`index.html`](EMS/myapp/templates/index.html))
- **Bar Chart**: Monthly attendance breakdown ([`attendance_chart.html`](EMS/myapp/templates/attendance_chart.html))

Charts are rendered using Chart.js and populated via AJAX calls to the API.

---

## Authentication & Authorization

- **Token Authentication**: Obtain a token via Django admin or DRF endpoints.
- **Permissions**: Most API endpoints require authentication (`IsAuthenticated`). See [`EMS/EMS/settings.py`](EMS/EMS/settings.py) for REST framework config.

---

## Setup & Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/employee-management-system.git
    cd employee-management-system/EMS
    ```

2. **Create & Activate Virtual Environment**
    ```bash
    python -m venv myenv
    myenv\Scripts\activate  # Windows
    # or
    source myenv/bin/activate      # Linux/Mac
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**

    Create a .env file by copying the .env.example file and then filling in your actual PostgreSQL credentials:

    cp .env.example .env
    Then edit .env:

    DEBUG=True
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=localhost
    DB_PORT=5432

5. **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

6. **Seed the Database (Optional)**
    ```bash
    python manage.py seed_data
    ```

7. **Create Superuser (for admin access)**
    ```bash
    python manage.py createsuperuser
    ```

8. **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

---

## Usage

- **API Access**: Use tools like Postman or curl with your token for authenticated requests.
- **Dashboards**: Visit `/api/dashboard/` for the main dashboard and `/api/attendance-chart/` for attendance analytics.
- **Admin Panel**: Visit `/admin/` to manage data directly.

---

## Development & Testing

- **Run Tests**
    ```bash
    pytest
    ```
    or
    ```bash
    python manage.py test
    ```

- **API Test Examples**: See [`EMS/tests/test_apis.py`](EMS/tests/test_apis.py) for sample API tests.

---

## Contributing

We welcome contributions!
1. Fork the repository
2. Create a feature branch
3. Commit your changes with clear messages
4. Submit a pull request

Please ensure your code follows Django best practices and includes tests.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For questions or support, please contact saurabhkawatra2001@gmail.com.

---

**Project maintained by Saurabh Kawatra**

---

## Deployment

- **Docker Support**: You can containerize the EMS project using Docker for easier deployment. Create a `Dockerfile` and `docker-compose.yml` in the project root to build and run the application with PostgreSQL.
- **Production Settings**: For production, set `DEBUG=False` in `.env` and configure `ALLOWED_HOSTS` in [`EMS/EMS/settings.py`](EMS/EMS/settings.py).

---

## Troubleshooting

- **Common Issues**:
  - Database connection errors: Check your credentials in `.env`.
  - Missing migrations: Run `python manage.py makemigrations` and `python manage.py migrate`.
  - Static files not loading: Run `python manage.py collectstatic` for production.
- **Logs**: Check the terminal output and Django logs for error messages.

---

## Environment Management

- **Virtual Environment**: Always activate your Python virtual environment (`myenv/`) before installing dependencies or running the server.
- **Requirements**: All Python dependencies are listed in `requirements.txt`.

---

## Key Files & Directories

- [`EMS/manage.py`](EMS/manage.py): Django management script.
- [`EMS/EMS/settings.py`](EMS/EMS/settings.py): Project settings.
- [`EMS/EMS/urls.py`](EMS/EMS/urls.py): Root URL configuration.
- [`EMS/myapp/models.py`](EMS/myapp/models.py): Data models.
- [`EMS/myapp/views.py`](EMS/myapp/views.py): API and dashboard views.
- [`EMS/myapp/serializers.py`](EMS/myapp/serializers.py): DRF serializers.
- [`EMS/myapp/templates/index.html`](EMS/myapp/templates/index.html): Dashboard (Pie Chart).
- [`EMS/myapp/templates/attendance_chart.html`](EMS/myapp/templates/attendance_chart.html): Attendance analytics (Bar Chart).
- [`EMS/myapp/management/commands/seed_data.py`](EMS/myapp/management/commands/seed_data.py): Database seeding script.
- [`EMS/tests/test_apis.py`](EMS/tests/test_apis.py): API test examples.