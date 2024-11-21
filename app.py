from flask import Flask, request, jsonify, Response, render_template
import markdown
app =Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/main")
def Main():
    return render_template("change.html")

@app.route("/testing")
def Testing():
    return "Tested OK"

@app.route("/tohtml", methods=["GET","POST"])
def text_to_html():
    # data = request.get_json()
    # content = data.get("toconvert")
    # print(content)
    content = request.form.get("toconvert")
    print(content)
    if not content:
        return "No text provided for conversion.", 400
    converted_data = markdown.markdown(content)
    # return converted_data
    return render_template("output.html", con=converted_data)

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True, port=5000)
