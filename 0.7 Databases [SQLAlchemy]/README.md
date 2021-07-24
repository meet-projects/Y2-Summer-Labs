# Databases with SQLAlchemy

## Objective: 
In this lab, you will learn about reading, adding, editing and deleting info from a SQLAlchemy database!
As well as structure the database table columns.






<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--AMKbrkDD--/c_imagga_scale,f_auto,fl_progressive,h_900,q_auto,w_1600/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rlrlpchkz57pxwwxvwid.png" width="450">




> Before we start, make sure to go to [This Repl.it](https://repl.it/@Loai17/Y2-Databases-Lab), fork it/copy the code to your machine in order to set up our environment for this lab.


## Twitter Lab:

1. Define a new table in `model.py`, call it `User`
    - It should have 5 columns:
        1. `id` - *Primary key*
        2. `full_name`
        3. `username`
        4. `email`
        5. `bio` - It should take a maximum of 280 letters.
         

2. Define a new table in `model.py`, call it `Tweet`
    - It should have 5 columns:
        1. `id` - *Primary key*
        2. `text` - It should take a maximum of 280 letters.
        3. `image_link` - This should be optional (We'll set this feature up later) 
        4. `username` - The username of the tweet owner.
        5. `likes` - An integer that should start equal to 0.
        
3. Now, after you're done with setting up `model.py`, let's move to `database.py`.
    - In `database.py`, we will write all of our database related functions!
    

4. In `database.py`, 
     1. Write a function that creates a new unique user!
     2. Write a function that creates a new tweet!
     3. Write a function that searches for a user by `username`.
     4. Write a function that adds a like to a tweet by `tweet id`.
     5. Write a function that prints ALL information about a `user`, with all the tweets related to this `user`, and number of likes for each `tweet`.
     6. Write a function that deletes a user by `username`.
     7. Write a function that edits a user account information.



##### Great job!
##### Call an Instructor/TA to check your completed tasks
 

If you have extra time, continue to the **Bonus Problems** *below*.  
If not, make sure your code is saved in **Repl.it**!


<img src="https://cached.imagescaler.hbpl.co.uk/resize/scaleWidth/888/cached.offlinehbpl.hbpl.co.uk/news/ORP/wendysMAIN-20200206101134487.png" width="400">




## Bonus Problems: 
1. Create an HTML page that displays all tweets.
    - Using `Flask Routing`, Show this HTML page.
    - Each tweet should display the owner's `username`.

2. Add a like button, and link it to the function in `database.py`.
    - It should add 1 like to a specific `tweet`, everytime a like button has been clicked.
    
3. Add a Tweet **Timestamp** attribute! It should take the real time and date and save it in Tweet.    
    
4. If you have extra time, complete yesterday's lab(s) if you haven't yet!

##### Great job on completing the bonus problems section!  
###### Make sure your code is saved in Repl.it or on your machine!


