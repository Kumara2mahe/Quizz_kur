###
# Quizz-kur

A simple quiz application build in Python by Tkinter. It is basically a multi-choice quiz contains 10 questions based on a topic and valids the answer by changing the background color accordingly and also count the score if correct.

<br>

## Description


- It has a guest interface where the Player can enter their name as they continue to play the quiz.

- A topic selection interface where the Player can choose between three topics to play the quiz based on the selected topic.

- For each question a 15s Countdown Timer is running to show the remaining time to answer the question shown and once the Timer ends it shows the correct answer and also add one point if the user choosen option is correct.

- After the 10th question, Player's name and totalscore is added to the database and also shown as a scorecard.

- Also a Try-More button shown under the totalscore to answer more Quiz questions.

- Try-More works as the above format and returns back to scorecard panel and showing the totalscore in addition of previous score with Try-More scores.

<br>

### App-Preview

<br>

![A sample video of showing how quizz_kur app works and look like.](/Images/preview.gif)

<br>

[# Preview of Previous version](https://raw.githubusercontent.com/Kumara2mahe/Quizz_kur/main/Images/old_preview.gif)

<br>

## Features

<br>

> ### LeaderBoard


- A Leaderboard option is available at the scorecard panel, which is the panel where the Player's total score is displayed after completing the 10 questions in any of the topic.

- Using the Leaderboard button, the Player can view the top5 scored Player in the first to fifth order.

<br>

> ### Try More


- A Try-More button to start the Quiz again with the next set of 10 quizzes collected from the database.

- Quiz rules are same as before and the totalscore displaying is calculated by adding the score got from first 10 set and the second 10 set.

<br>

> ### Admin Interface

<br>

- This interface is not added yet, it is still in the development stage.

<br>

## License
[MIT](https://choosealicense.com/licenses/mit/)