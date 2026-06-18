# Super Bonus: Identifying Fires using Google Maps!

<img src="https://www.dailynews.com/wp-content/uploads/2017/12/ldn-l-skirball-1207-ec-175628.jpg?w=526" width="450">


> Before you start working on your lab, we have prepared an environment for you already!   
> Go to this [Repl.it](https://repl.it/@Loai17/API-Labs-Setup), clone it to your account/copy it to your local machine, and feel free to start working!  
  
  
#### Resources:  
- [BreezoMeter](https://docs.breezometer.com/api-documentation/fires-api/v1/#examples) - offers personalized air quality & pollen data as well as **active fire alerts** with worldwide coverage & accuracy down to the street level.
- [Getting Latitude and Longitude Coordinartes using Google Maps API](https://developers.google.com/maps/documentation/javascript/examples/event-click-latlng) - Will be used in Bonus.
- [How to extract and change URL link using JS](https://stackoverflow.com/questions/30137059/how-can-i-extract-and-then-change-the-url-path-using-javascript#:~:text=function%20changeURL()%20%7B%20var%20theURL%20%3D%20window.,you%20won't%20see%20undefined.) - Might be needed for Bonus.

## Instructions:

In this lab, we will be using 2 main APIs, **Google Maps API** and **BreezoMeter API**!
We'll be creating an application that has a map, when you click on a location/enter coordinates (Latitude and Longitude) - it should tell you mainly if there are current fires in that place! And if we have more time we'll use other APIs from BreezoMeter! 

1. Go to [BreezoMeter](https://docs.breezometer.com/api-documentation/fires-api/v1/#examples), explore the API and its documentation, have an idea of what could be done with **BreezoMeter**!
    - Test out some of their examples!  

2. In `home.html`, Add a **form** that takes 2 inputs, a `Latitude`, and a `Longitutde` coordinates.
    - *They should be a **float**.*

3. In `main.py`, adjust the `home` function/route to be able to perform `GET` & `POST` requests!
    - Adjust the function to do a `POST` request on **Form Submit**.
    - The function should check if any **fires** exist currently in that coordinates area.
    - Pass your **results** to `home.html`, and show an alert if there are fires or not!

<img src="https://s.abcnews.com/images/International/AustralianWildfires_v01_sd_hpMain_16x9_992.jpg" width="350">  
    

##### Great job!
##### Call an Instructor/TA to check your completed tasks
 

## Bonus:
1. Make it so your web application also returns these results when entering Lat and Lng coordinates:
     - Current conditions using [**Air Quality API**](https://docs.breezometer.com/api-documentation/air-quality-api/v2/#current-conditions)
     - Daily forecast using [**Pollen API**](https://docs.breezometer.com/api-documentation/pollen-api/v2/#daily-forecast)
     - Current conditions using [**Weather API**](https://docs.breezometer.com/api-documentation/weather-api/v1/)

2. Using this [Google Maps API](https://developers.google.com/maps/documentation/javascript/examples/event-click-latlng), display a map in `home.html`, **On click** event, it should pass the coordinates you got to the function and check if there are any current fires!

3. Make a function that checks all of the available coordinates in the map, the function should let you know where do fires exist *(if any)*.


##### Great job on completing the bonus section!
##### Call an Instructor/TA to check your completed tasks
