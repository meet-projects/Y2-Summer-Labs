# Firebase Realtime Database

## Objective: 
In this lab, you will learn about reading, adding, editing and deleting info from a realtime database!
As well as the structure of the database.






<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--AMKbrkDD--/c_imagga_scale,f_auto,fl_progressive,h_900,q_auto,w_1600/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rlrlpchkz57pxwwxvwid.png" width="450">




> Before we start, make sure to go to open the folder from the previous lab, and continue to work there.


## Twitter Lab:

1. Setting up Realtime Database in `Firebase`:
    1. Go to your console and choose your project.
    2. Go to Realtime Database and create a database.
    3. Go to rules and change false to true.
    4. Make sure to copy the database's link.

2. Setting up Realtime Database in `app.py`:
    1. In the config dictionary add databaseURL as a key and the link you copied as the value.
    2. Intialize the 'db' using the firebase object.


3. Add in `signup.html` 3 inputs:
    1. `full_name`
    2. `username`
    3. `bio` - It should take a maximum of 280 letters.


4. When the user signs up:
    - Create a dictionary called user that contains the inputs as keys and values.
    - Add the user to the `database` through the child `Users` adding him through his uid (retrieve it through login_session).


5. Create a form in `home.html` to add a tweet to the database:
    - The form should contain:
        - `Title`.
        - `Text`- It should take a maximum of 280 letters.
        - `Image link` - This should be optional (We'll set this feature up later)


6. When the user submits a tweet:
    - Create a dictionary called `tweet` that contains the inputs as keys and values.
    - In the dictionary add a key named `uid` and the value as the uid of the user that wrote the tweet.
    - Add the tweet using the child `Tweets` to the `database` with a random key.

        
7. Create an html page called tweets.html:
    - in this html page display all the tweets that were written:
        - Go to the child `Tweets` and use get().val()
        


##### Great job!
##### Call an Instructor/TA to check your completed tasks
 

If you have extra time, continue to the **Bonus Problems** *below*.  
If not, make sure your code is pushed.


<img src="https://cached.imagescaler.hbpl.co.uk/resize/scaleWidth/888/cached.offlinehbpl.hbpl.co.uk/news/ORP/wendysMAIN-20200206101134487.png" width="400">




## Bonus Problems: 

1. Add a Tweet **Timestamp** attribute! It should take the real time and date and save it in Tweet. 

2. Add a like button:
    - It should add 1 like to a specific `tweet`, everytime a like button has been clicked using the database.   
    
##### Great job on completing the bonus problems section!  
###### Make sure your code is saved in Repl.it or on your machine!


