# Django CRM Web Application
## Overview
The Django CRM Web Application is a powerful customer relationship management (CRM) system built using Django, a high-level Python web framework, and MySQL as the database. This web application provides essential functionality for managing customer data, including user authentication (registration, login, and logout) and the ability to manipulate records (add and delete).


## Features
### User Authentication

**User Registration:** New users can create accounts by providing a username, email address, and password.
**User Login:** Registered users can securely log in using their credentials.
**User Logout:** Users can log out to end their session securely.

### Record Manipulation

**Add Records:** Authenticated users can add new records to the database. Each record includes relevant information such as customer name, contact details, and additional notes.
**Delete Records:** Users have the ability to delete records, allowing them to maintain an up-to-date and organized database.

### Database Management
**MySQL Database:** The application is designed to work seamlessly with a MySQL database, providing reliability and scalability for data storage.

### User-Friendly Interface

**Intuitive UI:** The user interface is designed with simplicity and ease of use in mind, making it accessible for users of all levels of technical expertise.

### Security
**Password Hashing:** User passwords are securely hashed and stored to protect user data.
**Session Management:** User sessions are managed to ensure secure and persistent authentication.

## Installation
To run the Django CRM Web Application locally, follow these steps:

Clone the Repository
```
git clone https://github.com/kram254/Django-CRM.git
```
Navigate to the Project Directory

```
cd django-crm
```

### Install Dependencies

```
pip install -r requirements.txt
```

## Database Configuration

Configure your MySQL database settings in the settings.py file.

### Apply Migrations

```
python manage.py migrate
```
Create a Superuser (Admin) Account
```
python manage.py createsuperuser
```

#### Run the Development Server

```
python manage.py runserver
```

### Access the Application
Open a web browser and navigate to http://localhost:8000/ to access the application.

## Usage
### User Authentication
#### Registration
Visit the registration page and provide the required information to create a new user account.

#### Login
Access the login page and enter your username and password to log in to your account.

### Logout
Click the logout button to securely end your session.

### Record Manipulation
#### Adding Records

After logging in, navigate to the "Add Record" page.
Fill in the customer details, including name, contact information, and any additional notes.
Click the "Add Record" button to save the new record.

#### Deleting Records

To delete a record, navigate to the "Delete Record" page.
Select the record you want to delete from the list.
Confirm the deletion action.

#### Deployment
For deploying this Django CRM Web Application in a production environment, it is recommended to use a web server such as Apache or Nginx, and a WSGI server like Gunicorn. Configure your server settings accordingly and make sure to secure your application and database access.

## Contributing
Contributions to this project are welcome! If you find any bugs or have ideas for improvements, please open an issue or submit a pull request. Make sure to follow the project's coding standards and guidelines.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
This project was inspired by the need for a simple and effective CRM solution.
Special thanks to the Django community for their continuous support and contributions.
### Contact Information
For questions or inquiries about this project, please contact:
**Emmanuel Ndaliro**
**Email:** markorlando 45@gmail.com
Feel free to reach out with any feedback or suggestions.
