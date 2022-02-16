DOCUMENTATION ON THE API
RUNNING

With django and pip installed on your machine run the following commands:


run pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

NAVIGATION AND TESTING
i build the app running locally on port:: HTTP://127.0.0.1:8000/API/SURVIVORS   with recommedations well observed  from the test document.

on the api that lists all survivors infected or not, scroll to bottom to create a survivor with the fields :name, age, gender, id and last location required while inventories are optional, i made the inventories level floating numbers that reperesent what percentage over 100 of a particular inventory the survivor has. a survivor can update is location and also inventories on the on survivors details api  HTTP://127.0.0.1:8000/API/<USERNAME>/ 

to discriminate infected from those not infected i created another column ‘ is_invented ’ i made it a boolean field than automatically turns true when 3 survivors flag a user as infected. This field uses another field to count and track amount of flagging. This can be achieved by checking the boolean field  on the detail page. I c0onnected to the CPU And download then display robots’ registry in a more readable manner on http://127.0.0.1:8000/robots/ . the last endpoint is the statistical analysis of the survivors, check the end point  :: http://127.0.0.1:8000/survivorstats/  to view percentage infected number remains and all.

Also check the API http://127.0.0.1:8000/api/survivors?is_infected=true ton check all infected and http://127.0.0.1:8000/api/survivors?is_infected=false for those not . I’ve also built custom filter with the API to you’ll see the the filter icon to the top right conner of the general list api HTTP://127.0.0.1:8000/API/SURVIVORS click to filter base on your preference 