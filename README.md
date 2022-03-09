# DOCUMENTATION ON THE API
### the ZOMBIE APOCALYPSE 2090 MODEL

### Over view

The year is 2090 and the world as we know it has been taken over by robots. Created as once friendly robots, have now turned against humankind, especially software engineers like yourself. Their mission is to transform everyone into mindless zombies for their entertainment. You as a resistance member (and the last survivor who knows how to code), i designated to develop a system to meet the following requirements

Add survivors to the database

A survivor has an inventory of resources (which you need to declare upon the registration of the survivor). This can include Water, Food, Medication and Ammunition.

Update survivor location

A survivor have the ability to update their last location, storing the new latitude/longitude pair in the base (no need to track locations, just replacing the previous one is enough).

Flag survivor as infected

In a chaotic situation like this, it's inevitable that a survivor may get transformed into a zombie. When this happens, we need to flag the survivor as infected.
A survivor is marked as infected when at least three other survivors report their contamination.

Connect to the Robot CPU system

Connect to the robot CPU system to get a list of all robots and their known locations. Robots have two categories (Flying robots and land robots). I sort this information in a meaningful and intuitive way for humans to understand and process. I use this link to get the list of robots
https://robotstakeover20210903110417.azurewebsites.net/robotcpu

Reports

The API also provide the following information:
• Percentage of infected survivors.
• Percentage of non-infected survivors.
• List of infected survivors
• List of non-infected survivors
• List of robots


## RUNNING

To solve the issue of likely clashing dependecies, i've provided a containaerise solution. so if you have docker and docker compose intalled on your machine it's an easier story to go about


run the following :


	docker-compose build 

//to build the image web then run


	docker-compose up 


and boom!! your app is running on port :8000 

but if you still wish to continue with the conventional local running, follow the instructions bellow:




With python and pip installed on your machine run the following commands:


run:

	pip install -r requirements.txt

	python manage.py migrate

	python manage.py runserver

# NAVIGATION AND TESTING

i build the app running locally on port:: HTTP://127.0.0.1:8000/API/SURVIVORS   with recommedations well observed  from the test document.

on the api that lists all survivors infected or not, scroll to bottom to create a survivor with the fields :name, age, gender, id and last location required while inventories are optional, i made the inventories level floating numbers that reperesent what percentage over 100 of a particular inventory the survivor has. a survivor can update is location and also inventories on the on survivors details api  HTTP://127.0.0.1:8000/API/<USERNAME>/ 

to discriminate infected from those not infected i created another column ‘ is_invented ’ i made it a boolean field than automatically turns true when 3 survivors flag a user as infected. This field uses another field to count and track amount of flagging. This can be achieved by checking the boolean field  on the detail page. I c0onnected to the CPU And download then display robots’ registry in a more readable manner on http://127.0.0.1:8000/robots/ . the last endpoint is the statistical analysis of the survivors, check the end point  :: http://127.0.0.1:8000/survivorstats/  to view percentage infected number remains and all.

Also check the API http://127.0.0.1:8000/api/survivors?is_infected=true ton check all infected and http://127.0.0.1:8000/api/survivors?is_infected=false for those not . I’ve also built custom filter with the API to you’ll see the the filter icon to the top right conner of the general list api HTTP://127.0.0.1:8000/API/SURVIVORS click to filter base on your preference 

  
  
# Limitations:

  

1. the recommendation limits to authentication so some intuitive functionalitis might not be in this app yet. 


thanks 

SODIQ
