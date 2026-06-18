from flask import Flask, jsonify, request, render_template
import random
import requests,json

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


# Variables for tasks
image_link = "https://media-exp1.licdn.com/dms/image/C4D03AQFpDpmWIPyk9g/profile-displayphoto-shrink_200_200/0?e=1594857600&v=beta&t=UnO3MUWlugLbqDzEtkk_9iBV-hw8Po_qkFEFw2x2PdA"

user_bio = "Graduated from MEET in Summer 2017, I love playing and making music, and ALWAYS down to eating burgers!"

posts = {"https://i.scdn.co/image/ab67706c0000da84dd3d0a4c335106e0bb4f9118":"Good morning people!","https://connect-prd-cdn.unity.com/26d9ef31-e673-4e19-977b-5d6b7e2e52ae_screenshotsat2.jpg":"#ScreenshotSaturday working on my videogame #2017","https://lh3.googleusercontent.com/proxy/YOiPRD0V5FVO2XgudSHHpDU193URu7CROKoHQxGusy1qk2fGoFdabdsGgPVLfiPdnlR66WWyiE1wi8Jc9zarc9hgo1Ts_rx6L5EWqsz3UjIaZzcVdStrTyDL_t9mZIenyxTJW1ouWwxRxND4ORmJEkrVRxawXYGVWQon12GP":"Took this picture in the middle of no mans land.","https://scontent.ftlv6-1.fna.fbcdn.net/v/t1.0-9/23172890_10210232119971838_533667112293504307_n.jpg?_nc_cat=104&_nc_sid=e3f864&_nc_ohc=Vh8WySjNLsMAX9lrgRn&_nc_ht=scontent.ftlv6-1.fna&oh=72d309e91647b972c8d4c4409eedd6fb&oe=5EFE49F8":"#tb While living on a yacht for 9 days all around the #Netherlands","https://scontent.ftlv6-1.fna.fbcdn.net/v/t31.0-8/20545640_10154754976097344_4443363175681941174_o.jpg?_nc_cat=107&_nc_sid=730e14&_nc_ohc=5ksyBTqce7IAX_cPHqW&_nc_ht=scontent.ftlv6-1.fna&oh=0756b4c3fb6dddd1cc3cf0ca8b13aa9d&oe=5EFFBC53":"Wanna play the guitar and sing?"}

#####


@app.route('/')  # '/' for the default page
def home():
  return render_template('index.html')


@app.route('/about')  # '/' for the default page
def about():
  return render_template('about.html')


if __name__ == "__main__":  # Makes sure this is the main process
	app.run(debug=True)