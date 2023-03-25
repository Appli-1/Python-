vales_oxxo_gas = 30000
vale_gastado_en_mes = 29900


if vales_oxxo_gas - vale_gastado_en_mes < 0:
    print("estamos en quiebra")
elif vales_oxxo_gas - vale_gastado_en_mes > 200:
    print("estamos bien pa")
else:
    print("nos queda poco pa")
    
resta = vales_oxxo_gas - vale_gastado_en_mes
print(resta) 


restante_es_mayor = vale_gastado_en_mes  and vales_oxxo_gas   #mayor and y menor or

print(restante_es_mayor )
    
    


