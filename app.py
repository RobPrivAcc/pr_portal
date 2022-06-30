from flask import Flask, render_template, request
from functions.bookin_date.orders import get_orders_table

from classes.time import Time
from classes.db.Con_String import ConString

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route('/bookin/')
def bookin():
    return render_template("bookin_date/bookin.html",
                           title='Book in date report',
                           date=Time(),
                           shops=ConString().get_shop_name())


@app.route('/bookin/report', methods=['POST', 'GET'])
def bookin_report():
    shop = ConString().get_shop_name(int(request.form['shop']))[0]
    months = request.form['months']
    years = request.form['years']
    date_range = Time.month_range(int(months), int(years))

    return render_template("bookin_date/bookin_report.html",
                           title='Book in date report ' + shop[1].title()
                                 + " ("
                                 + date_range[0] + ' - '
                                 + date_range[1] + ")",
                           date=Time(),
                           range=date_range,
                           shops=ConString().get_shop_name(),
                           payload=get_orders_table(int(shop[0]), date_range)
                           )


if __name__ == '__main__':
    app.run()
