# Firebase Authentication

## Objective: 
In this lab, you will learn about signing up, signing in & signing out users in your Flask app. <br/>
As well as setting up a Firebase project.




<img src="https://i.ytimg.com/vi/8sGY55yxicA/maxresdefault.jpg" width="450">




> Before we start, make sure to go to fork the repo and clone the code in order to set up our environment for this lab.


## Authentication Lab:

1. Create and set up a new Firebase project:
    - As displayed in the slides:
        1. Go to https://console.firebase.google.com/
        2. Create a new project and name it whatever you'd like.
        3. Go to Authentication and choose get started.
        4. Set up email and password authenticatication.
        

2. Connect the Firebase project to your Flask app:
    1. In your Firebase project:
        - Go to project setting and create a web app.
        - Copy the firebaseconfig lines.
    2. In the app.py file:
        - Create a dictionary called config and paste the copied lines (make sure to fix the syntax errors).
        - Intialize the firebase using pyrebase.
        - Intialize auth using the firebase object.
    
        
3. Signing up users:
    - In signup.html:
        1. Go over the form and understand the code.
    - In the signup route:
        1. If the method is 'POST' take the inputs and create a user with email & password.
        2. Don't forget to store the user in the login session and to use try and except.
        3. Redirect the route to the home page
        - **For Authentication you need a valid email and a 6 character long password**
    

4. Signing in users:
    - In signin.html:
        1. Go over the form and understand the code.
    - In the signin route:
        1. If the method is 'POST' take the inputs and signin the user with email & password.
        2. Don't forget to store the user in the login session and to use try and except.
        3. Redirect the route to the home page



##### Great job!
##### Call an Instructor/TA to check your completed tasks
 

If you have extra time, continue to the **Bonus Problems** *below*.  
If not, make sure your code is saved in **Repl.it**!



## Bonus Problems: 
1. In home.html:
    - Add a button called signout.
    - create a new route called signout:
        - The route signs out the user and redirects him to the signin page.

##### Great job on completing the bonus problems section!  
###### Make sure your code is saved in Repl.it or on your machine!


