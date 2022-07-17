# Python Review

## Objective: 
In this lab, you will practice the previous topics we have learned before during the yearlong!  
Refreshing your memories and reviewing specifically: Python basics, Lists, Dictionaries & Functions.


[![](https://camo.githubusercontent.com/131c25bd172508d5f376dd7fe56283ae7fda2194/68747470733a2f2f63646e302e746e7763646e2e636f6d2f77702d636f6e74656e742f626c6f67732e6469722f312f66696c65732f323031372f30392f625563767252632d312d373936783339382e6a7067)]()


**First things first, *fork* this repo(sitory) and *clone* it to your desktop!**


In this section, you are an engineer at Youtube!  
Susan, the CEO of Youtube, asks you to create an easier way to access, modify, and create youtube videos.  
You have an idea! Why not use Dictionaries? it's going to be super easy to do all of the requirements using them.

1. Create a new Python file, called **`pythonReview.py`**.
2. In `pythonReview.py`, create a new function called `create_youtube_video`.
    - It should take 4 inputs:
        - `title` 
        -  `description`
    - The function should create a new youtube video dictionary with the following keys:
        - `title` - The title/name of the video, and its value is the input.
        - `description` - The description of the video/Short explanation about the video, and its value is the input.
        - `likes` - Number of likes, should start equal to 0 as a value.
        - `dislikes` - Number of dislikes, should start also equal to 0 as a value.
        - `comments` - A dictionary of comments, where the "username" is the **key**, and the comment text is the **value**. Should start empty as a value.
    - The function returns the dictionary.

3. Define a new function called `like`:
    - The function takes a dictionary (youtube video) as an input
    - the function checks if likes is a key in the dictionary, if it is then it should add 1 to the value.
    - The function returns the dictionary.

4. Define a similar function, call it `dislike`. The function should add 1 dislike to the key `dislikes` if it's in the dictionary.

5. Define a new function, call it `add_comment`. The function should take 3 attributes:
    1. `youtubevideo` - The dictionary that contains the youtube video info.
    1. `username` - The username of the commenter.
    2. `comment_text` - The actual comment!
    - The function should add "username" as a **key** to "comments" dictionary, and "comment_text" as the **value**.
    - The function returns the dictionary.


6. Create a new youtube video **dictionary**, and fill in the attributes!
    - Test out all of the object's functions.
    - How would you add 495 likes?
    - Show your neighbor!


##### Great job on completing your first Lab!
##### Call an Instructor/TA to check your completed tasks
 

If you have extra time, continue to the **Bonus Problems** *below*.
<img src="https://developers.google.com/youtube/images/youtube_home_page_data_api.png" width="500">




## Bonus Problems: 
If you have finished and still have time, first of all **GOOD JOB!** 

1. Let's make a recommended videos algorithm!!
    - Firstly, add a key to the dictionary in **`create_youtube_video`**, call it `hashtag`. It should be a **list up to 5 words** that describe the video (the list should be taken as an input in the function).
    - Come up with a function called `similarity_to_video`, the function should take two youtube video dictionaries and return the percentage of similarity of the two videos!




<img src="https://cdn.dribbble.com/users/94656/screenshots/1141726/terminal2.gif" width="500">
