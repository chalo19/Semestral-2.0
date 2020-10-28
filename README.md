Casos de prueba

Nuestro grupo desarrollo distintos casos de prueba segun lo necesitado por el usuario para este proyecto los cuales son:

1. grabar_mision_y_vision

Este caso de prueba permite grabar tanto la mision como a su vez la vision de la empresa que se puede administrar por el administrador y esta sera visualizada en la pagina
final del prototipo

CODIGO: m = MisionyVision(
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

2. listar_mision

CODIGO: def listar_mision(self):
    lm= MisionyVision.objects.all()
    self.assertIsInstance(lm,MisionyVision)
    
if __name__ == "__main__":
    unittest.main()

Este caso de prueba permite ejecutar o visualizar correctamente la mision en la pagina web.
