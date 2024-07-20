# Firebase Realtime Database

1. Setting up Realtime Database in `Firebase`:
    1. Go to your console and choose your project.
    2. Go to Realtime Database and create a database.
    3. Go to rules and change false to true.
    4. Make sure to copy the database's link.

2. Setting up Realtime Database in `app.py`:
    1. In the config dictionary add databaseURL as a key and the link you copied as the value.
    2. Intialize the 'db' using the firebase object.


3. Add in `signup.html` 3 more inputs:(you already have the email and passoword)
    1. `full_name`
    2. `username`
    3. `bio` - It should take a maximum of 280 letters.


4. When the user signs up:
    - Create a dictionary called user that contains the inputs as keys and values.
    - Add the user to the `database` through the child `Users` adding him through his uid (retrieve it through login_session).


5. Create a form in `home.html` to add a Quote from Staff members to the database:
    - The form should contain:
        - `Title`.
        - `Text`- It should take a maximum of 280 letters.
        - `Image link` - This should be optional (We'll set this feature up later)


6. When the user submits a Quote:
    - Create a dictionary called `Quote` that contains the inputs as keys and values.
    - In the dictionary add a key named `uid` and the value as the uid of the user that wrote the quote.
    - Add the quote using the child `Quotes` to the `database` with a random key.
