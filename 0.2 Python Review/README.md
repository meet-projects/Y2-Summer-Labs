# Python Review - Basics and OOP 

## Objective: 
In this lab, you will practice the previous topics we have learned before during the yearlong!  
Refreshing your memories and reviewing specifically: Python and Object Oriented Programming.


[![](https://camo.githubusercontent.com/131c25bd172508d5f376dd7fe56283ae7fda2194/68747470733a2f2f63646e302e746e7763646e2e636f6d2f77702d636f6e74656e742f626c6f67732e6469722f312f66696c65732f323031372f30392f625563767252632d312d373936783339382e6a7067)]()


**First things first, *fork* this repo(sitory) and *clone* it to your desktop!**
**OR create a new Repl and call it "Python Review S21"**


## OOP Section
In this section, you are an engineer at Youtube!  
Susan, the CEO of Youtube, asks you to create an easier way to access, modify, and create youtube videos.  
You have an idea! Why not use OOP? it's going to be super easy to do all of the requirements using Object Oriented Programming.

1. Create a new Python file, called **`oopReview.py`**.
2. In `oopReview.py`, create a new Class called `YoutubeVideo`.
    - It should take 4 attributes:
    - `title` - The title/name of the video.
    - `description` - The description of the video/Short explanation about the video.
    - `likes` - Number of likes, should start equal to 0.
    - `dislikes` - Number of dislikes, should start also equal to 0.
    - `comments` - A dictionary of comments, where the "username" is the **key**, and the comment text is the **value**. Should start empty.

3. Define a new function in `YoutubeVideo` and call it `like`. The function should add 1 like to `likes`.

4. Define a similar function, call it `dislike`. The function should add 1 dislike to `dislikes`.

5. Define a new function, call it `add_comment`. The function should take 2 attributes:
    1. `username` - The username of the commenter.
    2. `comment_text` - The actual comment!
    - The function should add "username" as a **key** to "comments" dictionary, and "comment_text" as the **value**.

6. Define a new function, call it `print_info`.
    - Make it so the function prints all of the video's information, in a similar way to this:
    <img src="https://github.com/meet-projects/Y2-Summer-Labs/blob/master/0.2%20Python%20Review/YoutubeVideoExample-OOP.png?raw=true">


7. Create a new youtube video **object**, and fill in the attributes!
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
    - Firstly, add an attribute to **`YoutubeVideo`** class, call it `hashtag`. It should be a **list up to 5 words** that describe the video.
    - Come up with a function called `recommended_videos`, the function should return the videos with similar hashtags!




<img src="https://cdn.dribbble.com/users/94656/screenshots/1141726/terminal2.gif" width="500">
