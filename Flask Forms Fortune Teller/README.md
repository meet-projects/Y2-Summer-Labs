# Flask Forms: A Fancier Fortune Teller

## Overview
We’ll improve our fortune telling app by taking into account user input to determine the fortune.

## Instructions

### Step 1: Duplicate the Fortune Teller Lab
Duplicate the fortune teller lab from the last session.

### Step 2: Add a Form to `home.html`
In the new version, add a form to `home.html` with a text input box that asks the user to type their birth month and a button that reads “tell my fortune”. The form should send a POST request to the `/home` route.

### Step 3: Modify the `/home` Route Function
Modify the function called by the `/home` route to do the following:
- If the request is a GET request, it should render `home.html`.
- If the request is a POST request, it should retrieve the user input of birth month from the text box and call the method of `/fortune` route, passing it the user’s birth month (hint: this is where we need `url_for`).

### Step 4: Change the `/fortune` Route
Change the `/fortune` route so that instead of choosing a random integer to index into the list of fortunes, it uses the number of letters in the birth month.

### Step 5: Handle Long Input
Consider what happens if someone decides to input ‘the_very_best_month_of_the_year_to_be_born_in’ and your list only has 10 fortunes in it. Come up with a solution that doesn’t involve your program breaking. Some options:
- Check to see if the number of letters in the birth month is longer than the length of the list. If it is, return some fixed fortune, or
- Use the number of letters in the birth month mod the length of the list as your index, or
- Come up with your own idea!

### Step 6: Run and Test Your App
Try to run your app! Check that the home page displays as you intended. Obviously, the fortune link won’t work yet. Debug any problems that may arise.

## Bonuses/Extensions

### Bonus A: Why Use Redirect?
1. Copy and paste `app.py` into a separate file and save it.
2. Copy and paste the logic for choosing which fortune to display from the fortune route to the home route after the user input for birth month is retrieved from the form.
3. Remove the redirect and instead return `render_template` for the `fortune.html` template (passing in the chosen fortune).
4. Run and test your app and fix any errors that occur.
5. Go to the home page of your app, enter a month, and submit the form. Then, refresh the page in your browser. What happens? Can you explain why this happens?

#### Extra Bonus: Ensure Unique Fortunes
Ensure that the three chosen fortunes are always distinct (i.e. there are no repeats).

### Bonus B: All on One Page
Change the app so that instead of going to a separate page when the user clicks ‘tell my fortune’, the fortune appears below the form. Try to figure out all the steps to make this happen on your own, but instructors and TAs are here for you if you want some hints on how to accomplish this!

### Bonus C: More Sophisticated Fortune Telling
Add more HTML elements to the form to gather information about the user (name? Zodiac sign? Favorite color?) and invent a way to determine which fortune to select based on all the information. Be creative! Implement whatever ideas you come up with.
