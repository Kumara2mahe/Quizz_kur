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
score = 0


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

            # Function which creates the Topic-Select panel with multiple Topic-Buttons for each kind of quiz topic
            def userOptions():

                # Function which creates a LeaderBoard-Button and Exit-Button which quits the App for the ScoreCard Panel
                def creatingExit():

                    def exitingScoreCard():

                        # Disabling the Exit-Button after clicked, for preventing the function to be called twice
                        exit_button.configure(state=DISABLED)

                        # Destroying all the widgets created and visible in the ScoreCard Panel
                        root.after(400, lambda: score_button.destroy())
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

                    # Function which is operated by the LeaderBoard-Button to collect the top five scores from the database
                    def leaderboard():

                        # Function which creates the leaderboard with only the top5 data collected from the database
                        def leaderboard_show():

                            # Function which is operated by the LeaderBoard's Back-Button
                            def leaderboard_hide():

                                # Disabling the Back-Button after clicked, for preventing the function to be called twice
                                score_button.configure(state=DISABLED)

                                # Destroying all the widgets created in the leaderboard
                                leaderboard_label1.destroy()
                                leaderboard_label1_n.destroy()
                                leaderboard_label1_s.destroy()
                                leaderboard_text.destroy()
                                leaderboard_label.destroy()

                                # Changing back the Back-Button text to Leaderboard-Button and also changing the function assigned to it
                                root.after(100, lambda: score_button.configure(
                                    text="LeaderBoard", state=NORMAL, command=lambda: leaderboard()))

                                # Enabling the ScoreCard Panel's Exit-Button
                                exit_button.configure(state=NORMAL)
                                scoreLabel.configure(foreground="#F8FFE5")

                            # ------------------------------------- Leaderboard -StyleStarts----------------------------------------------------

                            # Changing the text on the Leaderboard-Button to a Back-Button and also changing the function assigned to it
                            root.after(100, lambda: score_button.configure(
                                text="< back", state=NORMAL, command=lambda: leaderboard_hide()))

                            # Disabling the Exit-Button and Hiding the total-score when the leaderboard is open
                            exit_button.configure(state=DISABLED)
                            scoreLabel.configure(foreground="#1E0905")

                            # Styling the leaderboard Title label
                            leaderboard_label_style = Style()
                            leaderboard_label_style.theme_use("default")
                            leaderboard_label_style.configure("L.TLabel", font=("Dodge", 15, "bold", "italic"),
                                                              foreground="#F8FFE5", background="#1E0905", borderwidth=2, width=30, height=10, focuscolor="none")

                            # Creating a label to show the leaderboard Title
                            leaderboard_label = Label(
                                root, text="LeaderBoard", font=("Dodge", 20, "bold", "italic"),
                                foreground="#F5F749", background="#1E0905")
                            leaderboard_label.place(
                                relx=0.55, rely=0.1, anchor=CENTER)

                            # Styling the leaderboard sub-Title labels
                            leaderboard_label1_n_style = Style()
                            leaderboard_label1_n_style.theme_use("default")
                            leaderboard_label1_n_style.configure("L.TLabel", font=("Dodge", 15, "bold", "italic"),
                                                                 foreground="#BF09D5", background="#1E0905", borderwidth=2, width=30, height=10, focuscolor="none")

                            # Creating a label to show the leaderboard sub-Titles
                            leaderboard_label1 = Label(
                                root, text="Name                               Score\r\n", style="L.TLabel")
                            leaderboard_label1.place(
                                relx=0.55, rely=0.3, anchor=CENTER)

                            # Styling the GuestNames displayed in the leaderboard
                            leaderboard_label1_n_style = Style()
                            leaderboard_label1_n_style.theme_use("default")
                            leaderboard_label1_n_style.configure("G.TLabel", font=("Dodge", 13, "bold", "italic"),
                                                                 foreground="#F8FFE5", background="#1E0905", borderwidth=2, width=30, height=10, focuscolor="none")

                            # Creating new label to show the GuestNames
                            leaderboard_label1_n = Label(
                                root, text=show_name, style="G.TLabel")
                            leaderboard_label1_n.place(
                                relx=0.25, rely=0.35, anchor=NW)

                            # Styling the GuestScores displayed in the leaderboard
                            leaderboard_label1_s_style = Style()
                            leaderboard_label1_s_style.theme_use("default")
                            leaderboard_label1_s_style.configure("P.TLabel", font=("Dodge", 13, "bold", "italic"),
                                                                 foreground="#F8FFE5", background="#1E0905", borderwidth=2, width=10, height=30, focuscolor="none")

                            # Creating new label to show the GuestScores
                            leaderboard_label1_s = Label(
                                root, text=show_score, style="P.TLabel")
                            leaderboard_label1_s.place(
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

                        # Querying the database and collects the top five scored names
                        co.execute(
                            "SELECT * FROM leaderboard ORDER BY score DESC")
                        points = co.fetchmany(5)

                        # Separating the names from the collected data
                        show_name = " "
                        for record in points:
                            show_name += str(record[0]) + "\r\n "

                        # Separating the scored from the collected data
                        show_score = " "
                        for record in points:
                            show_score += str(record[1]) + "\r\n "

                        # Committing the changes to the database
                        quizdata.commit()

                        # Closing the connection with the database
                        quizdata.close()

                        # Calling the function to create the leaderboard
                        root.after(500, lambda: leaderboard_show())

                    # >>

                    # ------------------------------------- ScoreCard Panel Button -StyleStarts----------------------------------------------------

                    # Creating a Exit-Button to quit the App
                    exit_button = Button(root, text="EXIT",
                                         style="E.TButton", command=lambda: exitingScoreCard())
                    exit_button.place(relx=0.15, rely=0.9, anchor=CENTER)

                    # Creating a LeaderBoard-Button to view your position in leaderboard
                    score_button_style = Style(root)
                    score_button_style.theme_use("default")
                    score_button_style.configure("L.TButton", font=("Playball", 10, "bold", "italic"),
                                                 foreground="#0A0908", background="#F6F67C", borderwidth=2, width=15, height=4, focuscolor="none")
                    # Mouse Hovering style
                    score_button_style.map("L.TButton", foreground=[
                        ("active", "!disabled", "#F0EFF4")], background=[("active", "#DB12AF")])
                    score_button = Button(
                        root, text="LeaderBoard", style="L.TButton", command=lambda: leaderboard())
                    score_button.place(relx=0.22, rely=0.05, anchor=NE)

                    # -------------------------------------------------------------------------------------------- ScoreCard Panel Button -StyleEnds----

                # >>

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

                # Function which creates the Rules Panel for Topic-3
                def topic_3():

                    # Function which is operated by the Topic-3's Rules Panel Back-Button
                    def back3():

                        # Disabling the Back-Button after clicked, for preventing the function to be called twice
                        back3_button.configure(state=DISABLED)

                        # Destroying all the widgets created in the Topic-Select Panel
                        root.after(600, lambda: back3_button.destroy())
                        root.after(500, lambda: rules.destroy())
                        root.after(500, lambda: start_button2.destroy())
                        root.after(500, lambda: label2.destroy())
                        root.after(500, lambda: label3.destroy())
                        root.after(500, lambda: label31.destroy())

                        # Calling the function to redirect to the User-Select panel
                        root.after(800, lambda: userSelect())

                    # >>

                    # Function for displaying the GuestName centered above the score
                    def scoreCard():

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

                        # Creating a 'leaderboard' table if not exists to store the Guestname and score
                        co.execute("""CREATE TABLE IF NOT EXISTS leaderboard (
                                    playername text,
                                    score integer
                                    )""")

                        # Updating the leaderboard with the Guest's name and total score
                        co.execute("INSERT INTO leaderboard VALUES (:text3, :point)",
                                   {
                                       "text3": text3,
                                       "point": point
                                   })

                        # Committing the changes to the database
                        quizdata.commit()

                        # Closing the connection with the database
                        quizdata.close()

                    # >>

                    # Function which is triggered by the Topic-3's Rules Panel Quiz Start-Button
                    def quiz1():

                        # Function which creates Topic-3's (Question #10)
                        def ques10():

                            # ------------------------------------- (Question #10)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques10_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques10_C_Opt_style = Style(root)
                                ques10_C_Opt_style.theme_use("default")
                                ques10_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                             foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques10_Opt4.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques10_Opt2.configure(state=DISABLED)
                                ques10_Opt3.configure(state=DISABLED)
                                ques10_Opt1.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #10)
                            def ques10_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques10_Opt_style = Style(root)
                                ques10_Opt_style.theme_use("default")
                                ques10_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                           foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques10_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques10_Opt1.configure(state=DISABLED)
                                ques10_Opt2.configure(state=DISABLED)
                                ques10_Opt3.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #10)
                                root.after(3000, lambda: points())

                            # Function which is triggered by Option-3 of (Question #10)
                            def ques10_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques10_Opt_style = Style(root)
                                ques10_Opt_style.theme_use("default")
                                ques10_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                           foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques10_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques10_Opt1.configure(state=DISABLED)
                                ques10_Opt2.configure(state=DISABLED)
                                ques10_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques10WO3_style = Style(root)
                                ques10WO3_style.theme_use("default")
                                ques10WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques10_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #10)
                            def ques10_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques10_Opt_style = Style(root)
                                ques10_Opt_style.theme_use("default")
                                ques10_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                           foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-2 to yellow color
                                ques10_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques10_Opt1.configure(state=DISABLED)
                                ques10_Opt3.configure(state=DISABLED)
                                ques10_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques10WO2_style = Style(root)
                                ques10WO2_style.theme_use("default")
                                ques10WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques10_Opt2.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-1 of (Question #10)
                            def ques10_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques10_Opt_style = Style(root)
                                ques10_Opt_style.theme_use("default")
                                ques10_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                           foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques10_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques10_Opt2.configure(state=DISABLED)
                                ques10_Opt3.configure(state=DISABLED)
                                ques10_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques10WO1_style = Style(root)
                                ques10WO1_style.theme_use("default")
                                ques10WO1_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques10_Opt1.configure(
                                    style="X.TRadiobutton"))

                            # -------------------------------------------------------------------------------------------- (Question #10) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-3's (Question #10) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #10)
                            label13 = Label(root, text="10. Which of the gas is not known as green house gas?", font=("Dodge", 14),
                                            foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label13.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #10) Options
                            ques10_Opt_style = Style(root)
                            ques10_Opt_style.theme_use("default")
                            ques10_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                       foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques10_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #10)
                            # Creating Option-1 and assigning a styler function to it
                            v10 = IntVar(root)
                            ques10_Opt1 = Radiobutton(root, text="Methane", variable=v10,
                                                      value=1, command=lambda: ques10_Opt_1())
                            ques10_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques10_Opt2 = Radiobutton(root, text="Nitrous oxide", variable=v10,
                                                      value=2, command=lambda: ques10_Opt_2())
                            ques10_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques10_Opt3 = Radiobutton(root, text="Carbon dioxide", variable=v10,
                                                      value=3, command=lambda: ques10_Opt_3())
                            ques10_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques10_Opt4 = Radiobutton(root, text="Hydrogen", variable=v10,
                                                      value=4, command=lambda: ques10_Opt_4())
                            ques10_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #10)
                            timer10 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                              foreground="#F0EFF4", background="#22333B", width=600)
                            timer10.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer10.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer10.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer10.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer10.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer10.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer10.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer10.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer10.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer10.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer10.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer10.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer10.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer10.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer10.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer10.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #10) after timer stops
                            root.after(15200, lambda: ques10_Correct())

                            # Destroying all the widgets showing (Question #10)
                            root.after(16100, timer10.destroy)
                            root.after(17400, ques10_Opt1.destroy)
                            root.after(17400, ques10_Opt2.destroy)
                            root.after(17500, ques10_Opt3.destroy)
                            root.after(17400, ques10_Opt4.destroy)
                            root.after(17500, label13.destroy)

                            # Calling the function to update the Total score to database and mean time displaying it to the Guest
                            root.after(18000, lambda: scoreCard())

                            # Calling the function to display the Total Score
                            root.after(18500, lambda: finalScore())

                            # Calling the function to create exit and leaderboard button
                            root.after(19500, lambda: creatingExit())

                        # -------------------------------------------------------------------------------------------- Topic-3's (Question #10) -StyleEnds----

                        # >>

                        # Function which creates Topic-3's (Question #9)
                        def ques9():

                            # ------------------------------------- (Question #9)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques9_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques9_C_Opt_style = Style(root)
                                ques9_C_Opt_style.theme_use("default")
                                ques9_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques9_Opt1.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques9_Opt2.configure(state=DISABLED)
                                ques9_Opt3.configure(state=DISABLED)
                                ques9_Opt4.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #9)
                            def ques9_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques9_Opt_style = Style(root)
                                ques9_Opt_style.theme_use("default")
                                ques9_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques9_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques9_Opt1.configure(state=DISABLED)
                                ques9_Opt2.configure(state=DISABLED)
                                ques9_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques9WO4_style = Style(root)
                                ques9WO4_style.theme_use("default")
                                ques9WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques9_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #9)
                            def ques9_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques9_Opt_style = Style(root)
                                ques9_Opt_style.theme_use("default")
                                ques9_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques9_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques9_Opt1.configure(state=DISABLED)
                                ques9_Opt2.configure(state=DISABLED)
                                ques9_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques9WO3_style = Style(root)
                                ques9WO3_style.theme_use("default")
                                ques9WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques9_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #9)
                            def ques9_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques9_Opt_style = Style(root)
                                ques9_Opt_style.theme_use("default")
                                ques9_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-2 to yellow color
                                ques9_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques9_Opt1.configure(state=DISABLED)
                                ques9_Opt3.configure(state=DISABLED)
                                ques9_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques9WO2_style = Style(root)
                                ques9WO2_style.theme_use("default")
                                ques9WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques9_Opt2.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-1 of (Question #9)
                            def ques9_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques9_Opt_style = Style(root)
                                ques9_Opt_style.theme_use("default")
                                ques9_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques9_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques9_Opt2.configure(state=DISABLED)
                                ques9_Opt3.configure(state=DISABLED)
                                ques9_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #9)
                                root.after(3000, lambda: points())

                            # -------------------------------------------------------------------------------------------- (Question #9) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-3's (Question #9) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #9)
                            label12 = Label(root, text="9. Quartz crystals normally used in quartz clocks etc. is chemically", font=("Dodge", 14),
                                            foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label12.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #9) Options
                            ques9_Opt_style = Style(root)
                            ques9_Opt_style.theme_use("default")
                            ques9_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques9_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #9)
                            # Creating Option-1 and assigning a styler function to it
                            v9 = IntVar(root)
                            ques9_Opt1 = Radiobutton(root, text="silicon dioxide", variable=v9,
                                                     value=1, command=lambda: ques9_Opt_1())
                            ques9_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques9_Opt2 = Radiobutton(root, text="germanium oxide", variable=v9,
                                                     value=2, command=lambda: ques9_Opt_2())
                            ques9_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques9_Opt3 = Radiobutton(root, text="mixture of germanium oxide\nand silicon dioxide", variable=v9,
                                                     value=3, command=lambda: ques9_Opt_3())
                            ques9_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques9_Opt4 = Radiobutton(root, text="sodium silicate", variable=v9,
                                                     value=4, command=lambda: ques9_Opt_4())
                            ques9_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #9)
                            timer9 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer9.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer9.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer9.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer9.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer9.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer9.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer9.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer9.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer9.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer9.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer9.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer9.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer9.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer9.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer9.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer9.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #9) after timer stops
                            root.after(15200, lambda: ques9_Correct())

                            # Destroying all the widgets showing (Question #9)
                            root.after(16100, timer9.destroy)
                            root.after(17400, ques9_Opt1.destroy)
                            root.after(17400, ques9_Opt2.destroy)
                            root.after(17500, ques9_Opt3.destroy)
                            root.after(17400, ques9_Opt4.destroy)
                            root.after(17500, label12.destroy)

                            # Calling the function to create Topic-3's (Question #10)
                            root.after(18000, lambda: ques10())

                        # -------------------------------------------------------------------------------------------- Topic-3's (Question #9) -StyleEnds----

                        # >>

                        # Function which creates Topic-3's (Question #8)
                        def ques8():

                            # ------------------------------------- (Question #8)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques8_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques8_C_Opt_style = Style(root)
                                ques8_C_Opt_style.theme_use("default")
                                ques8_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques8_Opt1.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques8_Opt2.configure(state=DISABLED)
                                ques8_Opt3.configure(state=DISABLED)
                                ques8_Opt4.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #8)
                            def ques8_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques8_Opt_style = Style(root)
                                ques8_Opt_style.theme_use("default")
                                ques8_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques8_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques8_Opt1.configure(state=DISABLED)
                                ques8_Opt2.configure(state=DISABLED)
                                ques8_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques8WO4_style = Style(root)
                                ques8WO4_style.theme_use("default")
                                ques8WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques8_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #8)
                            def ques8_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques8_Opt_style = Style(root)
                                ques8_Opt_style.theme_use("default")
                                ques8_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques8_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques8_Opt1.configure(state=DISABLED)
                                ques8_Opt2.configure(state=DISABLED)
                                ques8_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques8WO3_style = Style(root)
                                ques8WO3_style.theme_use("default")
                                ques8WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques8_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #8)
                            def ques8_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques8_Opt_style = Style(root)
                                ques8_Opt_style.theme_use("default")
                                ques8_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-2 to yellow color
                                ques8_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques8_Opt1.configure(state=DISABLED)
                                ques8_Opt3.configure(state=DISABLED)
                                ques8_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques8WO2_style = Style(root)
                                ques8WO2_style.theme_use("default")
                                ques8WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques8_Opt2.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-1 of (Question #8)
                            def ques8_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques8_Opt_style = Style(root)
                                ques8_Opt_style.theme_use("default")
                                ques8_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques8_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques8_Opt2.configure(state=DISABLED)
                                ques8_Opt3.configure(state=DISABLED)
                                ques8_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #8)
                                root.after(3000, lambda: points())

                            # -------------------------------------------------------------------------------------------- (Question #8) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-3's (Question #8) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #8)
                            label11 = Label(root, text="8. Washing soda is the common name for", font=("Dodge", 14),
                                            foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label11.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #8) Options
                            ques8_Opt_style = Style(root)
                            ques8_Opt_style.theme_use("default")
                            ques8_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques8_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #8)
                            # Creating Option-1 and assigning a styler function to it
                            v8 = IntVar(root)
                            ques8_Opt1 = Radiobutton(root, text="Sodium carbonate", variable=v8,
                                                     value=1, command=lambda: ques8_Opt_1())
                            ques8_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques8_Opt2 = Radiobutton(root, text="Calcium bicarbonate", variable=v8,
                                                     value=2, command=lambda: ques8_Opt_2())
                            ques8_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques8_Opt3 = Radiobutton(root, text="Sodium bicarbonate", variable=v8,
                                                     value=3, command=lambda: ques8_Opt_3())
                            ques8_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques8_Opt4 = Radiobutton(root, text="Calcium carbonate", variable=v8,
                                                     value=4, command=lambda: ques8_Opt_4())
                            ques8_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #8)
                            timer8 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer8.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer8.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer8.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer8.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer8.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer8.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer8.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer8.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer8.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer8.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer8.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer8.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer8.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer8.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer8.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer8.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #8) after timer stops
                            root.after(15200, lambda: ques8_Correct())

                            # Destroying all the widgets showing (Question #8)
                            root.after(16100, timer8.destroy)
                            root.after(17400, ques8_Opt1.destroy)
                            root.after(17400, ques8_Opt2.destroy)
                            root.after(17500, ques8_Opt3.destroy)
                            root.after(17400, ques8_Opt4.destroy)
                            root.after(17500, label11.destroy)

                            # Calling the function to create Topic-3's (Question #9)
                            root.after(18000, lambda: ques9())

                        # -------------------------------------------------------------------------------------------- Topic-3's (Question #8) -StyleEnds----

                        # >>

                        # Function which creates Topic-3's (Question #7)
                        def ques7():

                            # ------------------------------------- (Question #7)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques7_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques7_C_Opt_style = Style(root)
                                ques7_C_Opt_style.theme_use("default")
                                ques7_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques7_Opt1.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques7_Opt2.configure(state=DISABLED)
                                ques7_Opt3.configure(state=DISABLED)
                                ques7_Opt4.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #7)
                            def ques7_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques7_Opt_style = Style(root)
                                ques7_Opt_style.theme_use("default")
                                ques7_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques7_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques7_Opt1.configure(state=DISABLED)
                                ques7_Opt2.configure(state=DISABLED)
                                ques7_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques7WO4_style = Style(root)
                                ques7WO4_style.theme_use("default")
                                ques7WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques7_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #7)
                            def ques7_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques7_Opt_style = Style(root)
                                ques7_Opt_style.theme_use("default")
                                ques7_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques7_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques7_Opt1.configure(state=DISABLED)
                                ques7_Opt2.configure(state=DISABLED)
                                ques7_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques7WO3_style = Style(root)
                                ques7WO3_style.theme_use("default")
                                ques7WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques7_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #7)
                            def ques7_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques7_Opt_style = Style(root)
                                ques7_Opt_style.theme_use("default")
                                ques7_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-2 to yellow color
                                ques7_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques7_Opt1.configure(state=DISABLED)
                                ques7_Opt3.configure(state=DISABLED)
                                ques7_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques7WO2_style = Style(root)
                                ques7WO2_style.theme_use("default")
                                ques7WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques7_Opt2.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-1 of (Question #7)
                            def ques7_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques7_Opt_style = Style(root)
                                ques7_Opt_style.theme_use("default")
                                ques7_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques7_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques7_Opt2.configure(state=DISABLED)
                                ques7_Opt3.configure(state=DISABLED)
                                ques7_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #7)
                                root.after(3000, lambda: points())

                            # -------------------------------------------------------------------------------------------- (Question #7) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-3's (Question #7) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #7)
                            label10 = Label(root, text="7. The gas usually filled in the electric bulb is", font=("Dodge", 14),
                                            foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label10.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #7) Options
                            ques7_Opt_style = Style(root)
                            ques7_Opt_style.theme_use("default")
                            ques7_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques7_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #7)
                            # Creating Option-1 and assigning a styler function to it
                            v7 = IntVar(root)
                            ques7_Opt1 = Radiobutton(root, text="nitrogen", variable=v7,
                                                     value=1, command=lambda: ques7_Opt_1())
                            ques7_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques7_Opt2 = Radiobutton(root, text="hydrogen", variable=v7,
                                                     value=2, command=lambda: ques7_Opt_2())
                            ques7_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques7_Opt3 = Radiobutton(root, text="carbon dioxide", variable=v7,
                                                     value=3, command=lambda: ques7_Opt_3())
                            ques7_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques7_Opt4 = Radiobutton(root, text="oxygen", variable=v7,
                                                     value=4, command=lambda: ques7_Opt_4())
                            ques7_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #7)
                            timer7 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer7.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer7.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer7.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer7.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer7.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer7.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer7.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer7.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer7.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer7.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer7.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer7.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer7.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer7.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer7.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer7.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #7) after timer stops
                            root.after(15200, lambda: ques7_Correct())

                            # Destroying all the widgets showing (Question #7)
                            root.after(16100, timer7.destroy)
                            root.after(17400, ques7_Opt1.destroy)
                            root.after(17400, ques7_Opt2.destroy)
                            root.after(17500, ques7_Opt3.destroy)
                            root.after(17400, ques7_Opt4.destroy)
                            root.after(17500, label10.destroy)

                            # Calling the function to create Topic-3's (Question #8)
                            root.after(18000, lambda: ques8())

                        # -------------------------------------------------------------------------------------------- Topic-3's (Question #7) -StyleEnds----

                        # >>

                        # Function which creates Topic-3's (Question #6)
                        def ques6():

                            # ------------------------------------- (Question #6)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques6_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques6_C_Opt_style = Style(root)
                                ques6_C_Opt_style.theme_use("default")
                                ques6_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques6_Opt2.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques6_Opt1.configure(state=DISABLED)
                                ques6_Opt4.configure(state=DISABLED)
                                ques6_Opt3.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #6)
                            def ques6_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques6_Opt_style = Style(root)
                                ques6_Opt_style.theme_use("default")
                                ques6_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques6_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques6_Opt1.configure(state=DISABLED)
                                ques6_Opt2.configure(state=DISABLED)
                                ques6_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques6WO2_style = Style(root)
                                ques6WO2_style.theme_use("default")
                                ques6WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques6_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #6)
                            def ques6_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques6_Opt_style = Style(root)
                                ques6_Opt_style.theme_use("default")
                                ques6_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques6_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques6_Opt1.configure(state=DISABLED)
                                ques6_Opt2.configure(state=DISABLED)
                                ques6_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques6WO3_style = Style(root)
                                ques6WO3_style.theme_use("default")
                                ques6WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques6_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #6)
                            def ques6_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques6_Opt_style = Style(root)
                                ques6_Opt_style.theme_use("default")
                                ques6_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques6_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques6_Opt1.configure(state=DISABLED)
                                ques6_Opt3.configure(state=DISABLED)
                                ques6_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #6)
                                root.after(3000, lambda: points())

                            # Function which is triggered by Option-1 of (Question #6)
                            def ques6_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques6_Opt_style = Style(root)
                                ques6_Opt_style.theme_use("default")
                                ques6_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques6_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques6_Opt2.configure(state=DISABLED)
                                ques6_Opt3.configure(state=DISABLED)
                                ques6_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques6WO1_style = Style(root)
                                ques6WO1_style.theme_use("default")
                                ques6WO1_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques6_Opt1.configure(
                                    style="X.TRadiobutton"))

                            # -------------------------------------------------------------------------------------------- (Question #6) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-3's (Question #6) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #6)
                            label9 = Label(root, text="6. Chemical formula for water is", font=("Dodge", 14),
                                           foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label9.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #6) Options
                            ques6_Opt_style = Style(root)
                            ques6_Opt_style.theme_use("default")
                            ques6_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques6_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #6)
                            # Creating Option-1 and assigning a styler function to it
                            v6 = IntVar(root)
                            ques6_Opt1 = Radiobutton(root, text="NaAlO2", variable=v6,
                                                     value=1, command=lambda: ques6_Opt_1())
                            ques6_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques6_Opt2 = Radiobutton(root, text="H2O", variable=v6,
                                                     value=2, command=lambda: ques6_Opt_2())
                            ques6_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques6_Opt3 = Radiobutton(root, text="Al2O3", variable=v6,
                                                     value=3, command=lambda: ques6_Opt_3())
                            ques6_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques6_Opt4 = Radiobutton(root, text="CaSiO3", variable=v6,
                                                     value=4, command=lambda: ques6_Opt_4())
                            ques6_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #6)
                            timer6 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer6.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer6.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer6.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer6.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer6.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer6.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer6.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer6.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer6.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer6.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer6.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer6.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer6.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer6.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer6.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer6.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #6) after timer stops
                            root.after(15200, lambda: ques6_Correct())

                            # Destroying all the widgets showing (Question #6)
                            root.after(16100, timer6.destroy)
                            root.after(17400, ques6_Opt1.destroy)
                            root.after(17400, ques6_Opt2.destroy)
                            root.after(17500, ques6_Opt3.destroy)
                            root.after(17400, ques6_Opt4.destroy)
                            root.after(17500, label9.destroy)

                            # Calling the function to create Topic-3's (Question #7)
                            root.after(18000, lambda: ques7())

                        # -------------------------------------------------------------------------------------------- Topic-3's (Question #6) -StyleEnds----

                        # >>

                        # Function which creates Topic-3's (Question #5)
                        def ques5():

                            # ------------------------------------- (Question #5)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques5_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques5_C_Opt_style = Style(root)
                                ques5_C_Opt_style.theme_use("default")
                                ques5_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques5_Opt2.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques5_Opt1.configure(state=DISABLED)
                                ques5_Opt4.configure(state=DISABLED)
                                ques5_Opt3.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #5)
                            def ques5_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques5_Opt_style = Style(root)
                                ques5_Opt_style.theme_use("default")
                                ques5_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques5_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques5_Opt1.configure(state=DISABLED)
                                ques5_Opt2.configure(state=DISABLED)
                                ques5_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques5WO4_style = Style(root)
                                ques5WO4_style.theme_use("default")
                                ques5WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques5_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #5)
                            def ques5_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques5_Opt_style = Style(root)
                                ques5_Opt_style.theme_use("default")
                                ques5_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques5_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques5_Opt1.configure(state=DISABLED)
                                ques5_Opt2.configure(state=DISABLED)
                                ques5_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques5WO3_style = Style(root)
                                ques5WO3_style.theme_use("default")
                                ques5WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques5_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #5)
                            def ques5_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques5_Opt_style = Style(root)
                                ques5_Opt_style.theme_use("default")
                                ques5_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques5_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques5_Opt1.configure(state=DISABLED)
                                ques5_Opt3.configure(state=DISABLED)
                                ques5_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #5)
                                root.after(3000, lambda: points())

                            # Function which is triggered by Option-1 of (Question #5)
                            def ques5_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques5_Opt_style = Style(root)
                                ques5_Opt_style.theme_use("default")
                                ques5_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques5_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques5_Opt2.configure(state=DISABLED)
                                ques5_Opt3.configure(state=DISABLED)
                                ques5_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques5WO1_style = Style(root)
                                ques5WO1_style.theme_use("default")
                                ques5WO1_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques5_Opt1.configure(
                                    style="X.TRadiobutton"))

                            # -------------------------------------------------------------------------------------------- (Question #5) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-3's (Question #5) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #5)
                            label8 = Label(root, text="5. Which of the following metals forms an amalgam with other metals?", font=("Dodge", 14),
                                           foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label8.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #5) Options
                            ques5_Opt_style = Style(root)
                            ques5_Opt_style.theme_use("default")
                            ques5_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques5_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #5)
                            # Creating Option-1 and assigning a styler function to it
                            v5 = IntVar(root)
                            ques5_Opt1 = Radiobutton(root, text="Tin", variable=v5,
                                                     value=1, command=lambda: ques5_Opt_1())
                            ques5_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques5_Opt2 = Radiobutton(root, text="Mercury", variable=v5,
                                                     value=2, command=lambda: ques5_Opt_2())
                            ques5_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques5_Opt3 = Radiobutton(root, text="Lead", variable=v5,
                                                     value=3, command=lambda: ques5_Opt_3())
                            ques5_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques5_Opt4 = Radiobutton(root, text="Zinc", variable=v5,
                                                     value=4, command=lambda: ques5_Opt_4())
                            ques5_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #5)
                            timer5 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer5.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer5.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer5.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer5.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer5.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer5.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer5.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer5.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer5.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer5.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer5.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer5.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer5.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer5.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer5.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer5.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #5) after timer stops
                            root.after(15200, lambda: ques5_Correct())

                            # Destroying all the widgets showing (Question #5)
                            root.after(16100, timer5.destroy)
                            root.after(17400, ques5_Opt1.destroy)
                            root.after(17400, ques5_Opt2.destroy)
                            root.after(17500, ques5_Opt3.destroy)
                            root.after(17400, ques5_Opt4.destroy)
                            root.after(17500, label8.destroy)

                            # Calling the function to create Topic-3's (Question #6)
                            root.after(18000, lambda: ques6())

                        # -------------------------------------------------------------------------------------------- Topic-3's (Question #5) -StyleEnds----

                        # >>

                        # Function which creates Topic-3's (Question #4)
                        def ques4():

                            # ------------------------------------- (Question #4)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques4_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques4_C_Opt_style = Style(root)
                                ques4_C_Opt_style.theme_use("default")
                                ques4_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques4_Opt1.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques4_Opt4.configure(state=DISABLED)
                                ques4_Opt2.configure(state=DISABLED)
                                ques4_Opt3.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #4)
                            def ques4_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques4_Opt_style = Style(root)
                                ques4_Opt_style.theme_use("default")
                                ques4_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques4_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques4_Opt1.configure(state=DISABLED)
                                ques4_Opt2.configure(state=DISABLED)
                                ques4_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques4WO4_style = Style(root)
                                ques4WO4_style.theme_use("default")
                                ques4WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques4_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #4)
                            def ques4_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques4_Opt_style = Style(root)
                                ques4_Opt_style.theme_use("default")
                                ques4_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques4_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques4_Opt1.configure(state=DISABLED)
                                ques4_Opt2.configure(state=DISABLED)
                                ques4_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques4WO3_style = Style(root)
                                ques4WO3_style.theme_use("default")
                                ques4WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques4_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #4)
                            def ques4_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques4_Opt_style = Style(root)
                                ques4_Opt_style.theme_use("default")
                                ques4_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques4_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques4_Opt1.configure(state=DISABLED)
                                ques4_Opt3.configure(state=DISABLED)
                                ques4_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques4WO2_style = Style(root)
                                ques4WO2_style.theme_use("default")
                                ques4WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques4_Opt2.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-1 of (Question #4)
                            def ques4_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques4_Opt_style = Style(root)
                                ques4_Opt_style.theme_use("default")
                                ques4_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques4_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques4_Opt2.configure(state=DISABLED)
                                ques4_Opt3.configure(state=DISABLED)
                                ques4_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #4)
                                root.after(3000, lambda: points())

                            # -------------------------------------------------------------------------------------------- (Question #4) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-3's (Question #4) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #4)
                            label7 = Label(root, text="4. Which of the following is used in pencils?", font=("Dodge", 14),
                                           foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label7.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #4) Options
                            ques4_Opt_style = Style(root)
                            ques4_Opt_style.theme_use("default")
                            ques4_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques4_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #4)
                            # Creating Option-1 and assigning a styler function to it
                            v4 = IntVar(root)
                            ques4_Opt1 = Radiobutton(root, text="Graphite", variable=v4,
                                                     value=1, command=lambda: ques4_Opt_1())
                            ques4_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques4_Opt2 = Radiobutton(root, text="Silicon", variable=v4,
                                                     value=2, command=lambda: ques4_Opt_2())
                            ques4_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques4_Opt3 = Radiobutton(root, text="Charcoal", variable=v4,
                                                     value=3, command=lambda: ques4_Opt_3())
                            ques4_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques4_Opt4 = Radiobutton(root, text="Phosphorous", variable=v4,
                                                     value=4, command=lambda: ques4_Opt_4())
                            ques4_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #4)
                            timer4 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer4.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer4.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer4.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer4.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer4.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer4.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer4.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer4.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer4.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer4.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer4.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer4.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer4.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer4.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer4.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer4.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #4) after timer stops
                            root.after(15200, lambda: ques4_Correct())

                            # Destroying all the widgets showing (Question #4)
                            root.after(16100, timer4.destroy)
                            root.after(17400, ques4_Opt1.destroy)
                            root.after(17400, ques4_Opt2.destroy)
                            root.after(17500, ques4_Opt3.destroy)
                            root.after(17400, ques4_Opt4.destroy)
                            root.after(17500, label7.destroy)

                            # Calling the function to create Topic-3's (Question #5)
                            root.after(18000, lambda: ques5())

                        # -------------------------------------------------------------------------------------------- Topic-3's (Question #4) -StyleEnds----

                        # >>

                        # Function which creates Topic-3's (Question #3)
                        def ques3():

                            # ------------------------------------- (Question #3)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques3_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques1_C_Opt_style = Style(root)
                                ques1_C_Opt_style.theme_use("default")
                                ques1_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques3_Opt2.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques3_Opt1.configure(state=DISABLED)
                                ques3_Opt3.configure(state=DISABLED)
                                ques3_Opt4.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #3)
                            def ques3_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques3_Opt_style = Style(root)
                                ques3_Opt_style.theme_use("default")
                                ques3_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques3_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques3_Opt1.configure(state=DISABLED)
                                ques3_Opt2.configure(state=DISABLED)
                                ques3_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques1WO4_style = Style(root)
                                ques1WO4_style.theme_use("default")
                                ques1WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques3_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #3)
                            def ques3_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques3_Opt_style = Style(root)
                                ques3_Opt_style.theme_use("default")
                                ques3_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques3_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques3_Opt1.configure(state=DISABLED)
                                ques3_Opt2.configure(state=DISABLED)
                                ques3_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques3WO3_style = Style(root)
                                ques3WO3_style.theme_use("default")
                                ques3WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques3_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #3)
                            def ques3_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques3_Opt_style = Style(root)
                                ques3_Opt_style.theme_use("default")
                                ques3_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques3_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques3_Opt1.configure(state=DISABLED)
                                ques3_Opt3.configure(state=DISABLED)
                                ques3_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #3)
                                root.after(3000, lambda: points())

                            # Function which is triggered by Option-1 of (Question #3)
                            def ques3_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques3_Opt_style = Style(root)
                                ques3_Opt_style.theme_use("default")
                                ques3_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques3_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques3_Opt2.configure(state=DISABLED)
                                ques3_Opt3.configure(state=DISABLED)
                                ques3_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques1WO1_style = Style(root)
                                ques1WO1_style.theme_use("default")
                                ques1WO1_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques3_Opt1.configure(
                                    style="X.TRadiobutton"))

                            # -------------------------------------------------------------------------------------------- (Question #3) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-3's (Question #3) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #3)
                            label6 = Label(root, text="3. Chlorophyll is a naturally occurring chelate compound in which central metal is", font=("Dodge", 14),
                                           foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label6.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #3) Options
                            ques3_Opt_style = Style(root)
                            ques3_Opt_style.theme_use("default")
                            ques3_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques3_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #3)
                            # Creating Option-1 and assigning a styler function to it
                            v3 = IntVar(root)
                            ques3_Opt1 = Radiobutton(root, text="copper", variable=v3,
                                                     value=1, command=lambda: ques3_Opt_1())
                            ques3_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques3_Opt2 = Radiobutton(root, text="magnesium", variable=v3,
                                                     value=2, command=lambda: ques3_Opt_2())
                            ques3_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques3_Opt3 = Radiobutton(root, text="iron", variable=v3,
                                                     value=3, command=lambda: ques3_Opt_3())
                            ques3_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques3_Opt4 = Radiobutton(root, text="calcium", variable=v3,
                                                     value=4, command=lambda: ques3_Opt_4())
                            ques3_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #3)
                            timer3 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer3.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer3.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer3.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer3.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer3.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer3.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer3.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer3.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer3.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer3.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer3.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer3.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer3.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer3.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer3.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer3.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #3) after timer stops
                            root.after(15200, lambda: ques3_Correct())

                            # Destroying all the widgets showing (Question #3)
                            root.after(16100, timer3.destroy)
                            root.after(17400, ques3_Opt1.destroy)
                            root.after(17400, ques3_Opt2.destroy)
                            root.after(17500, ques3_Opt3.destroy)
                            root.after(17400, ques3_Opt4.destroy)
                            root.after(17500, label6.destroy)

                            # Calling the function to create Topic-3's (Question #4)
                            root.after(18000, lambda: ques4())

                            # -------------------------------------------------------------------------------------------- Topic-3's (Question #3) -StyleEnds----

                        # >>

                        # Function which creates Topic-3's (Question #2)
                        def ques2():

                            # ------------------------------------- (Question #2)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques2_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques2_C_Opt_style = Style(root)
                                ques2_C_Opt_style.theme_use("default")
                                ques2_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques2_Opt2.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques2_Opt1.configure(state=DISABLED)
                                ques2_Opt3.configure(state=DISABLED)
                                ques2_Opt4.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #2)
                            def ques2_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques2_Opt_style = Style(root)
                                ques2_Opt_style.theme_use("default")
                                ques2_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques2_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques2_Opt1.configure(state=DISABLED)
                                ques2_Opt2.configure(state=DISABLED)
                                ques2_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques2WO4_style = Style(root)
                                ques2WO4_style.theme_use("default")
                                ques2WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques2_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #2)
                            def ques2_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques2_Opt_style = Style(root)
                                ques2_Opt_style.theme_use("default")
                                ques2_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques2_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques2_Opt1.configure(state=DISABLED)
                                ques2_Opt2.configure(state=DISABLED)
                                ques2_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques2WO3_style = Style(root)
                                ques2WO3_style.theme_use("default")
                                ques2WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques2_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #2)
                            def ques2_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques2_Opt_style = Style(root)
                                ques2_Opt_style.theme_use("default")
                                ques2_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques2_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques2_Opt1.configure(state=DISABLED)
                                ques2_Opt3.configure(state=DISABLED)
                                ques2_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #2)
                                root.after(3000, lambda: points())

                            # Function which is triggered by Option-1 of (Question #2)
                            def ques2_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques2_Opt_style = Style(root)
                                ques2_Opt_style.theme_use("default")
                                ques2_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques2_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques2_Opt2.configure(state=DISABLED)
                                ques2_Opt3.configure(state=DISABLED)
                                ques2_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques2WO1_style = Style(root)
                                ques2WO1_style.theme_use("default")
                                ques2WO1_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques2_Opt1.configure(
                                    style="X.TRadiobutton"))

                            # -------------------------------------------------------------------------------------------- (Question #2) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-3's (Question #2) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #2)
                            label5 = Label(root, text="2. Which of the following is a non metal that remains liquid at room temperature?", font=("Dodge", 14),
                                           foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label5.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #2) Options
                            ques2_Opt_style = Style(root)
                            ques2_Opt_style.theme_use("default")
                            ques2_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques2_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #2)
                            # Creating Option-1 and assigning a styler function to it
                            v2 = IntVar(root)
                            ques2_Opt1 = Radiobutton(root, text="Phosphorous", variable=v2,
                                                     value=1, command=lambda: ques2_Opt_1())
                            ques2_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques2_Opt2 = Radiobutton(root, text="Bromine", variable=v2,
                                                     value=2, command=lambda: ques2_Opt_2())
                            ques2_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques2_Opt3 = Radiobutton(root, text="Chlorine", variable=v2,
                                                     value=3, command=lambda: ques2_Opt_3())
                            ques2_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques2_Opt4 = Radiobutton(root, text="Helium", variable=v2,
                                                     value=4, command=lambda: ques2_Opt_4())
                            ques2_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #2)
                            timer2 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer2.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer2.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer2.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer2.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer2.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer2.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer2.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer2.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer2.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer2.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer2.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer2.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer2.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer2.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer2.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer2.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #2) after timer stops
                            root.after(15200, lambda: ques2_Correct())

                            # Destroying all the widgets showing (Question #2)
                            root.after(16100, timer2.destroy)
                            root.after(17400, ques2_Opt1.destroy)
                            root.after(17500, ques2_Opt2.destroy)
                            root.after(17400, ques2_Opt3.destroy)
                            root.after(17400, ques2_Opt4.destroy)
                            root.after(17500, label5.destroy)

                            # Calling the function to create Topic-3's (Question #3)
                            root.after(18000, lambda: ques3())

                            # -------------------------------------------------------------------------------------------- Topic-3's (Question #2) -StyleEnds----

                        # >>

                        # Function which creates Topic-3's (Question #1)
                        def ques1():

                            # ------------------------------------- (Question #1)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques1_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques1_C_Opt_style = Style(root)
                                ques1_C_Opt_style.theme_use("default")
                                ques1_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques1_Opt2.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques1_Opt1.configure(state=DISABLED)
                                ques1_Opt3.configure(state=DISABLED)
                                ques1_Opt4.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #1)
                            def ques1_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques1_Opt_style = Style(root)
                                ques1_Opt_style.theme_use("default")
                                ques1_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques1_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques1_Opt1.configure(state=DISABLED)
                                ques1_Opt2.configure(state=DISABLED)
                                ques1_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques1WO4_style = Style(root)
                                ques1WO4_style.theme_use("default")
                                ques1WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques1_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #1)
                            def ques1_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques1_Opt_style = Style(root)
                                ques1_Opt_style.theme_use("default")
                                ques1_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques1_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques1_Opt1.configure(state=DISABLED)
                                ques1_Opt2.configure(state=DISABLED)
                                ques1_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques1WO3_style = Style(root)
                                ques1WO3_style.theme_use("default")
                                ques1WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques1_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #1)
                            def ques1_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques1_Opt_style = Style(root)
                                ques1_Opt_style.theme_use("default")
                                ques1_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques1_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques1_Opt1.configure(state=DISABLED)
                                ques1_Opt3.configure(state=DISABLED)
                                ques1_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #1)
                                root.after(3000, lambda: points())

                            # Function which is triggered by Option-1 of (Question #1)
                            def ques1_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques1_Opt_style = Style(root)
                                ques1_Opt_style.theme_use("default")
                                ques1_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques1_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques1_Opt2.configure(state=DISABLED)
                                ques1_Opt3.configure(state=DISABLED)
                                ques1_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques1WO1_style = Style(root)
                                ques1WO1_style.theme_use("default")
                                ques1WO1_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques1_Opt1.configure(
                                    style="X.TRadiobutton"))

                            # -------------------------------------------------------------------------------------------- (Question #1) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-3's (Question #1) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #1)
                            label4 = Label(root, text="1. Brass gets discoloured in air because of the presence of which of the following gases in air?", font=("Dodge", 14),
                                           foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label4.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #1) Options
                            ques1_Opt_style = Style(root)
                            ques1_Opt_style.theme_use("default")
                            ques1_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques1_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #1)
                            # Creating Option-1 and assigning a styler function to it
                            v1 = IntVar(root)
                            ques1_Opt1 = Radiobutton(root, text="Oxygen", variable=v1,
                                                     value=1, command=lambda: ques1_Opt_1())
                            ques1_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques1_Opt2 = Radiobutton(root, text="Hydrogen sulphide", variable=v1,
                                                     value=2, command=lambda: ques1_Opt_2())
                            ques1_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques1_Opt3 = Radiobutton(root, text="Carbon dioxide", variable=v1,
                                                     value=3, command=lambda: ques1_Opt_3())
                            ques1_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques1_Opt4 = Radiobutton(root, text="Nitrogen", variable=v1,
                                                     value=4, command=lambda: ques1_Opt_4())
                            ques1_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #1)
                            timer1 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer1.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer1.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer1.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer1.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer1.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer1.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer1.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer1.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer1.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer1.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer1.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer1.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer1.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer1.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer1.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer1.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #1) after timer stops
                            root.after(15200, lambda: ques1_Correct())

                            # Destroying all the widgets showing (Question #1)
                            root.after(16100, timer1.destroy)
                            root.after(17400, ques1_Opt1.destroy)
                            root.after(17400, ques1_Opt2.destroy)
                            root.after(17500, ques1_Opt3.destroy)
                            root.after(17400, ques1_Opt4.destroy)
                            root.after(17500, label4.destroy)

                            # Calling the function to create Topic-3's (Question #2)
                            root.after(18000, lambda: ques2())

                            # -------------------------------------------------------------------------------------------- Topic-3's (Question #1) -StyleEnds----

                        # >>

                        # Disabling the Quiz Start-Button after clicked, for preventing the function to be called twice
                        start_button2.configure(state=DISABLED)

                        # Destroying all the widgets created in the Rules Panel for Topic-3
                        root.after(500, rules.destroy)
                        root.after(600, start_button2.destroy)
                        root.after(500, label2.destroy)
                        root.after(500, back3_button.destroy)

                        # Calling the function to create Topic-3's (Question #1)
                        root.after(800, lambda: ques1())

                    # >>

                    # ------------------------------------- Rules Panel for Topic-3 -StyleStarts----------------------------------------------------

                    # Disabling the Topic-Button3 after clicked, for preventing the function to be called twice
                    topic_button3.configure(state=DISABLED)

                    # Destroying all the widgets created in the Topic-Select Panel
                    root.after(800, topic_button3.destroy)
                    root.after(400, topic_button1.destroy)
                    root.after(400, topic_button2.destroy)
                    root.after(400, back2_button.destroy)

                    # Changing the text in the Topic-Select Panel label instead of destroying it
                    root.after(800, label2.configure(text="Rules"))

                    # Displaying the rules related to Topic-3's Quiz
                    rules = Message(root, text="    1. Each question has a time limit of 15 seconds.\r\n    2. Once the option is selected it can't be changed.\r\n    3. Final Score is displayed at the end.\r\n    4. The following questions are based on science.", font=("Dodge", 12),
                                    foreground="#D1E3DD", background="#1E0905", width=400)
                    rules.place(relx=0.5, rely=0.42, anchor=CENTER)

                    # Creating and Styling the Quiz Start-Button
                    start_button2_style = Style()
                    start_button2_style.configure("B.TButton", font=("Playball", 17, "bold", "italic"),
                                                  foreground="#0A0908", background="#F6F67C", borderwidth=2, width=8, height=2)
                    start_button2 = Button(root, text="Start",
                                           style="B.TButton", command=lambda: quiz1())
                    start_button2.place(relx=0.5, rely=0.75, anchor=CENTER)

                    # Creating a Back-Button to return to User-Select Panel
                    # Styling Back-Button
                    back3_button_style = Style()
                    back3_button_style.theme_use("default")
                    back3_button_style.configure("E.TButton", font=("Playball", 10, "italic", "bold"),
                                                 foreground="#0A0908", background="#F6F67C", borderwidth=2, width=10, height=2, focuscolor="none")

                    back3_button = Button(root, text="< back",
                                          style="E.TButton", command=lambda: back3())
                    back3_button.place(relx=0.15, rely=0.9, anchor=CENTER)

                    # -------------------------------------------------------------------------------------------- Rules Panel for Topic-3 -StyleEnds----

                # >>

                # Function which creates the Rules Panel for Topic-2
                def topic_2():

                    # Function which is operated by the Topic-2's Rules Panel Back-Button
                    def back3():

                        # Disabling the Back-Button after clicked, for preventing the function to be called twice
                        back3_button.configure(state=DISABLED)

                        # Destroying all the widgets created in the Topic-Select Panel
                        root.after(600, lambda: back3_button.destroy())
                        root.after(500, lambda: rules.destroy())
                        root.after(500, lambda: start_button2.destroy())
                        root.after(500, lambda: label2.destroy())
                        root.after(500, lambda: label3.destroy())
                        root.after(500, lambda: label31.destroy())

                        # Calling the function to redirect to the User-Select panel
                        root.after(800, lambda: userSelect())

                    # >>

                    # Function for displaying the GuestName centered above the score
                    def scoreCard():

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

                        # Creating a 'leaderboard' table if not exists to store the Guestname and score
                        co.execute("""CREATE TABLE IF NOT EXISTS leaderboard (
                                    playername text,
                                    score integer
                                    )""")

                        # Updating the leaderboard with the Guest's name and total score
                        co.execute("INSERT INTO leaderboard VALUES (:text3, :point)",
                                   {
                                       "text3": text3,
                                       "point": point
                                   })

                        # Committing the changes to the database
                        quizdata.commit()

                        # Closing the connection with the database
                        quizdata.close()

                    # >>

                    # Function which is triggered by the Topic-2's Rules Panel Quiz Start-Button
                    def quiz1():

                        # Function which creates Topic-2's (Question #10)
                        def ques10():

                            # ------------------------------------- (Question #10)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques10_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques10_C_Opt_style = Style(root)
                                ques10_C_Opt_style.theme_use("default")
                                ques10_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                             foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques10_Opt1.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques10_Opt2.configure(state=DISABLED)
                                ques10_Opt3.configure(state=DISABLED)
                                ques10_Opt4.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #10)
                            def ques10_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques10_Opt_style = Style(root)
                                ques10_Opt_style.theme_use("default")
                                ques10_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                           foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques10_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques10_Opt1.configure(state=DISABLED)
                                ques10_Opt2.configure(state=DISABLED)
                                ques10_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques10WO4_style = Style(root)
                                ques10WO4_style.theme_use("default")
                                ques10WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques10_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #10)
                            def ques10_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques10_Opt_style = Style(root)
                                ques10_Opt_style.theme_use("default")
                                ques10_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                           foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques10_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques10_Opt1.configure(state=DISABLED)
                                ques10_Opt2.configure(state=DISABLED)
                                ques10_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques10WO3_style = Style(root)
                                ques10WO3_style.theme_use("default")
                                ques10WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques10_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #10)
                            def ques10_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques10_Opt_style = Style(root)
                                ques10_Opt_style.theme_use("default")
                                ques10_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                           foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-2 to yellow color
                                ques10_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques10_Opt1.configure(state=DISABLED)
                                ques10_Opt3.configure(state=DISABLED)
                                ques10_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques10WO2_style = Style(root)
                                ques10WO2_style.theme_use("default")
                                ques10WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques10_Opt2.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-1 of (Question #10)
                            def ques10_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques10_Opt_style = Style(root)
                                ques10_Opt_style.theme_use("default")
                                ques10_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                           foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques10_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques10_Opt2.configure(state=DISABLED)
                                ques10_Opt3.configure(state=DISABLED)
                                ques10_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #10)
                                root.after(3000, lambda: points())

                            # -------------------------------------------------------------------------------------------- (Question #10) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-2's (Question #10) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #10)
                            label13 = Label(root, text="10. '.WAV' extension refers usually to what kind of file?", font=("Dodge", 14),
                                            foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label13.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #10) Options
                            ques10_Opt_style = Style(root)
                            ques10_Opt_style.theme_use("default")
                            ques10_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                       foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques10_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #10)
                            # Creating Option-1 and assigning a styler function to it
                            v10 = IntVar(root)
                            ques10_Opt1 = Radiobutton(root, text="Audio file", variable=v10,
                                                      value=1, command=lambda: ques10_Opt_1())
                            ques10_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques10_Opt2 = Radiobutton(root, text="MS Office document", variable=v10,
                                                      value=2, command=lambda: ques10_Opt_2())
                            ques10_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques10_Opt3 = Radiobutton(root, text="Animation/movie file", variable=v10,
                                                      value=3, command=lambda: ques10_Opt_3())
                            ques10_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques10_Opt4 = Radiobutton(root, text="Image file", variable=v10,
                                                      value=4, command=lambda: ques10_Opt_4())
                            ques10_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #10)
                            timer10 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                              foreground="#F0EFF4", background="#22333B", width=600)
                            timer10.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer10.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer10.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer10.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer10.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer10.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer10.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer10.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer10.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer10.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer10.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer10.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer10.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer10.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer10.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer10.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #10) after timer stops
                            root.after(15200, lambda: ques10_Correct())

                            # Destroying all the widgets showing (Question #10)
                            root.after(16100, timer10.destroy)
                            root.after(17400, ques10_Opt1.destroy)
                            root.after(17400, ques10_Opt2.destroy)
                            root.after(17500, ques10_Opt3.destroy)
                            root.after(17400, ques10_Opt4.destroy)
                            root.after(17500, label13.destroy)

                            # Calling the function to update the Total score to database and mean time displaying it to the Guest
                            root.after(18000, lambda: scoreCard())

                            # Calling the function to display the Total Score
                            root.after(18500, lambda: finalScore())

                            # Calling the function to create exit and leaderboard button
                            root.after(19500, lambda: creatingExit())

                        # -------------------------------------------------------------------------------------------- Topic-2's (Question #10) -StyleEnds----

                        # >>

                        # Function which creates Topic-2's (Question #9)
                        def ques9():

                            # ------------------------------------- (Question #9)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques9_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques9_C_Opt_style = Style(root)
                                ques9_C_Opt_style.theme_use("default")
                                ques9_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques9_Opt1.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques9_Opt2.configure(state=DISABLED)
                                ques9_Opt3.configure(state=DISABLED)
                                ques9_Opt4.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #9)
                            def ques9_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques9_Opt_style = Style(root)
                                ques9_Opt_style.theme_use("default")
                                ques9_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques9_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques9_Opt1.configure(state=DISABLED)
                                ques9_Opt2.configure(state=DISABLED)
                                ques9_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques9WO4_style = Style(root)
                                ques9WO4_style.theme_use("default")
                                ques9WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques9_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #9)
                            def ques9_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques9_Opt_style = Style(root)
                                ques9_Opt_style.theme_use("default")
                                ques9_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques9_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques9_Opt1.configure(state=DISABLED)
                                ques9_Opt2.configure(state=DISABLED)
                                ques9_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques9WO3_style = Style(root)
                                ques9WO3_style.theme_use("default")
                                ques9WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques9_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #9)
                            def ques9_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques9_Opt_style = Style(root)
                                ques9_Opt_style.theme_use("default")
                                ques9_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-2 to yellow color
                                ques9_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques9_Opt1.configure(state=DISABLED)
                                ques9_Opt3.configure(state=DISABLED)
                                ques9_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques9WO2_style = Style(root)
                                ques9WO2_style.theme_use("default")
                                ques9WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques9_Opt2.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-1 of (Question #9)
                            def ques9_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques9_Opt_style = Style(root)
                                ques9_Opt_style.theme_use("default")
                                ques9_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques9_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques9_Opt2.configure(state=DISABLED)
                                ques9_Opt3.configure(state=DISABLED)
                                ques9_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #9)
                                root.after(3000, lambda: points())

                            # -------------------------------------------------------------------------------------------- (Question #9) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-2's (Question #9) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #9)
                            label12 = Label(root, text="9. The 'desktop' of a computer refers to the", font=("Dodge", 14),
                                            foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label12.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #9) Options
                            ques9_Opt_style = Style(root)
                            ques9_Opt_style.theme_use("default")
                            ques9_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques9_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #9)
                            # Creating Option-1 and assigning a styler function to it
                            v9 = IntVar(root)
                            ques9_Opt1 = Radiobutton(root, text="visible screen", variable=v9,
                                                     value=1, command=lambda: ques9_Opt_1())
                            ques9_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques9_Opt2 = Radiobutton(root, text="area around monitor", variable=v9,
                                                     value=2, command=lambda: ques9_Opt_2())
                            ques9_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques9_Opt3 = Radiobutton(root, text="top of mouse pad", variable=v9,
                                                     value=3, command=lambda: ques9_Opt_3())
                            ques9_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques9_Opt4 = Radiobutton(root, text="inside a folder", variable=v9,
                                                     value=4, command=lambda: ques9_Opt_4())
                            ques9_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #9)
                            timer9 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer9.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer9.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer9.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer9.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer9.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer9.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer9.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer9.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer9.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer9.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer9.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer9.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer9.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer9.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer9.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer9.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #9) after timer stops
                            root.after(15200, lambda: ques9_Correct())

                            # Destroying all the widgets showing (Question #9)
                            root.after(16100, timer9.destroy)
                            root.after(17400, ques9_Opt1.destroy)
                            root.after(17400, ques9_Opt2.destroy)
                            root.after(17500, ques9_Opt3.destroy)
                            root.after(17400, ques9_Opt4.destroy)
                            root.after(17500, label12.destroy)

                            # Calling the function to create Topic-2's (Question #10)
                            root.after(18000, lambda: ques10())

                        # -------------------------------------------------------------------------------------------- Topic-2's (Question #9) -StyleEnds----

                        # >>

                        # Function which creates Topic-2's (Question #8)
                        def ques8():

                            # ------------------------------------- (Question #8)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques8_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques8_C_Opt_style = Style(root)
                                ques8_C_Opt_style.theme_use("default")
                                ques8_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques8_Opt3.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques8_Opt2.configure(state=DISABLED)
                                ques8_Opt1.configure(state=DISABLED)
                                ques8_Opt4.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #8)
                            def ques8_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques8_Opt_style = Style(root)
                                ques8_Opt_style.theme_use("default")
                                ques8_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques8_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques8_Opt1.configure(state=DISABLED)
                                ques8_Opt2.configure(state=DISABLED)
                                ques8_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques8WO4_style = Style(root)
                                ques8WO4_style.theme_use("default")
                                ques8WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques8_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #8)
                            def ques8_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques8_Opt_style = Style(root)
                                ques8_Opt_style.theme_use("default")
                                ques8_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques8_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques8_Opt1.configure(state=DISABLED)
                                ques8_Opt2.configure(state=DISABLED)
                                ques8_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #8)
                                root.after(3000, lambda: points())

                            # Function which is triggered by Option-2 of (Question #8)
                            def ques8_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques8_Opt_style = Style(root)
                                ques8_Opt_style.theme_use("default")
                                ques8_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-2 to yellow color
                                ques8_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques8_Opt1.configure(state=DISABLED)
                                ques8_Opt3.configure(state=DISABLED)
                                ques8_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques8WO2_style = Style(root)
                                ques8WO2_style.theme_use("default")
                                ques8WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques8_Opt2.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-1 of (Question #8)
                            def ques8_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques8_Opt_style = Style(root)
                                ques8_Opt_style.theme_use("default")
                                ques8_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques8_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques8_Opt2.configure(state=DISABLED)
                                ques8_Opt3.configure(state=DISABLED)
                                ques8_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques8WO1_style = Style(root)
                                ques8WO1_style.theme_use("default")
                                ques8WO1_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques8_Opt1.configure(
                                    style="X.TRadiobutton"))

                            # -------------------------------------------------------------------------------------------- (Question #8) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-2's (Question #8) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #8)
                            label11 = Label(root, text="8. Computers calculate numbers in what mode?", font=("Dodge", 14),
                                            foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label11.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #8) Options
                            ques8_Opt_style = Style(root)
                            ques8_Opt_style.theme_use("default")
                            ques8_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques8_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #8)
                            # Creating Option-1 and assigning a styler function to it
                            v8 = IntVar(root)
                            ques8_Opt1 = Radiobutton(root, text="Decimal", variable=v8,
                                                     value=1, command=lambda: ques8_Opt_1())
                            ques8_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques8_Opt2 = Radiobutton(root, text="Octal", variable=v8,
                                                     value=2, command=lambda: ques8_Opt_2())
                            ques8_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques8_Opt3 = Radiobutton(root, text="Binary", variable=v8,
                                                     value=3, command=lambda: ques8_Opt_3())
                            ques8_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques8_Opt4 = Radiobutton(root, text="Hexa", variable=v8,
                                                     value=4, command=lambda: ques8_Opt_4())
                            ques8_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #8)
                            timer8 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer8.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer8.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer8.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer8.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer8.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer8.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer8.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer8.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer8.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer8.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer8.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer8.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer8.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer8.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer8.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer8.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #8) after timer stops
                            root.after(15200, lambda: ques8_Correct())

                            # Destroying all the widgets showing (Question #8)
                            root.after(16100, timer8.destroy)
                            root.after(17400, ques8_Opt1.destroy)
                            root.after(17400, ques8_Opt2.destroy)
                            root.after(17500, ques8_Opt3.destroy)
                            root.after(17400, ques8_Opt4.destroy)
                            root.after(17500, label11.destroy)

                            # Calling the function to create Topic-2's (Question #9)
                            root.after(18000, lambda: ques9())

                        # -------------------------------------------------------------------------------------------- Topic-2's (Question #8) -StyleEnds----

                        # >>

                        # Function which creates Topic-2's (Question #7)
                        def ques7():

                            # ------------------------------------- (Question #7)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques7_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques7_C_Opt_style = Style(root)
                                ques7_C_Opt_style.theme_use("default")
                                ques7_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques7_Opt3.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques7_Opt2.configure(state=DISABLED)
                                ques7_Opt1.configure(state=DISABLED)
                                ques7_Opt4.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #7)
                            def ques7_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques7_Opt_style = Style(root)
                                ques7_Opt_style.theme_use("default")
                                ques7_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques7_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques7_Opt1.configure(state=DISABLED)
                                ques7_Opt2.configure(state=DISABLED)
                                ques7_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques7WO4_style = Style(root)
                                ques7WO4_style.theme_use("default")
                                ques7WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques7_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #7)
                            def ques7_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques7_Opt_style = Style(root)
                                ques7_Opt_style.theme_use("default")
                                ques7_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques7_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques7_Opt1.configure(state=DISABLED)
                                ques7_Opt2.configure(state=DISABLED)
                                ques7_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #7)
                                root.after(3000, lambda: points())

                            # Function which is triggered by Option-2 of (Question #7)
                            def ques7_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques7_Opt_style = Style(root)
                                ques7_Opt_style.theme_use("default")
                                ques7_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-2 to yellow color
                                ques7_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques7_Opt1.configure(state=DISABLED)
                                ques7_Opt3.configure(state=DISABLED)
                                ques7_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques7WO2_style = Style(root)
                                ques7WO2_style.theme_use("default")
                                ques7WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques7_Opt2.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-1 of (Question #7)
                            def ques7_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques7_Opt_style = Style(root)
                                ques7_Opt_style.theme_use("default")
                                ques7_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques7_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques7_Opt2.configure(state=DISABLED)
                                ques7_Opt3.configure(state=DISABLED)
                                ques7_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques7WO1_style = Style(root)
                                ques7WO1_style.theme_use("default")
                                ques7WO1_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques7_Opt1.configure(
                                    style="X.TRadiobutton"))

                            # -------------------------------------------------------------------------------------------- (Question #7) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-2's (Question #7) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #7)
                            label10 = Label(root, text="7. The speed of your net access is defined in terms of", font=("Dodge", 14),
                                            foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label10.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #7) Options
                            ques7_Opt_style = Style(root)
                            ques7_Opt_style.theme_use("default")
                            ques7_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques7_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #7)
                            # Creating Option-1 and assigning a styler function to it
                            v7 = IntVar(root)
                            ques7_Opt1 = Radiobutton(root, text="RAM", variable=v7,
                                                     value=1, command=lambda: ques7_Opt_1())
                            ques7_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques7_Opt2 = Radiobutton(root, text="MHz", variable=v7,
                                                     value=2, command=lambda: ques7_Opt_2())
                            ques7_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques7_Opt3 = Radiobutton(root, text="Kbps", variable=v7,
                                                     value=3, command=lambda: ques7_Opt_3())
                            ques7_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques7_Opt4 = Radiobutton(root, text="Megabytes", variable=v7,
                                                     value=4, command=lambda: ques7_Opt_4())
                            ques7_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #7)
                            timer7 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer7.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer7.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer7.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer7.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer7.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer7.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer7.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer7.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer7.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer7.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer7.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer7.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer7.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer7.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer7.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer7.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #7) after timer stops
                            root.after(15200, lambda: ques7_Correct())

                            # Destroying all the widgets showing (Question #7)
                            root.after(16100, timer7.destroy)
                            root.after(17400, ques7_Opt1.destroy)
                            root.after(17400, ques7_Opt2.destroy)
                            root.after(17500, ques7_Opt3.destroy)
                            root.after(17400, ques7_Opt4.destroy)
                            root.after(17500, label10.destroy)

                            # Calling the function to create Topic-2's (Question #8)
                            root.after(18000, lambda: ques8())

                        # -------------------------------------------------------------------------------------------- Topic-2's (Question #7) -StyleEnds----

                        # >>

                        # Function which creates Topic-2's (Question #6)
                        def ques6():

                            # ------------------------------------- (Question #6)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques6_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques6_C_Opt_style = Style(root)
                                ques6_C_Opt_style.theme_use("default")
                                ques6_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques6_Opt2.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques6_Opt1.configure(state=DISABLED)
                                ques6_Opt4.configure(state=DISABLED)
                                ques6_Opt3.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #6)
                            def ques6_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques6_Opt_style = Style(root)
                                ques6_Opt_style.theme_use("default")
                                ques6_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques6_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques6_Opt1.configure(state=DISABLED)
                                ques6_Opt2.configure(state=DISABLED)
                                ques6_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques6WO2_style = Style(root)
                                ques6WO2_style.theme_use("default")
                                ques6WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques6_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #6)
                            def ques6_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques6_Opt_style = Style(root)
                                ques6_Opt_style.theme_use("default")
                                ques6_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques6_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques6_Opt1.configure(state=DISABLED)
                                ques6_Opt2.configure(state=DISABLED)
                                ques6_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques6WO3_style = Style(root)
                                ques6WO3_style.theme_use("default")
                                ques6WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques6_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #6)
                            def ques6_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques6_Opt_style = Style(root)
                                ques6_Opt_style.theme_use("default")
                                ques6_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques6_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques6_Opt1.configure(state=DISABLED)
                                ques6_Opt3.configure(state=DISABLED)
                                ques6_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #6)
                                root.after(3000, lambda: points())

                            # Function which is triggered by Option-1 of (Question #6)
                            def ques6_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques6_Opt_style = Style(root)
                                ques6_Opt_style.theme_use("default")
                                ques6_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques6_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques6_Opt2.configure(state=DISABLED)
                                ques6_Opt3.configure(state=DISABLED)
                                ques6_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques6WO1_style = Style(root)
                                ques6WO1_style.theme_use("default")
                                ques6WO1_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques6_Opt1.configure(
                                    style="X.TRadiobutton"))

                            # -------------------------------------------------------------------------------------------- (Question #6) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-2's (Question #6) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #6)
                            label9 = Label(root, text="6. How many bits is a byte?", font=("Dodge", 14),
                                           foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label9.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #6) Options
                            ques6_Opt_style = Style(root)
                            ques6_Opt_style.theme_use("default")
                            ques6_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques6_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #6)
                            # Creating Option-1 and assigning a styler function to it
                            v6 = IntVar(root)
                            ques6_Opt1 = Radiobutton(root, text="4 bits", variable=v6,
                                                     value=1, command=lambda: ques6_Opt_1())
                            ques6_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques6_Opt2 = Radiobutton(root, text="8 bits", variable=v6,
                                                     value=2, command=lambda: ques6_Opt_2())
                            ques6_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques6_Opt3 = Radiobutton(root, text="16 bits", variable=v6,
                                                     value=3, command=lambda: ques6_Opt_3())
                            ques6_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques6_Opt4 = Radiobutton(root, text="32 bits", variable=v6,
                                                     value=4, command=lambda: ques6_Opt_4())
                            ques6_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #6)
                            timer6 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer6.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer6.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer6.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer6.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer6.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer6.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer6.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer6.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer6.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer6.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer6.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer6.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer6.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer6.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer6.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer6.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #6) after timer stops
                            root.after(15200, lambda: ques6_Correct())

                            # Destroying all the widgets showing (Question #6)
                            root.after(16100, timer6.destroy)
                            root.after(17400, ques6_Opt1.destroy)
                            root.after(17400, ques6_Opt2.destroy)
                            root.after(17500, ques6_Opt3.destroy)
                            root.after(17400, ques6_Opt4.destroy)
                            root.after(17500, label9.destroy)

                            # Calling the function to create Topic-2's (Question #7)
                            root.after(18000, lambda: ques7())

                        # -------------------------------------------------------------------------------------------- Topic-2's (Question #6) -StyleEnds----

                        # >>

                        # Function which creates Topic-2's (Question #5)
                        def ques5():

                            # ------------------------------------- (Question #5)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques5_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques5_C_Opt_style = Style(root)
                                ques5_C_Opt_style.theme_use("default")
                                ques5_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques5_Opt2.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques5_Opt1.configure(state=DISABLED)
                                ques5_Opt4.configure(state=DISABLED)
                                ques5_Opt3.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #5)
                            def ques5_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques5_Opt_style = Style(root)
                                ques5_Opt_style.theme_use("default")
                                ques5_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques5_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques5_Opt1.configure(state=DISABLED)
                                ques5_Opt2.configure(state=DISABLED)
                                ques5_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques5WO4_style = Style(root)
                                ques5WO4_style.theme_use("default")
                                ques5WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques5_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #5)
                            def ques5_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques5_Opt_style = Style(root)
                                ques5_Opt_style.theme_use("default")
                                ques5_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques5_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques5_Opt1.configure(state=DISABLED)
                                ques5_Opt2.configure(state=DISABLED)
                                ques5_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques5WO3_style = Style(root)
                                ques5WO3_style.theme_use("default")
                                ques5WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques5_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #5)
                            def ques5_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques5_Opt_style = Style(root)
                                ques5_Opt_style.theme_use("default")
                                ques5_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques5_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques5_Opt1.configure(state=DISABLED)
                                ques5_Opt3.configure(state=DISABLED)
                                ques5_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #5)
                                root.after(3000, lambda: points())

                            # Function which is triggered by Option-1 of (Question #5)
                            def ques5_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques5_Opt_style = Style(root)
                                ques5_Opt_style.theme_use("default")
                                ques5_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques5_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques5_Opt2.configure(state=DISABLED)
                                ques5_Opt3.configure(state=DISABLED)
                                ques5_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques5WO1_style = Style(root)
                                ques5WO1_style.theme_use("default")
                                ques5WO1_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques5_Opt1.configure(
                                    style="X.TRadiobutton"))

                            # -------------------------------------------------------------------------------------------- (Question #5) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-2's (Question #5) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #5)
                            label8 = Label(root, text="5. '.MOV' extension refers usually to what kind of file?", font=("Dodge", 14),
                                           foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label8.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #5) Options
                            ques5_Opt_style = Style(root)
                            ques5_Opt_style.theme_use("default")
                            ques5_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques5_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #5)
                            # Creating Option-1 and assigning a styler function to it
                            v5 = IntVar(root)
                            ques5_Opt1 = Radiobutton(root, text="Image file", variable=v5,
                                                     value=1, command=lambda: ques5_Opt_1())
                            ques5_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques5_Opt2 = Radiobutton(root, text="Animation file", variable=v5,
                                                     value=2, command=lambda: ques5_Opt_2())
                            ques5_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques5_Opt3 = Radiobutton(root, text="Audio file", variable=v5,
                                                     value=3, command=lambda: ques5_Opt_3())
                            ques5_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques5_Opt4 = Radiobutton(root, text="MS Office document", variable=v5,
                                                     value=4, command=lambda: ques5_Opt_4())
                            ques5_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #5)
                            timer5 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer5.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer5.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer5.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer5.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer5.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer5.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer5.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer5.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer5.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer5.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer5.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer5.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer5.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer5.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer5.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer5.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #5) after timer stops
                            root.after(15200, lambda: ques5_Correct())

                            # Destroying all the widgets showing (Question #5)
                            root.after(16100, timer5.destroy)
                            root.after(17400, ques5_Opt1.destroy)
                            root.after(17400, ques5_Opt2.destroy)
                            root.after(17500, ques5_Opt3.destroy)
                            root.after(17400, ques5_Opt4.destroy)
                            root.after(17500, label8.destroy)

                            # Calling the function to create Topic-2's (Question #6)
                            root.after(18000, lambda: ques6())

                        # -------------------------------------------------------------------------------------------- Topic-2's (Question #5) -StyleEnds----

                        # >>

                        # Function which creates Topic-2's (Question #4)
                        def ques4():

                            # ------------------------------------- (Question #4)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques4_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques4_C_Opt_style = Style(root)
                                ques4_C_Opt_style.theme_use("default")
                                ques4_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques4_Opt1.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques4_Opt4.configure(state=DISABLED)
                                ques4_Opt2.configure(state=DISABLED)
                                ques4_Opt3.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #4)
                            def ques4_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques4_Opt_style = Style(root)
                                ques4_Opt_style.theme_use("default")
                                ques4_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques4_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques4_Opt1.configure(state=DISABLED)
                                ques4_Opt2.configure(state=DISABLED)
                                ques4_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques4WO4_style = Style(root)
                                ques4WO4_style.theme_use("default")
                                ques4WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques4_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #4)
                            def ques4_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques4_Opt_style = Style(root)
                                ques4_Opt_style.theme_use("default")
                                ques4_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques4_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques4_Opt1.configure(state=DISABLED)
                                ques4_Opt2.configure(state=DISABLED)
                                ques4_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques4WO3_style = Style(root)
                                ques4WO3_style.theme_use("default")
                                ques4WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques4_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #4)
                            def ques4_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques4_Opt_style = Style(root)
                                ques4_Opt_style.theme_use("default")
                                ques4_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques4_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques4_Opt1.configure(state=DISABLED)
                                ques4_Opt3.configure(state=DISABLED)
                                ques4_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques4WO2_style = Style(root)
                                ques4WO2_style.theme_use("default")
                                ques4WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques4_Opt2.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-1 of (Question #4)
                            def ques4_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques4_Opt_style = Style(root)
                                ques4_Opt_style.theme_use("default")
                                ques4_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques4_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques4_Opt2.configure(state=DISABLED)
                                ques4_Opt3.configure(state=DISABLED)
                                ques4_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #4)
                                root.after(3000, lambda: points())

                            # -------------------------------------------------------------------------------------------- (Question #4) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-2's (Question #4) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #4)
                            label7 = Label(root, text="4. http://www.google.com - is an example of what?", font=("Dodge", 14),
                                           foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label7.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #4) Options
                            ques4_Opt_style = Style(root)
                            ques4_Opt_style.theme_use("default")
                            ques4_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques4_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #4)
                            # Creating Option-1 and assigning a styler function to it
                            v4 = IntVar(root)
                            ques4_Opt1 = Radiobutton(root, text="A URL", variable=v4,
                                                     value=1, command=lambda: ques4_Opt_1())
                            ques4_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques4_Opt2 = Radiobutton(root, text="A URN", variable=v4,
                                                     value=2, command=lambda: ques4_Opt_2())
                            ques4_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques4_Opt3 = Radiobutton(root, text="A Website", variable=v4,
                                                     value=3, command=lambda: ques4_Opt_3())
                            ques4_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques4_Opt4 = Radiobutton(root, text="A URI", variable=v4,
                                                     value=4, command=lambda: ques4_Opt_4())
                            ques4_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #4)
                            timer4 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer4.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer4.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer4.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer4.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer4.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer4.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer4.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer4.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer4.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer4.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer4.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer4.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer4.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer4.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer4.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer4.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #4) after timer stops
                            root.after(15200, lambda: ques4_Correct())

                            # Destroying all the widgets showing (Question #4)
                            root.after(16100, timer4.destroy)
                            root.after(17400, ques4_Opt1.destroy)
                            root.after(17400, ques4_Opt2.destroy)
                            root.after(17500, ques4_Opt3.destroy)
                            root.after(17400, ques4_Opt4.destroy)
                            root.after(17500, label7.destroy)

                            # Calling the function to create Topic-2's (Question #5)
                            root.after(18000, lambda: ques5())

                        # -------------------------------------------------------------------------------------------- Topic-2's (Question #4) -StyleEnds----

                        # >>

                        # Function which creates Topic-2's (Question #3)
                        def ques3():

                            # ------------------------------------- (Question #3)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques3_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques1_C_Opt_style = Style(root)
                                ques1_C_Opt_style.theme_use("default")
                                ques1_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques3_Opt3.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques3_Opt1.configure(state=DISABLED)
                                ques3_Opt2.configure(state=DISABLED)
                                ques3_Opt4.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #3)
                            def ques3_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques3_Opt_style = Style(root)
                                ques3_Opt_style.theme_use("default")
                                ques3_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques3_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques3_Opt1.configure(state=DISABLED)
                                ques3_Opt2.configure(state=DISABLED)
                                ques3_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques1WO4_style = Style(root)
                                ques1WO4_style.theme_use("default")
                                ques1WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques3_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #3)
                            def ques3_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques3_Opt_style = Style(root)
                                ques3_Opt_style.theme_use("default")
                                ques3_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques3_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques3_Opt1.configure(state=DISABLED)
                                ques3_Opt2.configure(state=DISABLED)
                                ques3_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #3)
                                root.after(3000, lambda: points())

                            # Function which is triggered by Option-2 of (Question #3)

                            def ques3_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques3_Opt_style = Style(root)
                                ques3_Opt_style.theme_use("default")
                                ques3_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques3_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques3_Opt1.configure(state=DISABLED)
                                ques3_Opt3.configure(state=DISABLED)
                                ques3_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques3WO2_style = Style(root)
                                ques3WO2_style.theme_use("default")
                                ques3WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques3_Opt2.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-1 of (Question #3)
                            def ques3_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques3_Opt_style = Style(root)
                                ques3_Opt_style.theme_use("default")
                                ques3_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques3_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques3_Opt2.configure(state=DISABLED)
                                ques3_Opt3.configure(state=DISABLED)
                                ques3_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques1WO1_style = Style(root)
                                ques1WO1_style.theme_use("default")
                                ques1WO1_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques3_Opt1.configure(
                                    style="X.TRadiobutton"))

                            # -------------------------------------------------------------------------------------------- (Question #3) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-2's (Question #3) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #3)
                            label6 = Label(root, text="3. 'OS' computer abbreviation usually means ?", font=("Dodge", 14),
                                           foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label6.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #3) Options
                            ques3_Opt_style = Style(root)
                            ques3_Opt_style.theme_use("default")
                            ques3_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques3_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #3)
                            # Creating Option-1 and assigning a styler function to it
                            v3 = IntVar(root)
                            ques3_Opt1 = Radiobutton(root, text="Operating Server", variable=v3,
                                                     value=1, command=lambda: ques3_Opt_1())
                            ques3_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques3_Opt2 = Radiobutton(root, text="Open Software", variable=v3,
                                                     value=2, command=lambda: ques3_Opt_2())
                            ques3_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques3_Opt3 = Radiobutton(root, text="Operating System", variable=v3,
                                                     value=3, command=lambda: ques3_Opt_3())
                            ques3_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques3_Opt4 = Radiobutton(root, text="Optical Sensor", variable=v3,
                                                     value=4, command=lambda: ques3_Opt_4())
                            ques3_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #3)
                            timer3 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer3.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer3.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer3.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer3.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer3.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer3.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer3.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer3.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer3.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer3.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer3.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer3.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer3.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer3.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer3.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer3.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #3) after timer stops
                            root.after(15200, lambda: ques3_Correct())

                            # Destroying all the widgets showing (Question #3)
                            root.after(16100, timer3.destroy)
                            root.after(17400, ques3_Opt1.destroy)
                            root.after(17400, ques3_Opt2.destroy)
                            root.after(17500, ques3_Opt3.destroy)
                            root.after(17400, ques3_Opt4.destroy)
                            root.after(17500, label6.destroy)

                            # Calling the function to create Topic-2's (Question #4)
                            root.after(18000, lambda: ques4())

                            # -------------------------------------------------------------------------------------------- Topic-2's (Question #3) -StyleEnds----

                        # >>

                        # Function which creates Topic-2's (Question #2)
                        def ques2():

                            # ------------------------------------- (Question #2)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques2_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques2_C_Opt_style = Style(root)
                                ques2_C_Opt_style.theme_use("default")
                                ques2_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques2_Opt2.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques2_Opt1.configure(state=DISABLED)
                                ques2_Opt3.configure(state=DISABLED)
                                ques2_Opt4.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #2)
                            def ques2_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques2_Opt_style = Style(root)
                                ques2_Opt_style.theme_use("default")
                                ques2_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques2_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques2_Opt1.configure(state=DISABLED)
                                ques2_Opt2.configure(state=DISABLED)
                                ques2_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques2WO4_style = Style(root)
                                ques2WO4_style.theme_use("default")
                                ques2WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques2_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #2)
                            def ques2_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques2_Opt_style = Style(root)
                                ques2_Opt_style.theme_use("default")
                                ques2_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques2_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques2_Opt1.configure(state=DISABLED)
                                ques2_Opt2.configure(state=DISABLED)
                                ques2_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques2WO3_style = Style(root)
                                ques2WO3_style.theme_use("default")
                                ques2WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques2_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #2)
                            def ques2_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques2_Opt_style = Style(root)
                                ques2_Opt_style.theme_use("default")
                                ques2_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques2_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques2_Opt1.configure(state=DISABLED)
                                ques2_Opt3.configure(state=DISABLED)
                                ques2_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #2)
                                root.after(3000, lambda: points())

                            # Function which is triggered by Option-1 of (Question #2)
                            def ques2_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques2_Opt_style = Style(root)
                                ques2_Opt_style.theme_use("default")
                                ques2_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques2_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques2_Opt2.configure(state=DISABLED)
                                ques2_Opt3.configure(state=DISABLED)
                                ques2_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques2WO1_style = Style(root)
                                ques2WO1_style.theme_use("default")
                                ques2WO1_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques2_Opt1.configure(
                                    style="X.TRadiobutton"))

                            # -------------------------------------------------------------------------------------------- (Question #2) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-2's (Question #2) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #2)
                            label5 = Label(root, text="2. What is part of a database that holds only one type of information?", font=("Dodge", 14),
                                           foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label5.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #2) Options
                            ques2_Opt_style = Style(root)
                            ques2_Opt_style.theme_use("default")
                            ques2_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques2_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #2)
                            # Creating Option-1 and assigning a styler function to it
                            v2 = IntVar(root)
                            ques2_Opt1 = Radiobutton(root, text="Report", variable=v2,
                                                     value=1, command=lambda: ques2_Opt_1())
                            ques2_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques2_Opt2 = Radiobutton(root, text="Field", variable=v2,
                                                     value=2, command=lambda: ques2_Opt_2())
                            ques2_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques2_Opt3 = Radiobutton(root, text="Record", variable=v2,
                                                     value=3, command=lambda: ques2_Opt_3())
                            ques2_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques2_Opt4 = Radiobutton(root, text="File", variable=v2,
                                                     value=4, command=lambda: ques2_Opt_4())
                            ques2_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #2)
                            timer2 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer2.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer2.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer2.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer2.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer2.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer2.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer2.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer2.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer2.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer2.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer2.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer2.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer2.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer2.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer2.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer2.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #2) after timer stops
                            root.after(15200, lambda: ques2_Correct())

                            # Destroying all the widgets showing (Question #2)
                            root.after(16100, timer2.destroy)
                            root.after(17400, ques2_Opt1.destroy)
                            root.after(17500, ques2_Opt2.destroy)
                            root.after(17400, ques2_Opt3.destroy)
                            root.after(17400, ques2_Opt4.destroy)
                            root.after(17500, label5.destroy)

                            # Calling the function to create Topic-2's (Question #3)
                            root.after(18000, lambda: ques3())

                            # -------------------------------------------------------------------------------------------- Topic-2's (Question #2) -StyleEnds----

                        # >>

                        # Function which creates Topic-2's (Question #1)
                        def ques1():

                            # ------------------------------------- (Question #1)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques1_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques1_C_Opt_style = Style(root)
                                ques1_C_Opt_style.theme_use("default")
                                ques1_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques1_Opt3.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques1_Opt1.configure(state=DISABLED)
                                ques1_Opt2.configure(state=DISABLED)
                                ques1_Opt4.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #1)
                            def ques1_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques1_Opt_style = Style(root)
                                ques1_Opt_style.theme_use("default")
                                ques1_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques1_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques1_Opt1.configure(state=DISABLED)
                                ques1_Opt2.configure(state=DISABLED)
                                ques1_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques1WO4_style = Style(root)
                                ques1WO4_style.theme_use("default")
                                ques1WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques1_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #1)
                            def ques1_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques1_Opt_style = Style(root)
                                ques1_Opt_style.theme_use("default")
                                ques1_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques1_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques1_Opt1.configure(state=DISABLED)
                                ques1_Opt2.configure(state=DISABLED)
                                ques1_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #1)
                                root.after(3000, lambda: points())

                            # Function which is triggered by Option-2 of (Question #1)
                            def ques1_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques1_Opt_style = Style(root)
                                ques1_Opt_style.theme_use("default")
                                ques1_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques1_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques1_Opt1.configure(state=DISABLED)
                                ques1_Opt3.configure(state=DISABLED)
                                ques1_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques1WO2_style = Style(root)
                                ques1WO2_style.theme_use("default")
                                ques1WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques1_Opt2.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-1 of (Question #1)
                            def ques1_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques1_Opt_style = Style(root)
                                ques1_Opt_style.theme_use("default")
                                ques1_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques1_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques1_Opt2.configure(state=DISABLED)
                                ques1_Opt3.configure(state=DISABLED)
                                ques1_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques1WO1_style = Style(root)
                                ques1WO1_style.theme_use("default")
                                ques1WO1_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques1_Opt1.configure(
                                    style="X.TRadiobutton"))

                            # -------------------------------------------------------------------------------------------- (Question #1) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-2's (Question #1) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #1)
                            label4 = Label(root, text="1. What's a web browser?", font=("Dodge", 14),
                                           foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label4.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #1) Options
                            ques1_Opt_style = Style(root)
                            ques1_Opt_style.theme_use("default")
                            ques1_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques1_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #1)
                            # Creating Option-1 and assigning a styler function to it
                            v1 = IntVar(root)
                            ques1_Opt1 = Radiobutton(root, text="Kind of spider", variable=v1,
                                                     value=1, command=lambda: ques1_Opt_1())
                            ques1_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques1_Opt2 = Radiobutton(root, text="Search Engine", variable=v1,
                                                     value=2, command=lambda: ques1_Opt_2())
                            ques1_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques1_Opt3 = Radiobutton(root, text="Software to access Web", variable=v1,
                                                     value=3, command=lambda: ques1_Opt_3())
                            ques1_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques1_Opt4 = Radiobutton(root, text="World Wide Web", variable=v1,
                                                     value=4, command=lambda: ques1_Opt_4())
                            ques1_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #1)
                            timer1 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer1.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer1.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer1.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer1.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer1.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer1.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer1.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer1.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer1.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer1.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer1.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer1.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer1.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer1.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer1.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer1.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #1) after timer stops
                            root.after(15200, lambda: ques1_Correct())

                            # Destroying all the widgets showing (Question #1)
                            root.after(16100, timer1.destroy)
                            root.after(17400, ques1_Opt1.destroy)
                            root.after(17400, ques1_Opt2.destroy)
                            root.after(17500, ques1_Opt3.destroy)
                            root.after(17400, ques1_Opt4.destroy)
                            root.after(17500, label4.destroy)

                            # Calling the function to create Topic-2's (Question #2)
                            root.after(18000, lambda: ques2())

                            # -------------------------------------------------------------------------------------------- Topic-2's (Question #1) -StyleEnds----

                        # >>

                        # Disabling the Quiz Start-Button after clicked, for preventing the function to be called twice
                        start_button2.configure(state=DISABLED)

                        # Destroying all the widgets created in the Rules Panel for Topic-2
                        root.after(500, rules.destroy)
                        root.after(600, start_button2.destroy)
                        root.after(500, label2.destroy)
                        root.after(500, back3_button.destroy)

                        # Calling the function to create Topic-2's (Question #1)
                        root.after(800, lambda: ques1())

                    # >>

                    # ------------------------------------- Rules Panel for Topic-2 -StyleStarts----------------------------------------------------

                    # Disabling the Topic-Button2 after clicked, for preventing the function to be called twice
                    topic_button2.configure(state=DISABLED)

                    # Destroying all the widgets created in the Topic-Select Panel
                    root.after(800, topic_button2.destroy)
                    root.after(400, topic_button1.destroy)
                    root.after(400, topic_button3.destroy)
                    root.after(400, back2_button.destroy)

                    # Changing the text in the Topic-Select Panel label instead of destroying it
                    root.after(800, label2.configure(text="Rules"))

                    # Displaying the rules related to Topic-2's Quiz
                    rules = Message(root, text="    1. Each question has a time limit of 15 seconds.\r\n    2. Once the option is selected it can't be changed.\r\n    3. Final Score is displayed at the end.\r\n    4. The following questions are based on technology.", font=("Dodge", 12),
                                    foreground="#D1E3DD", background="#1E0905", width=400)
                    rules.place(relx=0.5, rely=0.42, anchor=CENTER)

                    # Creating and Styling the Quiz Start-Button
                    start_button2_style = Style()
                    start_button2_style.configure("B.TButton", font=("Playball", 17, "bold", "italic"),
                                                  foreground="#0A0908", background="#F6F67C", borderwidth=2, width=8, height=2)
                    start_button2 = Button(root, text="Start",
                                           style="B.TButton", command=lambda: quiz1())
                    start_button2.place(relx=0.5, rely=0.75, anchor=CENTER)

                    # Creating a Back-Button to return to User-Select Panel
                    # Styling Back-Button
                    back3_button_style = Style()
                    back3_button_style.theme_use("default")
                    back3_button_style.configure("E.TButton", font=("Playball", 10, "italic", "bold"),
                                                 foreground="#0A0908", background="#F6F67C", borderwidth=2, width=10, height=2, focuscolor="none")

                    back3_button = Button(root, text="< back",
                                          style="E.TButton", command=lambda: back3())
                    back3_button.place(relx=0.15, rely=0.9, anchor=CENTER)

                    # -------------------------------------------------------------------------------------------- Rules Panel for Topic-2 -StyleEnds----

                # >>

                # Function which creates the Rules Panel for Topic-1
                def topic_1():

                    # Function which is operated by the Topic-1's Rules Panel Back-Button
                    def back3():

                        # Disabling the Back-Button after clicked, for preventing the function to be called twice
                        back3_button.configure(state=DISABLED)

                        # Destroying all the widgets created in the Topic-Select Panel
                        root.after(600, lambda: back3_button.destroy())
                        root.after(500, lambda: rules.destroy())
                        root.after(500, lambda: start_button2.destroy())
                        root.after(500, lambda: label2.destroy())
                        root.after(500, lambda: label3.destroy())
                        root.after(500, lambda: label31.destroy())

                        # Calling the function to redirect to the User-Select panel
                        root.after(800, lambda: userSelect())

                    # >>

                    # Function for displaying the GuestName centered above the score
                    def scoreCard():

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

                        # Creating a 'leaderboard' table if not exists to store the Guestname and score
                        co.execute("""CREATE TABLE IF NOT EXISTS leaderboard (
                                    playername text,
                                    score integer
                                    )""")

                        # Updating the leaderboard with the Guest's name and total score
                        co.execute("INSERT INTO leaderboard VALUES (:text3, :point)",
                                   {
                                       "text3": text3,
                                       "point": point
                                   })

                        # Committing the changes to the database
                        quizdata.commit()

                        # Closing the connection with the database
                        quizdata.close()

                    # >>

                    # Function which is triggered by the Topic-1's Rules Panel Quiz Start-Button
                    def quiz1():

                        # Function which creates Topic-1's (Question #10)
                        def ques10():

                            # ------------------------------------- (Question #10)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques10_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques10_C_Opt_style = Style(root)
                                ques10_C_Opt_style.theme_use("default")
                                ques10_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                             foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques10_Opt1.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques10_Opt2.configure(state=DISABLED)
                                ques10_Opt3.configure(state=DISABLED)
                                ques10_Opt4.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #10)
                            def ques10_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques10_Opt_style = Style(root)
                                ques10_Opt_style.theme_use("default")
                                ques10_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                           foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques10_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques10_Opt1.configure(state=DISABLED)
                                ques10_Opt2.configure(state=DISABLED)
                                ques10_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques10WO4_style = Style(root)
                                ques10WO4_style.theme_use("default")
                                ques10WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques10_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #10)
                            def ques10_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques10_Opt_style = Style(root)
                                ques10_Opt_style.theme_use("default")
                                ques10_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                           foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques10_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques10_Opt1.configure(state=DISABLED)
                                ques10_Opt2.configure(state=DISABLED)
                                ques10_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques10WO3_style = Style(root)
                                ques10WO3_style.theme_use("default")
                                ques10WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques10_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #10)
                            def ques10_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques10_Opt_style = Style(root)
                                ques10_Opt_style.theme_use("default")
                                ques10_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                           foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-2 to yellow color
                                ques10_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques10_Opt1.configure(state=DISABLED)
                                ques10_Opt3.configure(state=DISABLED)
                                ques10_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques10WO2_style = Style(root)
                                ques10WO2_style.theme_use("default")
                                ques10WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques10_Opt2.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-1 of (Question #10)
                            def ques10_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques10_Opt_style = Style(root)
                                ques10_Opt_style.theme_use("default")
                                ques10_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                           foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques10_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques10_Opt2.configure(state=DISABLED)
                                ques10_Opt3.configure(state=DISABLED)
                                ques10_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #10)
                                root.after(3000, lambda: points())

                            # -------------------------------------------------------------------------------------------- (Question #10) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-1's (Question #10) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #10)
                            label13 = Label(root, text="10. Galileo was an Italian astronomer who developed", font=("Dodge", 14),
                                            foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label13.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #10) Options
                            ques10_Opt_style = Style(root)
                            ques10_Opt_style.theme_use("default")
                            ques10_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                       foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques10_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #10)
                            # Creating Option-1 and assigning a styler function to it
                            v10 = IntVar(root)
                            ques10_Opt1 = Radiobutton(root, text="Telescope", variable=v10,
                                                      value=1, command=lambda: ques10_Opt_1())
                            ques10_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques10_Opt2 = Radiobutton(root, text="Radiology", variable=v10,
                                                      value=2, command=lambda: ques10_Opt_2())
                            ques10_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques10_Opt3 = Radiobutton(root, text="4 Jupiter satellites", variable=v10,
                                                      value=3, command=lambda: ques10_Opt_3())
                            ques10_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques10_Opt4 = Radiobutton(root, text="All the above", variable=v10,
                                                      value=4, command=lambda: ques10_Opt_4())
                            ques10_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #10)
                            timer10 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                              foreground="#F0EFF4", background="#22333B", width=600)
                            timer10.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer10.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer10.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer10.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer10.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer10.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer10.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer10.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer10.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer10.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer10.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer10.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer10.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer10.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer10.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer10.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #10) after timer stops
                            root.after(15200, lambda: ques10_Correct())

                            # Destroying all the widgets showing (Question #10)
                            root.after(16100, timer10.destroy)
                            root.after(17400, ques10_Opt1.destroy)
                            root.after(17400, ques10_Opt2.destroy)
                            root.after(17500, ques10_Opt3.destroy)
                            root.after(17400, ques10_Opt4.destroy)
                            root.after(17500, label13.destroy)

                            # Calling the function to update the Total score to database and mean time displaying it to the Guest
                            root.after(18000, lambda: scoreCard())

                            # Calling the function to display the Total Score
                            root.after(18500, lambda: finalScore())

                            # Calling the function to create exit and leaderboard button
                            root.after(19500, lambda: creatingExit())

                        # -------------------------------------------------------------------------------------------- Topic-1's (Question #10) -StyleEnds----

                        # >>

                        # Function which creates Topic-1's (Question #9)
                        def ques9():

                            # ------------------------------------- (Question #9)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques9_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques9_C_Opt_style = Style(root)
                                ques9_C_Opt_style.theme_use("default")
                                ques9_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques9_Opt1.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques9_Opt2.configure(state=DISABLED)
                                ques9_Opt3.configure(state=DISABLED)
                                ques9_Opt4.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #9)
                            def ques9_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques9_Opt_style = Style(root)
                                ques9_Opt_style.theme_use("default")
                                ques9_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques9_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques9_Opt1.configure(state=DISABLED)
                                ques9_Opt2.configure(state=DISABLED)
                                ques9_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques9WO4_style = Style(root)
                                ques9WO4_style.theme_use("default")
                                ques9WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques9_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #9)
                            def ques9_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques9_Opt_style = Style(root)
                                ques9_Opt_style.theme_use("default")
                                ques9_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques9_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques9_Opt1.configure(state=DISABLED)
                                ques9_Opt2.configure(state=DISABLED)
                                ques9_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques9WO3_style = Style(root)
                                ques9WO3_style.theme_use("default")
                                ques9WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques9_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #9)
                            def ques9_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques9_Opt_style = Style(root)
                                ques9_Opt_style.theme_use("default")
                                ques9_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-2 to yellow color
                                ques9_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques9_Opt1.configure(state=DISABLED)
                                ques9_Opt3.configure(state=DISABLED)
                                ques9_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques9WO2_style = Style(root)
                                ques9WO2_style.theme_use("default")
                                ques9WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques9_Opt2.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-1 of (Question #9)
                            def ques9_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques9_Opt_style = Style(root)
                                ques9_Opt_style.theme_use("default")
                                ques9_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques9_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques9_Opt2.configure(state=DISABLED)
                                ques9_Opt3.configure(state=DISABLED)
                                ques9_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #9)
                                root.after(3000, lambda: points())

                            # -------------------------------------------------------------------------------------------- (Question #9) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-1's (Question #9) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #9)
                            label12 = Label(root, text="9. First human heart transplant operation conducted by Dr. Christiaan Barnard on Louis Washkansky, was conducted in", font=("Dodge", 14),
                                            foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label12.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #9) Options
                            ques9_Opt_style = Style(root)
                            ques9_Opt_style.theme_use("default")
                            ques9_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques9_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #9)
                            # Creating Option-1 and assigning a styler function to it
                            v9 = IntVar(root)
                            ques9_Opt1 = Radiobutton(root, text="1967", variable=v9,
                                                     value=1, command=lambda: ques9_Opt_1())
                            ques9_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques9_Opt2 = Radiobutton(root, text="1968", variable=v9,
                                                     value=2, command=lambda: ques9_Opt_2())
                            ques9_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques9_Opt3 = Radiobutton(root, text="1958", variable=v9,
                                                     value=3, command=lambda: ques9_Opt_3())
                            ques9_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques9_Opt4 = Radiobutton(root, text="1922", variable=v9,
                                                     value=4, command=lambda: ques9_Opt_4())
                            ques9_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #9)
                            timer9 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer9.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer9.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer9.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer9.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer9.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer9.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer9.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer9.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer9.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer9.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer9.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer9.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer9.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer9.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer9.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer9.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #9) after timer stops
                            root.after(15200, lambda: ques9_Correct())

                            # Destroying all the widgets showing (Question #9)
                            root.after(16100, timer9.destroy)
                            root.after(17400, ques9_Opt1.destroy)
                            root.after(17400, ques9_Opt2.destroy)
                            root.after(17500, ques9_Opt3.destroy)
                            root.after(17400, ques9_Opt4.destroy)
                            root.after(17500, label12.destroy)

                            # Calling the function to create Topic-1's (Question #10)
                            root.after(18000, lambda: ques10())

                        # -------------------------------------------------------------------------------------------- Topic-1's (Question #9) -StyleEnds----

                        # >>

                        # Function which creates Topic-1's (Question #8)
                        def ques8():

                            # ------------------------------------- (Question #8)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques8_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques8_C_Opt_style = Style(root)
                                ques8_C_Opt_style.theme_use("default")
                                ques8_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques8_Opt1.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques8_Opt2.configure(state=DISABLED)
                                ques8_Opt3.configure(state=DISABLED)
                                ques8_Opt4.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #8)
                            def ques8_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques8_Opt_style = Style(root)
                                ques8_Opt_style.theme_use("default")
                                ques8_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques8_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques8_Opt1.configure(state=DISABLED)
                                ques8_Opt2.configure(state=DISABLED)
                                ques8_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques8WO4_style = Style(root)
                                ques8WO4_style.theme_use("default")
                                ques8WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques8_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #8)
                            def ques8_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques8_Opt_style = Style(root)
                                ques8_Opt_style.theme_use("default")
                                ques8_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques8_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques8_Opt1.configure(state=DISABLED)
                                ques8_Opt2.configure(state=DISABLED)
                                ques8_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques8WO3_style = Style(root)
                                ques8WO3_style.theme_use("default")
                                ques8WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques8_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #8)
                            def ques8_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques8_Opt_style = Style(root)
                                ques8_Opt_style.theme_use("default")
                                ques8_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-2 to yellow color
                                ques8_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques8_Opt1.configure(state=DISABLED)
                                ques8_Opt3.configure(state=DISABLED)
                                ques8_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques8WO2_style = Style(root)
                                ques8WO2_style.theme_use("default")
                                ques8WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques8_Opt2.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-1 of (Question #8)
                            def ques8_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques8_Opt_style = Style(root)
                                ques8_Opt_style.theme_use("default")
                                ques8_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques8_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques8_Opt2.configure(state=DISABLED)
                                ques8_Opt3.configure(state=DISABLED)
                                ques8_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #8)
                                root.after(3000, lambda: points())

                            # -------------------------------------------------------------------------------------------- (Question #8) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-1's (Question #8) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #8)
                            label11 = Label(root, text="8. Epsom (England) is the place associated with", font=("Dodge", 14),
                                            foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label11.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #8) Options
                            ques8_Opt_style = Style(root)
                            ques8_Opt_style.theme_use("default")
                            ques8_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques8_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #8)
                            # Creating Option-1 and assigning a styler function to it
                            v8 = IntVar(root)
                            ques8_Opt1 = Radiobutton(root, text="Horse racing", variable=v8,
                                                     value=1, command=lambda: ques8_Opt_1())
                            ques8_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques8_Opt2 = Radiobutton(root, text="Polo", variable=v8,
                                                     value=2, command=lambda: ques8_Opt_2())
                            ques8_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques8_Opt3 = Radiobutton(root, text="Shooting", variable=v8,
                                                     value=3, command=lambda: ques8_Opt_3())
                            ques8_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques8_Opt4 = Radiobutton(root, text="Snooker", variable=v8,
                                                     value=4, command=lambda: ques8_Opt_4())
                            ques8_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #8)
                            timer8 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer8.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer8.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer8.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer8.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer8.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer8.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer8.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer8.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer8.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer8.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer8.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer8.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer8.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer8.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer8.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer8.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #8) after timer stops
                            root.after(15200, lambda: ques8_Correct())

                            # Destroying all the widgets showing (Question #8)
                            root.after(16100, timer8.destroy)
                            root.after(17400, ques8_Opt1.destroy)
                            root.after(17400, ques8_Opt2.destroy)
                            root.after(17500, ques8_Opt3.destroy)
                            root.after(17400, ques8_Opt4.destroy)
                            root.after(17500, label11.destroy)

                            # Calling the function to create Topic-1's (Question #9)
                            root.after(18000, lambda: ques9())

                        # -------------------------------------------------------------------------------------------- Topic-1's (Question #8) -StyleEnds----

                        # >>

                        # Function which creates Topic-1's (Question #7)
                        def ques7():

                            # ------------------------------------- (Question #7)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques7_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques7_C_Opt_style = Style(root)
                                ques7_C_Opt_style.theme_use("default")
                                ques7_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques7_Opt1.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques7_Opt2.configure(state=DISABLED)
                                ques7_Opt3.configure(state=DISABLED)
                                ques7_Opt4.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #7)
                            def ques7_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques7_Opt_style = Style(root)
                                ques7_Opt_style.theme_use("default")
                                ques7_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques7_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques7_Opt1.configure(state=DISABLED)
                                ques7_Opt2.configure(state=DISABLED)
                                ques7_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques7WO4_style = Style(root)
                                ques7WO4_style.theme_use("default")
                                ques7WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques7_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #7)
                            def ques7_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques7_Opt_style = Style(root)
                                ques7_Opt_style.theme_use("default")
                                ques7_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques7_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques7_Opt1.configure(state=DISABLED)
                                ques7_Opt2.configure(state=DISABLED)
                                ques7_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques7WO3_style = Style(root)
                                ques7WO3_style.theme_use("default")
                                ques7WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques7_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #7)
                            def ques7_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques7_Opt_style = Style(root)
                                ques7_Opt_style.theme_use("default")
                                ques7_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-2 to yellow color
                                ques7_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques7_Opt1.configure(state=DISABLED)
                                ques7_Opt3.configure(state=DISABLED)
                                ques7_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques7WO2_style = Style(root)
                                ques7WO2_style.theme_use("default")
                                ques7WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques7_Opt2.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-1 of (Question #7)
                            def ques7_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques7_Opt_style = Style(root)
                                ques7_Opt_style.theme_use("default")
                                ques7_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques7_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques7_Opt2.configure(state=DISABLED)
                                ques7_Opt3.configure(state=DISABLED)
                                ques7_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #7)
                                root.after(3000, lambda: points())

                            # -------------------------------------------------------------------------------------------- (Question #7) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-1's (Question #7) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #7)
                            label10 = Label(root, text="7. Fastest shorthand writer was", font=("Dodge", 14),
                                            foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label10.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #7) Options
                            ques7_Opt_style = Style(root)
                            ques7_Opt_style.theme_use("default")
                            ques7_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques7_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #7)
                            # Creating Option-1 and assigning a styler function to it
                            v7 = IntVar(root)
                            ques7_Opt1 = Radiobutton(root, text="Dr. G. D. Bist", variable=v7,
                                                     value=1, command=lambda: ques7_Opt_1())
                            ques7_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques7_Opt2 = Radiobutton(root, text="J.R.D. Tata", variable=v7,
                                                     value=2, command=lambda: ques7_Opt_2())
                            ques7_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques7_Opt3 = Radiobutton(root, text="J.M. Tagore", variable=v7,
                                                     value=3, command=lambda: ques7_Opt_3())
                            ques7_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques7_Opt4 = Radiobutton(root, text="Khudada Khan", variable=v7,
                                                     value=4, command=lambda: ques7_Opt_4())
                            ques7_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #7)
                            timer7 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer7.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer7.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer7.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer7.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer7.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer7.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer7.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer7.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer7.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer7.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer7.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer7.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer7.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer7.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer7.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer7.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #7) after timer stops
                            root.after(15200, lambda: ques7_Correct())

                            # Destroying all the widgets showing (Question #7)
                            root.after(16100, timer7.destroy)
                            root.after(17400, ques7_Opt1.destroy)
                            root.after(17400, ques7_Opt2.destroy)
                            root.after(17500, ques7_Opt3.destroy)
                            root.after(17400, ques7_Opt4.destroy)
                            root.after(17500, label10.destroy)

                            # Calling the function to create Topic-1's (Question #8)
                            root.after(18000, lambda: ques8())

                        # -------------------------------------------------------------------------------------------- Topic-1's (Question #7) -StyleEnds----

                        # >>

                        # Function which creates Topic-1's (Question #6)
                        def ques6():

                            # ------------------------------------- (Question #6)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques6_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques6_C_Opt_style = Style(root)
                                ques6_C_Opt_style.theme_use("default")
                                ques6_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques6_Opt2.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques6_Opt1.configure(state=DISABLED)
                                ques6_Opt4.configure(state=DISABLED)
                                ques6_Opt3.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #6)
                            def ques6_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques6_Opt_style = Style(root)
                                ques6_Opt_style.theme_use("default")
                                ques6_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques6_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques6_Opt1.configure(state=DISABLED)
                                ques6_Opt2.configure(state=DISABLED)
                                ques6_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques6WO2_style = Style(root)
                                ques6WO2_style.theme_use("default")
                                ques6WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques6_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #6)
                            def ques6_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques6_Opt_style = Style(root)
                                ques6_Opt_style.theme_use("default")
                                ques6_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques6_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques6_Opt1.configure(state=DISABLED)
                                ques6_Opt2.configure(state=DISABLED)
                                ques6_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques6WO3_style = Style(root)
                                ques6WO3_style.theme_use("default")
                                ques6WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques6_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #6)
                            def ques6_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques6_Opt_style = Style(root)
                                ques6_Opt_style.theme_use("default")
                                ques6_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques6_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques6_Opt1.configure(state=DISABLED)
                                ques6_Opt3.configure(state=DISABLED)
                                ques6_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #6)
                                root.after(3000, lambda: points())

                            # Function which is triggered by Option-1 of (Question #6)
                            def ques6_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques6_Opt_style = Style(root)
                                ques6_Opt_style.theme_use("default")
                                ques6_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques6_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques6_Opt2.configure(state=DISABLED)
                                ques6_Opt3.configure(state=DISABLED)
                                ques6_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques6WO1_style = Style(root)
                                ques6WO1_style.theme_use("default")
                                ques6WO1_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques6_Opt1.configure(
                                    style="X.TRadiobutton"))

                            # -------------------------------------------------------------------------------------------- (Question #6) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-1's (Question #6) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #6)
                            label9 = Label(root, text="6. FFC stands for", font=("Dodge", 14),
                                           foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label9.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #6) Options
                            ques6_Opt_style = Style(root)
                            ques6_Opt_style.theme_use("default")
                            ques6_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques6_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #6)
                            # Creating Option-1 and assigning a styler function to it
                            v6 = IntVar(root)
                            ques6_Opt1 = Radiobutton(root, text="Foreign Finance Corporation", variable=v6,
                                                     value=1, command=lambda: ques6_Opt_1())
                            ques6_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques6_Opt2 = Radiobutton(root, text="Film Finance Corporation", variable=v6,
                                                     value=2, command=lambda: ques6_Opt_2())
                            ques6_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques6_Opt3 = Radiobutton(root, text="Federation of Football Council", variable=v6,
                                                     value=3, command=lambda: ques6_Opt_3())
                            ques6_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques6_Opt4 = Radiobutton(root, text="None of the above", variable=v6,
                                                     value=4, command=lambda: ques6_Opt_4())
                            ques6_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #6)
                            timer6 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer6.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer6.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer6.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer6.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer6.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer6.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer6.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer6.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer6.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer6.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer6.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer6.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer6.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer6.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer6.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer6.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #6) after timer stops
                            root.after(15200, lambda: ques6_Correct())

                            # Destroying all the widgets showing (Question #6)
                            root.after(16100, timer6.destroy)
                            root.after(17400, ques6_Opt1.destroy)
                            root.after(17400, ques6_Opt2.destroy)
                            root.after(17500, ques6_Opt3.destroy)
                            root.after(17400, ques6_Opt4.destroy)
                            root.after(17500, label9.destroy)

                            # Calling the function to create Topic-1's (Question #7)
                            root.after(18000, lambda: ques7())

                        # -------------------------------------------------------------------------------------------- Topic-1's (Question #6) -StyleEnds----

                        # >>

                        # Function which creates Topic-1's (Question #5)
                        def ques5():

                            # ------------------------------------- (Question #5)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques5_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques5_C_Opt_style = Style(root)
                                ques5_C_Opt_style.theme_use("default")
                                ques5_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques5_Opt2.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques5_Opt1.configure(state=DISABLED)
                                ques5_Opt4.configure(state=DISABLED)
                                ques5_Opt3.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #5)
                            def ques5_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques5_Opt_style = Style(root)
                                ques5_Opt_style.theme_use("default")
                                ques5_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques5_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques5_Opt1.configure(state=DISABLED)
                                ques5_Opt2.configure(state=DISABLED)
                                ques5_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques5WO4_style = Style(root)
                                ques5WO4_style.theme_use("default")
                                ques5WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques5_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #5)
                            def ques5_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques5_Opt_style = Style(root)
                                ques5_Opt_style.theme_use("default")
                                ques5_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques5_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques5_Opt1.configure(state=DISABLED)
                                ques5_Opt2.configure(state=DISABLED)
                                ques5_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques5WO3_style = Style(root)
                                ques5WO3_style.theme_use("default")
                                ques5WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques5_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #5)
                            def ques5_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques5_Opt_style = Style(root)
                                ques5_Opt_style.theme_use("default")
                                ques5_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques5_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques5_Opt1.configure(state=DISABLED)
                                ques5_Opt3.configure(state=DISABLED)
                                ques5_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #5)
                                root.after(3000, lambda: points())

                            # Function which is triggered by Option-1 of (Question #5)
                            def ques5_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques5_Opt_style = Style(root)
                                ques5_Opt_style.theme_use("default")
                                ques5_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques5_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques5_Opt2.configure(state=DISABLED)
                                ques5_Opt3.configure(state=DISABLED)
                                ques5_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques5WO1_style = Style(root)
                                ques5WO1_style.theme_use("default")
                                ques5WO1_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques5_Opt1.configure(
                                    style="X.TRadiobutton"))

                            # -------------------------------------------------------------------------------------------- (Question #5) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-1's (Question #5) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #5)
                            label8 = Label(root, text="5. Hitler party which came into power in 1933 is known as", font=("Dodge", 14),
                                           foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label8.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #5) Options
                            ques5_Opt_style = Style(root)
                            ques5_Opt_style.theme_use("default")
                            ques5_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques5_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #5)
                            # Creating Option-1 and assigning a styler function to it
                            v5 = IntVar(root)
                            ques5_Opt1 = Radiobutton(root, text="Labour Party", variable=v5,
                                                     value=1, command=lambda: ques5_Opt_1())
                            ques5_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques5_Opt2 = Radiobutton(root, text="Nazi Party", variable=v5,
                                                     value=2, command=lambda: ques5_Opt_2())
                            ques5_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques5_Opt3 = Radiobutton(root, text="Ku-Klux-Klan", variable=v5,
                                                     value=3, command=lambda: ques5_Opt_3())
                            ques5_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques5_Opt4 = Radiobutton(root, text="Democratic Party", variable=v5,
                                                     value=4, command=lambda: ques5_Opt_4())
                            ques5_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #5)
                            timer5 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer5.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer5.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer5.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer5.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer5.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer5.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer5.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer5.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer5.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer5.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer5.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer5.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer5.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer5.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer5.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer5.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #5) after timer stops
                            root.after(15200, lambda: ques5_Correct())

                            # Destroying all the widgets showing (Question #5)
                            root.after(16100, timer5.destroy)
                            root.after(17400, ques5_Opt1.destroy)
                            root.after(17400, ques5_Opt2.destroy)
                            root.after(17500, ques5_Opt3.destroy)
                            root.after(17400, ques5_Opt4.destroy)
                            root.after(17500, label8.destroy)

                            # Calling the function to create Topic-1's (Question #6)
                            root.after(18000, lambda: ques6())

                        # -------------------------------------------------------------------------------------------- Topic-1's (Question #5) -StyleEnds----

                        # >>

                        # Function which creates Topic-1's (Question #4)
                        def ques4():

                            # ------------------------------------- (Question #4)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques4_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques4_C_Opt_style = Style(root)
                                ques4_C_Opt_style.theme_use("default")
                                ques4_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques4_Opt4.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques4_Opt1.configure(state=DISABLED)
                                ques4_Opt2.configure(state=DISABLED)
                                ques4_Opt3.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #4)
                            def ques4_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques4_Opt_style = Style(root)
                                ques4_Opt_style.theme_use("default")
                                ques4_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques4_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques4_Opt1.configure(state=DISABLED)
                                ques4_Opt2.configure(state=DISABLED)
                                ques4_Opt3.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #4)
                                root.after(3000, lambda: points())

                            # Function which is triggered by Option-3 of (Question #4)
                            def ques4_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques4_Opt_style = Style(root)
                                ques4_Opt_style.theme_use("default")
                                ques4_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques4_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques4_Opt1.configure(state=DISABLED)
                                ques4_Opt2.configure(state=DISABLED)
                                ques4_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques4WO3_style = Style(root)
                                ques4WO3_style.theme_use("default")
                                ques4WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques4_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #4)
                            def ques4_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques4_Opt_style = Style(root)
                                ques4_Opt_style.theme_use("default")
                                ques4_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques4_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques4_Opt1.configure(state=DISABLED)
                                ques4_Opt3.configure(state=DISABLED)
                                ques4_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques4WO2_style = Style(root)
                                ques4WO2_style.theme_use("default")
                                ques4WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques4_Opt2.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-1 of (Question #4)
                            def ques4_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques4_Opt_style = Style(root)
                                ques4_Opt_style.theme_use("default")
                                ques4_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques4_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques4_Opt2.configure(state=DISABLED)
                                ques4_Opt3.configure(state=DISABLED)
                                ques4_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques4WO1_style = Style(root)
                                ques4WO1_style.theme_use("default")
                                ques4WO1_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques4_Opt1.configure(
                                    style="X.TRadiobutton"))

                            # -------------------------------------------------------------------------------------------- (Question #4) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-1's (Question #4) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #4)
                            label7 = Label(root, text="4. For which of the following disciplines is Nobel Prize awarded?", font=("Dodge", 14),
                                           foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label7.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #4) Options
                            ques4_Opt_style = Style(root)
                            ques4_Opt_style.theme_use("default")
                            ques4_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques4_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #4)
                            # Creating Option-1 and assigning a styler function to it
                            v4 = IntVar(root)
                            ques4_Opt1 = Radiobutton(root, text="Physics and Chemistry", variable=v4,
                                                     value=1, command=lambda: ques4_Opt_1())
                            ques4_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques4_Opt2 = Radiobutton(root, text="Physiology or Medicine", variable=v4,
                                                     value=2, command=lambda: ques4_Opt_2())
                            ques4_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques4_Opt3 = Radiobutton(root, text="Literature, Peace and Economics", variable=v4,
                                                     value=3, command=lambda: ques4_Opt_3())
                            ques4_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques4_Opt4 = Radiobutton(root, text="All of the above", variable=v4,
                                                     value=4, command=lambda: ques4_Opt_4())
                            ques4_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #4)
                            timer4 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer4.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer4.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer4.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer4.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer4.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer4.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer4.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer4.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer4.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer4.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer4.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer4.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer4.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer4.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer4.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer4.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #4) after timer stops
                            root.after(15200, lambda: ques4_Correct())

                            # Destroying all the widgets showing (Question #4)
                            root.after(16100, timer4.destroy)
                            root.after(17400, ques4_Opt1.destroy)
                            root.after(17400, ques4_Opt2.destroy)
                            root.after(17500, ques4_Opt3.destroy)
                            root.after(17400, ques4_Opt4.destroy)
                            root.after(17500, label7.destroy)

                            # Calling the function to create Topic-1's (Question #5)
                            root.after(18000, lambda: ques5())

                        # -------------------------------------------------------------------------------------------- Topic-1's (Question #4) -StyleEnds----

                        # >>

                        # Function which creates Topic-1's (Question #3)
                        def ques3():

                            # ------------------------------------- (Question #3)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques3_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques1_C_Opt_style = Style(root)
                                ques1_C_Opt_style.theme_use("default")
                                ques1_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques3_Opt2.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques3_Opt1.configure(state=DISABLED)
                                ques3_Opt3.configure(state=DISABLED)
                                ques3_Opt4.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #3)
                            def ques3_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques3_Opt_style = Style(root)
                                ques3_Opt_style.theme_use("default")
                                ques3_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques3_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques3_Opt1.configure(state=DISABLED)
                                ques3_Opt2.configure(state=DISABLED)
                                ques3_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques1WO4_style = Style(root)
                                ques1WO4_style.theme_use("default")
                                ques1WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques3_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #3)
                            def ques3_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques3_Opt_style = Style(root)
                                ques3_Opt_style.theme_use("default")
                                ques3_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques3_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques3_Opt1.configure(state=DISABLED)
                                ques3_Opt2.configure(state=DISABLED)
                                ques3_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques1WO3_style = Style(root)
                                ques1WO3_style.theme_use("default")
                                ques1WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques3_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #3)
                            def ques3_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques3_Opt_style = Style(root)
                                ques3_Opt_style.theme_use("default")
                                ques3_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques3_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques3_Opt1.configure(state=DISABLED)
                                ques3_Opt3.configure(state=DISABLED)
                                ques3_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #3)
                                root.after(3000, lambda: points())

                            # Function which is triggered by Option-1 of (Question #3)
                            def ques3_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques3_Opt_style = Style(root)
                                ques3_Opt_style.theme_use("default")
                                ques3_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques3_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques3_Opt2.configure(state=DISABLED)
                                ques3_Opt3.configure(state=DISABLED)
                                ques3_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques1WO1_style = Style(root)
                                ques1WO1_style.theme_use("default")
                                ques1WO1_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques3_Opt1.configure(
                                    style="X.TRadiobutton"))

                            # -------------------------------------------------------------------------------------------- (Question #3) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-1's (Question #3) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #3)
                            label6 = Label(root, text="3. Garampani sanctuary is located at", font=("Dodge", 14),
                                           foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label6.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #3) Options
                            ques3_Opt_style = Style(root)
                            ques3_Opt_style.theme_use("default")
                            ques3_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques3_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #3)
                            # Creating Option-1 and assigning a styler function to it
                            v3 = IntVar(root)
                            ques3_Opt1 = Radiobutton(root, text="Junagarh, Gujarat", variable=v3,
                                                     value=1, command=lambda: ques3_Opt_1())
                            ques3_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques3_Opt2 = Radiobutton(root, text="Diphu, Assam", variable=v3,
                                                     value=2, command=lambda: ques3_Opt_2())
                            ques3_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques3_Opt3 = Radiobutton(root, text="Kohima, Nagaland", variable=v3,
                                                     value=3, command=lambda: ques3_Opt_3())
                            ques3_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques3_Opt4 = Radiobutton(root, text="Gangtok, Sikkim", variable=v3,
                                                     value=4, command=lambda: ques3_Opt_4())
                            ques3_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #3)
                            timer3 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer3.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer3.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer3.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer3.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer3.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer3.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer3.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer3.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer3.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer3.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer3.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer3.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer3.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer3.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer3.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer3.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #3) after timer stops
                            root.after(15200, lambda: ques3_Correct())

                            # Destroying all the widgets showing (Question #3)
                            root.after(16100, timer3.destroy)
                            root.after(17400, ques3_Opt1.destroy)
                            root.after(17400, ques3_Opt2.destroy)
                            root.after(17500, ques3_Opt3.destroy)
                            root.after(17400, ques3_Opt4.destroy)
                            root.after(17500, label6.destroy)

                            # Calling the function to create Topic-1's (Question #4)
                            root.after(18000, lambda: ques4())

                            # -------------------------------------------------------------------------------------------- Topic-1's (Question #3) -StyleEnds----

                        # >>

                        # Function which creates Topic-1's (Question #2)
                        def ques2():

                            # ------------------------------------- (Question #2)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques2_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques2_C_Opt_style = Style(root)
                                ques2_C_Opt_style.theme_use("default")
                                ques2_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques2_Opt2.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques2_Opt1.configure(state=DISABLED)
                                ques2_Opt3.configure(state=DISABLED)
                                ques2_Opt4.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #2)
                            def ques2_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques2_Opt_style = Style(root)
                                ques2_Opt_style.theme_use("default")
                                ques2_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques2_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques2_Opt1.configure(state=DISABLED)
                                ques2_Opt2.configure(state=DISABLED)
                                ques2_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques2WO2_style = Style(root)
                                ques2WO2_style.theme_use("default")
                                ques2WO2_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques2_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #2)
                            def ques2_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques2_Opt_style = Style(root)
                                ques2_Opt_style.theme_use("default")
                                ques2_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques2_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques2_Opt1.configure(state=DISABLED)
                                ques2_Opt2.configure(state=DISABLED)
                                ques2_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques2WO3_style = Style(root)
                                ques2WO3_style.theme_use("default")
                                ques2WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques2_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #2)
                            def ques2_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques2_Opt_style = Style(root)
                                ques2_Opt_style.theme_use("default")
                                ques2_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques2_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques2_Opt1.configure(state=DISABLED)
                                ques2_Opt3.configure(state=DISABLED)
                                ques2_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #2)
                                root.after(3000, lambda: points())

                            # Function which is triggered by Option-1 of (Question #2)
                            def ques2_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques2_Opt_style = Style(root)
                                ques2_Opt_style.theme_use("default")
                                ques2_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques2_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques2_Opt2.configure(state=DISABLED)
                                ques2_Opt3.configure(state=DISABLED)
                                ques2_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques2WO1_style = Style(root)
                                ques2WO1_style.theme_use("default")
                                ques2WO1_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques2_Opt1.configure(
                                    style="X.TRadiobutton"))

                            # -------------------------------------------------------------------------------------------- (Question #2) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-1's (Question #2) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #2)
                            label5 = Label(root, text="2. Eritrea, which became the 182nd member of the UN in 1993, is in the continent of", font=("Dodge", 14),
                                           foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label5.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #2) Options
                            ques2_Opt_style = Style(root)
                            ques2_Opt_style.theme_use("default")
                            ques2_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques2_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #2)
                            # Creating Option-1 and assigning a styler function to it
                            v2 = IntVar(root)
                            ques2_Opt1 = Radiobutton(root, text="Asia", variable=v2,
                                                     value=1, command=lambda: ques2_Opt_1())
                            ques2_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques2_Opt2 = Radiobutton(root, text="Africa", variable=v2,
                                                     value=2, command=lambda: ques2_Opt_2())
                            ques2_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques2_Opt3 = Radiobutton(root, text="Europe", variable=v2,
                                                     value=3, command=lambda: ques2_Opt_3())
                            ques2_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques2_Opt4 = Radiobutton(root, text="Australia", variable=v2,
                                                     value=4, command=lambda: ques2_Opt_4())
                            ques2_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #2)
                            timer2 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer2.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer2.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer2.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer2.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer2.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer2.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer2.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer2.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer2.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer2.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer2.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer2.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer2.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer2.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer2.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer2.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #2) after timer stops
                            root.after(15200, lambda: ques2_Correct())

                            # Destroying all the widgets showing (Question #2)
                            root.after(16100, timer2.destroy)
                            root.after(17400, ques2_Opt1.destroy)
                            root.after(17500, ques2_Opt2.destroy)
                            root.after(17400, ques2_Opt3.destroy)
                            root.after(17400, ques2_Opt4.destroy)
                            root.after(17500, label5.destroy)

                            # Calling the function to create Topic-1's (Question #3)
                            root.after(18000, lambda: ques3())

                            # -------------------------------------------------------------------------------------------- Topic-1's (Question #2) -StyleEnds----

                        # >>

                        # Function which creates Topic-1's (Question #1)
                        def ques1():

                            # ------------------------------------- (Question #1)'s Options -StyleStarts----------------------------------------------------

                            # Function for displaying the Correct-Answer
                            def ques1_Correct():

                                # Styling only the Correct-Answer RadioButton
                                ques1_C_Opt_style = Style(root)
                                ques1_C_Opt_style.theme_use("default")
                                ques1_C_Opt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                            foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Correct-Answer to green color
                                ques1_Opt2.configure(
                                    style="C.TRadiobutton", state=DISABLED)
                                ques1_Opt1.configure(state=DISABLED)
                                ques1_Opt3.configure(state=DISABLED)
                                ques1_Opt4.configure(state=DISABLED)

                            # Function which is triggered by Option-4 of (Question #1)
                            def ques1_Opt_4():

                                # Styling only the Option-4 RadioButton
                                ques1_Opt_style = Style(root)
                                ques1_Opt_style.theme_use("default")
                                ques1_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-4 to yellow color
                                ques1_Opt4.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques1_Opt1.configure(state=DISABLED)
                                ques1_Opt2.configure(state=DISABLED)
                                ques1_Opt3.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques1WO4_style = Style(root)
                                ques1WO4_style.theme_use("default")
                                ques1WO4_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques1_Opt4.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-3 of (Question #1)
                            def ques1_Opt_3():

                                # Styling only the Option-3 RadioButton
                                ques1_Opt_style = Style(root)
                                ques1_Opt_style.theme_use("default")
                                ques1_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-3 to yellow color
                                ques1_Opt3.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques1_Opt1.configure(state=DISABLED)
                                ques1_Opt2.configure(state=DISABLED)
                                ques1_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques1WO3_style = Style(root)
                                ques1WO3_style.theme_use("default")
                                ques1WO3_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques1_Opt3.configure(
                                    style="X.TRadiobutton"))

                            # Function which is triggered by Option-2 of (Question #1)
                            def ques1_Opt_2():

                                # Styling only the Option-2 RadioButton
                                ques1_Opt_style = Style(root)
                                ques1_Opt_style.theme_use("default")
                                ques1_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques1_Opt2.configure(
                                    style="O.TRadiobutton", state=DISABLED)
                                ques1_Opt1.configure(state=DISABLED)
                                ques1_Opt3.configure(state=DISABLED)
                                ques1_Opt4.configure(state=DISABLED)

                                # Calling the function to add one point to the Guest for (Question #1)
                                root.after(3000, lambda: points())

                            # Function which is triggered by Option-1 of (Question #1)
                            def ques1_Opt_1():

                                # Styling only the Option-1 RadioButton
                                ques1_Opt_style = Style(root)
                                ques1_Opt_style.theme_use("default")
                                ques1_Opt_style.configure("O.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                          foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                                # Disabling all Options and Coloring Option-1 to yellow color
                                ques1_Opt1.configure(
                                    style="O.TRadiobutton", state=DISABLED)

                                ques1_Opt2.configure(state=DISABLED)
                                ques1_Opt3.configure(state=DISABLED)
                                ques1_Opt4.configure(state=DISABLED)

                                # Setting the Wrong-Answer to red color
                                ques1WO1_style = Style(root)
                                ques1WO1_style.theme_use("default")
                                ques1WO1_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                                         foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")
                                root.after(4000, lambda: ques1_Opt1.configure(
                                    style="X.TRadiobutton"))

                            # -------------------------------------------------------------------------------------------- (Question #1) Options -StyleEnds----

                            # >>

                            # ------------------------------------- Topic-1's (Question #1) -StyleStarts----------------------------------------------------

                            # Creating new label to show the (Question #1)
                            label4 = Label(root, text="1. Entomology is the science that studies", font=("Dodge", 14),
                                           foreground="#D1E3DD", background="#1E0905", width=32, wraplength=350)  # 1E0905
                            label4.place(relx=0.75, rely=0.25, anchor=E)

                            # Styling the (Question #1) Options
                            ques1_Opt_style = Style(root)
                            ques1_Opt_style.theme_use("default")
                            ques1_Opt_style.configure("TRadiobutton", font=("Playball", 12, "bold", "italic"),
                                                      foreground="#D1E3DD", background="#1E0905", borderwidth=2, width=25, height=5)
                            ques1_Opt_style.map("TRadiobutton", foreground=[
                                ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                            # Creating the Options for (Question #1)
                            # Creating Option-1 and assigning a styler function to it
                            v1 = IntVar(root)
                            ques1_Opt1 = Radiobutton(root, text="Behavior of human beings", variable=v1,
                                                     value=1, command=lambda: ques1_Opt_1())
                            ques1_Opt1.place(
                                relx=0.35, rely=0.42, anchor=CENTER)

                            # Creating Option-2 and assigning a styler function to it
                            ques1_Opt2 = Radiobutton(root, text="Insects", variable=v1,
                                                     value=2, command=lambda: ques1_Opt_2())
                            ques1_Opt2.place(
                                relx=0.35, rely=0.52, anchor=CENTER)

                            # Creating Option-3 and assigning a styler function to it
                            ques1_Opt3 = Radiobutton(root, text="Scientific terms", variable=v1,
                                                     value=3, command=lambda: ques1_Opt_3())
                            ques1_Opt3.place(
                                relx=0.35, rely=0.62, anchor=CENTER)

                            # Creating Option-4 and assigning a styler function to it
                            ques1_Opt4 = Radiobutton(root, text="The formation of rocks", variable=v1,
                                                     value=4, command=lambda: ques1_Opt_4())
                            ques1_Opt4.place(
                                relx=0.35, rely=0.72, anchor=CENTER)

                            # Displaying CountDown-timer for (Question #1)
                            timer1 = Message(root, text="Timer\r\n   15", font=("Dodge", 12),
                                             foreground="#F0EFF4", background="#22333B", width=600)
                            timer1.place(relx=0.06, rely=0.1, anchor=CENTER)

                            # Periodically changing the Time-remaining after 1s
                            root.after(1100, lambda: timer1.configure(
                                text="Timer\r\n   14"))
                            root.after(2100, lambda: timer1.configure(
                                text="Timer\r\n   13"))
                            root.after(3100, lambda: timer1.configure(
                                text="Timer\r\n   12"))
                            root.after(4100, lambda: timer1.configure(
                                text="Timer\r\n   11"))
                            root.after(5100, lambda: timer1.configure(
                                text="Timer\r\n   10"))
                            root.after(6100, lambda: timer1.configure(
                                text="Timer\r\n   09"))
                            root.after(7100, lambda: timer1.configure(
                                text="Timer\r\n   08"))
                            root.after(8100, lambda: timer1.configure(
                                text="Timer\r\n   07"))
                            root.after(9100, lambda: timer1.configure(
                                text="Timer\r\n   06"))
                            root.after(10100, lambda: timer1.configure(
                                text="Timer\r\n   05"))
                            root.after(11100, lambda: timer1.configure(
                                text="Timer\r\n   04"))
                            root.after(12100, lambda: timer1.configure(
                                text="Timer\r\n   03"))
                            root.after(13100, lambda: timer1.configure(
                                text="Timer\r\n   02"))
                            root.after(14100, lambda: timer1.configure(
                                text="Timer\r\n   01"))
                            root.after(15100, lambda: timer1.configure(
                                text="Timer\r\n   00"))

                            # Calling the function to validate and styling the Correct Answer for (Question #1) after timer stops
                            root.after(15200, lambda: ques1_Correct())

                            # Destroying all the widgets showing (Question #1)
                            root.after(16100, timer1.destroy)
                            root.after(17400, ques1_Opt1.destroy)
                            root.after(17400, ques1_Opt2.destroy)
                            root.after(17500, ques1_Opt3.destroy)
                            root.after(17400, ques1_Opt4.destroy)
                            root.after(17500, label4.destroy)

                            # Calling the function to create Topic-1's (Question #2)
                            root.after(18000, lambda: ques2())

                            # -------------------------------------------------------------------------------------------- Topic-1's (Question #1) -StyleEnds----

                        # >>

                        # Disabling the Quiz Start-Button after clicked, for preventing the function to be called twice
                        start_button2.configure(state=DISABLED)

                        # Destroying all the widgets created in the Rules Panel for Topic-1
                        root.after(500, rules.destroy)
                        root.after(600, start_button2.destroy)
                        root.after(500, label2.destroy)
                        root.after(500, back3_button.destroy)

                        # Calling the function to create Topic-1's (Question #1)
                        root.after(800, lambda: ques10())

                    # >>

                    # ------------------------------------- Rules Panel for Topic-1 -StyleStarts----------------------------------------------------

                    # Disabling the Topic-Button1 after clicked, for preventing the function to be called twice
                    topic_button1.configure(state=DISABLED)

                    # Destroying all the widgets created in the Topic-Select Panel
                    root.after(800, topic_button1.destroy)
                    root.after(400, topic_button2.destroy)
                    root.after(400, topic_button3.destroy)
                    root.after(400, back2_button.destroy)

                    # Changing the text in the Topic-Select Panel label instead of destroying it
                    root.after(800, label2.configure(text="Rules"))

                    # Displaying the rules related to Topic-1's Quiz
                    rules = Message(root, text="    1. Each question has a time limit of 15 seconds.\r\n    2. Once the option is selected it can't be changed.\r\n    3. Final Score is displayed at the end.\r\n    4. The following questions are based on general topic.", font=("Dodge", 12),
                                    foreground="#D1E3DD", background="#1E0905", width=400)
                    rules.place(relx=0.5, rely=0.42, anchor=CENTER)

                    # Creating and Styling the Quiz Start-Button
                    start_button2_style = Style()
                    start_button2_style.configure("B.TButton", font=("Playball", 17, "bold", "italic"),
                                                  foreground="#0A0908", background="#F6F67C", borderwidth=2, width=8, height=2)
                    start_button2 = Button(root, text="Start",
                                           style="B.TButton", command=lambda: quiz1())
                    start_button2.place(relx=0.5, rely=0.75, anchor=CENTER)

                    # Creating a Back-Button to return to User-Select Panel
                    # Styling Back-Button
                    back3_button_style = Style()
                    back3_button_style.theme_use("default")
                    back3_button_style.configure("E.TButton", font=("Playball", 10, "italic", "bold"),
                                                 foreground="#0A0908", background="#F6F67C", borderwidth=2, width=10, height=2, focuscolor="none")

                    back3_button = Button(root, text="< back",
                                          style="E.TButton", command=lambda: back3())
                    back3_button.place(relx=0.15, rely=0.9, anchor=CENTER)

                    # -------------------------------------------------------------------------------------------- Rules Panel for Topic-1 -StyleEnds----

                # >>

                # ------------------------------------- Topic-Select Panel -StyleStarts----------------------------------------------------

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
                                       style="W.TButton", command=lambda: topic_1())
                topic_button1.place(relx=0.5, rely=0.3, anchor=CENTER)

                topic_button2 = Button(root, text="Technology",
                                       style="W.TButton", command=lambda: topic_2())
                topic_button2.place(relx=0.5, rely=0.5, anchor=CENTER)

                topic_button3 = Button(root, text="Science",
                                       style="W.TButton", command=lambda: topic_3())
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

                # -------------------------------------------------------------------------------------------- Topic-Select -StyleEnds----

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

            # Creating a Enter-Button which triggers the function for creating Topic-Select panel
            guestNameBtn = Button(
                root, text="Enter", style="S.TButton", command=lambda:  userOptions())
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
