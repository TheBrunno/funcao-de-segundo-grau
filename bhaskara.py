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
            print("-"*20)
            print("Descriminante delta")
            print("-"*20)
            self.delta = (self.b*self.b)-4*self.a*self.c
            if -4*self.a*self.c > 0:
                sinal = '+'
            else:
                sinal = ''
            print(f"Δ = b²-4*a*c\nΔ = ({self.b})²-4*({self.a})*({self.c})\nΔ = {self.b*self.b}{sinal}{-4*self.a*self.c}\nΔ = {self.delta}")
            i=1
            while True:
                if self.delta >= 0:
                    if i == 2:
                        print(f" | Raizes: ({self.raizUm}, {self.raizDois})", end="")
                        break
                    self.calcBhaskara()
                self.calcVertice()
                print("Resultados: ")
                print(f"a={self.a} | b={self.b} | c={self.c}\nΔ={self.delta} | Vertice: ({self.xv}, {self.yv})", end="")
                i+=1
                if self.delta < 0:
                    break

    def calcBhaskara(self):
        print("-"*20)
        print("Bhaskara")
        print("-"*20)
        print(f"x = (-b ± √Δ)/2a\nx = (-({self.b}) ± √{self.delta})/2*({self.a})\nx = ({-self.b} ± {sqrt(self.delta)})/{self.a*2}")
        self.raizUm = (-self.b+sqrt(self.delta))/2*self.a
        print("-"*20)
        print(f"x1 = ({-self.b} + {sqrt(self.delta)})/{self.a*2}\nx1 = {-self.b+sqrt(self.delta)}/{self.a*2}\nx1 = {(-self.b+sqrt(self.delta))/(self.a*2)}")
        self.raizDois = (-self.b-sqrt(self.delta))/2*self.a
        print("-"*20)
        print(f"x2 = ({-self.b} - {sqrt(self.delta)})/{self.a*2}\nx2 = {-self.b-sqrt(self.delta)}/{self.a*2}\nx2 = {(-self.b-sqrt(self.delta))/(self.a*2)}")

    def calcVertice(self):
        print("-"*20)
        print("Vertice")
        print("-"*20)
        self.xv = -self.b/(2*self.a)
        self.yv = -self.delta/(4*self.a)
        print(f"Xᵥ = -b/2*a\nXᵥ = -({self.b})/2*({self.a})\nXᵥ = {-self.b}/({2*self.a})\nXᵥ = {self.xv}")
        print("-"*20)
        print(f"Yᵥ = -Δ/4*a\nYᵥ = -({self.delta})/4*({self.a})\nYᵥ = {-self.delta}/({4*self.a})\nYᵥ = {self.yv}")
        print("-"*20)

delta = CalcRaiz(a, b, c)