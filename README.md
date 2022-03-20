# simple_ml_deploy_using_django
A simple ML problem to be deployed over the website using django. 

- This is a simple classification ml model deployed over a website using django framwork. 

- The LOGISTIC model has been trained over the Iris dataset from sklearn module. 

- django was installed and a new django project was initiated using `django-admin startproject iris_ml_django .` command

- A new app by the name of playground was created using django-admin `startapp playground` command
- 
- `settings.py` were altered to add the `playground` app to the installed apps. 

- `view.py` in the playground app was updated with the functions to be used in the the model. 

- `urls.py` in the playground app was updated to redirect the page to the path of home and result pages.

- `include` django object was used to include the app paths to the main project `urls.py` file.

- `python manage.py runserver` command was used to run the website on server. 


## Updates coming
1. Choose from ml models to make predictions
2. Option to upload a csv file to make batch predictions
3. Use bootstrap to beautify the app
4. Add user registeration and log in form with variable functionalities for each user
5. Much more


