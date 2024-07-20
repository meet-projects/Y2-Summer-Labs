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
   - `signup.html`: Template that contains a form where users can sign up.
   - `signin.html`: Template that contains a form where users can sign In.
   - `home.html`: Template for the home page where users can submit quotes.
   - `display.html`: Template for displaying the submitted quotes.
   - `thanks.html`: Template to thank the user for submiting the quote
   - `app.py`: Main Python file for the Flask application.


## Part 1: Initialize Your App


1. **Import Packages and Libraries**


   Import all the relevant packages and libraries in `app.py` and import `session`


2. **Initialize Your App**

- Initialize your Flask app and specify the `templates` and `static` folders.
- Add the secret key configuration:
`app.config['SECRET_KEY'] = 'super-secret-key'`.

3. Initialize firebase 
`firebase = pyrebase.initialize_app(Config)`
`auth = firebase.auth()`

4. **Add Routes**

-  Create routes  `/signin`, `/home`, `/thanks` and `/display` that each render the corresponding html page.
-  Create the main route (`/`) that renders the `signup.html` page


## Part 2: Sign Up 

1. **Add Form to `signup.html`**

- Create a form in `signup.html` to take in the user’s email and password.
- Create a link with the `<a>` tag below the form that says "Already have an account? Sign in here." and take the user to the `/signin` route


2. **in the signup route:**

- If the method is 'POST' take the inputs and create a user with email & password.
- Store the user in the `session` and also add a key `"quotes"` to the `session` whose value is an empty list.
- When the user submits, send the user to the `/home` route.


## Part 3: Sign In 

1. **Add Form to `SignIn.html`**

  - Create a form in `SignIn.html` to take in the user’s email and password.


2. **In the signin route:**

- If the method is 'POST' take the inputs and signin the user with email & password.
- Store the user in the `session` and also add a key `"quotes"` to the `session` whose value is an empty list.
- When the user submits, send the user to the `/home` route.

3. **In home.html:**
- Add a button called signout.
- create a new route called signout:
- The route signs out the user and redirects him to the signin page.

STOP HERE AND TEST EVERYTHING TO MAKE SURE IT WORKS

## Part 4: Adding Quotes 

1. **In home.html:**
- create a form with a single text box and a message for the user to type in their quote. The form should send a POST request to the route `/home`.

2. **In the home route:**
- If the method is 'POST' take the input from the form and add it to the `quotes` list in the `session`
- Once the quote is added redirect the user to the `/thanks` route.
  
3. **In thanks.html**
- Thank the user for submiting a quote and offer two links: one back to the `/home` route to submit another quote and one to the `/display` route to view all the quotes submitted so far.

## Part 5: Displaying Quotes 

1. **In the display route:**
- Get the list of quotes from the `session` and pass it to the `display.html` page using `render_template`.

2. **In display,html:**
- Loop through the list using jinja (see the Advanced Flask slides if you forgot how to do this) and display the quotes to the user
- Add a link to take you back to the `/home` route.
