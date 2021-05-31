from flask import Flask, render_template, request, send_from_directory

from  .forms import CommentForm

app = Flask(__name__)
app.config.from_object('project.config.Config')


@app.route("/", methods=["GET", "POST"])
def home():
    comment_form = CommentForm(request.form)
    return render_template("home.html", form=comment_form)


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)


@app.route("/client")
def client():
    client_list = ['Daniel', 'Juanita', 'Francisco']
    return render_template("client.html", clients=client_list)


if __name__ == '__main__':
    app.run(debug=True)
