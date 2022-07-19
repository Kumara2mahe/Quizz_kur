# This file creates the database with predefined questions using the data from the data.json file


# Importing the required modules for working with database and json data
import sqlite3
import json

# Importing os to check if the JSON file is available
import os


# Function for creating and setting up a database with predefined tables and fields from a JSON file
def settingUp():

    # Function for creating tables into the database and also inserting predefined data to it
    def initializingTable(tablename, topic):

        # Getting the table if exists
        co.execute(
            """SELECT name FROM sqlite_master WHERE type='table' AND name='%s'""" % tablename)

        # Checking if the table is alreading filled
        if (co.fetchall() == []):

            # Creating a table if not exists to store the Q & A for each Topic
            co.execute("""CREATE TABLE IF NOT EXISTS %s (
                        no TEXT,
                        question TEXT,
                        option1 TEXT,
                        option2 TEXT,
                        option3 TEXT,
                        option4 TEXT,
                        correct TEXT
                        )""" % tablename)

            for i in range(1, 11):

                # Inserting data into the table
                co.execute("INSERT INTO %s VALUES (:question_no, :question_entry, :option1_entry, :option2_entry, :option3_entry, :option4_entry, :correct_entry)" % tablename,
                           {
                               "question_no": questions[topic]["quiz" + str(i)]["id"],
                               "question_entry": questions[topic]["quiz" + str(i)]["question"],
                               "option1_entry": questions[topic]["quiz" + str(i)]["option1"],
                               "option2_entry": questions[topic]["quiz" + str(i)]["option2"],
                               "option3_entry": questions[topic]["quiz" + str(i)]["option3"],
                               "option4_entry": questions[topic]["quiz" + str(i)]["option4"],
                               "correct_entry": questions[topic]["quiz" + str(i)]["correct"]
                           })

        # # ~ Deleting the table if exists
        # co.execute("DROP TABLE IF EXISTS %s" % tablename)

    # Defining the path to JSON file in a variable
    path_to_json = "./data.json"

    # Confiming that the JSON is file is in path specified
    if (os.path.exists(path_to_json)):

        # Opening the JSON file and parsing its data into a python dictionary
        with open(path_to_json, "r") as file:
            questions = json.load(file)

            # Closing the file after parsing
            file.close()

        # Connecting to the App's Database, if not exists creating a new database
        quizdata = sqlite3.connect("quizz_kur.db")

        # Creating a cursor
        co = quizdata.cursor()

        # Calling the function to setting up the quizzes for Topic-1
        initializingTable("generalquestions", "topic1")

        # Calling the function to setting up the quizzes for Topic-2
        initializingTable("techquestions", "topic2")

        # Calling the function to setting up the quizzes for Topic-3
        initializingTable("sciencequestions", "topic3")

        # Committing the changes to the database
        quizdata.commit()

        # Closing the connection with the database
        quizdata.close()

        return "initialized"

    else:
        message = "ERROR: \"data.json\" doesn't exists in the current directory"
        return message


# settingUp()
