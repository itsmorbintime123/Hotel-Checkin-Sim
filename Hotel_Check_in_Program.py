#WARNING:

"""Keep getting an 'inconsistent line endings' popup whenever the code is tested, checked the files in visual studio* with the setting that shows spaces and line endings, saw no
inconsistency, checked the files in their respective programs (notepad for the text, excel for the csv) and again did not see any inconsistency. Didn't change the code at
all and it just started popping up. Only tested the code on windows, tried changing the line endings by clicking ok when the popup appears and it keeps reappearing whenever the
code is run, tested the code in thonny, which i don't think even has that popup functionality and it worked normally, deleting and reopening the file and restarting visual studio
and even my laptop didn't work, tried creating a new solution, didn't work. It may be worth noting that the program still works properly and the files are being written to as
they're supposed to, i just keep getting that popup.

*Visual Studio 2022"""



import csv
from datetime import datetime


class file_handler:

    def check_in_text(self):
    
        with open('hotel-activity.txt', 'a+') as text_file:
        
            text_file.seek(0)
            contents = text_file.read()

            name = input('Enter your name: ')

            checkin_datetime = datetime.now() #DT
            checkin_datetime_string = checkin_datetime.strftime('%d-%m-%Y %H:%M:%S') #DT
            checkin_date_string = checkin_datetime.strftime('%d-%m-%Y') #DT
            checkin_time_string = checkin_datetime.strftime('%H:%M:%S') #DT
            print(checkin_datetime_string) #DT

            checked_in_string  = f'{name} checked in'
            checked_out_string  = f'{name} checked out'

            check_in_successful = False

            if contents.count(checked_in_string) > contents.count(checked_out_string):
                print('already checked in')

            else:
                text_file.seek(0, 2)
                text_file.write(f'{name} checked in\n')
                check_in_successful = True
                print('you are checked in')

            return check_in_successful, checkin_date_string, checkin_time_string


    def check_out_text(self):
        
        with open('hotel-activity.txt', 'a+') as text_file:
        
            text_file.seek(0)
            contents = text_file.read()

            name = input('Enter your name: ')

            checkout_datetime = datetime.now() #DT
            checkout_datetime_string = checkout_datetime.strftime('%d-%m-%Y %H:%M:%S') #DT
            checkout_date_string = checkout_datetime.strftime('%d-%m-%Y') #DT
            checkout_time_string = checkout_datetime.strftime('%H:%M:%S') #DT
            print(checkout_datetime_string) #DT

            checked_in_string  = f'{name} checked in'
            checked_out_string  = f'{name} checked out'

            check_out_successful = False

            if contents.count(checked_in_string) > contents.count(checked_out_string):
                text_file.seek(0, 2)
                text_file.write(f'{name} checked out\n')
                check_out_successful = True
                print('you are checked out')

            else:
                print('not checked in')

            return check_out_successful, checkout_date_string, checkout_time_string


    def check_in_csv(self, check_in_succesful, checkin_date_string, checkin_time_string):

        with open('system-activity.csv', 'a+') as csv_file:
            writer = csv.writer(csv_file, delimiter = ',')

            if check_in_succesful:
                writer.writerow([checkin_date_string, checkin_time_string, 'Check-In'])


    def check_out_csv(self, check_out_succesful, checkout_date_string, checkout_time_string):

        with open('system-activity.csv', 'a+') as csv_file:
            writer = csv.writer(csv_file, delimiter = ',')

            if check_out_succesful:
                writer.writerow([checkout_date_string, checkout_time_string, 'Check-Out'])



"""the file_handler class is just to group the different functions together, it is not meant for creation of multiple instances (which is why there is no constructor), the
check_in_text method creates or opens the text file, reads the file, takes the name of the user as input, determines the date and time of checkin, splits the datetime string
into two strings, one for the date and one for the time, prints the datetime string after the name has been entered, checks if the user is already checked in and if not writes
an f-string to the file, otherwise prints a message, the check_out_text method does the exact same, just for the checkout, with the only notable difference being that it performs
it's action of checking the user out if the user is checked in (as opposed to not checked in, like the check_in_text method) both text-file-related methods also define a boolean
of which the value is based on whether the checkin and checkout were successful, this boolean is used by the csv methods to determine whether or not they should perform their
respective actions, the date and time strings are also used by the csv methods, the job of the csv methods is to first open or create the file, check whether the action (either
the checkin for the check_in_csv method or the checkout for the check_out_csv) were succesful and if so, write a line to the csv with the date, time and action (either 'Check-In'
or 'Check-Out')"""






def main():

    file_handling_object = file_handler()

    while True:
        in_or_out = input('Welcome to the Python Hotel Checkin, what would you like to do?\n[1]Check-in\n[2]Check-out\n')

        if in_or_out == '1':
            check_in_succesful, checkin_date_string, checkin_time_string = file_handling_object.check_in_text()
            file_handling_object.check_in_csv(check_in_succesful, checkin_date_string, checkin_time_string)

        elif in_or_out == '2':
            check_out_succesful, checkout_date_string, checkout_time_string = file_handling_object.check_out_text()
            file_handling_object.check_out_csv(check_out_succesful, checkout_date_string, checkout_time_string)

        else:
            print('invalid input')

if __name__ == "__main__":
    main()


"""The Main function prompts the user for input and based on that input defines a group of three variables returned by a method of the file_handler class to be able to use them
and calls two of the methods of the class (and just like with the variables, which ones depends on the user input), there are two options of user input: check-in or check-out"""
