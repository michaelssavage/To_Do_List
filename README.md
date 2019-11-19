# Comparing Imperative and Object-Oriented Programming

While Object-Oriented programming relies on models, imperative programming tends to rely on functions. In imperative, we focus on how a problem should be solved by having a good understanding of these functions. In my implementation of a to-do list I chose to write my OOP program in Python and my imperative approach in Java.

The Java Language is based on Object-Oriented Programming Paradigm. I thought it would be more beneficial for me if I tried to write it imperatively and avoid objects. I used one file to create the Java to-do list. It includes one class, Todo.java, and it reads and writes to a file instead of using a list of any sort. I used two global variables and kept everything public so that everything was visible in the program.

In comparison, my Python Language implementation uses a class for Task, Event, and Queue. The Queue is a Linked-List that helps to organise the Events and Tasks. Each object has it's own file so that the main file works well with abstraction. The Object-Oriented approach for a to-do list is more suitable because we perform few operations on lots of different variants of Tasks and Events which have common behavior.

For testing purposes, each program interprets user input into commands. The Python program has a test.py that does not use input but allows the user to see an intended scenario. 
