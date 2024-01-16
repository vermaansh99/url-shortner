from flask import Flask,render_template,request,redirect
from db.db import mongo
import secrets
import string



db = mongo["url-shortener"]
collection_name  = db["urls"]



def generate_shortcode(length=4):
    characters = string.ascii_letters + string.digits
    shortcode = ''.join(secrets.choice(characters) for _ in range(length))
    return shortcode




app = Flask(__name__)





@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<code>")
def show_user_profile(code):
    query = collection_name.find_one({"code":code})
    url = query["url"]
    return redirect(url)

@app.route("/create",methods=["GET", "POST"])
def create():
    if request.method == "POST":
        url = request.form.get("url")
        newPayload = {
            "code":generate_shortcode(),
            "url":url
        }
        collection_name.insert_one(newPayload)
        return {"url":"http://localhost:8080/"+newPayload["code"]}




if __name__ == "__main__":
    app.run(debug=True,port=8080)



