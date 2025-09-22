from flask import Flask, render_template
from faker import Faker

fake = Faker("ko-kr")

app = Flask(__name__)

users = []
for i in range(50):
    users.append({"name":fake.name(), "phone":fake.phone_number(), "email":fake.email(), "address":fake.address()})

@app.route("/")
def read_item():
    return render_template("index.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)