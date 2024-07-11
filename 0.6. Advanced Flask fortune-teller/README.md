# Fortune Teller Flask App

## Overview
This project is a simple Flask web app that tells your fortune. When the user opens the app, they will see a home page with a title, a description, and a link that says “Tell me my fortune”. When they click the link, they will go to a page that displays their fortune.

 - <img src="https://raw.githubusercontent.com/meet-projects/Y2-Summer-Labs/master/0.6.%20Advanced%20Flask%20fortune-teller/fortune.jpg" width="600" height="400">

## Instructions

### **Step 1: Initialize the Flask App and Create the `/home` Route**
1. Create a new file called `app.py`:
    ```python
    from flask import Flask, render_template
    import random

    app = Flask(__name__)

    # Route for the home page
    @app.route('/home')
    def home():
        return render_template('home.html')

    # Run the Flask app
    if __name__ == '__main__':
        app.run(debug=True)
    ```

### **Step 2: Create `home.html`**
1. Create a folder named `templates`.
2. Inside the `templates` folder, create a file named `home.html`:
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Fortune Teller</title>
    </head>
    <body>
        <h1>Welcome to the Fortune Teller</h1>
        <p>Click the link below to get your fortune!</p>
        <a href="/fortune">Tell me my fortune</a>
        <br>
        <a href="/indecisive">Indecisive Fortune Teller</a>
        <br>
        <a href="/magic">Magic 8 Ball</a>
    </body>
    </html>
    ```

### **Step 3: Create the `/fortune` Route and Template**
1. Add a route `/fortune` in `app.py`:
    ```python
    @app.route('/fortune')
    def fortune():
        fortunes = [
            "You will have a great day!",
            "A surprise is waiting for you.",
            "Today is your lucky day!",
            "Happiness will find you.",
            "Be cautious today.",
            "You will meet someone special.",
            "An opportunity will arise.",
            "Expect the unexpected.",
            "Good news is coming your way.",
            "You will achieve your goals."
        ]
        chosen_fortune = random.choice(fortunes)
        return render_template('fortune.html', fortune=chosen_fortune)
    ```

2. Create a file named `fortune.html` in the `templates` folder:
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Your Fortune</title>
    </head>
    <body>
        <h1>Your fortune is:</h1>
        <p>{{ fortune }}</p>
    </body>
    </html>
    ```

### **Step 4: Create the `/indecisive` Route and Template**
1. Add a route `/indecisive` in `app.py`:
    ```python
    @app.route('/indecisive')
    def indecisive():
        fortunes = [
            "You will have a great day!",
            "A surprise is waiting for you.",
            "Today is your lucky day!",
            "Happiness will find you.",
            "Be cautious today.",
            "You will meet someone special.",
            "An opportunity will arise.",
            "Expect the unexpected.",
            "Good news is coming your way.",
            "You will achieve your goals."
        ]
        chosen_fortunes = random.sample(fortunes, 3)
        return render_template('indecisive.html', fortunes=chosen_fortunes)
    ```

2. Create a file named `indecisive.html` in the `templates` folder:
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Indecisive Fortune</title>
    </head>
    <body>
        <h1>I'm not sure what will happen to you, but it will be one of the following three things:</h1>
        <ul>
            {% for fortune in fortunes %}
            <li>{{ fortune }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    ```

### **Step 5: Create the `/magic` and `/response` Routes and Templates**
1. Add routes `/magic` and `/response` in `app.py`:
    ```python
    @app.route('/magic')
    def magic():
        return render_template('magic.html')

    @app.route('/response')
    def response():
        responses = [
            "Yes",
            "No",
            "Maybe",
            "Only on Tuesdays",
            "I think so, but one can never be sure",
            "Why are you asking me?"
        ]
        chosen_response = random.choice(responses)
        return render_template('response.html', response=chosen_response)
    ```

2. Create a file named `magic.html` in the `templates` folder:
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Magic 8 Ball</title>
    </head>
    <body>
        <h1>Ask a yes or no question:</h1>
        <form action="/response">
            <input type="text" name="question" placeholder="Type your question here">
            <button type="submit">Ask</button>
        </form>
    </body>
    </html>
    ```

3. Create a file named `response.html` in the `templates` folder:
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Magic 8 Ball Response</title>
    </head>
    <body>
        <h1>Your answer is:</h1>
        <p>{{ response }}</p>
    </body>
    </html>
    ```

### **Step 6: Run the App and Test**
1. Run your Flask app:
    ```bash
    python3 app.py
    ```

2. Open your browser and go to `http://127.0.0.1:5000/home` to see the home page. Test the links to ensure they navigate correctly and display the fortunes and magic 8 ball responses as expected.

### Bonus 
#### 1 Indecisive Fortune Teller:
- Ensure the `/indecisive` route chooses three distinct fortunes from the list.
- Modify the home page to include a link to the `/indecisive` route.

#### 2 Magic 8 Ball:
-  Add the `/magic` route to display a form where users can ask a yes or no question.
-  Add the `/response` route to display a random answer from a predefined list of responses.
-  Modify the home page to include a link to the `/magic` route.

### 3 styling:
- Use HTML and CSS to beautify your app.
- Add images, colors, styles, borders, backgrounds, centering, etc.

Great job on completing the Fortune Teller app! If you finish early, try implementing the bonus extensions or come up with your own ideas to enhance the app further.
