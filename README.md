<p align="center">
<img src="https://cdn.discordapp.com/attachments/1217825406699180052/1251199309542854810/banniere_format_modifie.jpg?ex=666db5a9&is=666c6429&hm=2764ce1d57f802fd7acfc1155849c421f347ac7a345442c672da10146739597c&" alt="Hbnb"/> </p>

# HBnB Evolution Project

Welcome to the HBnB Evolution project!
This project is inspired by AirBnB and aims to create a web application using Python and Flask.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [UML Diagram](#uml-diagram)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Dockerization](#dockerization)
- [Contributing](#contributing)
- [License](#license)

## Overview

The HBnB Evolution project is designed to help you learn how to build a web application from scratch. You will create a web application with the following components:

1. **Sketching with UML**: Designing the architecture using Unified Modeling Language (UML).
2. **Testing Our Logic**: Creating tests for the API and business logic.
3. **Building the API**: Implementing the API using Flask.
4. **File-Based Data Storage**: Starting with a file-based system for data storage.
5. **Packaging with Docker**: Containerizing the application using Docker.

## Project Structure

The project is organized into the following layers:

1. **Services Layer**: Handles all the requests and responses.
2. **Business Logic Layer**: Processes and makes decisions.
3. **Persistence Layer**: Manages data storage, initially file-based.

Key entities in our data model include Places, Users, Reviews, Amenities, Country, and City.

## UML Diagram

Here is a UML diagram representing the core entities and their relationships:

<img src ="https://cdn.discordapp.com/attachments/1217825406699180052/1251200281975324743/UML_classes_diagram.png?ex=666db691&is=666c6511&hm=1ebf4809d645f6b329e2229c2a2ca5149d61d4a0800e2e15a18e8ca18a9937ca&">

**Entities**:

| **Class** | **Attributes** |
|-----------|----------------|
| **Place** | `id`, `name`, `description`, `address`, `city_id`, `latitude`, `longitude`, `host_id`, `number_of_rooms`, `number_of_bathrooms`, `price_per_night`, `max_guests`, `amenities`, `reviews`, `created_at`, `updated_at` |
| **User**  | `id`, `email`, `password`, `first_name`, `last_name`, `created_at`, `updated_at` |
| **Review**| `id`, `place_id`, `user_id`, `rating`, `comment`, `created_at`, `updated_at` |
| **Amenity**| `id`, `name`, `created_at`, `updated_at` |
| **Country**| `name` |
| **City**  | `id`, `name`, `country_code`, `created_at`, `updated_at` |


## Installation instruction

```
Python Scripts:
- Python scripts must be written to run with Python 3.8.5 on Ubuntu 20.04 LTS, using python3 (version 3.8.*)
- Windows 11 WSL 2 2.1.5
- The code must follow the PEP 8 style (pycodestyle version 2.7.*).
```


1. Clone the repository:

```bash
git clone git@github.com:CLMNTDFR/holbertonschool-hbnb.git
cd holbertonschool-hbnb
```

2. Create a virtual environment and activate it:

```
python3 -m venv venv
source venv/bin/activate
```
## Dockerization

To containerize the application using Docker Compose:

1. Build and start the Docker containers:
```
docker-compose up --build
```

2. Open your browser and navigate to http://localhost:5000/ or http://0.0.0.0:5000/ to access the API graphical interface.

## Environment Configuration

- `Ubuntu` (22.04 LTS): Linux distribution
- `Docker` (26.1.3): Containerization platform
- `Gunicorn` (20.1.0): Python WSGI HTTP Server for Unix
- `Flask` (2.0.2): Micro web framework for Python
- `Flask-RESTful`: Extension for building REST APIs with Flask
- `Flask-RESTx` (0.5.1): Extension for adding swagger to Flask APIs
- `Flask-SQLAlchemy`: Flask extension for SQLAlchemy integration
- `Werkzeug` (2.0.2): WSGI utility library for Python
- `pytest` (6.2.4): Framework for running Python tests

## API Endpoints

### User Management
- **POST** `/users`: Create a new user.
- **GET** `/users`: Retrieve a list of all users.
- **GET** `/users/{user_id}`: Retrieve details of a specific user.
- **PUT** `/users/{user_id}`: Update an existing user.
- **DELETE** `/users/{user_id}`: Delete a user.

### Country and City Management
- **GET** `/countries`: Retrieve all pre-loaded countries.
- **GET** `/countries/{country_code}`: Retrieve details of a specific country.
- **GET** `/countries/{country_code}/cities`: Retrieve all cities in a specific country.
- **POST** `/cities`: Create a new city.
- **GET** `/cities`: Retrieve all cities.
- **GET** `/cities/{city_id}`: Retrieve details of a specific city.
- **PUT** `/cities/{city_id}`: Update an existing city.
- **DELETE** `/cities/{city_id}`: Delete a specific city.

### Amenity Management
- **POST** `/amenities`: Create a new amenity.
- **GET** `/amenities`: Retrieve a list of all amenities.
- **GET** `/amenities/{amenity_id}`: Retrieve detailed information about a specific amenity.
- **PUT** `/amenities/{amenity_id}`: Update an existing amenity.
- **DELETE** `/amenities/{amenity_id}`: Delete a specific amenity.

### Place Management
- **POST** `/places`: Create a new place.
- **GET** `/places`: Retrieve a list of all places.
- **GET** `/places/{place_id}`: Retrieve detailed information about a specific place.
- **PUT** `/places/{place_id}`: Update an existing place.
- **DELETE** `/places/{place_id}`: Delete a specific place.

### Review Management
- **POST** `/places/{place_id}/reviews`: Create a new review for a specified place.
- **GET** `/users/{user_id}/reviews`: Retrieve all reviews written by a specific user.
- **GET** `/places/{place_id}/reviews`: Retrieve all reviews for a specific place.
- **GET** `/reviews/{review_id}`: Retrieve detailed information about a specific review.
- **PUT** `/reviews/{review_id}`: Update an existing review.
- **DELETE** `/reviews/{review_id}`: Delete a specific review.


## Testing

To run the unit tests, use the following command:
```
python3 -m unittest discover -s tests
```
## Currently, we have 72 tests passing
```
----------------------------------------------------------------------
  Ran 72 tests in 1.362s

  OK
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Repository Files and Descriptions</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 10px;
            border: 1px solid #DDDDDD;
            text-align: left;
        }
        th {
            background-color: #F2F2F2;
        }
    </style>
</head>
<body>
    <h1>Repository Files and Descriptions</h1>
    <table>
        <thead>
            <tr>
                <th>File</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
        <tr>
                <td><code>run.py</code></td>
                        <td>entry point for executing your Flask application, initializing the app and starting the server to listen for incoming requests</td>
                </td>
            </tr>
            <tr>
                <td>app/</td>
                <td>
                    <ul>
                        <li><code>__init__.py</code>: Initializes the Flask application.</li>
                        <li><code>models/</code>: Contains the data models and database setup.</li>
                        <li><code>api/</code>: Contains the route handlers for the web application.</li>
                        <li><code>persistence/</code>: Contains files related to data persistence.</li>
                    </ul>
                </td>
            </tr>
            <tr>
                <td>tests/</td>
                        <td> directory contains various test files that verify different aspects of the application</td>
                </td>
            </tr>
            <tr>
                <td><code>README.md</code></td>
                <td>Documentation about the project, including setup instructions and usage.</td>
            </tr>
            <tr>
                <td><code>Dockerfile</code></td>
                <td>Defines the Docker image configuration, specifying the environment setup and dependencies.</td>
            </tr>
            <tr>
                <td><code>docker-compose.yml</code></td>
                <td>Defines the Docker services for the application, including the web server and database.</td>
            </tr>
            <tr>
                <td><code>requirements.txt</code></td>
                <td>Lists all the necessary Python packages and their specific versions required to run your project</td>
            </tr>
            <tr>
                <td><code>data.json</code></td>
                <td>File contains sample data that is used to populate your application's database</td>
            </tr>
            <!-- Add more rows as needed -->
        </tbody>
    </table>
</body>
</html>

### Contributing
- Delphine Hannon [Delphine-H](https://github.com/Delphine-H)
- Clément Defer [CLMNTDFR](https://github.com/CLMNTDFR)
- Stephanie Carvalho [Stefani-web](https://github.com/Stefani-web)

### License
Distributed under the MIT License. See LICENSE for more information.
[LICENSE](https://github.com/CLMNTDFR/holbertonschool-hbnb/blob/main/LICENSE)
Copyright (c) 2024 Delphine HANNON , Clement DEFER, Stephanie CARVALHO
