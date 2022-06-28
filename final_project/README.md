# YOUR PROJECT TITLE
#### Video Demo:  <https://youtu.be/yGv8-iQJbU8>
#### Description:
This is a python command-line based contact application that enables you to store, search, delete, list and create contacts. This application uses python for operations and SQL database for storage.

#### def main():

This is the main function, when running it asks for input of option from user and call functions according to the options provided by user. This program continues to run until the user inputs 'exit' or 'quit' case insensitively.

#### def search_contacts(name):

This function takes an argument which is a name of a contact to be searched, the function searches the database by running SQL queries and prints all matching contacts.

#### def list_names():

This function queries the database for all contacts, it then stores all the results for cleaning and formating before prints all existing contacts.

#### def new_contact(name, number, email):

This function takes three arguements(name, number, email) provided by user, then it inputs the data into the satabase using SQL queries while checking for errors and wrong input.

#### def delete_contact(name):

This function only takes name as arguement, checks the database to see if contact exists and then deletes it if it does.

This is my web application, It handles all the back end operations and renders the necessary html pages, also it is responsible for accessing and
entering data into the database. Also it checks for the methods employed by the page requests and reacts to them, respectively and redirects to new pages
necessary.

This route renders search.html if requested with GET but takes input from the search page if requested with POST. When requested with post, the route takes the name of the contact the user must have inputed and passas it on into a function that will query the database and return the countacts that matches the users input.

This route displays the new contact page if requested via GET, But on the other hand if requested via POST it collects all data(name, number and email) inputed by user and tries to input it into the database by running SQL queries but redirects to error page if any error is encountered.
