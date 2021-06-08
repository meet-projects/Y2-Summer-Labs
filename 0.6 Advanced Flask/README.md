# Advanced Flask Lab

## Objective: 
In this lab, you will learn about passing variables to templates (HTML pages) and displaying them... by creating your very own Instagram page!  

By the end of this lab, you will have your Instagram profile page look something like this:  



<img src="https://github.com/meet-projects/Y2-Summer-Labs/blob/master/0.6%20Advanced%20Flask/AdvancedFlask-Instagram.png" width="450">




> Before we start, make sure to go to [This Repl.it](https://repl.it/@Loai17/Advanced-Flask-Lab), fork it/copy the code to your machine in order to set up our environment for this lab.


## Instructions:

In this lab, we'll be creating our own kind of Instagram profile page!  
We have provided your Repl.it with some HTML, CSS, and JS already, so not to worry about design; We'll be focusing on our programming skills!  

1. Run `main.py`; Did everything load up correctly?
    - Fix the incorrectly loaded content
    - *Hint: Take a look at `index.html`, are all pictures visible? Are all scripts linked correctly?*

2. In `main.py`, you have a variable called `image_link`, and another variable called `user_bio`:
    - **Pass** these *two variables* to `index.html`
    - **Replace** the first image with `image_link`
    - **Replace** the **description** `<h1>` with `user_bio`
    - Run `main.py`, how is it lookin' now? ;)
    - *Feel free* to change the values of `image_link` and `user_bio` to your own image and bio! 
        
Now, after you're done with setting up the profile info, let's display our posts!  

3. In `main.py` theres a variable called `posts`, it's a dictionary that has image links as *Keys*, and post captions as *Values*!
    - Pass `posts` to `index.html`, and display each post correctly!
    - *Hint: hmmm.. how can we **loop** through these posts and show them on the page?*
    - *Feel free* to change the dictionary keys and values to create your own Instagram profile!


##### That's so cool! You have just created your first advanced flask application!
##### Call an Instructor/TA to check your completed tasks
 

If you have extra time, continue to the **Bonus Problems** *below*.  
If not, make sure your code is saved in **Repl.it**!


<img src="https://miro.medium.com/max/1200/1*SzN6u2U98S4RyhWo_WyaHQ.png" width="400">




## Bonus Problems: 
1. Fill in the **Social Media** icons with accessible links!
    - Make sure to **pass** the links variables and linking them correctly in `index.html`.
    
2. If you add too many posts, it'll start getting clunky and messy... try to fix it!
    - *Hint: maybe something like, say, every 3 posts on a row? or something like that.*

##### Great job on completing the bonus problems section!  
###### Make sure your code is saved in Repl.it


