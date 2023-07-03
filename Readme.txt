/api/Booking

Step 1 – Setting up the project

Sign up and login to 
http://github.com
. Create a new repository named LittleLemon.

Clone your directory called workspace in your local machine.

Create a Python virtual environment in the workspace directory.

Install the Django framework in this virtual environment.

Create a Django project called LittleLemon.

Create a new Django app called restaurant.

Define the index() view that renders the home page of your application – index.html. Configure the URL routes.

Put the index.html in the templates folder under the BASE_DIR.

Run the server and check if the home page is displayed.

Default Django installation homepage
Clone your GitHub repository in the outer LittleLemon folder.

Add and commit the project files.

Push the changes to the remote repository.


Step 2 – Setting up the MySQL database and users

Install the mysqlclient library.

Configure your project for the MySQL database.

Declare the Menu and Reservation models.

Migrate the models.

Register the models with the admin app.

Create a superuser.

Add and commit the changes to your project.

Push the changes to the remote repository.

Step 3 – Implementing the Django REST Framework

Install the Django REST Framework.

Add restframework to INSTALLED_APPS and run migrations

Declare serializer classes for the menu and reservation models

Declare ModelViewSet classes for the menu and reservation models, and set the serializer_class attribute of each.

Use DefaultRouter to register views.

Add the routers.urls to URLConf.

With DRF’s browsable API, perform CRUD operations on menu and reservation models.

Add and commit the changes to your project.

Push the changes to the remote repository.

Step 4 – Installing Djoser and testing with Insomnia

Install the djoser library

Add djoser to INSTALLED_APPS and run migrations

Configure the settings.py file for token authentication.

Set the permission_classes attribute of the ViewSets to IsAuthenticated

Obtain the authorization token from the admin interface.

Use the token to authenticate the API endpoints.

Use Insomnia to test the API endpoints.

Insomnia Client with Post request
Add and commit the changes to your project.

Push the changes to the remote repository.

Step 5 – Creating the unit tests

Create a tests folder in the LittleLemon project package folder.

Use Django’s testing framework to write unit tests for testing the models and views.

Run the tests using manage.py. 

Add and commit the changes to your project.

Push the changes to the remote repository.
