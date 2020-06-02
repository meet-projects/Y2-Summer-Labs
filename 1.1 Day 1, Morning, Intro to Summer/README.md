# Intro to Y2 Summer - HTML, CSS, JS & OOP Review Lab

## Objective: 
In this lab, you will practice the previous topics we have learned before during the yearlong!  
Refreshing your memories and reviewing specifically: HTML, CSS, JS and Object Oriented Programming!


[![](https://camo.githubusercontent.com/131c25bd172508d5f376dd7fe56283ae7fda2194/68747470733a2f2f63646e302e746e7763646e2e636f6d2f77702d636f6e74656e742f626c6f67732e6469722f312f66696c65732f323031372f30392f625563767252632d312d373936783339382e6a7067)]()


**First things first, *fork* this repo(sitory) and *clone* it to your desktop!**

## HTML Section
1. Create a file "hello.html".<br/> Open the 'hello.html' file using a browser (Like Chrome/Firefox), the page should be empty.<br/><br/> 
2. Make your page stand out!<br/> To do that change it to be about a topic that you’re interested in,<br/> your page should have the following (doesn’t have to be in order):<br/>
> -- Add/change the title of your page <br/> -- A body tag <br/> -- A paragraph inside the body <br/> -- An h1 tag inside the body <br/> -- An h2 tag inside the body.<br/><br/>


3. Add an image.<br/> In the same hello.html file, add an image related to the topic you wrote about. **Set the width to 400px**.<br/><br/>
4. Add a link.<br/>
Add a link to the Wikipedia page about the animal or the topic you're interested in.
<br/><br/>

## CSS Section

1. Use the Tag selector to change the background of your HTML page to your favorite color.<br/>
2. Use an ID selector to set a CSS property of one element on your page.<br/>
A property could be: font-size, border, color, etc...<br/>

3. Use a class selector to set a CSS property of one element on your page.<br/>

<br/>

## Javascript Section 

1. Create a new file **"main.js"**, and link it to **"hello.html"**.
2. In **"main.js"**, define a new *function* called "changeBackgroundColor", that takes 1 argument -> "color"
    - The function should change the background color of "hello.html" to "color".
3. Add a "button" tag in **"hello.html"** with a text that says "Change BG Color".
    - The button has to have an "onclick" attribute, linked to the "changeBackgroundColor(color)" function.
    - Fill in the "color" argument whatever you like!
4. Test out your button!
    - Try it with different "color" values.

## OOP Section
In this section, you are an engineer at Youtube!  
Susan, the CEO of Youtube, asks you to create an easier way to access, modify, and create youtube videos.  
You have an idea! Why not use OOP? it's going to be super easy to do all of the requirements using Object Oriented Programming.

1. Create a new Python file, called **"oopReview.py"**.
2. In "oopReview.py", create a new Class called "YoutubeVideo".
    - It should take 4 attributes:
    - title - The title/name of the video.
    - description - The description of the video/Short explanation about the video.
    - likes - Number of likes, should start equal to 0.
    - dislikes - Number of dislikes, should start also equal to 0.
    - comments - A dictionary of comments, where the "username" is the **key**, and the comment text is the **value**. Should start empty.

3. Define a new function in "YoutubeVideo" and call it "like". The function should add 1 like to "likes".

4. Define a similar function, call it "dislike". The function should add 1 dislike to "dislikes".

5. Define a new function, call it "add_comment". The function should take 2 attributes:
    1. "username" - The username of the commenter.
    2. "comment_text" - The actual comment!
    - The function should add "username" as a **key** to "comments" dictionary, and "comment_text" as the **value**.

6. Define a new function, call it "print_info.
    - Make it so the function prints all of the video's information, in a similar way to this:
    <img src="https://github.com/meet-projects/Y2-Summer-Labs/blob/master/1.1%20Day%201%2C%20Morning%2C%20Intro%20to%20Summer/YoutubeVideoExample-OOP.png">


7. Create a new youtube video **object**, and fill in the attributes, try to make it a funny video!
    - Test out all of the object's functions.
    - How would you add 495 likes?
    - Show your neighbor! Have a laugh :)


##### Great job on completing your first Lab!
##### Call an Instructor/TA to check your completed tasks
 

If you have extra time, continue to the **Bonus Problems** *below*.
<img src="https://developers.google.com/youtube/images/youtube_home_page_data_api.png" width="500">




## Bonus Problems: 
If you have finished and still have time, first of all **GOOD JOB!** 

1. Costumize the "changeBackgroundColor" function in **"main.js"** to change switch between 2 colors, instead of switching to 1 specific color.
    - For example:
        1. The background is Blue.
        2. On 1st button click, the background will change to Yellow.
        3. On 2nd button click, the background will change to Blue.
        4. And so on... (Keeps switching between Yellow and Blue on every new click!)


2. Costumize the **"YoutubeVideo"** class in **"oopReview.py"**, define a new function called "delete_bad_comments".
    - The function should check all comments for a **list** of bad words, and if any of the bad words are there, the function should delete the comment!
    - Example: bad_words_list = ["****","Shoot","Hate","Prick","noob"] 
    - If any of the words in the above list happen to be in any comment, the comment itself should be taken off and deleted for being offensive.







<img src="https://cdn.dribbble.com/users/94656/screenshots/1141726/terminal2.gif" width="500">

