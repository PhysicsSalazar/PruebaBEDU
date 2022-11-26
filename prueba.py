#Creamos valores para nuestros datos
descuento=0.12
lista_de_precios=[14.27, 268.28, 18.61, 503.90, 16.75, 139.36, 202.77, 95.32]

#Calculamos el subtotal usando un ciclo for
subtotal=0
for precio in lista_de_precios:
    subtotal=subtotal + precio

#Calculamos el valor de descuento
    valor_de_descuento=subtotal * descuento

#Calculamos el valor total a pagar
    total_a_pagar=subtotal - valor_de_descuento

#Redondeamos a dos cifras por que los datos son monedas
    total_a_pagar=round(total_a_pagar,2)

#Imprimimos el resultado
print("El total es:",total_a_pagar)
