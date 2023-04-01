# Hotel-Checkin-Sim

Introduction:

This code is the source code for a simple file managing, hotel checkin software written in python. The hotel checkin is just a scenario, the code is just meant to manage a couple of files. It is a console-based application, so it runs in the python prompt. Because of this, in order to run the application you would need to have python installed on your machine. Other than that, it also uses the csv and datetime modules.  


Summary:

The hotel checkin software allows users to enter a name and check in and out of this fictional Hotel. The activity is logged in a text and csv file, more on that later. 


Limitations:

There is no real hotel. It also only uses text and csv. 


Overview program:

The file handling project simulates checking in into a hotel by inputting what you want to do (check in or out) entering your name and then the program writes
"{name} checked in/out" in the text file, in the csv it writes the date, time and action like: 31-03-2023,19:46:40,Check-In. After entering your name it also prints the
current date and time. It also has checks in place so you can only check in if you're not already checked in and checkout only if you are checked in. 


Structure:

The code has one class 'file_handler', which has methods to do all the file handling. There is also a 'Main()' function that instantiates the class, takes input for the main menu and calls the methods of the class. 

minimum python version required to run code: unknown, code made and tested in python 3.9
