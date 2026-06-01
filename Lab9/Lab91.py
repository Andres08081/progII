from abc import ABC, abstractmethod

class Vehiculo(ABC): 

    @abstractmethod
    def arrancar(self):
        """Método abstracto: obligatorio implementar en el hijo."""
        pass

    def pitar(self):
        """Método normal: ya tiene lógica heredable."""
        print("¡Beep beep!")

class Moto(Vehiculo):
    def arrancar(self):
        print("La moto ha arrancado.")


mi_moto = Moto()
mi_moto.arrancar()  
mi_moto.pitar()     
