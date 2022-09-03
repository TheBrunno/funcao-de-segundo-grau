from math import sqrt


a = str(input("Insira o valor de a: "))
b = str(input("Insira o valor de b: "))
c = str(input("Insira o valor de c: "))


class CalcRaiz:
    def __init__(self, a, b, c):
        self.raiz=0
        try:
            self.a = int(a)
            self.b = int(b)
            self.c = int(c)
        except(TypeError, ValueError):
            print("Insira valores validos")
        else:
            self.delta = (self.b*self.b)-4*self.a*self.c
            if self.delta > 0:
                self.raiz=2
            elif self.delta == 0:
                self.raiz=1
            if self.delta < 0:
                self.raiz=-1
            else:
                print(self.calcBhaskara())
            print(self.calcVertice())

    def calcBhaskara(self):
        if self.raiz == 2 or self.raiz == 1:
            self.raizUm = (-self.b+sqrt(self.delta))/2*self.a
            if self.raiz == 2:
                self.raizDois = (-self.b-sqrt(self.delta))/2*self.a
        return self.raizUm, self.raizDois

    def calcVertice(self):
        self.xv = -self.b/(2*self.a)
        self.yv = -self.delta/(4*self.a)
        return self.xv, self.yv

delta = CalcRaiz(a, b, c)