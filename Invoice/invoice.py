from jinja2 import Environment, FileSystemLoader
import jdatetime
import pdfkit

print(20 * '-', 'customer info', 20 * '-')
order_number = input('order number: ')
customer_name = input('customer name: ')
economical_number = input('economical number: ')
national_code = input('national code: ')
address = input('address: ')
postal_code = input('postal code: ')
phone_number = input('phone number: ')

print(20 * '-', 'product info ', 20 * '-')
number_of_products = int(input('number of products: '))
products = []

for i in range(number_of_products):
    pr = {}
    print(20 * '-', 'product info ', 20 * '-')
    pr['code'] = input('code: ')
    pr['name'] = input('name: ')
    pr['number'] = int(input('number: '))
    pr['unit'] = input('unit: ')
    pr['unit_amount'] = int(input('unit amount: '))
    pr['total_amount'] = pr['unit_amount'] * pr['number']
    pr['discount'] = int(input('discount: '))
    pr['discount_amount'] = pr['total_amount'] - pr['discount']
    pr['tax'] = int(input('tax: '))
    pr['total'] = pr['discount_amount'] + pr['tax']

    products.append(pr)

sum_total = {'sum_unit_amount': 0, 'sum_total_amount': 0, 'sum_discount': 0,
             'sum_discount_amount': 0, 'sum_tax': 0, 's_total': 0}

for product in products:
    sum_total['sum_unit_amount'] += product['unit_amount']
    sum_total['sum_total_amount'] += product['total_amount']
    sum_total['sum_discount'] += product['discount']
    sum_total['sum_discount_amount'] += product['discount_amount']
    sum_total['sum_tax'] += product['tax']
    sum_total['s_total'] += product['total']

term = input('1-cash 2-installment: ')
terms_of_sale = "نقدی" if term == 1 else "قسطی"
description = input('description : ')


context = {
    'order_number': order_number,
    'date': jdatetime.date.strftime(jdatetime.date.today(), "%Y/%m/%d"),
    'customer_name': customer_name,
    'economical_number': economical_number,
    'national_code': national_code,
    'address': address,
    'postal_code': postal_code,
    'phone_number': phone_number,
    'products': products,  # dictionary type
    'sum_total': sum_total,  # dictionary type
    'terms_of_sale': terms_of_sale,
    'description': description,
}


env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template("template.html")

output = template.render(context)

with open(r"templates\new-template.html", mode="w", encoding="utf-8") as tm:
    tm.write(output)


wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"  # path of 'wkhtmltopdf' software
file = r"templates\new-template.html"  # path of html template
confing = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf)
pdfkit.from_file(file, output_path="inv.pdf", configuration=confing)



