# define complex number class and small test
import math

class complex:
    # constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    # add two complex numbers
    def add(self, other):
        return complex(self.real + other.real, self.imag + other.imag)
    # subtract two complex numbers
    def subtract(self, other):
        return complex(self.real - other.real, self.imag - other.imag)
    # multiply two complex numbers
    def multiply(self, other):
        return complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
    # divide two complex numbers
    def divide(self, other):
        denom = other.real ** 2 + other.imag ** 2
        return complex((self.real * other.real + self.imag * other.imag) / denom, (self.imag * other.real - self.real * other.imag) / denom)
    # convert rectangular to polar coordinates
    def rect2polar(self):
        return math.sqrt(self.real **2 + self.imag**2), math.degrees(math.atan2(self.imag, self.real))
    # get complex conjugate
    def complex_conjugate(self):
        return complex(self.real, -self.imag)
    # convert polar to rectangular coordinates
    def polar2rect(self, r, theta):
        return complex(r * math.cos(theta), r * math.sin(theta))
    # print complex number in rectangular form
    def print(self):
        print(f"{self.real} + {self.imag}i")
    # get polar coordinates of complex number
    def print_polar(self):
        r, theta = self.rect2polar()
        print(f"{r} ∠ {theta}")

z1 = complex(2,7)
z2= complex(3,5)

z1.print()

z2.print()

print("__________")
sum = z1.add(z2)

sum.print()
sum.print_polar()