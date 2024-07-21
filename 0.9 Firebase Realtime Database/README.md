# Firebase Realtime Database

1. Set up Realtime Database in `app.py`:
    1. In the config dictionary paste the link you copied as the value of the key `"databaseURL"`
    2. Intialize the 'db' using the firebase object.


2. Add three more inputs to the form in `signup.html` that takes the email and passoword:
   - `full_name`
   - `username`
   - `bio` that takes a maximum of 280 characters.


3. In the `/` route of `app.py`:
    - Create a dictionary called `user` that contains the keys `full_name`, `email`, `username`, and `bio` as keys and the corresponding user inputs as values.
    - Add the `user` dictionary to the database through the child `Users` adding him through his uid (retrieve it through the `session`).

4. Add two more inputs to the form in `home.html`:
    -`hearer`: who overheard the quote and is submiting it 
    -`speaker`: which staff member said the quote

5. In the `/home` route of `app.py`:
    - Create a dictionary called `quote` that contains `hearer`, `speaker`, and `text` as keys.
    - Get the uid of the current user from the `session`
    - Add a key `uid` to the dictionary `quote` with the value as the uid of the user that wrote the quote.
    - Add the quote to the database using the child `Quotes` with a random key.

8. Create an html page called Quotes.html:
    - in this html page display all the quotes that were written:
        - Go to the child `Quotes` and use get().val()
        

