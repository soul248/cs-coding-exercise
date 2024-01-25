from faker import Faker
from random import randrange
from random import choice

faker = Faker()

with open("cs-coding-exercise-mock-data.sql", "w") as file:
    file.write("USE cscodingexercise;\n")
    file.write("""CREATE TABLE users (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(100),
                    last_name VARCHAR(100),
                    email VARCHAR(100),
                    created_at DATETIME);\n""")
    file.write("""CREATE TABLE relations (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    user1_id INT,
                    user2_id INT,
                    created_at DATETIME);\n""")
    
    users = "INSERT INTO users (name, last_name, email, created_at) VALUES "
    for user_id in range(1, 1001):
        name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        users += f"(\"{name}\", \"{last_name}\", \"{email}\", NOW()), \n"
    file.write(users.rstrip(', \n') + "; \n")

    for user_id in range(1, 1001): 
        relations = "INSERT INTO relations (user1_id, user2_id, created_at) VALUES "
        for relation in range (1, randrange(10,25)):
            user2_id = choice([i for i in range(0,1001) if i not in [user_id]])
            relations += f"({user_id}, {user2_id}, NOW()), \n"
        file.write(relations.rstrip(', \n') + "; \n")
    
    file.write("CREATE INDEX user1_id_idx ON relations(user1_id); \n")