# --- Quizz-kur --- a quiz application designed by Kumara


# importing tkinter and tkinter.ttk modules for creating the GUI
from tkinter import *
from tkinter.ttk import *

# importing the messagebox class to create a messagebox
from tkinter import messagebox

# importing sqlite3 for create and work with databases
import sqlite3

# importing a setup function to setting up this application, with more dynamic functionality
from setup import settingUp

# importing tkinter as variable for special purposes
import tkinter as tk


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

        # >>

        # Function which is operated by the User-Select's Admin-Button to create Admin-SignIn panel
        def admins():

            # Function which creates the Admin-Interface with buttons for updating predefined Quiz
            def adminOptionsPanel(adminID):

                # Function which is operated by the Admin-Interface's LogOut-Button
                def logOut():

                    # Disabling the LogOut-Button after clicked, for preventing the function to be called twice
                    logOut_button.configure(state=DISABLED)

                    # Destroying all the widgets created in the Admin-Interface panel
                    root.after(800, lambda: logOut_button.destroy())
                    root.after(700, lambda: leaderboard_UpdateBtn.destroy())
                    root.after(700, lambda: quiz_UpdateBtn.destroy())
                    root.after(700, lambda: leaderboard_btn.destroy())
                    root.after(700, lambda: label2.destroy())
                    root.after(700, lambda: label3.destroy())
                    root.after(700, lambda: label31.destroy())

                    # Calling the function to redirect to the User-Select panel
                    root.after(1000, lambda: userSelect())

                # >>

                # Function which is operated by the LeaderBoard-Button in the Admin-Interface to collect the top 10 scores from the database
                def leaderboard():

                    # Function which creates the leaderboard with the top 5 data collected from the database
                    def leaderboard_show():

                        # Function which is operated by the LeaderBoard's Back-Button
                        def leaderboard_hide():

                            # Disabling the Back-Button after clicked, for preventing the function to be called twice
                            leaderboard_btn.configure(state=DISABLED)

                            # Destroying all the widgets created in the leaderboard
                            leaderboard_subtitle.destroy()
                            leaderboard_name_label.destroy()
                            leaderboard_score_label.destroy()
                            leaderboard_id_label.destroy()
                            leaderboard_background.destroy()

                            # Changing back the Back-Button text to Leaderboard-Button and also changing the function assigned to it
                            root.after(100, lambda: leaderboard_btn.configure(
                                text="LeaderBoard", state=NORMAL, command=lambda: leaderboard()))

                            # Enabling the Admin-Interface's LogOut-Button
                            logOut_button.configure(state=NORMAL)

                        # >>

                        # ------------------------------------- Leaderboard -StyleStarts----------------------------------------------------

                        # Changing the text on the Leaderboard-Button to a Back-Button and also changing the function assigned to it
                        root.after(100, lambda: leaderboard_btn.configure(
                            text="< back", state=NORMAL, command=lambda: leaderboard_hide()))

                        # Disabling the LogOut-Button when the leaderboard is open
                        logOut_button.configure(state=DISABLED)

                        # Creating a background for the leaderboard panel
                        leaderboard_background = Canvas(
                            root, width=440, height=300, background="#1E0905")
                        leaderboard_background.place(
                            relx=0.59, rely=0.55, anchor=CENTER)

                        # Styling the leaderboard sub-Title labels
                        leaderboard_subtitle_style = Style()
                        leaderboard_subtitle_style.theme_use("default")
                        leaderboard_subtitle_style.configure("L.TLabel", font=("Dodge", 14, "bold", "italic"),
                                                             foreground="#F8FFE5", background="#1E0905", borderwidth=2, focuscolor='none')

                        # Creating a label to show the leaderboard sub-Titles
                        leaderboard_subtitle = Label(
                            root, text="Name                                    Score              ID\r\n", style="L.TLabel")
                        leaderboard_subtitle.place(
                            relx=0.58, rely=0.29, anchor=CENTER)

                        # Styling the GuestNames displayed in the leaderboard
                        leaderboard_name_label_style = Style()
                        leaderboard_name_label_style.theme_use("default")
                        leaderboard_name_label_style.configure("N.TLabel", font=("Dodge", 13, "bold", "italic"),
                                                               foreground="#F8FFE5", background="#1E0905", borderwidth=2, focuscolor='none')

                        # Creating a label to show the GuestNames
                        leaderboard_name_label = Label(
                            root, text=show_names, style="N.TLabel")
                        leaderboard_name_label.place(
                            relx=0.25, rely=0.35, anchor=NW)

                        # Styling the guests score and id labels
                        leaderboard_score_label_style = Style()
                        leaderboard_score_label_style.theme_use("default")
                        leaderboard_score_label_style.configure("P.TLabel", font=("Dodge", 13, "bold", "italic"),
                                                                foreground="#F8FFE5", background="#1E0905", borderwidth=2, focuscolor='none')

                        # Creating the guests score label
                        leaderboard_score_label = Label(
                            root, text=show_scores, style="P.TLabel")
                        leaderboard_score_label.place(
                            relx=0.7, rely=0.35, anchor=NE)

                        # Creating the guests id label
                        leaderboard_id_label = Label(
                            root, text=show_ids, style="P.TLabel")
                        leaderboard_id_label.place(
                            relx=0.9, rely=0.35, anchor=NE)

                        # -------------------------------------------------------------------------------------------- Leaderboard -StyleEnds----

                    # >>

                    # Disabling the LeaderBoard-Button after clicked, for preventing the function to be called twice
                    leaderboard_btn.configure(state=DISABLED)

                    # Connecting to the App's Database, if not exists creating a new database
                    quizzkur_DB = sqlite3.connect("quizz_kur.db")

                    # Creating a cursor
                    co = quizzkur_DB.cursor()

                    # Creating a 'leaderboard' table if not exists to store the Guestname and score
                    co.execute("""CREATE TABLE IF NOT EXISTS leaderboard (
                                playername text,
                                score integer
                                )""")

                    # Querying the database and collect the top 10 scored users with their 'oid'
                    co.execute(
                        "SELECT *, oid FROM leaderboard ORDER BY score DESC")
                    points = co.fetchmany(10)

                    # Separating the names from the collected data
                    show_names = " "
                    for record in points:
                        show_names += str(record[0]) + "\n "

                    # Separating the scores from the collected data
                    show_scores = " "
                    for record in points:
                        show_scores += str(record[1]) + "\n "

                    # Separating the ids from the collected data
                    show_ids = " "
                    for record in points:
                        show_ids += str(record[2]) + "\n "

                    # Committing the changes to the database
                    quizzkur_DB.commit()

                    # Closing the connection with the database
                    quizzkur_DB.close()

                    # Calling the function to create the leaderboard
                    root.after(500, lambda: leaderboard_show())

                # >>

                # Function which creates the Leaderboard-Update Panel with Update-Button and a field for GuestId
                def leaderboardUpdatePanel():

                    # Function which destroys all the widgets created in the Leaderboard-Update Panel and redirects to the Admin-Interface
                    def leaderboardUpdateDestroyer():

                        # Disabling the Back-Button after clicked, for preventing the function to be called twice
                        leaderboard_U_backBtn.configure(state=DISABLED)

                        # Destroying all the widgets created in the Leaderboard-Update Panel
                        root.after(
                            1000, lambda: leaderboard_U_hintlabel.destroy())
                        root.after(
                            1100, lambda: leaderboard_U_backBtn.destroy())
                        root.after(
                            1200, lambda: leaderboard_U_entrylabel.destroy())
                        root.after(1200, lambda: leaderboard_U_entry.destroy())
                        root.after(1200, lambda: remove_btn.destroy())
                        root.after(1300, lambda: leaderboard_Ulabel.destroy())
                        root.after(2000, lambda: label3.destroy())
                        root.after(2000, lambda: label31.destroy())

                        # Calling the function to redirect to the Admin-Interface
                        root.after(2000, lambda: adminOptionsPanel(adminID))

                    # >>

                    # Function which operated by the Leaderboard-Update Panel's Remove-Button to remove the GuestRecord from the Leaderboard
                    def removeGuest():

                        # Confirming that the GuestId-Entry is not empty
                        if (leaderboard_U_entry.get() == ""):

                            # Showing a error message
                            messagebox.showerror(
                                "Error: empty field", "GuestId can't be empty")

                        # Confirming that the value from GuestId-Entry is an Integer
                        elif (leaderboard_U_entry.get().isdigit()):

                            # Connecting to the App's Database, if not exists creating a new database
                            quizzkur_DB = sqlite3.connect("quizz_kur.db")

                            # Creating a cursor
                            co = quizzkur_DB.cursor()

                            # Checking if the GuestId exists in the database
                            co.execute(
                                "SELECT oid FROM leaderboard WHERE oid = '%s'" % leaderboard_U_entry.get())
                            isGuestexists = co.fetchone()

                            if (isGuestexists is None):

                                # Showing a error message if the GuestId doesn't exists in the Database
                                messagebox.showerror(
                                    "Error: invalid entry", f"GuestId : '{leaderboard_U_entry.get()}' doesn't exists in the Database")

                            else:

                                # Showing a confirmation dialog with some message if the GuestId exists
                                click = messagebox.askquestion(
                                    "Confirmation: delete", f"Do you really want to delete?,\r\n\nGuestId : {leaderboard_U_entry.get()}  from leaderboard.")

                                if (click == "yes"):

                                    # Removing the Guest from Leaderboard with the matching Id
                                    co.execute(
                                        "DELETE from leaderboard WHERE oid = '%s'" % leaderboard_U_entry.get())

                                    # Creating a label to show that the selected GuestId is removed
                                    removed_info = Label(root, text=f"Guest-Id : {leaderboard_U_entry.get()} is removed", font=(
                                        "Dodge", 14), foreground="#F6F67C", background="#1E0905")
                                    removed_info.place(
                                        relx=0.6, rely=0.9, anchor=CENTER)

                                    # Calling the function to delete all the widgets created in the Leaderboard-Update Panel and also redirect to the Admin-Interface
                                    root.after(
                                        1000, lambda: leaderboardUpdateDestroyer())
                                    root.after(
                                        2800, lambda: removed_info.destroy())

                                else:

                                    # Resetting the value of GuestId-Entry if pressed 'no'
                                    leaderboard_U_entryVar.set("")
                                    leaderboard_U_entry.focus_set()

                            # Committing the changes to the database
                            quizzkur_DB.commit()

                            # Closing the connection with the database
                            quizzkur_DB.close()

                        else:

                            # Showing a error message when the value from GuestId-Entry is not an Integer
                            messagebox.showerror(
                                "Error: invalid entry", f"Entered Value: '{leaderboard_U_entry.get()}' is not valid, make sure to use only Whole Numbers or Integers")

                    # >>

                    # ------------------------------------- Leaderboard-Update Panel -StyleStarts----------------------------------------------------

                    # Creating a label to show the screen Title
                    leaderboard_Ulabel = Label(root, text="Update Leaderboard", font=("Dodge", 25, "bold"),
                                               foreground="#D1E3DD", background="#1E0905")
                    leaderboard_Ulabel.place(
                        relx=0.5, rely=0.2, anchor=CENTER)

                    # Creating a label to show the field name
                    leaderboard_U_entrylabel = Label(root, text="Guest ID", font=("Dodge", 20, "italic"),
                                                     foreground="#DB12AF", background="#1E0905")
                    leaderboard_U_entrylabel.place(
                        relx=0.25, rely=0.4, anchor=CENTER)

                    # Creating a label to show the Hints
                    leaderboard_U_hintlabel = Label(root, text="  Hint :\r\n# Type guestID number to be removed\r\n# Value must be any whole number", font=("Dodge", 10),
                                                    foreground="#D4B0F9", background="#1E0905")
                    leaderboard_U_hintlabel.place(
                        relx=0.55, rely=0.68, anchor=CENTER)

                    # Creating a GuestId-Entry for the entering the guestID number to be removed
                    leaderboard_U_entryVar = StringVar()
                    leaderboard_U_entry = Entry(root, textvariable=leaderboard_U_entryVar,
                                                font=("Dodge", 20, "bold", "italic"), width=10, justify=CENTER)
                    leaderboard_U_entry.focus_set()
                    leaderboard_U_entry.place(
                        relx=0.5, rely=0.4, anchor=CENTER)

                    # Styling the Remove-Button
                    remove_btn_style = Style()
                    remove_btn_style.theme_use("default")
                    remove_btn_style.configure("W.TButton", font=("Playball", 15, "italic"),
                                               foreground="#F0EFF4", background="#BF09D5", borderwidth=2, width=7, focuscolor='none')
                    # Mouse Hovering style
                    remove_btn_style.map('W.TButton', foreground=[(
                        'active', '!disabled', '#F0EFF4')], background=[('active', '#DB12AF')])

                    # Creating a Remove-Button
                    remove_btn = Button(root, text="Remove",
                                        style="W.TButton", command=lambda: removeGuest())
                    remove_btn.place(
                        relx=0.72, rely=0.4, anchor=CENTER)

                    # Creating a Back-Button to go back to Admin-Interface
                    leaderboard_U_backBtn = Button(root, text="< back",
                                                   style="E.TButton", command=lambda: leaderboardUpdateDestroyer())
                    leaderboard_U_backBtn.place(
                        relx=0.1, rely=0.9, anchor=CENTER)

                    # -------------------------------------------------------------------------------------------- Leaderboard-Update Panel -StyleEnds----

                # >>

                # Function which creates the Quiz-Topics Panel with multiple Topic-Buttons for Admins to choose which Topic to update
                def quizTopicsPanel():

                    # Function which is operated by the Quiz-Topics Panel's Back-Button
                    def quizTopicsPanelDestroyer():

                        # Disabling the Back-Button after clicked, for preventing the function to be called twice
                        quiz_T_backBtn.configure(state=DISABLED)

                        # Destroying all the widgets created in the Quiz-Topics Panel
                        root.after(600, lambda: quiz_T_backBtn.destroy())
                        root.after(500, lambda: quiz_T_topicBtn1.destroy())
                        root.after(500, lambda: quiz_T_topicBtn2.destroy())
                        root.after(500, lambda: quiz_T_topicBtn3.destroy())
                        root.after(500, lambda: quiz_Tlabel.destroy())
                        root.after(500, lambda: label3.destroy())
                        root.after(500, lambda: label31.destroy())

                        # Calling the function to redirect to the Admin-Interface
                        root.after(800, lambda: adminOptionsPanel(adminID))

                    # >>

                    # Function which creates the Quiz-Update Panel with 10 QuizNumber-Buttons for Admins to choose which Quiz to modify
                    def quizUpdatePanel(selected_topic, quizDB, quizCount):

                        # Function which destroying all the QuizNumber-Buttons in the Quiz-Update Panel
                        def quizNumButtonDestroyer(buttons):

                            # Destroying each QuizNumber-Button
                            for btn in buttons:
                                btn.destroy()

                        # >>

                        # Function which is operated by the QuizNumber-Button to create Quiz-Edit Panel
                        def quizEditPanel(quiz_U_closed, quiz_number=""):

                            # Function which destroys all the widgets created in the Quiz-Edit Panel and redirects to the Quiz-Update Panel
                            def quizEditPanelDestroyer():

                                # Disabling the Back-Button after clicked, for preventing the function to be called twice
                                quiz_E_backBtn.configure(state=DISABLED)

                                # Destroying all the widgets created in the Quiz-Edit Panel
                                root.after(
                                    1000, lambda: quiz_E_saveBtn.destroy())
                                root.after(1200, lambda: quiz_E_ques.destroy())
                                root.after(1200, lambda: quiz_E_opt1.destroy())
                                root.after(1200, lambda: quiz_E_opt2.destroy())
                                root.after(1200, lambda: quiz_E_opt3.destroy())
                                root.after(1200, lambda: quiz_E_opt4.destroy())
                                root.after(
                                    1200, lambda: quiz_E_Correct.destroy())
                                root.after(
                                    1300, lambda: quiz_E_qlabel.destroy())
                                root.after(
                                    1300, lambda: quiz_E_opt1_label.destroy())
                                root.after(
                                    1300, lambda: quiz_E_opt2_label.destroy())
                                root.after(
                                    1300, lambda: quiz_E_opt3_label.destroy())
                                root.after(
                                    1300, lambda: quiz_E_opt4_label.destroy())
                                root.after(
                                    1300, lambda: quiz_E_Correct_label.destroy())
                                root.after(
                                    1350, lambda: quiz_E_label.destroy())
                                root.after(
                                    1350, lambda: quiz_E_nlabel.destroy())
                                root.after(
                                    1450, lambda: quiz_E_backBtn.destroy())

                                # Calling the function to redirect to the Quiz-Update Panel
                                root.after(1550, lambda: quizUpdatePanel(
                                    selected_topic, quizDB, quizCount))

                            # >>

                            # Function which operated by the Quiz-Edit Panel's Save-Button to update the Database with modified Quiz-Data
                            def saveModifiedQuiz(question_no, defaultC_value):

                                # Disabling the Save-Button after clicked, for preventing the function to be called twice & also Back-Button
                                quiz_E_saveBtn.configure(state=DISABLED)
                                quiz_E_backBtn.configure(state=DISABLED)

                                # Checking if none of the entries are empty
                                if (quiz_E_ques.get() == "" or quiz_E_opt1.get() == "" or quiz_E_opt2.get() == "" or quiz_E_opt3.get() == "" or quiz_E_opt4.get() == "" or quiz_E_Correct.get() == ""):

                                    # Showing a error message
                                    messagebox.showerror(
                                        "Error: empty field", "Field is empty")

                                    # Re-enabling both the Buttons
                                    quiz_E_saveBtn.configure(state=NORMAL)
                                    quiz_E_backBtn.configure(state=NORMAL)

                                else:

                                    # Creating a List to hold all the value of 4 Options from the Quiz-Edit Panel
                                    availableOptions = [
                                        quiz_E_opt1.get(),
                                        quiz_E_opt2.get(),
                                        quiz_E_opt3.get(),
                                        quiz_E_opt4.get()
                                    ]
                                    # Assigning a variable to hold data of option uniqueness
                                    uniqueOptions = True

                                    # Checking if all the 4 Options are unique
                                    i, j = 0, 0
                                    for option in availableOptions:

                                        # Comparing with each option to make sure none of the value of option matches
                                        if(uniqueOptions):

                                            i += 1
                                            for opt in availableOptions:

                                                j += 1
                                                if (i != j and option == opt):

                                                    # Re-assigning the variable as not-unique
                                                    uniqueOptions = False
                                                    break

                                            # Resetting
                                            j = 0

                                    # Showing error message when all the value of Options are not-unique
                                    if (uniqueOptions == False):

                                        # Showing a error message when none of the value of Option Entries matches to the CorrectOption-Entry value
                                        messagebox.showerror(
                                            "Error: invalid entry", "All Options must be have a unique value, none of the Option value doesn't match.")

                                        # Re-enabling both the Buttons
                                        quiz_E_saveBtn.configure(state=NORMAL)
                                        quiz_E_backBtn.configure(state=NORMAL)

                                    # Checking if the CorrectOption-Entry value matches to any of the 4 Options
                                    elif (uniqueOptions and [opt for opt in availableOptions if opt == quiz_E_Correct.get()]):

                                        # Showing a confirmation dialog with some message if the GuestId exists
                                        click = messagebox.askquestion(
                                            "Confirmation: update", "Changes made to Database can't be reverted, are you sure?")

                                        if (click == "yes"):

                                            # Connecting to the App's Database, if not exists creating a new database
                                            quizzkur_DB = sqlite3.connect(
                                                "quizz_kur.db")

                                            # Creating a cursor
                                            co = quizzkur_DB.cursor()

                                            # Updating the modifications made on the selected Quiz to the Database
                                            co.execute(f"UPDATE {quizDB} SET question = :question_entry, option1 = :option1_entry, option2 = :option2_entry, option3 = :option3_entry, option4 = :option4_entry, correct = :correct_entry WHERE oid = :question_no",
                                                       {
                                                           "question_entry": quiz_E_ques.get(),
                                                           "option1_entry": quiz_E_opt1.get(),
                                                           "option2_entry": quiz_E_opt2.get(),
                                                           "option3_entry": quiz_E_opt3.get(),
                                                           "option4_entry": quiz_E_opt4.get(),
                                                           "correct_entry": quiz_E_Correct.get(),

                                                           "question_no": question_no
                                                       })

                                            # Committing the changes to the database
                                            quizzkur_DB.commit()

                                            # Closing the connection with the database
                                            quizzkur_DB.close()

                                            # Creating a label to show that Quiz is processing and updated
                                            update_info = Label(root, text="- processing.", font=("Dodge", 12, "bold", "italic"),
                                                                foreground="#F6F67C", background="#1E0905", width=25)

                                            # Showing the processing message
                                            root.after(300, lambda: update_info.place(
                                                relx=0.5, rely=0.07, anchor=CENTER))
                                            root.after(600, lambda: update_info.configure(
                                                text="- processing.."))
                                            root.after(900, lambda: update_info.configure(
                                                text="- processing..."))
                                            root.after(1200, lambda: update_info.configure(
                                                text="- processing...."))
                                            ##
                                            root.after(1500, lambda: update_info.configure(
                                                text="- updated successfully", foreground="#38B000"))

                                            # Calling the function to delete all the widgets created in the Quiz-Edit Panel and also redirect to the Quiz-Update Panel
                                            root.after(
                                                2500, lambda: update_info.destroy())
                                            root.after(
                                                2000, lambda: quizEditPanelDestroyer())

                                        else:

                                            # Re-enabling both the Buttons
                                            quiz_E_saveBtn.configure(
                                                state=NORMAL)
                                            quiz_E_backBtn.configure(
                                                state=NORMAL)

                                    else:

                                        # Showing a error message when none of the value of Option Entries matches to the CorrectOption-Entry value
                                        messagebox.showerror(
                                            "Error: invalid entry", "Correct Option's value should match with any of the other Option's value")

                                        # Resetting the value of CorrectOption-Entry to default
                                        quiz_E_Correct_Var.set(defaultC_value)

                                        # Re-enabling both the Buttons
                                        quiz_E_saveBtn.configure(state=NORMAL)
                                        quiz_E_backBtn.configure(state=NORMAL)

                            # >>

                            # Checking if the Quiz-Update Panel is closed
                            if (quiz_U_closed):

                                # ------------------------------------- Quiz-Edit Panel -StyleStarts----------------------------------------------------

                                # Connecting to the App's Database, if not exists creating a new database
                                quizzkur_DB = sqlite3.connect("quizz_kur.db")

                                # Creating a cursor
                                co = quizzkur_DB.cursor()

                                # Querying the specified table in the database and collecting the quiz which matchs the Quiz-number
                                co.execute(
                                    "SELECT *, oid FROM %s WHERE oid = '%s'" % (quizDB, str(quiz_number)))
                                quiz_data = co.fetchall()

                                # Committing the changes to the database
                                quizzkur_DB.commit()

                                # Closing the connection with the database
                                quizzkur_DB.close()

                                # Creating a label to show the screen Title
                                quiz_E_label = Label(root, text="Question", font=("Dodge", 15, "bold"),
                                                     foreground="#D1E3DD", background="#1E0905")
                                quiz_E_label.place(
                                    relx=0.12, rely=0.07, anchor=CENTER)

                                # Creating a label to show the selected Quiz-Number
                                quiz_E_nlabel = Label(root, text="# " + quiz_data[0][0], font=("Dodge", 15, "bold"),
                                                      foreground="#BF09D5", background="#1E0905")
                                quiz_E_nlabel.place(
                                    relx=0.25, rely=0.07, anchor=CENTER)

                                # ---------- Creating label for the Entries in Quiz-Edit Panel -----

                                # Creating a label to show the hint label for Question-Entry
                                quiz_E_qlabel = Label(root, text="# Type new question", font=("Dodge", 10, "italic"),
                                                      foreground="#DB12AF", background="#1E0905")
                                quiz_E_qlabel.place(
                                    relx=0.85, rely=0.32, anchor=CENTER)

                                # Creating label for Option1-Entry
                                quiz_E_opt1_label = Label(root, text="Option 1", font=("Dodge", 14, "bold"),
                                                          foreground="#DB12AF", background="#1E0905")
                                quiz_E_opt1_label.place(
                                    relx=0.1, rely=0.45, anchor=CENTER)

                                # Creating label for Option2-Entry
                                quiz_E_opt2_label = Label(root, text="Option 2", font=("Dodge", 14, "bold"),
                                                          foreground="#DB12AF", background="#1E0905")
                                quiz_E_opt2_label.place(
                                    relx=0.6, rely=0.45, anchor=CENTER)

                                # Creating label for Option3-Entry
                                quiz_E_opt3_label = Label(root, text="Option 3", font=("Dodge", 14, "bold"),
                                                          foreground="#DB12AF", background="#1E0905")
                                quiz_E_opt3_label.place(
                                    relx=0.1, rely=0.65, anchor=CENTER)

                                # Creating label for Option4-Entry
                                quiz_E_opt4_label = Label(root, text="Option 4", font=("Dodge", 14, "bold"),
                                                          foreground="#DB12AF", background="#1E0905")
                                quiz_E_opt4_label.place(
                                    relx=0.6, rely=0.65, anchor=CENTER)

                                # Creating label for CorrectOption-Entry
                                quiz_E_Correct_label = Label(root, text="# Correct Answer", font=("Dodge", 12, "bold"),
                                                             foreground="#38B000", background="#1E0905")
                                quiz_E_Correct_label.place(
                                    relx=0.53, rely=0.93, anchor=CENTER)

                                # >>

                                # ---------- Creating Entries for updating the selected Quiz -----

                                # Creating the entry for updating Quiz-Question
                                quiz_E_ques_Var = StringVar()
                                quiz_E_ques = tk.Entry(root, textvariable=quiz_E_ques_Var,
                                                       font=("Dodge", 13, "bold", "italic"), width=60, background="#F3FAE1")
                                quiz_E_ques.focus_set()
                                quiz_E_ques.place(
                                    relx=0.5, rely=0.23, anchor=CENTER, height=30)

                                # Creating the entry for updating Quiz-Option1
                                quiz_E_opt1_Var = StringVar()
                                quiz_E_opt1 = tk.Entry(root, textvariable=quiz_E_opt1_Var,
                                                       font=("Dodge", 11, "bold", "italic"), width=20, background="#EEC7FC")
                                quiz_E_opt1.place(
                                    relx=0.33, rely=0.45, anchor=CENTER, height=30)

                                # Creating the entry for updating Quiz-Option2
                                quiz_E_opt2_Var = StringVar()
                                quiz_E_opt2 = tk.Entry(root, textvariable=quiz_E_opt2_Var,
                                                       font=("Dodge", 11, "bold", "italic"), width=20, background="#EEC7FC")
                                quiz_E_opt2.place(
                                    relx=0.83, rely=0.45, anchor=CENTER, height=30)

                                # Creating the entry for updating Quiz-Option3
                                quiz_E_opt3_Var = StringVar()
                                quiz_E_opt3 = tk.Entry(root, textvariable=quiz_E_opt3_Var,
                                                       font=("Dodge", 11, "bold", "italic"), width=20, background="#EEC7FC")
                                quiz_E_opt3.place(
                                    relx=0.33, rely=0.65, anchor=CENTER, height=30)

                                # Creating the entry for updating Quiz-Option4
                                quiz_E_opt4_Var = StringVar()
                                quiz_E_opt4 = tk.Entry(root, textvariable=quiz_E_opt4_Var,
                                                       font=("Dodge", 11, "bold", "italic"), width=20, background="#EEC7FC")
                                quiz_E_opt4.place(
                                    relx=0.83, rely=0.65, anchor=CENTER, height=30)

                                # Creating the entry for updating Quiz-CorrectOption
                                quiz_E_Correct_Var = StringVar()
                                quiz_E_Correct = tk.Entry(root, textvariable=quiz_E_Correct_Var,
                                                          font=("Dodge", 11, "bold", "italic"), width=24, background="lightgreen")
                                quiz_E_Correct.place(
                                    relx=0.5, rely=0.85, anchor=CENTER, height=30)

                                # Inserting the selected Quiz's data into its relevant Entries
                                for item in quiz_data:
                                    quiz_E_ques.insert(0, item[1])
                                    quiz_E_opt1.insert(0, item[2])
                                    quiz_E_opt2.insert(0, item[3])
                                    quiz_E_opt3.insert(0, item[4])
                                    quiz_E_opt4.insert(0, item[5])
                                    quiz_E_Correct.insert(0, item[6])

                                # Styling the Quiz Save-Button
                                quiz_E_saveBtn_style = Style()
                                quiz_E_saveBtn_style.theme_use("default")
                                quiz_E_saveBtn_style.configure("W.TButton", font=("Playball", 16, "italic"),
                                                               foreground="#F0EFF4", background="#BF09D5", borderwidth=2, width=6, focuscolor='none')
                                # Mouse Hovering style
                                quiz_E_saveBtn_style.map('W.TButton', foreground=[(
                                    'active', '!disabled', '#F0EFF4')], background=[('active', '#DB12AF')])

                                # Creating Quiz Save-Button to save the modifications made on the Quiz data
                                quiz_E_saveBtn = Button(root, text="Save QA",
                                                        style="W.TButton", command=lambda: saveModifiedQuiz(quiz_data[0][0], quiz_data[0][6]))
                                quiz_E_saveBtn.place(
                                    relx=0.9, rely=0.9, anchor=CENTER)

                                # Creating a Back-Button to go back to Quiz-Update Panel
                                # Styling Back-button
                                quiz_E_backBtn_style = Style()
                                quiz_E_backBtn_style.theme_use("default")
                                quiz_E_backBtn_style.configure("E.TButton", font=("Playball", 10, "italic", "bold"),
                                                               foreground="#0A0908", background="#F6F67C", borderwidth=2, width=10, height=2, focuscolor="none")
                                # Mouse Hovering style
                                quiz_E_backBtn_style.map('E.TButton', foreground=[
                                    ('active', '!disabled', '#F0EFF4')], background=[('active', '#DB12AF')])

                                quiz_E_backBtn = Button(root, text="< back",
                                                        style="E.TButton", command=lambda: quizEditPanelDestroyer())
                                quiz_E_backBtn.place(
                                    relx=0.1, rely=0.9, anchor=CENTER)

                                # -------------------------------------------------------------------------------------------- Quiz-Edit Panel -StyleEnds----

                            else:

                                # ----- Closing the Quiz-Update Panel

                                # Disabling the clicked QuizNumber-Button, for preventing the function to be called twice
                                quiz_Btn = root.focus_get()
                                quiz_Btn.configure(state=DISABLED)

                                # Destroying all the widgets created in the Quiz-Update Panel
                                root.after(
                                    1000, lambda: quizNumButtonDestroyer(quiz_UButtons))
                                root.after(
                                    1100, lambda: quiz_U_nextBtn.destroy())
                                root.after(
                                    1100, lambda: quiz_U_backBtn.destroy())
                                root.after(1300, lambda: quiz_Ulabel.destroy())

                                # Assigning the text on the clicked QuizNumber-Button to a variable as a integer
                                quiz_number = int(quiz_Btn["text"])

                                # Calling the function to create Quiz-Edit Panel
                                root.after(
                                    1500, lambda: quizEditPanel(True, quiz_number))

                        # >>

                        # Function which destroys all the widgets created on Quiz-Update Panel and switch to new panel according to the button clicked
                        def quizUpdatePanelSwitcher(triggerBy=""):

                            # Disabling the Back & Next Buttons after clicked, for preventing the function to be called twice
                            quiz_U_backBtn.configure(state=DISABLED)
                            quiz_U_nextBtn.configure(state=DISABLED)

                            # Destroying all the widgets created in the Quiz-Update Panel
                            root.after(
                                1000, lambda: quizNumButtonDestroyer(quiz_UButtons))
                            root.after(1100, lambda: quiz_U_nextBtn.destroy())
                            root.after(1100, lambda: quiz_U_backBtn.destroy())
                            root.after(1200, lambda: quiz_Ulabel.destroy())

                            # Checking which button is clicked
                            if (triggerBy == "Next" or triggerBy == "< back"):

                                quizSetCount = 0
                                if (triggerBy == "Next"):

                                    # Increasing the Quiz set count
                                    quizSetCount = quizCount + 10

                                if (triggerBy == "< back"):

                                    # Decreasing the Quiz set count
                                    quizSetCount = quizCount - 10

                                # Calling the function to recreate the Quiz-Update Panel with next 10 set of Quiz
                                root.after(1500, lambda: quizUpdatePanel(
                                    selected_topic, quizDB, quizSetCount))

                            else:

                                # Calling the function to redirect to the Quiz-Topics Panel
                                root.after(1500, lambda: quizTopicsPanel())

                        # >>

                        # ------------------------------------- Quiz-Update Panel -StyleStarts----------------------------------------------------

                        # Connecting to the App's Database, if not exists creating a new database
                        quizzkur_DB = sqlite3.connect("quizz_kur.db")

                        # Creating a cursor
                        co = quizzkur_DB.cursor()

                        # Querying the specified table in the database and collecting a set of 10 Quiz-number
                        co.execute("SELECT no FROM %s" % (quizDB))
                        quizNumbers = co.fetchmany(quizCount)

                        # Getting the length of both total available Quiz and queryed Quiz
                        co.execute("SELECT no FROM %s" % (quizDB))
                        totalquiz = len(co.fetchall())
                        quizLength = [totalquiz, len(quizNumbers)]

                        # Committing the changes to the database
                        quizzkur_DB.commit()

                        # Closing the connection with the database
                        quizzkur_DB.close()

                        # Shrinking the List to hold only 10 quiz, if holds more
                        while (len(quizNumbers) > 10):
                            quizNumbers.pop(0)

                        # Creating a label to show the selected topic as screen Title
                        quiz_Ulabel = Label(root, text=selected_topic, font=("Dodge", 18, "bold"),
                                            foreground="#D1E3DD", background="#1E0905")
                        quiz_Ulabel.place(
                            relx=0.25, rely=0.1, anchor=CENTER)

                        # Styling QuizNumber-Buttons
                        quiz_UButton_style = Style()
                        quiz_UButton_style.theme_use("default")
                        quiz_UButton_style.configure("W.TButton", font=("Playball", 12, "bold", "italic"),
                                                     foreground="#F0EFF4", background="#BF09D5", borderwidth=2, width=3, focuscolor='none')
                        # Mouse Hovering style
                        quiz_UButton_style.map('W.TButton', foreground=[(
                            'active', '!disabled', '#F0EFF4')], background=[('active', '#DB12AF')])

                        # Assigning X,Y coordinates for QuizNumber-Buttons
                        xy_coordinates = [
                            (0.5, 0.25),
                            (0.4, 0.4),
                            (0.6, 0.4),
                            (0.3, 0.55),
                            (0.5, 0.55),
                            (0.7, 0.55),
                            (0.2, 0.7),
                            (0.4, 0.7),
                            (0.6, 0.7),
                            (0.8, 0.7)
                        ]

                        # Creating and placing all the QuizNumber-Buttons like a Equilateral Triangle
                        quiz_UButtons = []
                        for num, axis in zip(quizNumbers, xy_coordinates):

                            # Creating QuizNumber-Button to create Quiz-Edit Panel
                            numButton = Button(
                                root, text=num, style="W.TButton", command=lambda: quizEditPanel(False))
                            numButton.place(
                                relx=axis[0], rely=axis[1], anchor=CENTER)

                            # Adding the created buttons to a list variable
                            quiz_UButtons.append(numButton)

                        # Creating a Back-Button to go back to Quiz-Topics Panel
                        # Styling Back-Button
                        quiz_U_backBtn_style = Style()
                        quiz_U_backBtn_style.theme_use("default")
                        quiz_U_backBtn_style.configure("E.TButton", font=("Playball", 10, "italic", "bold"),
                                                       foreground="#0A0908", background="#F6F67C", borderwidth=2, width=10, height=2, focuscolor="none")
                        # Mouse Hovering style
                        quiz_U_backBtn_style.map('E.TButton', foreground=[
                            ('active', '!disabled', '#F0EFF4')], background=[('active', '#DB12AF')])

                        quiz_U_backBtn = Button(root, text="< back",
                                                style="E.TButton", command=lambda: quizUpdatePanelSwitcher())
                        quiz_U_backBtn.place(
                            relx=0.1, rely=0.9, anchor=CENTER)

                        # Styling Next-Button
                        quiz_U_nextBtn_style = Style()
                        quiz_U_nextBtn_style.theme_use("default")
                        quiz_U_nextBtn_style.configure("F.TButton", font=("Playball", 12, "italic", "bold"),
                                                       foreground="#0A0908", background="#DB12AF", borderwidth=2, width=10, height=2, focuscolor="none")
                        # Mouse Hovering style
                        quiz_U_nextBtn_style.map('F.TButton', foreground=[
                            ('active', '!disabled', '#F0EFF4')], background=[('active', '#C9184A')])

                        # Creating the Next-Button to switch the next Quiz set
                        quiz_U_nextBtn = Button(root, text="Next",
                                                style="F.TButton", command=lambda: quizUpdatePanelSwitcher(quiz_U_nextBtn["text"]))

                        # Showing the Next-Button, if database has one more Quiz set
                        if (quizLength[0] != quizLength[1]):

                            # Placing the button on the Quiz-Update Panel
                            quiz_U_nextBtn.place(
                                relx=0.88, rely=0.9, anchor=CENTER)

                        else:

                            # Changing the Back-Button function for returning back to previous Quiz set
                            quiz_U_backBtn.configure(
                                command=lambda: quizUpdatePanelSwitcher(quiz_U_backBtn["text"]))

                        # -------------------------------------------------------------------------------------------- Quiz-Update Panel -StyleEnds----

                    # >>

                    # Function which is operated by the Quiz-Topics Panel's Topic-Buttons to initialize another function to create Quiz-Update Panel
                    def quizUpdatePanelInitiator(topicButton_clicked):

                        # Disabling the Topic-Button after clicked, for preventing the function to be called twice
                        topicButton_clicked.configure(state=DISABLED)

                        # Collecting Quiz according to the button clicked
                        if (topicButton_clicked["text"] == "General Knowledge"):

                            # Destroying all the Topic-Buttons created in the Quiz-Topics Panel
                            root.after(450, quiz_T_topicBtn1.destroy)
                            root.after(400, quiz_T_topicBtn2.destroy)
                            root.after(400, quiz_T_topicBtn3.destroy)

                            # Calling the function to create the Quiz-Update Panel
                            root.after(800, lambda: quizUpdatePanel(
                                "General Knowledge", "generalquestions", 10))

                        if (topicButton_clicked["text"] == "Technology"):

                            # Destroying all the Topic-Buttons created in the Quiz-Topics Panel
                            root.after(450, quiz_T_topicBtn2.destroy)
                            root.after(400, quiz_T_topicBtn1.destroy)
                            root.after(400, quiz_T_topicBtn3.destroy)

                            # Calling the function to create the Quiz-Update Panel
                            root.after(800, lambda: quizUpdatePanel(
                                "Technology", "techquestions", 10))

                        if (topicButton_clicked["text"] == "Science"):

                            # Destroying all the Topic-Buttons created in the Quiz-Topics Panel
                            root.after(450, quiz_T_topicBtn3.destroy)
                            root.after(400, quiz_T_topicBtn1.destroy)
                            root.after(400, quiz_T_topicBtn2.destroy)

                            # Calling the function to create the Quiz-Update Panel
                            root.after(800, lambda: quizUpdatePanel(
                                "Science", "sciencequestions", 10))

                        # Destroying the remaining widgets created in the Quiz-Topics Panel
                        root.after(400, quiz_T_backBtn.destroy)
                        root.after(450, quiz_Tlabel.destroy)

                    # ------------------------------------- Quiz-Topics Panel -StyleStarts----------------------------------------------------

                    # Creating a label to show the screen Title
                    quiz_Tlabel = Label(root, text="Choose a TOPIC", font=("Dodge", 20),
                                        foreground="#D1E3DD", background="#1E0905")
                    quiz_Tlabel.place(relx=0.5, rely=0.12, anchor=CENTER)

                    # Styling Quiz-Topics Panel's Buttons
                    quiz_T_topicBtn_style = Style()
                    quiz_T_topicBtn_style.theme_use("default")
                    quiz_T_topicBtn_style.configure("W.TButton", font=("Playball", 15, "bold", "italic"),
                                                    foreground="#0A0908", background="#F6F67C", borderwidth=2, width=20, height=2)
                    # Mouse Hovering style
                    quiz_T_topicBtn_style.map("W.TButton", foreground=[(
                        "active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                    # Creating Topic-Buttons for Quiz-Topics Panel
                    quiz_T_topicBtn1 = Button(root, text="General Knowledge",
                                              style="W.TButton", command=lambda: quizUpdatePanelInitiator(quiz_T_topicBtn1))
                    quiz_T_topicBtn1.place(relx=0.5, rely=0.3, anchor=CENTER)

                    quiz_T_topicBtn2 = Button(root, text="Technology",
                                              style="W.TButton", command=lambda: quizUpdatePanelInitiator(quiz_T_topicBtn2))
                    quiz_T_topicBtn2.place(relx=0.5, rely=0.5, anchor=CENTER)

                    quiz_T_topicBtn3 = Button(root, text="Science",
                                              style="W.TButton", command=lambda: quizUpdatePanelInitiator(quiz_T_topicBtn3))
                    quiz_T_topicBtn3.place(relx=0.5, rely=0.7, anchor=CENTER)

                    # Creating a Back-Button to go back to Admin-Interface
                    # Styling Back-Button
                    quiz_T_backBtn_style = Style()
                    quiz_T_backBtn_style.theme_use("default")
                    quiz_T_backBtn_style.configure("E.TButton", font=("Playball", 10, "italic", "bold"),
                                                   foreground="#0A0908", background="#F6F67C", borderwidth=2, width=10, height=2, focuscolor="none")
                    # Mouse Hovering style
                    quiz_T_backBtn_style.map("E.TButton", foreground=[
                        ("active", "!disabled", "#F0EFF4")], background=[("active", "#DB12AF")])

                    quiz_T_backBtn = Button(root, text="< back",
                                            style="E.TButton", command=lambda: quizTopicsPanelDestroyer())
                    quiz_T_backBtn.place(relx=0.15, rely=0.9, anchor=CENTER)

                    # -------------------------------------------------------------------------------------------- Quiz-Topics Panel -StyleEnds----

                # >>

                # Function which closes the Admin-Interface and redirecting to Leaderboard-Update or Quiz-Topics Panel related to the Update Button clicked
                def updatePanelInitiator(updateButton):

                    # Disabling the clicked Update-Button, for preventing the function to be called twice
                    updateButton.configure(state=DISABLED)

                    # Destroying all the widgets created in the Admin-Interface
                    root.after(500, lambda: logOut_button.destroy())
                    root.after(500, lambda: leaderboard_btn.destroy())
                    root.after(500, lambda: label2.destroy())

                    if (updateButton == leaderboard_UpdateBtn):

                        root.after(500, lambda: quiz_UpdateBtn.destroy())
                        root.after(
                            700, lambda: leaderboard_UpdateBtn.destroy())

                        # Calling the function to create the Leaderboard-Update Panel
                        root.after(1000, lambda: leaderboardUpdatePanel())

                    if (updateButton == quiz_UpdateBtn):

                        root.after(
                            500, lambda: leaderboard_UpdateBtn.destroy())
                        root.after(700, lambda: quiz_UpdateBtn.destroy())

                        # Calling the function to create the Quiz-Topics Panel
                        root.after(1000, lambda: quizTopicsPanel())

                # >>

                # ------------------------------------- Admin-Interface -StyleStarts----------------------------------------------------

                # # Changing the background color for the 2nd time
                window_background.configure(background="#1E0905")

                # Creating a label to show the screen Title
                label2 = Label(root, text="Options", font=("Dodge", 25),
                               foreground="#D1E3DD", background="#1E0905")
                label2.place(relx=0.5, rely=0.2, anchor=CENTER)

                # Creating a label to show the user type
                label3 = Label(root, text="admin", font=("Dodge", 10, "italic"),
                               foreground="#F8FFE5", background="#1E0905")
                label3.place(relx=0.99, rely=0.01, anchor=NE)

                # Creating a label which shows the logged in AdminName
                label31 = Label(root, text=adminID, font=("Dodge", 15, "bold"),
                                foreground="#F5F749", background="#1E0905")
                label31.place(relx=0.995, rely=0.094, anchor=E)

                # Styling Admin-Interface's Update Buttons
                record_button_style = Style()
                record_button_style.theme_use("default")
                record_button_style.configure("W.TButton", font=("Playball", 13, "bold", "italic"),
                                              foreground="#0A0908", background="#F6F67C", borderwidth=2, width=15, height=1, focuscolor="none")
                # Mouse Hovering style
                record_button_style.map("W.TButton", foreground=[(
                    "active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

                # Creating a Leaderboard-Update Button
                leaderboard_UpdateBtn = Button(root, text="Leaderboard\n    Update",
                                               style="W.TButton", command=lambda: updatePanelInitiator(leaderboard_UpdateBtn))
                leaderboard_UpdateBtn.place(relx=0.5, rely=0.4, anchor=CENTER)

                # Creating a Quiz-Update Button
                quiz_UpdateBtn = Button(root, text="Q & A\n    Update",
                                        style="W.TButton", command=lambda: updatePanelInitiator(quiz_UpdateBtn))
                quiz_UpdateBtn.place(relx=0.5, rely=0.6, anchor=CENTER)

                # Styling the Leaderboard-Button
                leaderboard_btn_style = Style(root)
                leaderboard_btn_style.theme_use("default")
                leaderboard_btn_style.configure("L.TButton", font=("Playball", 10, "bold", "italic"),
                                                foreground="#0A0908", background="#F6F67C", borderwidth=2, width=15, height=4, focuscolor="none")
                # Mouse Hovering style
                leaderboard_btn_style.map("L.TButton", foreground=[
                    ("active", "!disabled", "#F0EFF4")], background=[("active", "#DB12AF")])

                # Creating the Leaderboard-Button and placing it on the screen
                leaderboard_btn = Button(
                    root, text="LeaderBoard", style="L.TButton", command=lambda: leaderboard())
                leaderboard_btn.place(relx=0.22, rely=0.05, anchor=NE)

                # Creating a LogOut-Button to return to User-Select Panel
                # Styling LogOut-Button
                logOut_button_style = Style()
                logOut_button_style.theme_use("default")
                logOut_button_style.configure("E.TButton", font=("Playball", 10, "italic", "bold"),
                                              foreground="#0A0908", background="#F6F67C", borderwidth=2, width=10, height=2, focuscolor="none")
                # Mouse Hovering style
                logOut_button_style.map("E.TButton", foreground=[
                    ("active", "!disabled", "#F0EFF4")], background=[("active", "#DB12AF")])

                logOut_button = Button(root, text="log out",
                                       style="E.TButton", command=lambda: logOut())
                logOut_button.place(relx=0.1, rely=0.9, anchor=CENTER)

                # -------------------------------------------------------------------------------------------- Admin-Interface -StyleEnds----

            # >>

            # Function which validates the entered credentials, if credentials are valid diverts the Admin to Admin-Interface
            def credentialValidator():

                # Disabling the SignIn-Button after clicked, for preventing the function to be called twice
                signInBtn.configure(state=DISABLED)

                # Connecting to the App's Database, if not exists creating a new database
                quizzkur_DB = sqlite3.connect("quizz_kur.db")

                # Creating a cursor
                co = quizzkur_DB.cursor()

                # Querying the 'admincredentials' table, to pick the matched AdminName
                co.execute(
                    "SELECT * FROM admincredentials WHERE adminname = '%s'" % adminName.get())
                credentials = co.fetchall()

                # Converting tuples of admin credentials into separate strings
                queryed_name = ""
                for account in credentials:
                    queryed_name += str(account[0])

                queryed_pwd = ""
                for account in credentials:
                    queryed_pwd += str(account[1])

                # Checking if none of the entries are empty
                if (adminName.get() == "" or adminPwd.get() == ""):

                    # Showing a error message
                    messagebox.showerror(
                        "Error: empty field", "Admin name or Password field is empty")

                    # Re-enabling the CreateAccount-Button
                    signInBtn.configure(state=NORMAL)

                # Checking if the entered AdminName matches with the queryed AdminName from database
                elif (adminName.get() == queryed_name):

                    # Checking if the entered AdminPassword matches with the queryed AdminPassword from database
                    if (adminPwd.get() == queryed_pwd):

                        # Destroying all the widgets created on the Admin-Login Panel
                        root.after(1000, lambda: [adminName.destroy(),
                                                  adminPwd.destroy(),
                                                  adminName_label.destroy(),
                                                  adminPwd_label.destroy(),
                                                  back1_button.destroy(),
                                                  label1.destroy(),
                                                  signUp_label.destroy(),
                                                  signInBtn.destroy(),
                                                  signUp_Btn.destroy(),
                                                  ])

                        # Calling the function to create the Admin-Interface
                        root.after(
                            1100, lambda: adminOptionsPanel(queryed_name))

                    else:

                        # Showing a error message when password doesn't match
                        messagebox.showerror(
                            "Error: invalid entry", "password is invalid")

                        # Re-enabling the CreateAccount-Button
                        signInBtn.configure(state=NORMAL)

                else:

                    # Showing a error message when AdminName doesn't exists in database
                    messagebox.showerror(
                        "Error: invalid entry", "Admin name is invalid")

                    # Re-enabling the CreateAccount-Button
                    signInBtn.configure(state=NORMAL)

                # Committing the changes to the database
                quizzkur_DB.commit()

                # Closing the connection with the database
                quizzkur_DB.close()

            # >>

            # Function which creates the Admin-SignUp Panel to create new admin account
            def adminSignUpPanel():

                # Function which closes the Admin-SignUp Window and maximizes the Admin-SignIn Window
                def exit_SignUp():

                    # Showing a confirmation dialog with some message
                    click = messagebox.askquestion("Confirmation: exit",
                                                   "Do you really want to exit, Sign Up?")

                    if (click == "yes"):

                        # Re-enabling the SignUp-Button
                        signUp.after(
                            480, lambda: signUp_Btn.configure(state=NORMAL))

                        # Closing the Admin-SignUp window
                        signUp.after(500, lambda: signUp.destroy())

                        # Maximizing and Showing the Admin-SignIn Window back
                        root.after(800, lambda: root.deiconify())

                # >>

                # Function which is operated by the CreateAccount-Button to create new account with the entered credentials
                def createAccount():

                    # Disabling the CreateAccount-Button after clicked, for preventing the function to be called twice
                    createAccount_Btn.configure(state=DISABLED)

                    # Checking if none of the entries are empty
                    if (admin_n_Name.get() == "" or admin_n_Pwd.get() == "" or admin_rePwd.get() == ""):

                        # Showing a error message
                        messagebox.showerror(
                            "Error: empty field", "Field is empty")

                        # Re-enabling the CreateAccount-Button
                        createAccount_Btn.configure(state=NORMAL)

                    # Checking if both the passwords in the password fields are matching
                    elif (admin_n_Pwd.get() == admin_rePwd.get()):

                        # Connecting to the App's Database, if not exists creating a new database
                        quizzkur_DB = sqlite3.connect("quizz_kur.db")

                        # Creating a cursor
                        co = quizzkur_DB.cursor()

                        # Creating a 'admincredentials' table if not exists to store the new AdminName and Password
                        co.execute("""CREATE TABLE IF NOT EXISTS admincredentials (
                                    adminname TEXT,
                                    password CHAR
                                    )""")

                        # Querying the 'admincredentials' table, to pick the matched AdminName
                        co.execute(
                            "SELECT adminname FROM admincredentials WHERE adminname = '%s'" % admin_n_Name.get())
                        adminID = co.fetchone()

                        # Checking that the 'adminID' variable is not empty
                        if (adminID != None):

                            # Showing a error message
                            messagebox.showerror(
                                "Error: duplicate entry", "username is already occupied, try new")

                            # Resetting all the fields in the SignUp window
                            admin_n_NameVar.set("")
                            admin_n_PwdVar.set("")
                            admin_rePwdVar.set("")

                            # Re-enabling the CreateAccount-Button
                            createAccount_Btn.configure(state=NORMAL)

                        else:

                            # Creating a new Admin with the credentials
                            co.execute("INSERT INTO admincredentials VALUES (:name, :pwd)",
                                       {
                                           "name": admin_n_Name.get(),
                                           "pwd": admin_n_Pwd.get()
                                       })

                            # Creating a label to show the new Adminname
                            created_label0 = Label(
                                signUp, text="' " + str(admin_n_Name.get()) + " '", font=("Dodge", 12, "bold"), foreground="#0A014F", background="#D4B0F9", justify=RIGHT)
                            created_label0.place(
                                relx=0.71, rely=0.89, anchor=E)

                            # Creating a label to show the account created message
                            created_label1 = Label(
                                signUp, text="- has been created", font=("Dodge", 10), foreground="#0A014F", background="#D4B0F9")
                            created_label1.place(
                                relx=0.85, rely=0.89, anchor=CENTER)

                            # Destroying the CreateAccount-Button and the SignUp window
                            signUp.after(
                                1200, lambda: createAccount_Btn.destroy())
                            signUp.after(1800, signUp.destroy)

                            # Re-enabling the SignUp-Button in the SignIn window
                            signUp.after(
                                1750, lambda: signUp_Btn.configure(state=NORMAL))

                            # Showing the SignIn(parent) window again
                            root.after(1800, lambda: root.deiconify())

                        # Committing the changes to the database
                        quizzkur_DB.commit()

                        # Closing the connection with the database
                        quizzkur_DB.close()

                    # Showing a error message when both the passwords doesn't match
                    else:

                        # Showing a error message
                        messagebox.showerror(
                            "Error: invalid entry", "Password doesn't match, retype it correctly")

                        # Resetting the password fields in the SignUp window
                        admin_n_PwdVar.set("")
                        admin_rePwdVar.set("")

                        # Re-enabling the CreateAccount-Button
                        createAccount_Btn.configure(state=NORMAL)

                # >>

                # ------------------------------------- Admin-SignUp Panel -StyleStarts----------------------------------------------------

                # Disabling the SignUp-Button after clicked, for preventing the function to be called twice
                signUp_Btn.configure(state=DISABLED)

                # Hiding the parent window when SignUp window is open
                root.withdraw()

                # Opening a new window for showing SignUp Panel Options
                signUp = Toplevel(root)

                # Giving Title to the SignUp window
                signUp.title("Creating Admin account")

                # Setting the window width, height and position on the user screen
                signUp.geometry("600x400+400+150")

                # Making the new window a non-resizable window as the parent window
                signUp.resizable(0, 0)

                # Assigning the image as an object of PhotoImage class.
                p1 = PhotoImage(file="./Images/icon.png")
                signUp.iconphoto(False, p1)

                # Making the SignUp window focused
                signUp.lift()
                signUp.focus_set()
                signUp.focus_force()
                signUp.grab_set()

                # Overriding the SignUp window close (x) button function with a new function
                signUp.protocol("WM_DELETE_WINDOW", exit_SignUp)

                # Setting the SignUp window background color
                signUp_background = Canvas(
                    signUp, width=3000, height=1500, background="#D4B0F9")
                signUp_background.place(anchor=CENTER)

                # Creating a new label to show the screen Title
                label_1 = Label(signUp, text="Create New account", font=("Dodge", 20),
                                foreground="#0A014F", background="#D4B0F9")
                label_1.place(relx=0.5, rely=0.15, anchor=CENTER)

                # Creating a entry for the new admin name and making it focused
                admin_n_NameVar = StringVar()
                admin_n_Name = Entry(signUp, textvariable=admin_n_NameVar,
                                     font=("Dodge", 15), width=15)
                admin_n_Name.focus_set()
                admin_n_Name.place(relx=0.5, rely=0.33, anchor=CENTER)

                # Creating a entry for the new password
                admin_n_PwdVar = StringVar()
                admin_n_Pwd = Entry(signUp, textvariable=admin_n_PwdVar,
                                    font=("Dodge", 15, "italic"), width=15, show="*")
                admin_n_Pwd.place(relx=0.5, rely=0.46, anchor=CENTER)

                # Creating an entry for the re-type password
                admin_rePwdVar = StringVar()
                admin_rePwd = Entry(signUp, textvariable=admin_rePwdVar,
                                    font=("Dodge", 15, "italic"), width=15, show="*")
                admin_rePwd.place(relx=0.5, rely=0.59, anchor=CENTER)

                # Creating an label for the admin name entry
                admin_n_Namelabel = Label(signUp, text="UserName",
                                          font=("Dodge", 13), foreground="#0A014F", background="#D4B0F9", justify=RIGHT)
                admin_n_Namelabel.place(relx=0.25, rely=0.33, anchor=CENTER)

                # Creating an label for the password entry
                admin_n_Pwdlabel = Label(signUp, text="Password",
                                         font=("Dodge", 13), foreground="#0A014F", background="#D4B0F9", justify=RIGHT)
                admin_n_Pwdlabel.place(relx=0.25, rely=0.46, anchor=CENTER)

                # Creating an label for the re-type password entry
                admin_re_Pwdlabel = Label(signUp, text="re-type Password",
                                          font=("Dodge", 13), foreground="#0A014F", background="#D4B0F9", justify=RIGHT)
                admin_re_Pwdlabel.place(relx=0.2, rely=0.59, anchor=CENTER)

                # Styling CreateAccount-Button
                createAccount_Btn_style = Style(signUp)
                createAccount_Btn_style.theme_use("default")
                createAccount_Btn_style.configure("I.TButton", font=("Playball", 13, "bold", "italic"),
                                                  foreground="#F0EFF4", background="#BF09D5", borderwidth=2, width=9, height=2, focuscolor="none")
                # Mouse Hovering style
                createAccount_Btn_style.map("I.TButton", foreground=[(
                    "active", "!disabled", "#F0EFF4")], background=[("active", "#DB12AF")])

                # Creating a CreateAccount-Button
                createAccount_Btn = Button(
                    signUp, text="Create", style="I.TButton", command=lambda: createAccount())
                createAccount_Btn.place(relx=0.5, rely=0.77, anchor=CENTER)

                # Creating a Back-Button to return to Admin-Login Panel
                # Styling Back-Button
                exit1_button_style = Style(signUp)
                exit1_button_style.theme_use("default")
                exit1_button_style.configure("E.TButton", font=("Playball", 11, "italic", "bold"),
                                             foreground="#F0EFF4", background="#BF09D5", borderwidth=2, width=7, height=2, focuscolor="none")
                # Mouse Hovering style
                exit1_button_style.map("E.TButton", foreground=[("active", "!disabled", "#0A0908")],
                                       background=[("active", "#F5F749")])

                exit1_button = Button(signUp, text="exit",
                                      style="E.TButton", command=lambda: exit_SignUp())
                exit1_button.place(relx=0.15, rely=0.9, anchor=CENTER)

                # -------------------------------------------------------------------------------------------- Admin-SignUp Panel -StyleEnds----

            # >>

            # ------------------------------------- Admin-Login Panel -StyleStarts----------------------------------------------------

            # Disabling the Admin-Button after clicked, for preventing the function to be called twice
            admin.configure(state=DISABLED)

            # Changing the text in the label instead of destroying it
            label1.configure(text="ADMIN", font=("Dodge", 22, "bold"))
            label1.place(relx=0.5, rely=0.18, anchor=CENTER)

            # Destroying the User-Select Buttons created in the User-Select panel
            guest.destroy()
            admin.destroy()

            # Creating a entry for the admin name
            adminNameVar = StringVar()
            adminName = Entry(root, textvariable=adminNameVar,
                              font=("Dodge", 15), width=15)
            adminName.focus_set()
            adminName.place(relx=0.5, rely=0.35, anchor=CENTER)

            # Creating a entry for the password
            adminPwdVar = StringVar()
            adminPwd = Entry(root, textvariable=adminPwdVar,
                             font=("Dodge", 15, "italic"), width=15, show="*")
            adminPwd.place(relx=0.5, rely=0.47, anchor=CENTER)

            # Creating a label for the admin name entry
            adminName_label = Label(root, text="Name",
                                    font=("Dodge", 15), foreground="#0A014F", background="#D4B0F9", justify=RIGHT)
            adminName_label.place(relx=0.25, rely=0.35, anchor=CENTER)

            # Creating a label for the password entry
            adminPwd_label = Label(root, text="Password",
                                   font=("Dodge", 15), foreground="#0A014F", background="#D4B0F9", justify=RIGHT)
            adminPwd_label.place(relx=0.25, rely=0.47, anchor=CENTER)

            # Styling SignIn-Button
            signInBtn_style = Style()
            signInBtn_style.theme_use("default")
            signInBtn_style.configure("I.TButton", font=("Playball", 15, "bold", "italic"),
                                      foreground="#F0EFF4", background="#BF09D5", borderwidth=2, width=7, height=2, focuscolor="none")
            # Mouse Hovering style
            signInBtn_style.map("I.TButton", foreground=[(
                "active", "!disabled", "#F0EFF4")], background=[("active", "#DB12AF")])

            # Creating a SignIn-Button for admin to signIn
            signInBtn = Button(
                root, text="Sign In", style="I.TButton", command=lambda: credentialValidator())
            signInBtn.place(relx=0.5, rely=0.62, anchor=CENTER)

            # Creating a label for the SignUp option
            signUp_label = Label(root, text="don't have an account?",
                                 font=("Dodge", 10), foreground="#0A014F", background="#D4B0F9", justify=CENTER)
            signUp_label.place(relx=0.45, rely=0.75, anchor=CENTER)

            # Styling SignUp-Button
            signUpBtn_style = Style()
            signUpBtn_style.theme_use("default")
            signUpBtn_style.configure("U.TLabel", font=("Playball", 11, "bold", "italic", "underline"),
                                      foreground="#0A014F", background="#D4B0F9", borderwidth=2, width=7, height=2, focuscolor="none")
            # Mouse Hovering style
            signUpBtn_style.map("U.TLabel", foreground=[(
                "active", "!disabled", "#DB12AF")], background=[("active", "#D4B0F9")])

            # Creating a SignUp-Button to create a new account
            signUp_Btn = Button(
                root, text="Sign Up", style="U.TLabel", command=lambda: adminSignUpPanel())
            signUp_Btn.place(relx=0.63, rely=0.75, anchor=CENTER)

            # -------------------------------------------------------------------------------------------- Admin-Login Panel -StyleEnds----

        # >>

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

                    # Function which is operated by the ScoreCard Panel's Exit-Button close Scorecard and also redirect to User-Select panel
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

                            # Function which is operated by the LeaderBoard's Back-Button to close Leaderboard
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
                        quizzkur_DB = sqlite3.connect("quizz_kur.db")

                        # Creating a cursor
                        co = quizzkur_DB.cursor()

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
                        quizzkur_DB.commit()

                        # Closing the connection with the database
                        quizzkur_DB.close()

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
                    quizzkur_DB = sqlite3.connect("quizz_kur.db")

                    # Creating a cursor
                    co = quizzkur_DB.cursor()

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
                    quizzkur_DB.commit()

                    # Closing the connection with the database
                    quizzkur_DB.close()

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
                                               foreground="#F0EFF4", background="#BF09D5", borderwidth=2, width=10, focuscolor="none")
                    # Mouse Hovering style
                    try_button_style.map("W.TButton", foreground=[(
                        "active", "!disabled", "#F0EFF4")], background=[("active", "#DB12AF")])

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
                    ques_Opt_style.map("TRadiobutton", foreground=[
                        ("active", "!disabled", "#0A0908")], background=[("active", "#F5F749")])

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
                                                foreground="#0A0908", background="#F6F67C", borderwidth=2, width=22, height=4, focuscolor="none")

                    # Wrong-Option Style
                    wrongOpt_style = Style(root)
                    wrongOpt_style.theme_use("default")
                    wrongOpt_style.configure("X.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                             foreground="#0A0908", background="#FD151B", borderwidth=2, width=24, height=5, focuscolor="none")

                    # Correct-Option Style
                    correctOpt_style = Style(root)
                    correctOpt_style.theme_use("default")
                    correctOpt_style.configure("C.TRadiobutton", font=("Playball", 14, "bold", "italic"),
                                               foreground="#0A0908", background="#38B000", borderwidth=2, width=22, height=4, focuscolor="none")
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
