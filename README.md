# Classwork on using the Django ORM capability from the console
#### you managed to create both models and have a foreign key linking them. You did not add the data or the full column set for the models inside the database. 3/5 Score: 2/2
## Exercise 1:
* Create new model for ```Author```
- Author should have properties for ```first_name``` and ```last_name```

* Create a new model for ```Post```
- Post should have properties for ```title```, ```content```, ```date_posted```, and ```author```
-- ```date_posted``` should automatically populate with current date on create
-- ```author``` should be a foreign key that points back to the Author of the post(s)


* Open the Django shell
- Import the models
- Create an instance of ```Author``` in the shell
- Create 3 posts associated with the author

Use the Django shell and the admin console to check that the records were created

From the shell copy the commands your entered in the shell to create the instances and the relationships AT THE BOTTOM OF THIS README.


============================

Copy the shell commands you used here!

