# Firebase Realtime Database

1. Set up Realtime Database in `app.py`:
   - In the config dictionary paste the link you copied as the value of the key `"databaseURL"`
   - Intialize the database with the line `db =firebase.database()` after the variable `firebase` has been defined


3. Add two more inputs to the form in `signup.html` that takes the email and passoword:
   - `full_name`
   - `username`

4. In the `/` route of `app.py`:
    - Create a dictionary called `user` that contains the keys `full_name`, `email`, and `username` as keys and the corresponding user inputs as values.
    - Add the `user` dictionary to the database through the child `Users` adding him through his uid (retrieve it through the `session`).

5. Add two more inputs to the form in `home.html`:
    -`hearer`: who overheard the quote and is submiting it 
    -`speaker`: which staff member said the quote

6. In the `/home` route of `app.py`:
    - Create a dictionary called `quote` that contains `hearer`, `speaker`, and `text` as keys.
    - Get the uid of the current user from the `session` and store it in the variable `userid`
    - Add a key `uid` to the dictionary `quote` with the value `userid`
    - Add the quote to the database using the child `Quotes` with a random key.
  
7. In the `/display` route of `app.py`:
    - get the dictionary of all the quotes in the database using `get().val()` and pass it to `display.html` instead of the list of quotes you passed yesterday

8. In `display.html`:
    - change your loop to account for the fact that you now have a dictionary instead of list and display both the text of the quote and the person who said
        

