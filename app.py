from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


@app.route('/')
def home_page():
    table_data = []
    return render_template("home.html", table_data=table_data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/Team")
def contact():
    return render_template("team.html")

@app.route("/", methods=["POST"])
def get_website_url():
    website_url = request.form.get("website_url")
    print("website url", website_url)
    return redirect(url_for("home_page"))




if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)