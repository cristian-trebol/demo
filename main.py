from cups import Cups

from invoice import Invoice

cups = Cups(cups='ES3431431431', subsistema='Canarias')
print("Pais: " + cups.getPais())
factura = Invoice(cups=cups, iva=0.21, base=100, fecha_inicio_suministro='2020-01-01',
                  fecha_fin_suministro='2020-01-31')
print("Pais desde factura: " + factura.cups.getPais())

print('Total a pagar: ' + str(factura.total_a_pagar()))
