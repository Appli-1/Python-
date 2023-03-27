# introducimos los input para poner cuanto dinero tenemos
yuan = int(input('Cuantos yuan tines? '))
yen = int(input('Cuantos yen tines? '))
won = int(input('Cuantos won tines? '))

#convertimos los yuanes, yen, won a dolares
total_usd = (yuan*0.15)+(yen*0.0076)+(won*0.00077)
#tenemos el total en dolares
print('total dolares'+ str(total_usd ))
