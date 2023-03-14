class Opciones:
    def __init__(self):
        pass

    def genero(self):
        GENERO = (('M', 'Masculino'), ('F', 'Femenino'),)
        return GENERO

    def mes(self):
        MESES = (
        ('Ene', 'Enero'), ('Feb', 'Febrero'), ('Mar', 'Marzo'), ('Abr', 'Abril'), ('May', 'Mayo'), ('Jun', 'Junio'),
        ('Jul', 'Julio'), ('Ago', 'Agosto'), ('Sep', 'Septiembre'), ('Oct', 'Octubre'), ('Nov', 'Noviembre'),
        ('Dic', 'Diciembre'),)
        return MESES

    def masa(self):
            MASA = (('kg', ' Kilogramos'), ('Lb', 'Libras'),)
            return MASA
    # def anio(self):
    #     ANIO = ((),(),(),(),(),())