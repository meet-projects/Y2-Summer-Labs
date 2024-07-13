# Lab: Creating a Photo Gallery with Flask (Routing Focus)

**Objective:**
In this lab, you will create a simple photo gallery web application using Flask. By the end of this lab, you will have a web page that displays a collection of photos with captions, focusing on routing.

## Instructions

### Step 1: Set Up Your Flask Environment

1. Create a new folder for your project.
2. Create a new file named `app.py` in your project directory.

### Step 2: Create HTML Files

1. Create a `templates` folder in your project folder.
2. Inside the `templates` folder, create and add the following HTML files:

#### `gallery.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Photo Gallery</title>
  </head>
  <body>
    <h1>My Photo Gallery</h1>
    <div class="gallery">
      <div class="photo">
        <a href="/photo1">
          <img src="https://via.placeholder.com/300" alt="Photo 1" />
          <div class="caption">Caption 1</div>
        </a>
      </div>
      <div class="photo">
        <a href="/photo2">
          <img src="https://via.placeholder.com/300" alt="Photo 2" />
          <div class="caption">Caption 2</div>
        </a>
      </div>
      <div class="photo">
        <a href="/photo3">
          <img src="https://via.placeholder.com/300" alt="Photo 3" />
          <div class="caption">Caption 3</div>
        </a>
      </div>
      <div class="photo">
        <a href="/photo4">
          <img src="https://via.placeholder.com/300" alt="Photo 4" />
          <div class="caption">Caption 4</div>
        </a>
      </div>
      <div class="photo">
        <a href="/photo5">
          <img src="https://via.placeholder.com/300" alt="Photo 5" />
          <div class="caption">Caption 5</div>
        </a>
      </div>
    </div>
  </body>
</html>
```

#### `photo1.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Photo 1</title>
  </head>
  <body>
    <div class="photo-container">
      <img src="https://via.placeholder.com/300" alt="Photo 1" />
      <div class="caption">Caption 1</div>
      <br />
      <a href="/">Back to Gallery</a>
    </div>
  </body>
</html>
```

#### `photo2.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Photo 2</title>
  </head>
  <body>
    <div class="photo-container">
      <img src="https://via.placeholder.com/300" alt="Photo 2" />
      <div class="caption">Caption 2</div>
      <br />
      <a href="/">Back to Gallery</a>
    </div>
  </body>
</html>
```

#### `photo3.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Photo 3</title>
  </head>
  <body>
    <div class="photo-container">
      <img src="https://via.placeholder.com/300" alt="Photo 3" />
      <div class="caption">Caption 3</div>
      <br />
      <a href="/">Back to Gallery</a>
    </div>
  </body>
</html>
```

#### `photo4.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Photo 4</title>
  </head>
  <body>
    <div class="photo-container">
      <img src="https://via.placeholder.com/300" alt="Photo 4" />
      <div class="caption">Caption 4</div>
      <br />
      <a href="/">Back to Gallery</a>
    </div>
  </body>
</html>
```

#### `photo5.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Photo 5</title>
  </head>
  <body>
    <div class="photo-container">
      <img src="https://via.placeholder.com/300" alt="Photo 5" />
      <div class="caption">Caption 5</div>
      <br />
      <a href="/">Back to Gallery</a>
    </div>
  </body>
</html>
```

### Step 3: Implement Routing in Flask

1. Open `app.py` and set up the basic Flask application structure. Your task is to create routes for each HTML file.

#### `app.py`

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('gallery.html')


if __name__ == '__main__':
    app.run(debug=True)
```

### Step 4: Run the Application

1. Run the Flask application:
   ```bash
   python3 app.py
   ```
2. Open your browser and go to `http://localhost:5000/` to see your photo gallery and test the routing.

### Step 5: Test Navigation

1. Click on each photo to navigate to its individual page.
2. Use the "Back to Gallery" link to return to the main gallery page.

Congratulations! You've successfully created a photo gallery with Flask, focusing on routing and navigation.
