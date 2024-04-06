from flask import Flask, request, redirect, render_template
from chatgpt import Chat
from scrape import getMajorMap
from markdown import markdown

names = ['Aeronautical Management Technology (Air Traffic Management) - BS', 'Aeronautical Management Technology (Air Transportation Management) - BS', 'Aeronautical Management Technology (Professional Flight) - BS', 'Aeronautical Management Technology (Unmanned Aerial Systems) - BS', 'Aerospace Engineering (Aeronautics) - BSE', 'Aerospace Engineering (Astronautics) - BSE', 'Aerospace Engineering (Autonomous Vehicle Systems) - BSE', 'Applied Science (Aviation) - BAS', 'Applied Science (Graphic Information Technology) - BAS', 'Applied Science (Internet and Web Development) - BAS', 'Applied Science (Operations Management) - BAS', 'Biomedical Engineering - BSE', 'Biomedical Engineering (Biological Devices) - BSE', 'Biomedical Engineering (Biomedical Devices) - BSE', 'Chemical Engineering - BSE', 'Civil Engineering - BSE', 'Civil Engineering (Sustainable Engineering) - BSE', 'Computer Science - BS', 'Computer Science (Cybersecurity) - BS', 'Computer Science (Software Engineering) - BS', 'Computer Systems Engineering - BSE', 'Computer Systems Engineering (Cybersecurity) - BSE', 'Construction Engineering - BSE', 'Construction Management and Technology - BS', 'Electrical Engineering - BSE', 'Electrical Engineering (Electric Power and Energy Systems) - BSE', 'Engineering - BSE', 'Engineering (Automotive Systems) - BSE', 'Engineering (Electrical Systems) - BSE', 'Engineering (Mechanical Engineering Systems) - BSE', 'Engineering (Robotics) - BSE', 'Engineering Management - BSE', 'Engineering Science (Business) - BS', 'Engineering Science (Microelectronics) - BS', 'Environmental and Resource Management - BS', 'Environmental Engineering - BSE', 'Graphic Information Technology - BS', 'Graphic Information Technology (Full-Stack Web Development) - BS', 'Graphic Information Technology (User Experience) - BS', 'Human Systems Engineering - BS', 'Human Systems Engineering (User Experience) - BS', 'Industrial Engineering - BSE', 'Informatics - BS', 'Information Technology - BS', 'Manufacturing Engineering - BS', 'Materials Science and Engineering - BSE', 'Mechanical Engineering - BSE', 'Mechanical Engineering (Computational Mechanics) - BSE', 'Mechanical Engineering (Energy and Environment) - BSE', 'Robotics and Autonomous Systems - BS', 'Software Engineering - BS', 'Technological Entrepreneurship and Management - BS']

app = Flask(__name__, static_url_path='/static')


return_message = "Welcome to the career companion. Let me generate some suggestions for you."

@app.route("/")
def home():
    global return_message
    return_message = "Welcome to the career companion. Let me generate some suggestions for you."
    # return '<a href="/chat">Chat</a>'
    return render_template('home.html')

@app.route("/submit", methods=['POST'])
def submit():
    global client
    global return_message
    if request.method == "POST":
        print(request.form["major"])
        print(request.form["interests"])
        i = names.index(request.form["major"])
        mm = getMajorMap(i)
        client = Chat(request.form['major'], request.form['interests'], mm)
        return_message = client.getInit()
    return redirect("/chat")

@app.route('/chat', methods=['POST', 'GET'])
def chat():
    global return_message
    if request.method == "POST":
        message = request.form["message"]
        return_message = client.getResponse(message)
    return render_template('index.html')

@app.route('/message', methods=['GET'])
def message():
    return markdown(return_message)
    
app.run(debug=True)