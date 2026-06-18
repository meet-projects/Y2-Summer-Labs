# Quoteboard Web App

Today, we are building a web app that stores and displays quotes that a user inputs.

## Project Setup

1. **Create Project Folder**

   Inside the `Y2 SUMMER LABS` directory, create a folder named `Login-Session-Lab`.

2. **Project Structure**

   In your project folder, create the following directories and files:
   - `static/`: Folder for CSS files.
   - `templates/`: Folder for HTML template files.
   - `home.html`: Template for the home page where users can submit quotes.
   - `display.html`: Template for displaying the submitted quotes.
   - `thanks.html`: Template for thanking users after successfully submitting a quote.
   - `error.html`: Template for handling errors.
   - `app.py`: Main Python file for the Flask application.

## Part 1: Initialize Your App

1. **Import Packages and Libraries**

   Import all the relevant packages and libraries in `app.py`.

2. **Initialize Your App**

   Initialize your Flask app and specify the `templates` and `static` folders. Add the secret key configuration.

3. **Add Routes**

4.  Create routes for each HTML page that redirects to that specific page.
**remember to add `app.config['SECRET_KEY'] = 'super-secret-key'`.**
**refer back to the slides if you need a reminder**


## Part 2: Home Page

1. **Add Form to `home.html`**

   Create a form in `home.html` to take in a quote, the quote's author, and the author's age.

2. **Store Form Information**

   When the form is submitted, store the form's information in `login_session`, example: `login_session['age'] = age`. Redirect the form to `thanks.html`.

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

## Bonus

1. **Add Button for Additional Quotes**

   Add a button to the display page to take in additional quotes.

2. **Modify `display.html` to Loop Through Quotes**

   Modify the `display.html` template to loop through a list of submitted quotes and display all of them.

3. **CSS Styling**

   Use CSS to make your quoteboard look like an actual whiteboard. Add your styles in a CSS file inside the `static/` folder and link it in your HTML templates.

Happy coding!
