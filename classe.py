from numpy import pi

class circunferencia(object):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return pi*self.raio**2

    def perimetro(self):
        return 2*self.raio*pi

def main():
    a = circunferencia(3)
    b = circunferencia(10)

    print(a.perimetro())
    print(b.perimetro())


if __name__ == "__main__":
    main()
