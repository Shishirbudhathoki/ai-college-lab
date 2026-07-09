from flask import Flask, request, render_template_string
import joblib

app = Flask(__name__)
model = joblib.load("model.joblib")

PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>News Article Categorizer</title>

    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:Arial,sans-serif;
        }

        body{
            background:linear-gradient(135deg,#667eea,#764ba2);
            display:flex;
            justify-content:center;
            align-items:center;
            min-height:100vh;
        }

        .container{
            background:white;
            width:700px;
            padding:30px;
            border-radius:15px;
            box-shadow:0 10px 25px rgba(0,0,0,.2);
        }

        h1{
            text-align:center;
            color:#333;
            margin-bottom:20px;
        }

        textarea{
            width:100%;
            height:220px;
            padding:15px;
            border:2px solid #ccc;
            border-radius:10px;
            font-size:16px;
            resize:none;
        }

        textarea:focus{
            border-color:#667eea;
            outline:none;
        }

        button{
            width:100%;
            margin-top:20px;
            padding:15px;
            border:none;
            border-radius:10px;
            background:#667eea;
            color:white;
            font-size:18px;
            cursor:pointer;
        }

        button:hover{
            background:#4b5fd3;
        }

        .result{
            margin-top:25px;
            padding:15px;
            border-radius:10px;
            background:#f2f6ff;
            text-align:center;
            font-size:22px;
            color:#333;
            font-weight:bold;
        }

        .category{
            color:#667eea;
        }

    </style>
</head>

<body>

<div class="container">

<h1>📰 News Article Categorizer</h1>

<form method="POST">

<textarea
name="article"
placeholder="Paste your news article here..."
required></textarea>

<button type="submit">
Predict Category
</button>

</form>

{% if prediction %}

<div class="result">
Predicted Category :
<span class="category">{{ prediction }}</span>
</div>

{% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def index():

    prediction = None

    if request.method=="POST":

        article = request.form["article"]

        prediction = model.predict([article])[0]

    return render_template_string(PAGE,prediction=prediction)

if __name__=="__main__":
    app.run(debug=True)