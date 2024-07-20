# Quoteboard Web App


Today, we are building a web app that stores and displays quotes that a user inputs.
it's not just any quotes, it's Quotes from your favorite staff members!!


## Project Setup


1. **Create Project Folder**


   Inside the `Y2 SUMMER LABS` directory, create a folder named `Authentication-Lab`.


2. **Project Structure**


   In your project folder, create the following directories and files:
   - `static`: Folder for CSS files.
   - `templates`: Folder for HTML template files.


   - `SignUp.html`: Template that contains a form where users can sign up.
  - `SignIn.html`: Template that contains a form where users can sign In.
   - `home.html`: Template for the home page where users can submit quotes.
   - `display.html`: Template for displaying the submitted quotes.
   - `thanks.html`: Template for thanking users after successfully submitting a quote.
   - `error.html`: Template for handling errors.
   - `app.py`: Main Python file for the Flask application.


## Part 1: Initialize Your App


1. **Import Packages and Libraries**


   Import all the relevant packages and libraries in `app.py`.


2. **Initialize Your App**

- Initialize your Flask app and specify the `templates` and `static` folders.
- Add the secret key configuration:
`app.config['SECRET_KEY'] = 'super-secret-key'`.

3. Initialize firebase 
`firebase = pyrebase.initialize_app(Config)`
`auth = firebase.auth()`

4. **Add Routes**

-  Create routes for each HTML page that redirects to that page.


## Part 2:SignUp 

1. **Add Form to `SignUp.html`**

- Create a form in `SignUp.html` to take in the user’s email and password.


2. **in the signup route:**

- If the method is 'POST' take the inputs and create a user with email & password.
- Don't forget to store the user in the login session and to use try and except.
- Redirect the route to the home page.
- For Authentication you need a valid email and a 6 character long password.




## Part 3:SignIn 

1. **Add Form to `SignIn.html`**

  - Create a form in `SignIn.html` to take in the user’s email and password.


2. **In the signin route:**

- If the method is 'POST' take the inputs and signin the user with email & password.
- Don't forget to store the user in the login session and to use try and except.
- Redirect the route to the home page.

- Show the user's name in the route and in the display.html.
- **In home.html:**
- Add a button called signout.
- create a new route called signout:
- The route signs out the user and redirects him to the signin page.


3. **Link to Thanks Route**


   Add a link in `thanks.html` to redirect back to the home page.


4. **Handle Errors**


   Use `try` and `except` to handle errors with storing the form responses in the login session. If there is an error, users should be redirected to `error.html`.


## Part 3: Display Page


1. **Fill in `display.html`**


   Create a template in `display.html` to display a quote, author, and age.


2. **Pass Information to `display.html`**


   Pass information from `login_session` to `display.html`.


3. **Check Display Page**


   Ensure that the display page correctly shows the quote that a user enters.



## REALTIME DATABASE
1. Setting up Realtime Database in `Firebase`:
    1. Go to your console and choose your project.
    2. Go to Realtime Database and create a database.
    3. Go to rules and change false to true.
    4. Make sure to copy the database's link.

2. Setting up Realtime Database in `app.py`:
    1. In the config dictionary add databaseURL as a key and the link you copied as the value.
    2. Intialize the 'db' using the firebase object.


3. Add in `signup.html` 3 more inputs:(you already have the email and passoword)
    1. `full_name`
    2. `username`
    3. `bio` - It should take a maximum of 280 letters.


4. When the user signs up:
    - Create a dictionary called user that contains the inputs as keys and values.
    - Add the user to the `database` through the child `Users` adding him through his uid (retrieve it through login_session).


5. Create a form in `home.html` to add a Quote from Staff members to the database:
    - The form should contain:
        - `Title`.
        - `Text`- It should take a maximum of 280 letters.
        - `Image link` - This should be optional (We'll set this feature up later)


6. When the user submits a Quote:
    - Create a dictionary called `Quote` that contains the inputs as keys and values.
    - In the dictionary add a key named `uid` and the value as the uid of the user that wrote the quote.
    - Add the quote using the child `Quotes` to the `database` with a random key.

        
7. Create an html page called Quotes.html:
    - in this html page display all the quotes that were written:
        - Go to the child `Quotes` and use get().val()
        
