from flask import Flask, request, render_template, redirect
import csv

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("thankyou.html")
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong, try again.'


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email}, {subject}, {message}")


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        csv_writer = csv.writer(database2, delimiter=' ', quotechar=" ", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(f"\n{email}\n{subject}\n\n{message}\n\n")


if __name__ == "__main__":
    app.run()
