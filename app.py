from flask import Flask, render_template, request
from functions.bookin_date.orders import get_orders_table
from functions.department.calculations import test, display_type_table, display_sub_type_table, display_products_table
from classes.time import Time
from classes.db.Con_String import ConString

app = Flask(__name__)


class DataStorage:
    data_dict = {}


dataStorage = DataStorage()


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


# Booking report
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


# Department report
@app.route('/department/', methods=['POST', 'GET'])
def department():
    dataStorage.data_dict = {}

    dataStorage.data_dict['shops_list'] = ConString().get_shop_name()

    return render_template("department/department_index.html",
                           title='Sale by Department Report',
                           shops=dataStorage.data_dict['shops_list'])


@app.route('/department/report', methods=['POST', 'GET'])
def department_report_type():

    dataStorage.data_dict['date_range'] = []

    print(str(request.form['isFullYear']))

    if str(request.form['isFullYear']) == 'false':
        dataStorage.data_dict['date_range'] = [request.form['dateFrom'],
                                               request.form['dateTo']]

    dataStorage.data_dict['shop'] = ConString().get_shop_name(int(request.form['shop']))[0]
    dataStorage.data_dict['obiect_list'] = test(dataStorage.data_dict['shop'][0], dataStorage.data_dict['date_range'])
    dataStorage.data_dict['main_cat_html'] = display_type_table(dataStorage.data_dict['obiect_list'])
    dataStorage.data_dict['title'] = 'Sale by Department Report for ' + dataStorage.data_dict['shop'][1].title()

    return render_template("department/department_type.html",
                           title=dataStorage.data_dict['title'],
                           shop=dataStorage.data_dict['shop'],
                           shops=dataStorage.data_dict['shops_list'],
                           type=dataStorage.data_dict['main_cat_html'],
                           dates=dataStorage.data_dict['date_range'],
                           full_year=request.form['isFullYear']
                           )


@app.route('/department/report/<main_type>/', methods=['POST', 'GET'])
def department_report_subType(main_type):
    dataStorage.data_dict['main_sub_cat_html'] = display_sub_type_table(dataStorage.data_dict['obiect_list'], main_type)

    return render_template("department/department_sub_type.html",
                           title=dataStorage.data_dict['title'],
                           shops=dataStorage.data_dict['shops_list'],
                           main_type_name=main_type,
                           type=dataStorage.data_dict['main_cat_html'],
                           sub_type=dataStorage.data_dict['main_sub_cat_html'],
                           dates=dataStorage.data_dict['date_range'])


@app.route('/department/report/<main_type>/<sub_type>/', methods=['POST', 'GET'])
def department_report_products(main_type, sub_type):
    dataStorage.data_dict['products_html'] = display_products_table(dataStorage.data_dict['obiect_list'],
                                                                    main_type,
                                                                    sub_type)

    return render_template("department/department_products.html",
                           title=dataStorage.data_dict['title'],
                           shops=dataStorage.data_dict['shops_list'],
                           main_type_name=main_type,
                           sub_type_name=sub_type,
                           type=dataStorage.data_dict['main_cat_html'],
                           sub_type=dataStorage.data_dict['main_sub_cat_html'],
                           products=dataStorage.data_dict['products_html'],
                           dates=dataStorage.data_dict['date_range'])


if __name__ == '__main__':
    app.run()
