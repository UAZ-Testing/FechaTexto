# coding=utf-8

import unittest
from conversor_fecha import ConversorFecha


class CalculadoraTest(unittest.TestCase):
    # Test fixtures

    def setUp(self):
        self.conversor = ConversorFecha()

    def tearDown(self):
        pass

    # Pruebas de fechas inválidas

    def test_fecha_formato_invalido_1(self):
        self.assertEqual(self.conversor.get_fecha_texto('qwerqwrwq'),
                         'fecha inválida')

    def test_fecha_formato_invalido_2(self):
        self.assertEqual(self.conversor.get_fecha_texto('1/6/12'),
                         'fecha inválida')

    # Pruebas de fechas válidas

    def test_fecha_pasada_1(self):
        self.assertEqual(self.conversor.get_fecha_texto('06/04/0355'),
                         'seis de abril del trecientos cincuenta y cinco')

    def test_fecha_pasada_2(self):
        self.assertEqual(self.conversor.get_fecha_texto('12/12/0035'),
                     'doce de diciembre del treinta y cinco')

    def test_fecha_pasada_3(self):
        self.assertEqual(self.conversor.get_fecha_texto('01/02/0001'),
                     'uno de febrero del uno')

    def test_fecha_pasada_4(self):
        self.assertEqual(self.conversor.get_fecha_texto('02/11/1001'),
                     'dos de noviembre del mil uno')

    def test_fecha_pasada_5(self):
        self.assertEqual(self.conversor.get_fecha_texto('12/08/1800'),
                         'doce de agosto del mil ochocientos')

    def test_fecha_pasada_6(self):
        self.assertEqual(self.conversor.get_fecha_texto('28/09/1999'),
                     'veintiocho de septiembre del mil novecientos noventa y '
                     'nueve')

    def test_fecha_pasada_7(self):
        self.assertEqual(self.conversor.get_fecha_texto('10/08/2014'),
                         'diez de agosto del dos mil catorce')

    def test_fecha_futura_1(self):
        self.assertEqual(self.conversor.get_fecha_texto('12/04/9000'),
                         'doce de abril del nueve mil')

    def test_fecha_futura_2(self):
        self.assertEqual(self.conversor.get_fecha_texto('31/12/9999'),
                         'treinta y uno de diciembre del nueve mil '
                         'novecientos noventa y nueve')

    def test_fecha_futura_3(self):
        self.assertEqual(self.conversor.get_fecha_texto('10/09/2017'),
                         'diez de septiembre del dos mil diecisiete')



# Ejecuta las pruebas implementadas

if __name__ == '__main__':
    unittest.main()
