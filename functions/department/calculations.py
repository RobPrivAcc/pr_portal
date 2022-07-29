from classes.db.Con_String import ConString
from classes.db.connection import SqlQuery
from classes.html.table import Table
from classes.department.DepartmentProduct import DepartmentProduct
from classes.department.Calculations import Calculations
from classes.TimeDate import TimeDate

types_list = []

dates = (TimeDate()).get_last_and_current_year()


def test(shop_no):
    # sql = f'''SELECT [Type of Item], [SubType], [Name of item], SUM([QuantityBought] * [Priceofitem]) as [value]
    #                     FROM Orders
    #                         inner join Stock on [Name of Item] = replace([NameOfItem],' ** Product Return  ** : ','')
    #                         inner join [Days] on [Order Number] = OrderNo
    #                     WHERE
    #                         [Date] > '2022-06-01 00:00:01' AND
    #                         [Date] < '2022-06-30 23:59:59'
    #                         --AND [Type of Item] = 'Aquatic'
    #                         --and [SubType] = 'Decoration - Substrate'
    #                         group by [Type of Item], [SubType], [Name of item] order by [Type of Item], [SubType];'''

    sql = f'''SELECT [Type of Item], [SubType], [Name of item], 

        ISNULL((select SUM([QuantityBought] * [Priceofitem]) 
            FROM
                Orders
                inner join [Days] on [Order Number] = OrderNo
            WHERE
                NameOfItem = s.[Name of Item] and
                [Date] BETWEEN '{dates[0][0]} 00:00:01' AND '{dates[0][1]} 23:59:59'), '0') as value1,
        
        ISNULL((select SUM([QuantityBought] * [Priceofitem]) 
            FROM
                Orders
                inner join [Days] on [Order Number] = OrderNo
            WHERE
                NameOfItem = s.[Name of Item] and
                [Date] BETWEEN '{dates[1][0]} 00:00:01' AND '{dates[1][1]} 23:59:59'),'0') as value2

    FROM Orders o
        inner join Stock s on s.[Name of Item] = replace(o.[NameOfItem],' ** Product Return  ** : ','') 

    GROUP BY [Type of Item], [SubType], [Name of item]
    order by [Type of Item], [SubType], [Name of item]'''

    l = ConString().get_string(shop_no)

    orde = SqlQuery(l).query_execute(sql)

    orders_list = []
    # types_list = []

    for o in orde:
        if float(o[3]) > 0 or float(o[4]) > 0:
            orders_list.append(o)
            product = DepartmentProduct()
            product.set_name(o[2])
            product.set_categories(o[0], o[1])
            product.add_year(dates[0][0][:4], o[3])
            product.add_year(dates[1][0][:4], o[4])
            types_list.append(product)

    return types_list
    # return orders_list


def display_type_table(obiect):
    header = ['Type',
              '2021',
              '2022',
              'Growth %']
    cal = Calculations(obiect)

    departments_dic = {'header': header,
                       'row': cal.summarise_type()}
    table_param = {'id': "departmentTable",
                   'class': ["selectedCatRow"]}
    return display_table(departments_dic, table_param)


def display_sub_type_table(obiect, mainType):
    header = ['Sub Type',
              '2021',
              '2022',
              'Growth %']
    cal = Calculations(obiect)

    departments_dic = {'header': header,
                       'row': cal.summarise_sub_type(mainType)}

    table_param = {'id': "sub_typeTable",
                   'class': ["selectedSubCatRow"]}

    return display_table(departments_dic, table_param)


def display_products_table(obiect, mainType, subType):
    header = ['Product Name',
              '2021',
              '2022',
              'Growth %']
    cal = Calculations(obiect)

    departments_dic = {'header': header,
                       'row': cal.summarise_products(mainType, subType)}

    table_param = {'id': "productsTable",
                   'class': ["selectedProductsRow"]}

    return display_table(departments_dic, table_param)


def display_table(header, param):
    table = Table(header, True)
    table.add_table_id(param['id'])
    table.enable_row_class(param['class'])
    return table.get_table()
