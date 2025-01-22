import os
from flask import Flask, request, render_template

from model2 import predict
from mysql_connect import mysqlconnector

UPLOAD_FOLDER = "./static/dog_image"

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload_user_files():
    if request.method == "POST":
        upload_file = request.files["upload_file"]
        img_path = os.path.join(UPLOAD_FOLDER, upload_file.filename)
        upload_file.save(img_path)
        result, score = predict(img_path)
        if result not in mysqlconnector():
            return render_template("fail_result.html", result=result, img_path=img_path)
        else:
            return render_template(
                "result.html", score=int(score * 100), result=result, img_path=img_path
            )


if __name__ == "__main__":
    app.run(debug=True)
