# Flask Routing Lab: Photo Gallery

**Overview:**
We’ll build a virtual photo gallery that a user can “walk” through and see cool photos!

## Instructions

### Step 1: 
Create a new folder for your project and create a new file named `app.py` in your project folder.

### Step 2:
Copy-paste the following code into `app.py`:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    
if __name__ == '__main__':
    app.run(debug=True)
```

### Step 3:
Edit the `home()` function to return a string that defines an .html page. The page should have a heading, as well as text welcoming the user to a photo gallery containing three types of photos: food, pets, and outer space. 

Note: to write a string across multiple lines in python, use triple quotes, for example:

	mystring=’’’this string
 
			is defined on two lines’’’

### Step 4:
Edit the html string returned by the `home()` function so that at the botton of the page is a hyperlink that takes the user to a route called `/food1`. The text of the hyperlink should be something like “go to the first food photo”.


### Step 5: 
1. Run the Flask application: navigate to the folder you created, and type
   ```bash
   python3 app.py
   ```
2. Open your browser and go to `http://127.0.0.1:5000/` to see if your page appears. The hyperlink won’t work (yet). Fix any errors that come up.

### Step 6: 
In `app.py`, define a new route called  `/food1` and immediately below it a method that returns a .html page displaying a photo of some food that you like (you can also add a description if you want), and two hyperlinks: one going back to the main entrance (i.e. the home page), and one going on to the next food photo. The main entrance hyperlink should take the user to the route `/home` and the next photo link should take the user to the route `/food2`

### Step 7: 
In your browser, refresh the page `127.0.0.1:5000/home` and try to click on the link. If all goes well, your first food photo page should appear! Test the link taking you back to the home page. Fix any errors that may come up.

### Step 8: 
Repeat the basics of steps 5 and 6 to create a gallery with 10 rooms: the main entrance, three food photos, three pet photos, and three outer space photos. You should choose these photos yourself! Each room should have its own route that returns an html page. Organize your gallery so that the rooms are linked in the following manner:

<img width="478" alt="Screen Shot 2024-07-16 at 3 23 28 AM" src="https://github.com/user-attachments/assets/423ea1c3-86b4-4436-91ad-d4115a55d427">

That means you will have to eventually change the html page returned by the `/home` route to contain 4 links: to the rooms Food 1, Food 3, Space 1, and Pet 2. If you have any questions about what you are supposed to be doing, ask an instructor or TA!

## Bonus
### Step 1:
Give each photo room a name and dispay the name at the top of the page

### Step 2:
In the main entrance (i.e. the home page), add an option to teleport to any of the photo rooms. You can choose how you want to implement this: it can be a text input from the user (and display an error message if they enter an invalid room name), a radio button, a drop-down menu, ... whatever you want! The only requirement is that it take the user to whichever photo room they choose to go to.
