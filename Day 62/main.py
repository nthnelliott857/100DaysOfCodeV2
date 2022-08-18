from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, InputRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
FIELDS = []

class MyInputRequired(InputRequired):
    field_flags = ()

class CafeForm(FlaskForm):
    fields = {}
    cafe = StringField(label='Cafe name', validators=[MyInputRequired()])
    # cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField(label='location', validators=[MyInputRequired(), URL(require_tld=True, message="Invalid URL")])
    open = StringField(label='open', validators=[MyInputRequired()])
    close = StringField(label='close', validators=[MyInputRequired()])
    coffee = StringField(label='coffee', validators=[MyInputRequired()])
    wifi = StringField(label='wifi', validators=[MyInputRequired()])
    power = StringField(label='power', validators=[MyInputRequired()])
    submit = SubmitField(label='Submit')
    fields['cafe'] = cafe
    # fields['location'] = location
    # fields['open']= open
    # fields['close']= close
    # fields['coffee']= coffee
    # fields['wifi']= wifi
    # fields['power']= power

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")



@app.route('/add', methods=["GET", "Post"])
def add_cafe():
    form = CafeForm()
    if request.method == 'GET':
        return render_template('add.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            # for field in form.fields.keys():
            #     print(form.fields[field])
            data = [form.cafe.data, form.location.data, form.open.data, form.close.data, form.coffee.data,
                    form.power.data, form.wifi.data]
            to_write = "\n"
            for item in data:
                to_write += f"{item},"
            to_write = to_write[0:len(to_write) - 1]
            print(data)
            print(to_write)
            f = open('static/cafe-data.csv', mode='a', encoding='UTF-8')
            f.write(to_write)
            f.close()
            return render_template('add.html', form=form)
        else:
            return render_template('add.html', form=form)
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()



@app.route('/cafes')
def cafes():
    with open(r'static/cafe-data.csv', newline='', encoding='UTF-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        global FIELDS
        FIELDS = list_of_rows[0]
        # print(list_of_rows)
    # return render_template('cafes.html')
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
