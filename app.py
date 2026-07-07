from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        maths = int(request.form["maths"])
        science = int(request.form["science"])
        english = int(request.form["english"])

        total = maths + science + english
        percentage = total / 3

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        else:
            grade = "C"

        return render_template(
            "index.html",
            name=name,
            total=total,
            percentage=round(percentage, 2),
            grade=grade
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

