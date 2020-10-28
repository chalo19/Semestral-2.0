from django.test import TestCase
import unittest
from .models import MisionyVision

# Create your tests here.

def grabar_mision_y_vision(self):
        m = MisionyVision(
            mision="Garantizar la satisfacción y servicio de excelencia, ofreciendo una alternativa para maximizar el tiempo del cliente, creando la combinación perfecta entre servicio y calidad que provoque la lealtad de nuestros clientes."
            ,vision="Ser una de las empresas más eficientes para el lavado de automóviles en Chile, ofreciendo a cada uno de nuestros clientes soluciones prácticas para el aseo de sus vehículos con la calidad, servicio y compromiso que nos caracteriza, y así poder garantizar la lealtad del consumidor."
        )
        valor=0
        try:
            m.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)

def listar_mision(self):
    lm= MisionyVision.objects.all()
    self.assertIsInstance(lm,MisionyVision)
        
if __name__ == "__main__":
    unittest.main()