harga = 350
quantity=350

if quantity > 200:
    if quantity > 500:
        print('total lebih dari 500')
    elif quantity < 500 and harga >300:
        print('totalnya antara 300 dan 500')
    else:
        print('totalnya antara 200 dan 500')
elif quantity==200:
    print('totalnya ada 200')
else:
    print('total kurang dari 200')