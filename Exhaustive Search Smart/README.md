# Prisoners Dilemma, Exhaustive Search w/ Basic Neural Network
### School AI Project 
---
This is an Exhaustive Search Neural Network I wrote to solve or at least try to solve the prisoner's dilemma. </br>
While I call it a neural network, it really isn't since it only has 1 level of nodes and isn't really impressive.</br>
<br>
<br>
<br>
The program works by first running a number of iterations just testing the waters (can be changed in the config.json file)
before then going through the motions of looking at past habits and predicting the moves its opponent will do next.
<br>
<br>
The only inputs it uses is a finite amount of memory which stores the previous number of moves (defined in config.json) 
and all previous patterns. It will then exhaustively go through every possible combination of moves it can possibly do and
will then calculate a score based on previous patterns the opponent has made.
<br>
<br>
It will then output its next move.