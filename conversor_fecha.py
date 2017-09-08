# coding=utf-8

from datetime import datetime


class ConversorFecha:
    def __init__(self):
        self.meses = {'01': 'enero', '02': 'febrero', '03': 'marzo',
                      '04': 'abril', '05': 'mayo', '06': ' junio',
                      '07': 'julio', '08': 'agosto', '09': 'septiembre',
                      '10': 'octubre', '11': 'noviembre', '12': 'diciembre'}

        self.decenas = ['diez', 'veinte', 'treinta', 'cuarenta', 'cincuenta',
                        'sesenta', 'setencha', 'ochenta', 'noventa']

        self.decenas_compuestas = ['veinti', 'treinta y', 'cuarenta y',
                                   'cincuenta y', 'sesenta y', 'setenta y',
                                   'ochenta y', 'noventa y']

        self.centenas = ['ciento', 'doscientos', 'trecientos', 'cuatrocientos',
                         'quinientos', 'seiscientos', 'setecientos',
                         'ochocientos', 'novecientos']

        self.millares = ['mil', 'dos mil', 'tres mil', 'cuatro mil',
                         'cinco mil', 'seis mil', 'siete mil', 'ocho mil',
                         'nueve mil']

        self.once_a_diecinueve = ['once', 'doce', 'trece', 'catorce', 'quince',
                                  'dieciseis', 'diecisiete', 'dieciocho',
                                  'diecinueve', 'veinte']

        self.unidades = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis',
                         'siete', 'ocho', 'nueve']

    def get_fecha_texto(self, fecha):
        try:
            datetime.strptime(fecha, '%d/%m/%Y')
            partes = fecha.split('/')
            dia = self.get_numero_texto(partes[0]).strip()
            mes = self.meses[partes[1]].strip()
            anio = self.get_numero_texto(partes[2]).strip()
            return '%s de %s del %s' % (dia, mes, anio)
        except ValueError:
            return 'fecha inválida'

    def get_numero_texto(self, numero):
        numero_str = ''
        if len(numero) == 4:
            if numero[0] != '0':
                numero_str += self.millares[int(numero[0]) - 1]
            if numero[1] != '0':
                if numero[1] == '1' and (numero[2] != '0' or numero[3] != '0'):
                    numero_str += ' ciento'
                else:
                    numero_str += ' %s' % self.centenas[int(numero[1]) - 1]
            numero = numero[2:]
        unidades_establecidas = False
        if numero[0] != '0':
            if numero[1] == '0':
                numero_str += ' %s' % self.decenas[int(numero[0]) - 1]
            elif numero[0] == '1':
                numero_str += ' %s' % self.once_a_diecinueve[int(numero[1]) - 1]
                unidades_establecidas = True
            else:
                numero_str += ' %s' % self.decenas_compuestas[
                    int(numero[0]) - 2]
        if not unidades_establecidas and numero[1] != '0':
            if numero[0] != '2':
                numero_str += ' '
            numero_str += self.unidades[int(numero[1]) - 1]

        return numero_str
