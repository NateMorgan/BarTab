class Tab:

  menu ={
    'wine': 5,
    'beer':3,
    'soft_drink': 2,
    'chicken': 10,
    'beef':15,
    'veggie': 12,
    'dessert': 6
  }

  def __init__(self):
    self.total = 0
    self.items = []

  def orderItem(self, item):
    self.items.append(item)
    self.total += self.menu[item]

  def print_bill(self,tax,service):
    tax = self.total * (tax/100)
    service = self.total  * (service/100)
    total = self.total + tax + service

    for item in self.items:
      print(f'{item:20} ${self.menu[item]}')
    print(f'{"Total:":20} ${total:.2f}')

table1 = Tab()

table1.orderItem('soft_drink')
table1.orderItem('chicken')
table1.orderItem('dessert')
table1.print_bill(10,10)

table2 = Tab()

table2.orderItem('wine')
table2.orderItem('beef')
table2.print_bill(10,10)

