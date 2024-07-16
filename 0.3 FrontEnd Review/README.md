# FrontEnd Review - HTML, CSS, JS 

## Objective: 
In this lab, you will practice the previous topics we have learned before during the yearlong!  
Refreshing your memories and reviewing specifically: HTML, CSS and JS.


[![](https://camo.githubusercontent.com/131c25bd172508d5f376dd7fe56283ae7fda2194/68747470733a2f2f63646e302e746e7763646e2e636f6d2f77702d636f6e74656e742f626c6f67732e6469722f312f66696c65732f323031372f30392f625563767252632d312d373936783339382e6a7067)]()


**First things first, *fork* this repo(sitory) and *clone* it to your desktop!**

## HTML Section
1. Create a file `hello.html`.<br/> Open the `hello.html` file using a browser (Like Chrome/Firefox), the page should be empty.<br/><br/> 
2. Make your page stand out!<br/> To do that change it to be about a topic that you're interested in,<br/> your page should have the following (doesn't have to be in order):<br/>
> - Add/change the title of your page  
> - A body tag   
> - A paragraph inside the body  
> - An h1 tag inside the body  
> - An h2 tag inside the body.<br/><br/>


3. Add an image.<br/> In the same `hello.html` file, add an image related to the topic you wrote about. **Set the width to 400px**.<br/><br/>
4. Add a link.<br/>
Add a link to the Wikipedia page about the animal or the topic you're interested in.
<br/><br/>

5. use the `<input type="radio">`tag to let the user pick their favorite color.(if you're unfimliar with the tag, look it up!)

## CSS Section

1. Use the Tag selector to change the background of your HTML page to your favorite color.<br/>
2. Use an ID selector to set a CSS property of one element on your page.<br/>
A property could be: font-size, border, color, etc...<br/>

3. Use a class selector to set a CSS property of one element on your page.<br/>
 
<br/>

## Javascript Section 

1. Create a new file `main.js` , and link it to **`hello.html`**.
2. In **`main.js`**, define a new *function* called `changeBackgroundColor`, that takes 1 argument -> `color`
    - The function should change the background color of "hello.html" to "color".
3. Add a "button" tag in **`hello.html`** with a text that says "Change BG Color".
    - The button has to have an `onclick` attribute, linked to the `changeBackgroundColor(color)` function.
    - Fill in the `color` argument whatever you like!
4. Test out your button!
    - Try it with different `color` values.



## Bonus Problems: 
If you have finished and still have time, first of all **GOOD JOB!** 

1. Costumize the `changeBackgroundColor` function in **`main.js`** to change switch between 2 colors, instead of switching to 1 specific color.
    - For example:
        1. The background is Blue.
        2. On 1st button click, the background will change to Yellow.
        3. On 2nd button click, the background will change to Blue.
        4. And so on... (Keeps switching between Yellow and Blue on every new click!)
2. Add a button that plays a song of your choice
    - *Use a drop down to switch between audios
    
3. Add a button that makes the background color change continuously.

4. Remember the images we added? Now let’s add a video from your favorite youtuber!
*Create a list of video URLs, and use a button to switch through them

