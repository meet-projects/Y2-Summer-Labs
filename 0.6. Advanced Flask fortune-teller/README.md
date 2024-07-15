# Fortune Teller Flask App

## Overview
This project is a simple Flask web app that tells your fortune. When the user opens the app, they will see a home page with a title, a description, and a link that says “Tell me my fortune”. When they click the link, they will go to a page that displays their fortune.

 - <img src="https://raw.githubusercontent.com/meet-projects/Y2-Summer-Labs/master/0.6.%20Advanced%20Flask%20fortune-teller/fortune.jpg" width="600" height="400">

## Instructions

# Advanced Flask Lab: The Fortune Teller

## Overview:
Today, we will be building a web app that tells your fortune. When the user opens the app, they should see a home page with a title, a description, and a link that says “Tell me my fortune”. When they click the link, they will go to a page that displays their fortune.

## Instructions:

### Step 1:
Add a route `/home` so that when the user tries to access `127.0.0.1:5000/home` the template `home.html` is displayed.

### Step 2:
Complete the template `home.html`. For now, make it fairly simple with a title, description, and link to tell your fortune. The link should take you to the route `fortune`.

### Step 3:
Try to run your app! Check that the home page displays as you intended. Obviously, the Fortune link won’t work yet. Debug any problems that may arise.

### Step 4:
Add a route `/fortune` that does the following:
- Create a list with at least 10 possible fortunes (each fortune should be a string).
- Choose a random fortune from this list (Hint: start by choosing a random int…remember the Python review!).
- Display the template `fortune.html`, passing it the chosen fortune.

### Step 5:
Complete the template `fortune.html`. It should say something like “Your fortune is:” and then display the random fortune that was chosen and passed to the template. (e.g. “Your fortune is: Abdalla is going to chase you around IASA”).

### Step 6:
Try to run your app again! Check that everything works as intended. Debug any problems that may arise.

If you finish up to here before the end of the session, great job! You can do one or both of the following options as a bonus:

### Option 1:
Use HTML and/or CSS to beautify your app! You can add images, colors, styles, borders, backgrounds, centering… whatever inspires you.

### Option 2:
Try some of the challenges below to add more features to your fortune telling app!

### Option 3:
Come up with your own idea for an extension to your fortune teller and implement it!

## Bonuses/Extensions:

### Bonus A: Indecisive Fortune Teller

#### Step 1:
Add a route `/indecisive` that does the following:
- Create a list containing the same fortunes that you made in route `/fortune`.
- Use a loop and the `random` library to select 3 random  fortunes from the list and save them inside a new list called `indesisive_fortunes`, then pass the list through the `indecisive` route .
- Display a template `indecisive.html`, passing it the list of three random fortunes.

#### Step 2:
- Create a template `indecisive.html` in your templates folder. This page should display text along the lines of “I’m not sure what will happen to you, but it will be one of the following three things:” 
- loop through the list you passed in `indecisive` route and show the three random options.You can choose exactly what to say and how to display it!

#### Step 3:
Add a link to the `/indecisive` route on the home page so that the user can choose if they’d rather ask a decisive or indecisive program for their fate.

#### Step 4:
Run and test your app and fix any errors that occur.

**EXTRA BONUS:** Ensure that the three chosen fortunes are always distinct (i.e. there are no repeats).

### Bonus B: Magic 8 Ball(Never heard of a magic 8 ball? [Read more about it here](https://en.wikipedia.org/wiki/Magic_8_Ball))

#### Step 1:
Add a route `/magic` that displays an HTML template `magic.html`.

#### Step 2:
Create a template `magic.html` in the template folder that displays the text “Ask a yes or no question”, a text input HTML tag that allows the user to type a yes or no question, and a button whose `onClick` method is a link to a route `/response`.

#### Step 3:
Add a link to the `/magic` route on the home page.

#### Step 4:
Run your app and test that everything looks good so far except for the actual button click, which shouldn’t work yet because you haven’t yet defined the route `/response`.

#### Step 5:
Add a route `/response` that does the following:
- Choose a random integer between 1 and 3.
- Display a template `response.html`, passing the integer you chose.

#### Step 6:
Create a template `response.html`. This page should display just one line of text, determined as follows:
- If the integer is 1, it displays "yes".
- If the integer is 2, it displays "no".
- If the integer is 3, it displays whatever silly answer you want. For example, “only on Tuesdays” or “I think so, but one can never be sure” or “why are you asking me?”...use your creativity!

#### Step 7:
Run and test your app and fix any errors that occur.

