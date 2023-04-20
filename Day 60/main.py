from flask import Flask, render_template, request
import requests
import smtplib

# smtp credentials
MY_EMAIL = "aditirao292@gmail.com"
MY_PASSWORD = "CD9A4DEA1D457B9C39EDA1CC8F2271F24C18"

posts = requests.get("https://api.npoint.io/71155047727ef50796aa").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name_entry = request.form['name']
        email_entry = request.form['email']
        phone_entry = request.form['phone']
        message_entry = request.form['message']
        message = f'''Subject: Contact Form\n
                    Name: {name_entry}\n
                    Email: {email_entry}\n
                    Phone: {phone_entry}\n
                    \n
                    Message: {message_entry} 
                    '''
        with smtplib.SMTP("smtp.elasticemail.com", 2525) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="lgvishalsangam@gmail.com", msg=message)
        return render_template("contact.html", h1_entry="We have received your email!")
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
