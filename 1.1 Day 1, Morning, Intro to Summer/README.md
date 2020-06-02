# Intro to CS - Linux Lab

## Objective: 
In this lab, you will learn how to use basic `Linux` commands. These will help you organize your work for this year and for the rest of your journey at MEET!



[![](https://chemnitzer.linux-tage.de/2017/static/img/box/tuxel.gif)]()



## Instructions:

1. Open a **Linux** `terminal` by double-clicking on this icon:
    1. [![](https://lh3.googleusercontent.com/proxy/cHRNI6pM0BqLsW-a3wmXRTTl58d1Jy6bik0vhEV4lGW5bZxfQPpDmhOhNTq5sndTHG9gilISn-xfUOjcI7Q0wVVTFglYnZFYlSdc2epg7GoA7a4ym5X9)]()
    1. You should see something like this pop up:
    1. [![](https://www.howtogeek.com/thumbcache/2/200/f5f162d5614c29a6e114429a33dd6088/wp-content/uploads/2013/03/linux-terminal-on-ubuntu.png)]()


1. Navigate to your **desktop** by typing `cd Desktop`
    1. `cd` means **C**hange **D**irectory (A directory is a folder)

1. Make a directory called **Day1** using `mkdir`. 
    1. And then type `ls` - a command that shows you the list of all files/folders in the current directory. 
    1. What do you see?



1. Change directories to **Day1**. Type `pwd` to print the name of the current folder you are in. Does it say **Day1**?



1. On **Day1**, make a new folder using `mkdir` called **newFolder**. 
    1. Use `ls` to check that **newFolder** is there.



1. Click on the **Day1** folder in your **Desktop** to see if **newFolder** is there. (You probably already know how to explore folders this way.)
    1. In your **Day1** folder, *Right-click* and click **Create Folder** to make a new folder.
    1. Name it **anotherFolder**.

1. In the **Linux terminal**, type `ls` to confirm that **anotherFolder** is now in the **Day1** folder.

1. Figure out how to open *Firefox* using the **Linux terminal**!
<br>

##### Great job on completing your first Lab!
##### Call an Instructor/TA to check your completed tasks
 

If you have extra time, continue to the **Bonus Problems** *below*.









[![](https://thumbs.gfycat.com/ArcticOblongHornedtoad-max-1mb.gif)]()




## Bonus Problems:

1. In the Linux terminal **Day1** folder, type: `idle3 newFile.py &`. 
    1. This makes a *new Python* file called **newFile**.

1. Type `ls` to confirm that **newFile.py** is in your **Day1** folder.

1. Copy **newFile.py** to **newFolder** by typing: `cp newFile.py newFolder` 

1. Change directories to **newFolder** to check if a copy of **newFile.py** is there.
    1. You just copied a file!

1. Type `cd ..` (where you include two period points after `cd`)
    1. This allows us to change directories to the *parent* folder **Day 1**. This means you move *back* out of **newFolder** up to the **Day1** folder.

1. Make **anotherFile.py** using the **idle3 ___ &** command as shown in **Bonus Problems #1**.
    1. Type `ls` to see if it’s there.

1. Now move **anotherFile.py** to **anotherFolder** by typing: `mv anotherFile.py anotherFolder` 

1. Type `ls`. You should see that **anotherFile.py** is no longer in **Day1**!
    1. But now change directories to **anotherFolder**. And type `ls` to see that **anotherFile.py** is there! 
    1. You just moved a file!



<img src="https://cdn.dribbble.com/users/94656/screenshots/1141726/terminal2.gif" width="500">

