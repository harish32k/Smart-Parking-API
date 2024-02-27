## Smart Parking API

### Description

The Flask REST API serves as the backend for the IoT Smart Parking solution. It provides endpoints for accessing, adding, deleting, and updating information in the cloud-based database server. This API is crucial for both the end-user application and the IoT modules to interact with the system.

### Components

1. **Internet of Things (IoT) Module**: Monitors parking status and updates availability to the internet.
2. **Cloud-based Database Server**: Stores all parking and user data.
3. **API Server**: Provides endpoints for end-user application and IoT module to access database information.
4. **End-user Application**: Allows users to access parking information, status updates, and navigate to available parking spots.

### Implementation Details

#### Database

- Relational database hosted on Amazon Web Services' Amazon Relational Database Service (RDS).
- MySQL DBMS used to store user info, parking info, and location info.

#### API for Database

- REST API deployed on a Heroku server, listening to HTTP requests.
- Endpoints provided for retrieving, adding, deleting, and updating information in the database.
- Handles concurrent transactions to prevent inconsistencies.
- Mobile app and IoT modules make regular API requests.
- API utilizes JSON data for communication.

This repository is setup for deployment on Heroku platform.

### Setup Instructions
1. Clone this repository to your local machine.
2. Install required dependencies using `pip install -r requirements.txt`.
3. Configure database connection settings in `config.py`.
4. Run the Flask server using `python app.py`.
