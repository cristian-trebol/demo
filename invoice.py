from UtilsFecha import UtilsFecha


class Invoice:
    def __init__(self,cups,iva,base,fecha_inicio_suministro,fecha_fin_suministro):
        self.cups = cups
        self.iva = iva
        self.base = base
        if UtilsFecha().fecha_fin_mayor_a_inicio(fecha_inicio_suministro,fecha_fin_suministro):
            self.fecha_inicio_suministro = fecha_inicio_suministro
            self.fecha_fin_suministro = fecha_fin_suministro
        else:
            raise Exception('Fechas mal')
    def total_a_pagar(self):
        return self.base * self.iva
