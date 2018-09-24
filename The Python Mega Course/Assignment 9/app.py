from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jessequinn:9155@localhost/height_collector'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email_ = db.Column(db.String(120), unique=True, nullable=False)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        height = request.form['height_name']

        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            send_email(email, height)
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            return render_template('success.html')

    return render_template('index.html', text='Email exists')


if __name__ == '__main__':
    app.debug = True
    app.run()
