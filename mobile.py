mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here
#  Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT

mobile_info = mobile_data.get('data')
exchange_rate = mobile_data.get('exchnage_rate')
for info in mobile_info:
    mobile_name = info.get('name')
    mobile_price = float(info.get('price').strip('USD'))
    bdt_rate = round(mobile_price * exchange_rate)
    made_in = info.get('made')
    output = f'{mobile_name} is made in {made_in}. The price is {mobile_price} which is almost equal to {bdt_rate} BDT'
    print(output)