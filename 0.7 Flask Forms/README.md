# Using Forms with Flask - Facebook Lab

## Objective: 
In this lab, you will learn about taking and processing information, given by a user via HTML forms!









> Before we start, make sure to fork the repo and clone the code.


## Instructions:

As you can see, in the code we provided, you have a ready `app.py` (Flask app), `login.html`, `home.html` and `home.html files, these will be the files you will edit this lab. Explore the project files to have a better understanding of what's going on, even try to **run** the app!  
It should look something like this:  
<img src="https://github.com/meet-projects/Y2-Seminar2020-Labs/blob/master/Day%202%2C%20Session%202%2C%20Flask%20Forms/facebook-login.png" width=450>

  
First things first, in the top of `app.py`, you have some variables configured. Feel free to edit them according to your own preferences. The variables looks something like this:
```python
username = "llo2ay"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]
```
  

1. Editing the `login` *route* in `app.py`, and the **login form** in `login.html`. It should:
    - Take input in the form, and process it in `login` *route*.
    - You should check if it's a `POST` request:
        - If it is, check for credentials. (if the username and password from `login.html` match the `username` and `password` variables)
        - If they match, you should proceed to `home.html`.
        - Make sure to update the `<form>` attributes (method and action) accordingly.
    - If it's a `GET` request. you should stay on the `login.html` page to try again.
        - Remember: `GET` is the default method.
        
    

2. Create/Define a new *route* in `app.py` and call it `home`.
    - You should link `home` *route* to `home.html`.
    - Make sure to replace `render_template('home.html')` with `redirect(url_for('home'))` in the `login` *route*.
    - **Checkpoint!** Test out your website, make sure it works properly.


    
3. Using `facebook_friends` list, **pass it** to `home.html` using the `home` function/route in `app.py`.
    - Replace the current "friends" in the page with a `for loop` that loops through this list.
    - Costumize/Edit `facebook_friends` list and add your classmates/family members.
    - Run your app. Show your friends/family members.



4. Now, let's add a variable route called `friend_exists` with name as an input:
    - You should create a new route, called `/friend_exists` that additionally takes a variable in the route called name, for example - /friends_exists/Fouad.
    - The route should render `friend_exists.html`.
    - Make sure that this route accepts `GET` and `POST` as methods.
    - Add a link to each "friend" in `home.html` (`facebook_friends` list).
    - Make the link the route `friend_exists` and the name of the friend.
    - The function checks if the name is in the `facebook_friends` and displays True or False according to the results in 'friend_exists.html`.


##### Great job!
##### Call an Instructor/TA to check your completed tasks
 

If you have extra time, continue to the **Bonus Problems** *below*.  
If not, make sure your code is saved in **Repl.it**!






## Bonus Problems: 
1. When you **login**, is the username case sensitive? If not, fix these issues so your app could work properly.

2. Add a dictionary of usernames and passwords, accounts that are allowed to log in to your Facebook app.
 
3. Instead of `friend_exists/{{name}}`, make the link to each "friend" in `home.html` (`facebook_friends` list), that when clicked, it should Google the name. 
  - In other words, if you click on `"Loai"`, it should take you to the results google page when searching for "Loai".
 
4. If you have extra time, complete yesterday's (or any other) lab(s) if you haven't yet!

##### Great job on completing the bonus problems section!  
###### Make sure your code is saved in Repl.it


