# APIs 101

## Objective: 
In this lab, you will learn about taking already written code from other sources and use it in our apps!  
APIs!!!





<img src="https://images.yourstory.com/cs/wordpress/2018/02/API.gif" width="450">



## Instructions:

As you can see, in the [Repl.it](https://repl.it/@Loai17/Y2-Forms-Lab) we provided above, you have a ready `main.py` (Flask app), `model.py` and `database.py` files. Explore the project files to have a better understanding of what's going on, even try to **run** the app!  
It should look something like this:  
<img src="https://github.com/meet-projects/Y2-Summer-Labs/blob/master/3.2%20Day%203%2C%20Afternoon%2C%20Flask%20Forms/UsersList-Forms.png" width="500">  

1. Add a new *route* in `main.py`, call it `signup`.. it should render an HTML page, called `signup.html`.
    - In `signup.html`, create a form that takes:
        1. `Full Name`
        2. `Username`
        3. `Password`
        4. `Bio`
    - The route should create a new user with the provided information, when submitting the form!
    - Can we create 2 users with the same username? Handle these errors in advance to prevent them later.

2. Add another *route* in `main.py`, call it `login`.. it should render an HTML page, called `login.html`.
    - In `login.html`, create a form that takes:
        1. `Username`
        2. `Password`
    - The route should **check** if an account with the username `Username` exists, if so, does the password match?
    - **If** the account credentials for login are correct, the page should go to **home** to display all users information.
    - **If not**, you should keep the user on `login` page. 
        
3. Now, after you're done with setting up the `login` and `signup` features, let's add an `edit_account` route!
    - You should create a new route, that looks something like this: `/edit/{{user_id}}`, for example - `/edit/3` would allow us to edit the account information that belongs to user with the id -> 3.
    - The `edit_account` HTML page should have a form just like `signup.html`, so our users can have the possibility of changing/editing any piece of information they'd like! IT should look something like this:
    <img src="https://github.com/meet-projects/Y2-Summer-Labs/blob/master/3.2%20Day%203%2C%20Afternoon%2C%20Flask%20Forms/UserEdit-Forms.png" width="500">  
    
    - If certain attributes and information were not touched/changed, they must stay the same.  
    - Lastly, you should add a `<button>` for each user block in `home.html`, that will take us to edit the information of each specific user! It should look something like this:  
    <img src="https://github.com/meet-projects/Y2-Summer-Labs/blob/master/3.2%20Day%203%2C%20Afternoon%2C%20Flask%20Forms/UsersListWithEdit-Forms.png" width="500">  
    

##### Great job!
##### Call an Instructor/TA to check your completed tasks
 

If you have extra time, continue to the **Bonus Problems** *below*.  
If not, make sure your code is saved in **Repl.it**!


<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--O0ZYhf0U--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://raw.githubusercontent.com/AlbertoMontalesi/InspiredWebDev-Tutorials/master/screenshots/1_HTML_form.png" width="400">




## Bonus Problems: 
1. When you **signup/login**, is it case sensitive? If not, fix these issues so your app could work properly.

2. If a specific user is logged in, he/she should be able to only edit **his/her** information, not everyone else's! Solve this issue.
    
3. Come up with a **Search** *functionality*, it should be a search bar (form), that searches if specific users exist! This function should be able to search users by their:
    - Username
    - Full name
    - **Extra challenge**: If specific words happen to exist in their bio!
    
4. If you have extra time, complete yesterday's lab(s) if you haven't yet!

##### Great job on completing the bonus problems section!  
###### Make sure your code is saved in Repl.it


