from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text_field")  # Get the text from the form
        # Save the text to a file
        with open("saved_text.txt", "w") as file:
            file.write(text)
        
        # Print the text to the terminal
        print("Submitted text:", text)
        
        return render_template("index.html")
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,port=80)
