from flask import Flask, render_template, url_for, request
import requests
import smtplib

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def home():
    fake_blog_posts = requests.get('https://api.npoint.io/2903f724d13a84280bf8').json()
    print(fake_blog_posts)
    return render_template("index.html", posts=fake_blog_posts)

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/<int:number>")
def post(number):
    fake_blog_post = requests.get('https://api.npoint.io/2903f724d13a84280bf8').json()[number - 1]
    print(fake_blog_post)
    return render_template("post.html", post=fake_blog_post)

@app.route("/contact", methods=["GET", "POST"])
@app.route("/form-entry", methods=["GET", "POST"])
def receive_data():
    if request.method == 'POST':
        #print(request.form)
        send_notification_email(request.form)
        # for key in request.form.keys():
        #     print(request.form[key])
        return render_template("contact.html", control=True)
    elif request.method == 'GET':
        return render_template("contact.html", control=False)



def send_notification_email(contact_info):
    my_email = "natedoggg109312@gmail.com"
    my_password = "HorseDartNinjaPilot#6"
    message = "New Message:\n"
    for key in contact_info.keys():
        message += f"{key.capitalize()}: "
        message += contact_info[key]
        message += "\n"
    #print(message)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="nthnelliott857@gmail.com", msg=message)



if __name__ == "__main__":
    app.run(debug=True)
