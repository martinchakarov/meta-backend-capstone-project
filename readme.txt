To create the same virtual environment that was used to create this project:

1. Open your terminal in the same directory that this file is located in
2. Execute the following command to create the virtual environment and install the dependencies:

    python3 -m venv env && pip3 install -r requirements.txt

3. Execute this command to activate the environment:

    source env/bin/activate (mac/Linux)

    OR

    .\env\Scripts\activate (Windows)

4. When you're done reviewing, you can use the command 'deactivate' to exit the environment

--------------------

Admin credentials:

- username: admin
- password: admin


--------------------

Routes for testing:

1. Authentication

[POST] http://127.0.0.1:8000/auth/users/ - register with username and password
[POST] http://127.0.0.1:8000/auth/token/login/ - login with username and password to obtain auth token

Then, add the Bearer token to Insomnia

2. Testing the Menu API

[GET] http://127.0.0.1:8000/restaurant/menu/ - get a list of all menu items
[POST] http://127.0.0.1:8000/restaurant/menu/ - add an item to the menu with title, price and inventory
[GET] http://127.0.0.1:8000/restaurant/menu/1 - get the first menu item if it exists
[PUT/PATCH] http://127.0.0.1:8000/restaurant/menu/1/ - update the first menu item if it exists
[DELETE] http://127.0.0.1:8000/restaurant/menu/1/ - delete the first menu item if it exists

3. Testing the Booking API

[GET] http://127.0.0.1:8000/restaurant/booking/tables/ - get a list of all bookings
[POST] http://127.0.0.1:8000/restaurant/booking/tables/ - add a booking with name, no_of_guests and booking_date (YYYY-MM-DD)
[GET] http://127.0.0.1:8000/restaurant/booking/tables/1 - get the first booking if it exists
[PUT/PATCH] http://127.0.0.1:8000/restaurant/booking/tables/1/ - update the first booking if it exists
[DELETE] http://127.0.0.1:8000/restaurant/booking/tables/1/ - delete the first booking if it exists

4. Logging out

[POST] http://127.0.0.1:8088/auth/token/logout/ - log out 
