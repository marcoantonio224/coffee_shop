# Uda-Spice Latte Cafe

  ## Description
    This is the backend server for Uda-Spice Latte Cafe for Udacity's users,
    baristas, and managers. Here we composed 3 main features for Public Users,
    Baristas, and Managers.

  ## Coding Style
    The backend was configured using RESTful API patterns with Flask and Auth0 (a third party authentication system)

  ## Technologies
   Backend: [Python], [Flask], ['SQLAlchemy'], [PostgreSQL]

  ## Getting Started

   ### Create Local Environment
   - If not done so, please install virtual environment. This keeps your dependencies for each project separate and organized:  `pip install virtualenv`

   - Then create the environment inside the src folder:
    1. virtualenv cs_env
    2. cd cs_env
    3. source bin/activate
    To **deactivate** environment, type: `deactivate`

    ### Install Prerequisites
      Please install first all the modules for the project to get it started if you haven't done so already. Make sure you are in the parent directory of requirements.txt.
      Command: `pip install -r requirements.txt`

    ### Server Side Development
      To run a Flask application, make sure you set up the proper environmental variables within the command line and run the application for the backend.

    ### Database Setup.
      This application uses MySQL for database management. Keep in mind on line 18 of `api.py` there's code commented out `# db_drop_and_create_all()`. If you were to uncomment this code, it will erase the drinks and restart the database. Its allows the postman to run tests correctly when the database is dropped and created again because the test revolves around the drink with `id` of `1`.


    ### Commands:
    Make sure to be in the **src** directory for assigning `api.py` to the FLASK_APP variable. Then proceed with the following commands.
    `export FLASK_APP=api.py`  (Sets the application)
    `flask run --reload` (Sets the project in development mode with --reload)

    ### Authentication
    Our application consists of an authenticated system with Auth0. There are 3 Roles for a user, only 2 require permission of for certain operations delineated below:
      1. Public (See all drinks)
        `No permission needed.`
      2. Barista (See the drinks details)
        `permission['get:drinks-detail']`
      3. Manager (Able to create, edit, remove, and see the details of a drink)
        `permission['get:drinks-detail', post:drinks, patch:drinks, delete:drinks	]`

    Only the developer who created the Auth0 application/api can assign roles to particular email addresses. The permission allows the user to perform certain tasks, otherwise would get a 401 error **Unauthorized**.
      - `get:drinks-detail`: Able to see the ingredients of the drink
      - `post:drinks`: Able to create a new drink.
      - `patch:drinks`: Edit an existing drink.
      - `delete:drinks`: Delete a drink.

    These permissions come from a valid/authenticated token from Auth0. If not familiar with Auth0, please click link below to learn about it [https://auth0.com/docs/get-started]

  ### API Endpoints
    Here are the endpoints of our API application.
    **Base URL**: [http://127.0.0.1:5000]
    **API Keys**: This version of the application **does**  require authentication or API Keys.

    Our RESTful API application are tested using postman.
    If you do not have postman installed, please take the time to install it [https://www.postman.com/downloads/]

    Once installed, You can import the data from
    `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`

    ***NOTE***: The **API TOKENS** for `MANAGER` and `BARISTA` in `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json` are only valid for testing purposes with `POSTMAN` for 20 days as of starting today (08/14/2020).

    Hit the Runner feature in postman to run and test all endpoints.

    You can see the results for the tested endpoints in  `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_test_run.json`

    ## Deployment
      `N/A`

    ## Authors
    - Marco A. Canchola (Full Stack Developer)
    - Udacity Instructors

    ## Acknowledgements
    - Udacity
    - Auth0 (https://auth0.com/)
    - Python Docs (https://docs.python.org/3/tutorial/venv.html)
    - Postman (https://www.guru99.com/postman-tutorial.html)
