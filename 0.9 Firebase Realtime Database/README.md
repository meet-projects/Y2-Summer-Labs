# Firebase Realtime Database

1. Set up Realtime Database in `app.py`:
   - In the config dictionary paste the link you copied as the value of the key `"databaseURL"`
   - Intialize the database with the line `db =firebase.database()` after the variable `firebase` has been defined


3. In `signup.html`:
   - Add two more text inputs, `full_name` and `username`, to the existing form 

5. In the `/` route of `app.py`:
    - Right after you get the email and password from the form, create a dictionary called `user` that contains the keys `full_name`, `email`, and `username` as keys and the corresponding user inputs as values.
    - Add the `user` dictionary you made to the database through the child `Users` and using the uid from `session['user']` as the ID.
      
6. In `home.html`:
   - add another text input to the form where the user can write who said the quote
   
8. In the `/home` route of `app.py`:
    - Delete the code where you stored the quote in the `session`.
    - Create a dictionary called `quote` that contains the keys `'text'` and `'said_by'` with values coming from the user inputs.
    - Add a key `uid` to the dictionary `quote` whose value is the uid of the current user from the `session`
    - Add the quote to the database using the child `Quotes` with a random key.
  
9. In the `/display` route of `app.py`:
    - get the dictionary of all the quotes in the database using `get().val()` and pass it to `display.html` instead of the list of quotes you passed yesterday

10. In `display.html`:
    - change your loop to account for the fact that you now have a dictionary instead of list and display both the text of the quote and the person who said
        

