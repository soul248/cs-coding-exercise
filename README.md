# cs-coding-exercise

To run this exercise you just need to open up a terminal and type: `docker compose up -d --build`
Then head in your browser to [http://localhost:5108/](http://localhost:5108/) there you wild find the swagger documentation to test the endpoints. It may take a couple of minutes the first time it boots up the database.

There are 2 containers running:
 - Flask
	 - Contains a CRUD of Users and an endpoint to calculate the deegrees of separation between to users. It finds a path, not the shortest one. That would've required a graph implementation.
 - Mysql 8
	 - Contains a `cscodingexercise` database with 2 tables: `users` and `relations`.
	 - Relations has an index to help speed up the queries (not that is really needed with this small dataset)
	 - To connect to it just head to `localhost:3306` with user `cscodingexercise` and pass `cscodingexercise`

There's also a fake data creator under the folder `fake_data_creator` which basically produces an sql file to populate data for the exercise. I made a 1000 users dataset each one with relations ranging between 10 and 25 friends.