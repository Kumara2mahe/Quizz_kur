# --- Quizz-kur --- a quiz application designed by Kumara


# importing tkinter and tkinter.ttk modules for creating the GUI
from tkinter import *
from tkinter.ttk import *

# importing sqlite3 for create and work with databases
import sqlite3

# importing a setup function to setting up this application, with more dynamic functionality
from setup import settingUp


root = Tk()

# Giving Title to the root window
root.title("Quizz-kur")

# Setting the window width, height and position on the user screen
root.geometry("600x400+400+150")

# This makes the quiz apps window non-resizable
root.resizable(0, 0)

# Assigning the image as an object of PhotoImage class.
p1 = PhotoImage(file="./Images/icon.png")
# Setting that image as an icon to the window
root.iconphoto(False, p1)

# Defining a variable to track Start-Button click
err_attempt = 0

# Defining initial values for Score
point = 0

# Assigning a variable to check a function is called or not
tryInitiatorCall = False


# Function which creates the Home-Screen
def main():

    # Function which creates the User-Select panel with buttons for both admins and guests
    def userSelect():

        # Function which is operated by the User-Select's Back-Button
        def back1():

            # Disabling the Back-Button after clicked, for preventing the function to be called twice
            back1_button.configure(state=DISABLED)

            # Destroying all the widgets created in the User-Select panel
            root.after(600, lambda: back1_button.destroy())
            root.after(500, lambda: guest.destroy())
            root.after(500, lambda: admin.destroy())
            root.after(500, lambda: label1.destroy())

            # Calling the function to show the Home-Screen
            root.after(800, lambda: main())

        ##

        # Function which is operated by the User-Select's Admin-Button
        def admins():

            # ------------------------------------- Admin (404) -StyleStarts----------------------------------------------------

            # Function to show the developement message and also redirecting back to User-Select panel
            def adminOptions():

                # Creating new labels to create message
                message1 = Label(text="Error: 404", font=("Dodge", 33),
                                 foreground="#0A014F", background="#D4B0F9")
                message1.place(relx=0.5, rely=0.3, anchor=CENTER)

                message1_1 = Label(text="This is function is still in the developent stage\nTry Again later. ", font=("Dodge", 16),
                                   foreground="#0A014F", background="#D4B0F9", wraplength=600, justify=CENTER)
                message1_1.place(relx=0.5, rely=0.5, anchor=CENTER)

                # Creating the redirecting message label with a countdown timer
                message1_2 = Label(text="...redirecting in 5s", font=("Dodge", 12),
                                   foreground="#0A014F", background="#D4B0F9")
                message1_2.place(relx=0.25, rely=0.9, anchor=CENTER)  # 912F56

                # Animating the redirecting message label color and countdown
                root.after(250, lambda: message1_2.configure(
                    foreground="#912F56"))
                root.after(500, lambda: message1_2.configure(
                    foreground="#0A014F"))
                root.after(750, lambda: message1_2.configure(
                    foreground="#912F56"))
                root.after(1000, lambda: message1_2.configure(
                    text="...redirecting in 4s", foreground="#0A014F"))
                root.after(1250, lambda: message1_2.configure(
                    foreground="#912F56"))
                root.after(1500, lambda: message1_2.configure(
                    foreground="#0A014F"))
                root.after(1750, lambda: message1_2.configure(
                    foreground="#912F56"))
                root.after(2000, lambda: message1_2.configure(
                    text="...redirecting in 3s", foreground="#0A014F"))
                root.after(2250, lambda: message1_2.configure(
                    foreground="#912F56"))
                root.after(2500, lambda: message1_2.configure(
                    foreground="#0A014F"))
                root.after(2750, lambda: message1_2.configure(
                    foreground="#912F56"))
                root.after(3000, lambda: message1_2.configure(
                    text="...redirecting in 2s", foreground="#0A014F"))
                root.after(3250, lambda: message1_2.configure(
                    foreground="#912F56"))
                root.after(3500, lambda: message1_2.configure(
                    foreground="#0A014F"))
                root.after(3750, lambda: message1_2.configure(
                    foreground="#912F56"))
                root.after(4000, lambda: message1_2.configure(
                    text="...redirecting in 1s", foreground="#0A014F"))

                # Destroying all the widgets created by the
                root.after(4100, lambda: message1_1.destroy())
                root.after(4300, lambda: message1.destroy())
                root.after(4500, lambda: message1_2.destroy())

                # Calling the function to redirect to the User-Select panel
                root.after(5000, lambda: userSelect())

            # Disabling the Admin-Button after clicked, for preventing the function to be called twice
            admin.configure(state=DISABLED)

            # Destroying all the widgets created in the User-Select panel
            root.after(500, lambda: guest.destroy())
            root.after(600, lambda: admin.destroy())
            root.after(500, lambda: back1_button.destroy())
            root.after(500, lambda: label1.destroy())

            # Calling the function to show the development message
            root.after(800, lambda: adminOptions())

        # -------------------------------------------------------------------------------------------- Admin (404) Panel -StyleEnds----

        ##

        # Function which is operated by the User-Select's Guest-Button
        def users():

            # Function which creates the Topic-Selection panel with multiple Topic-Buttons for each kind of quiz topic
            def topicSelectionPanel():

                # Function which is operated by the Topic-Select Panel's Back-Button
                def back2():

                    # Disabling the Back-Button after clicked, for preventing the function to be called twice
                    back2_button.configure(state=DISABLED)

                    # Destroying all the widgets created in the Topic-Select Panel
                    root.after(600, lambda: back2_button.destroy())
                    root.after(500, lambda: topic_button1.destroy())
                    root.after(500, lambda: topic_button2.destroy())
                    root.after(500, lambda: topic_button3.destroy())
                    root.after(500, lambda: label2.destroy())
                    root.after(500, lambda: label3.destroy())
                    root.after(500, lambda: label31.destroy())

                    # Calling the function to redirect to the User-Select panel
                    root.after(800, lambda: userSelect())

                # >>

                # Function which creates a LeaderBoard-Button and Exit-Button which quits the App for the ScoreCard Panel
                def creatingExit():

                    def exitingScoreCard():

                        # Disabling the Exit-Button after clicked, for preventing the function to be called twice
                        exit_button.configure(state=DISABLED)

                        # Destroying all the widgets created and visible in the ScoreCard Panel
                        root.after(400, lambda: score_button.destroy())
                        root.after(400, lambda: try_button.destroy())
                        root.after(400, lambda: label3.destroy())
                        root.after(500, lambda: scoreboard.destroy())
                        root.after(500, lambda: label31.destroy())
                        root.after(500, lambda: scoreLabel.destroy())
                        root.after(600, lambda: exit_button.destroy())

                        # Resetting the Guest score to zero
                        global point
                        point = 0

                        # Calling the function to redirect to the User-Select panel
                        root.after(700, lambda: userSelect())

                    # >>

                    # Function which is operated by the LeaderBoard-Button in the ScoreCard-Panel to collect the top 5 scores from the database
                    def leaderboard():

                        # Function which creates the leaderboard with the top 5 data collected from the database
                        def leaderboard_show():

                            # Function which is operated by the LeaderBoard's Back-Button
                            def leaderboard_hide():

                                # Disabling the Back-Button after clicked, for preventing the function to be called twice
                                score_button.configure(state=DISABLED)

                                # Destroying all the widgets created in the leaderboard
                                leaderboard_subtitle.destroy()
                                leaderboard_name_label.destroy()
                                leaderboard_score_label.destroy()
                                leaderboard_text.destroy()
                                leaderboard_background.destroy()
                                leaderboard_title.destroy()

                                # Changing back the Back-Button text to Leaderboard-Button and also changing the function assigned to it
                                root.after(100, lambda: score_button.configure(
                                    text="LeaderBoard", state=NORMAL, command=lambda: leaderboard()))

                                # Enabling the ScoreCard Panel's Exit-Button
                                exit_button.configure(state=NORMAL)

                                # Showing the total-score and TryMore-Button
                                scoreLabel.configure(foreground="#F8FFE5")

                                # Showing TryMore-Button if exists
                                try:
                                    try_button.lift()
                                except:
                                    pass

                            # ------------------------------------- Leaderboard -StyleStarts----------------------------------------------------

                            # Changing the text on the Leaderboard-Button to a Back-Button and also changing the function assigned to it
                            root.after(100, lambda: score_button.configure(
                                text="< back", state=NORMAL, command=lambda: leaderboard_hide()))

                            # Disabling the Exit-Button and Hiding the total-score when the leaderboard is open
                            exit_button.configure(state=DISABLED)
                            scoreLabel.configure(foreground="#1E0905")

                            # Hiding TryMore-Button if exists
                            try:
                                try_button.lower()
                            except:
                                pass

                            # Creating a background for the leaderboard panel
                            leaderboard_background = Canvas(
                                root, width=400, height=280, background="#1E0905")
                            leaderboard_background.place(
                                relx=0.55, rely=0.53, anchor=CENTER)

                            # Creating a label to show the leaderboard Title
                            leaderboard_title = Label(
                                root, text="LeaderBoard", font=("Dodge", 20, "bold", "italic"),
                                foreground="#F5F749", background="#1E0905")
                            leaderboard_title.place(
                                relx=0.55, rely=0.1, anchor=CENTER)

                            # Styling the leaderboard sub-Title labels
                            leaderboard_subtitle_style = Style()
                            leaderboard_subtitle_style.theme_use("default")
                            leaderboard_subtitle_style.configure("L.TLabel", font=("Dodge", 15, "bold", "italic"),
                                                                 foreground="#BF09D5", background="#1E0905", borderwidth=2, width=30, height=10, focuscolor="none")

                            # Creating a label to show the leaderboard sub-Titles
                            leaderboard_subtitle = Label(
                                root, text="Name                               Score\r\n", style="L.TLabel")
                            leaderboard_subtitle.place(
                                relx=0.55, rely=0.3, anchor=CENTER)

                            # Styling the GuestNames displayed in the leaderboard
                            leaderboard_name_label_style = Style()
                            leaderboard_name_label_style.theme_use("default")
                            leaderboard_name_label_style.configure("G.TLabel", font=("Dodge", 13, "bold", "italic"),
                                                                   foreground="#F8FFE5", background="#1E0905", borderwidth=2, width=30, height=10, focuscolor="none")

                            # Creating new label to show the GuestNames
                            leaderboard_name_label = Label(
                                root, text=show_names, style="G.TLabel")
                            leaderboard_name_label.place(
                                relx=0.25, rely=0.35, anchor=NW)

                            # Styling the GuestScores displayed in the leaderboard
                            leaderboard_score_label_style = Style()
                            leaderboard_score_label_style.theme_use("default")
                            leaderboard_score_label_style.configure("P.TLabel", font=("Dodge", 13, "bold", "italic"),
                                                                    foreground="#F8FFE5", background="#1E0905", borderwidth=2, width=10, height=30, focuscolor="none")

                            # Creating new label to show the GuestScores
                            leaderboard_score_label = Label(
                                root, text=show_scores, style="P.TLabel")
                            leaderboard_score_label.place(
                                relx=0.88, rely=0.35, anchor=NE)

                            # Styling the message about the leaderboard
                            leaderboard_text = Style()
                            leaderboard_text.theme_use("default")
                            leaderboard_text.configure("T.TLabel", font=("Dodge", 9, "bold", "italic"),
                                                       foreground="#F6F67C", background="#1E0905")

                            # Creating new label to show the message about the leaderboard
                            leaderboard_text = Label(
                                root, text="* leaderboard showing   TOP 5", style="T.TLabel")
                            leaderboard_text.place(
                                relx=0.84, rely=0.96, anchor=CENTER)

                            # -------------------------------------------------------------------------------------------- Leaderboard -StyleEnds----

                        # >>

                        # Disabling the LeaderBoard-Button after clicked, for preventing the function to be called twice
                        score_button.configure(state=DISABLED)

                        # Connecting to the App's Database, if not exists creating a new database
                        quizdata = sqlite3.connect("quizz_kur.db")

                        # Creating a cursor
                        co = quizdata.cursor()

                        # Creating a 'leaderboard' table if not exists to store the Guestname and score
                        co.execute("""CREATE TABLE IF NOT EXISTS leaderboard (
                                    playername text,
                                    score integer
                                    )""")

                        # Querying the database and collect the top 5 scored users
                        co.execute(
                            "SELECT * FROM leaderboard ORDER BY score DESC")
                        points = co.fetchmany(5)

                        # Separating the names from the collected data
                        show_names = " "
                        for record in points:
                            show_names += str(record[0]) + "\r\n "

                        # Separating the scores from the collected data
                        show_scores = " "
                        for record in points:
                            show_scores += str(record[1]) + "\r\n "

                        # Committing the changes to the database
                        quizdata.commit()

                        # Closing the connection with the database
                        quizdata.close()

                        # Calling the function to create the leaderboard
                        root.after(500, lambda: leaderboard_show())

                    # >>

                    # ------------------------------------- ScoreCard Panel Button -StyleStarts----------------------------------------------------

                    # Creating a Exit-Button to quit the App
                    global exit_button
                    exit_button = Button(root, text="EXIT",
                                         style="E.TButton", command=lambda: exitingScoreCard())
                    exit_button.place(relx=0.1, rely=0.9, anchor=CENTER)

                    # Creating a LeaderBoard-Button to view your position in leaderboard
                    score_button_style = Style(root)
                    score_button_style.theme_use("default")
                    score_button_style.configure("L.TButton", font=("Playball", 10, "bold", "italic"),
                                                 foreground="#0A0908", background="#F6F67C", borderwidth=2, width=15, height=4, focuscolor="none")
                    # Mouse Hovering style
                    score_button_style.map("L.TButton", foreground=[
                        ("active", "!disabled", "#F0EFF4")], background=[("active", "#DB12AF")])

                    global score_button
                    score_button = Button(
                        root, text="LeaderBoard", style="L.TButton", command=lambda: leaderboard())
                    score_button.place(relx=0.22, rely=0.05, anchor=NE)

                    # -------------------------------------------------------------------------------------------- ScoreCard Panel Button -StyleEnds----

                # >>

                # Function for counting correct answers giving point according to that
                def points():

                    global point
                    point += 1

                # Function for displaying the Total Score
                def finalScore():

                    global scoreLabel
                    scoreLabel = Label(root, text=point,
                                       font=("Dodge", 25, "bold"), foreground="#F8FFE5", background="#1E0905")
                    scoreLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

                # >>

                # Function for displaying the GuestName centered above the score
                def scoreCard(quizNumber):

                    # Creating a new label to show the page Title
                    global scoreboard
                    scoreboard = Label(root, text="ScoreBoard", font=("Dodge", 10, "italic"),
                                       foreground="#F8FFE5", background="#1E0905")
                    scoreboard.place(relx=0.5, rely=0.25, anchor=CENTER)

                    # Re-aligning the GuestName to the center above the score
                    label31.configure(
                        text=text3, font=("Playball", 24, "bold"))
                    label31.place(relx=0.5, rely=0.35, anchor=CENTER)

                    # Connecting to the App's Database, if not exists creating a new database
                    quizdata = sqlite3.connect("quizz_kur.db")

                    # Creating a cursor
                    co = quizdata.cursor()

                    # Checking if the Leaderboard updated for the first time or not
                    if (quizNumber == 10):

                        # Creating a 'leaderboard' table if not exists to store the Guestname and score
                        co.execute("""CREATE TABLE IF NOT EXISTS leaderboard (
                                    playername TEXT,
                                    score INTEGER
                                    )""")

                        # Updating the leaderboard by creating new Guest's name and total score
                        co.execute("INSERT INTO leaderboard VALUES (:text3, :point)",
                                   {
                                       "text3": text3,
                                       "point": point
                                   })

                    else:

                        # Updating the Guest Score in the matching name to the 'leaderboard' table in the Database
                        co.execute("UPDATE leaderboard SET score = :guest_score WHERE playername = :guest_name",
                                   {
                                       "guest_score": point,
                                       "guest_name": text3
                                   })

                    # Committing the changes to the database
                    quizdata.commit()

                    # Closing the connection with the database
                    quizdata.close()

                # >>

                # Function which creates a Try-More button in the ScoreCard Panel
                def createTryMore(topicName, topicTable, quizNumber):

                    # Function which creates the Rules Panel for the second time with a Quiz Initiating Timer
                    def quizInitiator(topicName, topicTable, quizNumber):

                        global tryInitiatorCall

                        # Checking if the function is called twice
                        if (tryInitiatorCall):

                            # Creating a label to show the screen Title
                            label2 = Label(root, text="Rules", font=("Dodge", 30),
                                           foreground="#D1E3DD", background="#1E0905")
                            label2.place(relx=0.5, rely=0.12, anchor=CENTER)

                            # Displaying the rules for the Quiz
                            rules = Message(root, text="    1. Each question has a time limit of 15 seconds.\r\n    2. Once the option is selected it can't be changed.\r\n    3. Final Score is displayed at the end.\r\n    4. The following questions are based on '%s'." % topicName, font=("Dodge", 12),
                                            foreground="#D1E3DD", background="#1E0905", width=450)
                            rules.place(relx=0.5, rely=0.42, anchor=CENTER)

                            # Creating and Displaying the Quiz Initiating Timer
                            initTimer = Label(text="Quiz starts in 5 seconds . ... .", font=("Dodge", 12),
                                              foreground="#F6F67C", background="#1E0905")
                            root.after(1000, lambda: initTimer.place(
                                relx=0.68, rely=0.9, anchor=CENTER))

                            # Periodically changing the Time-remaining after 1s
                            root.after(1950, lambda: initTimer.configure(
                                text=""))
                            root.after(2000, lambda: initTimer.configure(
                                text="Quiz starts in 4 seconds .  ...."))
                            root.after(2950, lambda: initTimer.configure(
                                text=""))
                            root.after(3000, lambda: initTimer.configure(
                                text="Quiz starts in 3 seconds . ... ."))
                            root.after(3950, lambda: initTimer.configure(
                                text=""))
                            root.after(4000, lambda: initTimer.configure(
                                text="Quiz starts in 2 seconds .... ."))
                            root.after(4950, lambda: initTimer.configure(
                                text=""))
                            root.after(5000, lambda: initTimer.configure(
                                text="Quiz starts in 1 second . ... ."))
                            root.after(5950, lambda: initTimer.configure(
                                text=""))

                            # Destroying all the widgets created in the Rules Panel for the second time
                            root.after(6000, lambda: label2.destroy())
                            root.after(6000, lambda: rules.destroy())
                            root.after(6000, lambda: initTimer.destroy())

                            # Re-assigning the variable to default value
                            tryInitiatorCall = False

                            # Increasing the question number
                            quizNumber += 1

                            # Calling the function to create more Quiz
                            root.after(6200, lambda: quizQuestion(
                                topicName, topicTable, quizNumber))

                        else:

                            # Re-assigning the variable to confirm function called
                            tryInitiatorCall = True

                            # Resizing and Re-aligning the GuestName back to the NorthEast corner
                            root.after(800, lambda: label31.configure(
                                font=("Dodge", 15, "bold")))
                            root.after(800, lambda: label31.place(
                                relx=0.995, rely=0.094, anchor=E))

                            # Destroying all the widgets created in the ScoreCard Panel
                            root.after(400, lambda: score_button.destroy())
                            root.after(600, lambda: scoreboard.destroy())
                            root.after(600, lambda: scoreLabel.destroy())
                            root.after(400, lambda: exit_button.destroy())
                            root.after(900, lambda: try_button.destroy())

                            # Calling the function to create the Rules Panel for the second time
                            root.after(1300, lambda: quizInitiator(
                                topicName, topicTable, quizNumber))

                    # >>

                    # ------------------------------------- TryMore-Button -StyleStarts----------------------------------------------------

                    # Creating a TryMore-Button to anwser more quiz
                    # Styling TryMore-Button
                    try_button_style = Style()
                    try_button_style.theme_use("default")
                    try_button_style.configure("W.TButton", font=("Playball", 12, "bold", "italic"),
                                               foreground="#F0EFF4", background="#BF09D5", borderwidth=2, width=10, focuscolor='none')
                    # Mouse Hovering style
                    try_button_style.map('W.TButton', foreground=[(
                        'active', '!disabled', '#F0EFF4')], background=[('active', '#DB12AF')])

                    # TryMore-Button
                    global try_button
                    try_button = Button(root, text="Try more..",
                                        style="W.TButton", command=lambda: quizInitiator(topicName, topicTable, quizNumber))
                    try_button.place(
                        relx=0.5, rely=0.7, anchor=CENTER)

                    # -------------------------------------------------------------------------------------------- TryMore-Button -StyleEnds----

                # >>

                # Function which creates the Quiz from the data collected from the database, also with a CountDownTimer
                def quizQuestion(topicName, topicTable, quizNumber):

                    # ------------------------------------- Selected & Correct Option -StyleStarts----------------------------------------------------

                    # Function for displaying the Correct-Answer
                    def ques_Correct():

                        # Checking which Option matches to the Correct-Answer and Styling it to Green color
                        if (v1.get() == correct_option):
                            ques_Opt1.configure(
                                style="C.TRadiobutton", state=DISABLED)
                            ques_Opt2.configure(state=DISABLED)
                            ques_Opt3.configure(state=DISABLED)
                            ques_Opt4.configure(state=DISABLED)

                        elif (v2.get() == correct_option):
                            ques_Opt2.configure(
                                style="C.TRadiobutton", state=DISABLED)
                            ques_Opt1.configure(state=DISABLED)
                            ques_Opt3.configure(state=DISABLED)
                            ques_Opt4.configure(state=DISABLED)

                        elif (v3.get() == correct_option):
                            ques_Opt3.configure(
                                style="C.TRadiobutton", state=DISABLED)
                            ques_Opt2.configure(state=DISABLED)
                            ques_Opt1.configure(state=DISABLED)
                            ques_Opt4.configure(state=DISABLED)

                        elif (v4.get() == correct_option):
                            ques_Opt4.configure(
                                style="C.TRadiobutton", state=DISABLED)
                            ques_Opt2.configure(state=DISABLED)
                            ques_Opt3.configure(state=DISABLED)
                            ques_Opt1.configure(state=DISABLED)

                    # Function which is triggered by Option-4 button
                    def ques_Opt_4():

                        # Disabling all Options and Coloring Option-4 to yellow color
                        ques_Opt4.configure(
                            style="O.TRadiobutton", state=DISABLED)
                        ques_Opt1.configure(state=DISABLED)
                        ques_Opt2.configure(state=DISABLED)
                        ques_Opt3.configure(state=DISABLED)

                        # Checking if Option-4 matches to the Correct-Answer
                        if (v4.get() == correct_option):

                            # Calling the function to add one point to the Guest for current Quiz
                            root.after(2000, lambda: points())

                        else:

                            # Setting the Wrong-Answer to red color
                            root.after(2000, lambda: ques_Opt4.configure(
                                style="X.TRadiobutton"))

                    # Function which is triggered by Option-3 button
                    def ques_Opt_3():

                        # Disabling all Options and Coloring Option-3 to yellow color
                        ques_Opt3.configure(
                            style="O.TRadiobutton", state=DISABLED)
                        ques_Opt1.configure(state=DISABLED)
                        ques_Opt2.configure(state=DISABLED)
                        ques_Opt4.configure(state=DISABLED)

                        # Checking if Option-3 matches to the Correct-Answer
                        if (v3.get() == correct_option):

                            # Calling the function to add one point to the Guest for current Quiz
                            root.after(2000, lambda: points())

                        else:

                            # Setting the Wrong-Answer to red color
                            root.after(2000, lambda: ques_Opt3.configure(
                                style="X.TRadiobutton"))

                    # Function which is triggered by Option-2 button
                    def ques_Opt_2():

                        # Disabling all Options and Coloring Option-2 to yellow color
                        ques_Opt2.configure(
                            style="O.TRadiobutton", state=DISABLED)
                        ques_Opt1.configure(state=DISABLED)
                        ques_Opt3.configure(state=DISABLED)
                        ques_Opt4.configure(state=DISABLED)

                        # Checking if Option-2 matches to the Correct-Answer
                        if (v2.get() == correct_option):

                            # Calling the function to add one point to the Guest for current Quiz
                            root.after(2000, lambda: points())

                        else:

                            # Setting the Wrong-Answer to red color
                            root.after(2000, lambda: ques_Opt2.configure(
                                style="X.TRadiobutton"))

                    # Function which is triggered by Option-1 button
                    def ques_Opt_1():

                        # Disabling all Options and Coloring Option-1 to yellow color
                        ques_Opt1.configure(
                            style="O.TRadiobutton", state=DISABLED)
                        ques_Opt2.configure(state=DISABLED)
                        ques_Opt3.configure(state=DISABLED)
                        ques_Opt4.configure(state=DISABLED)

                        # Checking if Option-1 matches to the Correct-Answer
                        if (v1.get() == correct_option):

                            # Calling the function to add one point to the Guest for current Quiz
                            root.after(2000, lambda: points())

                        else:

                            # Setting the Wrong-Answer to red color
                            root.after(2000, lambda: ques_Opt1.configure(
                                style="X.TRadiobutton"))

                    # -------------------------------------------------------------------------------------------- Selected & Correct Option -StyleEnds----

                    # >>

                    # ------------------------------------- Quiz-Template -StyleStarts----------------------------------------------------

                    # Connecting to the App's Database, if not exists creating a new database
                    quizzkur_DB = sqlite3.connect("quizz_kur.db")

                    # Creating a cursor
                    co = quizzkur_DB.cursor()

                    # Querying the specified table in the database and collecting the total Quiz-number
                    co.execute("SELECT * FROM %s" % (topicTable))
                    totalquiz = len(co.fetchall())

                    # Querying the specified table in the database and collecting the quiz which matchs the Quiz-number
                    co.execute(
                        "SELECT *, oid FROM %s WHERE oid = %s" % (topicTable, str(quizNumber)))
                    quiz_data = co.fetchall()

                    # Assigning each record into a separate variable
                    for record in quiz_data:
                        q_number = record[0]
                        question = record[1]
                        option1 = record[2]
                        option2 = record[3]
                        option3 = record[4]
                        option4 = record[5]
                        correct_option = record[6]

                    # Committing the changes to the database
                    quizzkur_DB.commit()

                    # Closing the connection with the database
                    quizzkur_DB.close()

                    # Creating new label to show the Quiz-Question
                    label = Label(root, text=q_number + ".    " + question, font=("Dodge", 14),
                                  foreground="#D1E3DD", background="#1E0905", width=40, wraplength=450)
                    label.place(relx=0.85, rely=0.25, anchor=E)

                    # Styling the Quiz-Options
                    ques_Opt_style = Style(root)
                    ques_Opt_style.theme_use("default")
                    ques_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                             foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                    ques_Opt_style.map('TRadiobutton', foreground=[
                        ('active', '!disabled', '#0A0908')], background=[('active', '#F5F749')])

                    # Creating the Quiz-Options
                    # Creating Option-1 and assigning the value and styler function
                    v1 = StringVar(root)
                    v1.set(option1)
                    ques_Opt1 = Radiobutton(root, text=option1, variable=v1,
                                            value=option1, command=lambda: ques_Opt_1())
                    ques_Opt1.place(
                        relx=0.35, rely=0.42, anchor=CENTER)

                    # Creating Option-2 and assigning the value and styler function
                    v2 = StringVar(root)
                    v2.set(option2)
                    ques_Opt2 = Radiobutton(root, text=option2, variable=v2,
                                            value=option2, command=lambda: ques_Opt_2())
                    ques_Opt2.place(
                        relx=0.35, rely=0.52, anchor=CENTER)

                    # Creating Option-3 and assigning the value and styler function
                    v3 = StringVar(root)
                    v3.set(option3)
                    ques_Opt3 = Radiobutton(root, text=option3, variable=v3,
                                            value=option3, command=lambda: ques_Opt_3())
                    ques_Opt3.place(
                        relx=0.35, rely=0.62, anchor=CENTER)

                    # Creating Option-4 and assigning the value and styler function
                    v4 = StringVar(root)
                    v4.set(option4)
                    ques_Opt4 = Radiobutton(root, text=option4, variable=v4,
                                            value=option4, command=lambda: ques_Opt_4())
                    ques_Opt4.place(
                        relx=0.35, rely=0.72, anchor=CENTER)

                    # ------- Validation Styles for Options ----------
                    # Selected-Option Style
                    selectedOpt_style = Style(root)
                    selectedOpt_style.theme_use("default")
                    selectedOpt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor='none')

                    # Wrong-Option Style
                    wrongOpt_style = Style(root)
                    wrongOpt_style.theme_use("default")
                    wrongOpt_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                             foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor='none')

                    # Correct-Option Style
                    correctOpt_style = Style(root)
                    correctOpt_style.theme_use("default")
                    correctOpt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                               foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor='none')
                    # ---------------------------------------------

                    # Displaying CountDown-timer
                    timer = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                    foreground="#F0EFF4", background="#22333B", width=600)
                    timer.place(
                        relx=0.06, rely=0.1, anchor=CENTER)

                    # Periodically changing the Time-remaining after 1s
                    root.after(1100, lambda: timer.configure(
                        text="Timer\r\n   14"))
                    root.after(2100, lambda: timer.configure(
                        text="Timer\r\n   13"))
                    root.after(3100, lambda: timer.configure(
                        text="Timer\r\n   12"))
                    root.after(4100, lambda: timer.configure(
                        text="Timer\r\n   11"))
                    root.after(5100, lambda: timer.configure(
                        text="Timer\r\n   10"))
                    root.after(6100, lambda: timer.configure(
                        text="Timer\r\n   09"))
                    root.after(7100, lambda: timer.configure(
                        text="Timer\r\n   08"))
                    root.after(8100, lambda: timer.configure(
                        text="Timer\r\n   07"))
                    root.after(9100, lambda: timer.configure(
                        text="Timer\r\n   06"))
                    root.after(10100, lambda: timer.configure(
                        text="Timer\r\n   05"))
                    root.after(11100, lambda: timer.configure(
                        text="Timer\r\n   04"))
                    root.after(12100, lambda: timer.configure(
                        text="Timer\r\n   03"))
                    root.after(13100, lambda: timer.configure(
                        text="Timer\r\n   02"))
                    root.after(14100, lambda: timer.configure(
                        text="Timer\r\n   01"))
                    root.after(15100, lambda: timer.configure(
                        text="Timer\r\n   00"))

                    # Calling the function to validate and styling the Correct Answer after timer stops
                    root.after(15200, lambda: ques_Correct())

                    # Destroying all the widgets showing Quiz contents
                    root.after(16100, timer.destroy)
                    root.after(17400, ques_Opt1.destroy)
                    root.after(17400, ques_Opt2.destroy)
                    root.after(17400, ques_Opt3.destroy)
                    root.after(17400, ques_Opt4.destroy)
                    root.after(17500, label.destroy)

                    # Checking if all the 10 Quiz are complete
                    if (quizNumber % 10 == 0):

                        # Calling the function to update the Total score to database and mean time displaying it to the Guest
                        root.after(18000, lambda: scoreCard(quizNumber))

                        # Calling the function to display the Total Score
                        root.after(18500, lambda: finalScore())

                        # Calling the function to create exit and leaderboard button
                        root.after(19500, lambda: creatingExit())

                        # Checking if the Quiz reaches the max-limit
                        if (quizNumber != totalquiz):

                            # Calling the function to create a TryMore-Button
                            root.after(20200, lambda: createTryMore(
                                topicName, topicTable, quizNumber))

                    else:
                        # Increasing the question number
                        quizNumber += 1

                        # Calling the function to create next Quiz
                        root.after(18000, lambda: quizQuestion(
                            topicName, topicTable, quizNumber))

                    # -------------------------------------------------------------------------------------------- Quiz-Template -StyleEnds----

                # >>

                # Function which creates the Rules Panel for Quiz
                def quizRules(clicked_topic_button):

                    # Function which is operated by the Rules Panel Back-Button
                    def back3():

                        # Disabling the Back-Button after clicked, for preventing the function to be called twice
                        back3_button.configure(state=DISABLED)

                        # Destroying all the widgets created in the Topic-Selection Panel
                        root.after(600, lambda: back3_button.destroy())
                        root.after(500, lambda: rules.destroy())
                        root.after(500, lambda: start_button2.destroy())
                        root.after(500, lambda: label2.destroy())
                        root.after(500, lambda: label3.destroy())
                        root.after(500, lambda: label31.destroy())

                        # Calling the function to redirect to the User-Select panel
                        root.after(800, lambda: userSelect())

                    # >>

                    # Function which is triggered by the Rules Panel Quiz Start-Button to initialize another function to start Quiz
                    def quizInitializer(topicName, topicTable):

                        # Disabling the Quiz Start-Button after clicked, for preventing the function to be called twice
                        start_button2.configure(state=DISABLED)

                        # Destroying all the widgets created in the Rules Panel
                        root.after(500, rules.destroy)
                        root.after(600, start_button2.destroy)
                        root.after(500, label2.destroy)
                        root.after(500, back3_button.destroy)

                        # Calling the function to create Quiz
                        root.after(800, lambda: quizQuestion(
                            topicName, topicTable, 1))

                    # >>

                    # ------------------------------------- Rules Panel for Quiz -StyleStarts----------------------------------------------------

                    # Creating and Styling the Quiz Start-Button
                    start_button2_style = Style()
                    start_button2_style.configure("B.TButton", font=("Playball", 17, "bold", "italic"),
                                                  foreground="#0A0908", background="#F6F67C", borderwidth=2, width=8, height=2)
                    start_button2 = Button(root, text="Start",
                                           style="B.TButton")
                    start_button2.place(relx=0.5, rely=0.75, anchor=CENTER)

                    # Assigning Quizzes according to the button clicked
                    if (clicked_topic_button["text"] == "General Knowledge"):

                        # Disabling the Topic-Button1 after clicked, for preventing the function to be called twice
                        topic_button1.configure(state=DISABLED)

                        # Destroying all the widgets created in the Topic-Selection Panel
                        root.after(800, topic_button1.destroy)
                        root.after(400, topic_button2.destroy)
                        root.after(400, topic_button3.destroy)
                        root.after(400, back2_button.destroy)

                        # Assigning a function to the Quiz Start-Button with database as parameter to get the relavent Quiz
                        start_button2.configure(
                            command=lambda: quizInitializer("General Knowledge", "generalquestions"))

                    if (clicked_topic_button["text"] == "Technology"):

                        # Disabling the Topic-Button2 after clicked, for preventing the function to be called twice
                        topic_button2.configure(state=DISABLED)

                        # Destroying all the widgets created in the Topic-Select Panel
                        root.after(800, topic_button2.destroy)
                        root.after(400, topic_button1.destroy)
                        root.after(400, topic_button3.destroy)
                        root.after(400, back2_button.destroy)

                        # Assigning a function to the Quiz Start-Button with database as parameter to get the relavent Quiz
                        start_button2.configure(
                            command=lambda: quizInitializer("General Knowledge", "techquestions"))

                    if (clicked_topic_button["text"] == "Science"):

                        # Disabling the Topic-Button3 after clicked, for preventing the function to be called twice
                        topic_button3.configure(state=DISABLED)

                        # Destroying all the widgets created in the Topic-Select Panel
                        root.after(800, topic_button3.destroy)
                        root.after(400, topic_button1.destroy)
                        root.after(400, topic_button2.destroy)
                        root.after(400, back2_button.destroy)

                        # Assigning a function to the Quiz Start-Button with database as parameter to get the relavent Quiz
                        start_button2.configure(
                            command=lambda: quizInitializer("General Knowledge", "sciencequestions"))

                    # Changing the text in the Topic-Select Panel label instead of destroying it
                    root.after(800, label2.configure(text="Rules"))

                    # Displaying the rules for the Quiz
                    rules = Message(root, text="    1. Each question has a time limit of 15 seconds.\r\n    2. Once the option is selected it can't be changed.\r\n    3. Final Score is displayed at the end.\r\n    4. The following questions are based on '%s'." % clicked_topic_button["text"], font=("Dodge", 12),
                                    foreground="#D1E3DD", background="#1E0905", width=450)
                    rules.place(relx=0.5, rely=0.42, anchor=CENTER)

                    # Creating a Back-Button to return to User-Select Panel
                    # Styling Back-Button
                    back3_button_style = Style()
                    back3_button_style.theme_use("default")
                    back3_button_style.configure("E.TButton", font=("Playball", 10, "italic", "bold"),
                                                 foreground="#0A0908", background="#F6F67C", borderwidth=2, width=10, height=2, focuscolor="none")

                    back3_button = Button(root, text="< back",
                                          style="E.TButton", command=lambda: back3())
                    back3_button.place(relx=0.15, rely=0.9, anchor=CENTER)

                    # -------------------------------------------------------------------------------------------- Rules Panel for Quiz -StyleEnds----

                # >>

                # ------------------------------------- Topic-Selection Panel -StyleStarts----------------------------------------------------

                # Disabling the Enter-Button after clicked, for preventing the function to be called twice
                guestNameBtn.configure(state=DISABLED)

                # Getting the guest name from entry field
                text3 = guestName.get()

                # Destroying all the widgets created in the User-Login panel
                back1_button.destroy()
                label1.destroy()
                guestName.destroy()
                guestNameBtn.destroy()

                # # Changing the background color for the 2nd time
                window_background.configure(background="#1E0905")

                # Creating a new label to show the screen Title
                label2 = Label(root, text="Topics", font=("Dodge", 30),
                               foreground="#D1E3DD", background="#1E0905")
                label2.place(relx=0.5, rely=0.12, anchor=CENTER)

                # Creating a label to show the user type
                label3 = Label(root, text="Guest", font=("Dodge", 10, "italic"),
                               foreground="#F8FFE5", background="#1E0905")
                label3.place(relx=0.99, rely=0.01, anchor=NE)

                # Creating a new label which shows the guest name
                label31 = Label(root, text=text3, font=("Dodge", 15, "bold"),
                                foreground="#F5F749", background="#1E0905")
                label31.place(relx=0.995, rely=0.094, anchor=E)

                # Styling Topic-Select Panel's Buttons
                topic_button_style = Style()
                topic_button_style.theme_use("default")
                topic_button_style.configure("W.TButton", font=("Playball", 15, "bold", "italic"),
                                             foreground="#0A0908", background="#F6F67C", borderwidth=2, width=20, height=2)
                # Mouse Hovering style
                topic_button_style.map("W.TButton", foreground=[(
                    "active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                # Creating Topic-Buttons for Topic-Select Panel
                topic_button1 = Button(root, text="General Knowledge",
                                       style="W.TButton", command=lambda: quizRules(topic_button1))
                topic_button1.place(relx=0.5, rely=0.3, anchor=CENTER)

                topic_button2 = Button(root, text="Technology",
                                       style="W.TButton", command=lambda: quizRules(topic_button2))
                topic_button2.place(relx=0.5, rely=0.5, anchor=CENTER)

                topic_button3 = Button(root, text="Science",
                                       style="W.TButton", command=lambda: quizRules(topic_button3))
                topic_button3.place(relx=0.5, rely=0.7, anchor=CENTER)

                # Creating a Back-Button to return to User-Select Panel
                # Styling Back-Button
                back2_button_style = Style()
                back2_button_style.theme_use("default")
                back2_button_style.configure("E.TButton", font=("Playball", 10, "italic", "bold"),
                                             foreground="#0A0908", background="#F6F67C", borderwidth=2, width=10, height=2, focuscolor="none")
                # Mouse Hovering style
                back2_button_style.map("E.TButton", foreground=[
                    ("active", "!disabled", "#F0EFF4")], background=[("active", "#DB12AF")])

                back2_button = Button(root, text="< back",
                                      style="E.TButton", command=lambda: back2())
                back2_button.place(relx=0.15, rely=0.9, anchor=CENTER)

                # -------------------------------------------------------------------------------------------- Topic-Selection -StyleEnds----

            # >>

            # ------------------------------------- User-Login Panel -StyleStarts----------------------------------------------------

            # Disabling the Guest-Button after clicked, for preventing the function to be called twice
            guest.configure(state=DISABLED)

            # Changing the text in the label instead of destroying it
            label1.configure(text="Type Your Name")

            # Destroying the User-Select Buttons created in the User-Select panel
            guest.destroy()
            admin.destroy()

            # Creating a new entry for the guest name
            guestNameVar = StringVar()
            guestName = Entry(root, textvariable=guestNameVar,
                              font=("Dodge", 20, "bold", "italic"), width=30, justify=CENTER)
            guestName.focus_set()
            guestName.place(relx=0.5, rely=0.4, anchor=CENTER)

            # Creating a Enter-Button which triggers the function for creating Topic-Selection panel
            guestNameBtn = Button(
                root, text="Enter", style="S.TButton", command=lambda:  topicSelectionPanel())
            guestNameBtn.place(relx=0.5, rely=0.6, anchor=CENTER)

            # -------------------------------------------------------------------------------------------- User-Login -StyleEnds----

        # >>

        # ------------------------------------- User-Select Panel -StyleStarts----------------------------------------------------

        # Changing the background color for the 1st time
        window_background.configure(background="#D4B0F9")

        # Creating a new label to show the screen Title
        label1 = Label(root, text="Sign In", font=("Dodge", 22),
                       foreground="#0A014F", background="#D4B0F9")
        label1.place(relx=0.5, rely=0.22, anchor=CENTER)

        # Styling User-Select Buttons
        buttons_style = Style()
        buttons_style.theme_use("default")
        buttons_style.configure("S.TButton", font=("Playball", 15, "bold", "italic"),
                                foreground="#F0EFF4", background="#BF09D5", borderwidth=2, width=10, height=2, focuscolor="none")
        # Mouse Hovering style
        buttons_style.map("S.TButton", foreground=[(
            "active", "!disabled", "#F0EFF4")], background=[("active", "#DB12AF")])

        # Creating a Button for guest as Guest-Button
        guest = Button(root, text="Guest",
                       style="S.TButton", command=lambda: users())
        guest.place(relx=0.5, rely=0.4, anchor=CENTER)

        # Creating a Button for admin as Admin-Button
        admin = Button(root, text="Admin",
                       style="S.TButton", command=lambda: admins())
        admin.place(relx=0.5, rely=0.6, anchor=CENTER)

        # Creating a Back-Button to return to Home-Screen
        # Styling Back-Button
        back1_button_style = Style()
        back1_button_style.theme_use("default")
        back1_button_style.configure("E.TButton", font=("Playball", 10, "italic", "bold"),
                                     foreground="#F0EFF4", background="#BF09D5", borderwidth=2, width=10, height=2, focuscolor="none")
        # Mouse Hovering style
        back1_button_style.map("E.TButton", foreground=[("active", "!disabled", "#0A0908")],
                               background=[("active", "#F5F749")])

        back1_button = Button(root, text="< back",
                              style="E.TButton", command=lambda: back1())
        back1_button.place(relx=0.15, rely=0.9, anchor=CENTER)

        #  -------------------------------------------------------------------------------------------- User-Select -StyleEnds----

    # >>

    # Function which is operated by the Home-Screen's Start-Button
    def start():

        # Disabling the Start-Button after clicked, for preventing the function to be called twice
        start_button.configure(state=DISABLED)

        # Creating Labels for displaying the setup error-message if occurs
        error_msg = Label(root, font=("Dodge", 10),
                          foreground="#B0CECE", background="#22333B")
        global err_attempt

        # Calling the function to setting up Q & A for the app inside a database for the firsttime
        set_up = settingUp()

        if (set_up == "initialized"):

            # Destroying the Home-Screen's Start-Button
            start_button.after(500, start_button.destroy)
            error_msg.after(100, error_msg.destroy)

            # Resetting Start-Button clicks
            err_attempt = 0

            # Changing the color of the Home-Screen App-Name and destroying the label in 1.6s
            root.after(200, lambda: label0.configure(foreground="#832161"))
            root.after(400, lambda: label0.configure(foreground="#DA4167"))
            root.after(600, lambda: label0.configure(foreground="#177E89"))
            root.after(800, lambda: label0.configure(foreground="#DB3A34"))
            root.after(1000, lambda: label0.configure(foreground="#F5F749"))
            root.after(1200, lambda: label0.configure(foreground="#41EAD4"))
            root.after(1400, lambda: label0.configure(foreground="#F0EFF4"))
            root.after(1600, label0.destroy)

            # Calling the function to create the User-Select panel
            root.after(1800, lambda: userSelect())

        else:

            # Tracking the number of Start-Button clicks only when showing error-message
            err_attempt += 1

            if err_attempt < 4:

                # Showing the error message to the user if the Start-Button click is less than 4
                error_msg.configure(text=set_up)
                error_msg.place(relx=0.7, rely=0.9, anchor=CENTER)
                error_msg.after(2000, error_msg.destroy)

                # Enabling the Start-Button again
                root.after(2100, lambda: start_button.configure(state=NORMAL))

            else:
                # Showing the error message to the user if the Start-Button is clicked more than 3
                error_msg.configure(
                    text="Too many attempts, closing app in 5s")
                error_msg.place(relx=0.7, rely=0.9, anchor=CENTER)

                root.after(1000, lambda: error_msg.configure(
                    text="Too many attemps, closing app in 4s"))
                root.after(2000, lambda: error_msg.configure(
                    text="Too many attemps, closing app in 3s"))
                root.after(3000, lambda: error_msg.configure(
                    text="Too many attemps, closing app in 2s"))
                root.after(4000, lambda: error_msg.configure(
                    text="Too many attemps, closing app in 1s"))
                error_msg.after(4800, error_msg.destroy)

                # Quitting the application
                root.after(5000, lambda: root.destroy())

    # >>

    # ------------------------------------- Home Panel (or) Home-Screen -StyleStarts----------------------------------------------------

    # Setting the Home-Screen's background color
    window_background = Canvas(
        root, width=3000, height=1500, background="#22333B")
    window_background.place(anchor=CENTER)

    # Creating Labels for displaying the App-Name
    label0 = Label(root, text="Quizz-kur", font=("Dodge", 60),
                   foreground="#FFFFFF", background="#22333B")
    label0.place(relx=0.5, rely=0.33, anchor=CENTER)

    # Styling Home-Screen's Start-Button
    start_button_style = Style()
    start_button_style.theme_use("default")
    start_button_style.configure("TButton", font=("Playball", 15, "bold", "italic"),
                                 foreground="#0A0908", background="#F6F67C", borderwidth=2)
    # Mouse Hovering style
    start_button_style.map("TButton", foreground=[("active", "!disabled", "#0A0908")],
                           background=[("active", "#F5F749")])

    # Creating Home-Screen's Start-Button
    start_button = Button(root, text="Start", command=lambda: start())
    start_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    # -------------------------------------------------------------------------------------------- Home-Screen -StyleEnds----

    root.mainloop()


if __name__ == "__main__":
    main()
