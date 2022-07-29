from classes.db.Con_String import ConString
from classes.db.connection import SqlQuery
from classes.order import Order
from classes.html.table import Table


def get_orders(shop_no: int, dates: list):
    query = f'''SELECT [DateTime] as 'BookedInDate'
      ,[DateOrdered]
      ,[Action]
      ,[CurrentUser]
	  ,[Supplier]
	  ,[InvoiceRef]
      ,[GeneratedBy]
      ,(select sum(Price * TotalCheckedQuantity) From RepSub Where OrderNo = SUBSTRING([Action], CHARINDEX('#', [Action]) + 1, len([Action]) - CHARINDEX('#', [Action]))) as 'TotalCost'
      ,[Expenses]
      ,SUBSTRING([Action], CHARINDEX('#', [Action]) + 1, len([Action]) - CHARINDEX('#', [Action])) as 'OrderNumber'
  FROM [ActionLog]
  inner join RepMain on RepOrderNo = SUBSTRING([Action], CHARINDEX('#', [Action]) + 1, len([Action]) - CHARINDEX('#', [Action]))
 where [Action] like 'Replenishment Order INCREASED%' and [DateTime] BETWEEN '{dates[0]} 00:00:01' and '{dates[1]} 23:59:59'
 ORDER BY [DateTime]
 '''

    l = ConString().get_string(shop_no)

    orde = SqlQuery(l).query_execute(query)

    orders_list = []

    for o in orde:
        orders_list.append(Order(o))

    return orders_list


def get_orders_table(shop_no: int, dates: list):
    order_table_list = []
    for order in get_orders(shop_no, dates):
        order_table_list.append(order.display())

    table_content = {'header': ['Order Number',
                                'Ordered Date',
                                'Booked Date',
                                'Invoice reference',
                                'Created By',
                                'Supplier',
                                'Total checked value',
                                'Expenses'],
                     'row': order_table_list}

    table = Table(table_content, True)
    table.enable_filters('myFunction')
    table.add_table_id("bookInTable")

    return table.get_table()
