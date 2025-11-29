import numpy as np

class Lingkaran:
    def __init__(self, pusatx, pusaty, radius):
        self.radius = radius
        self.pusatx = pusatx
        self.pusaty = pusaty
    
    def getPusat(self):
        return self.pusatx, self.pusaty

    def getRadius(self):
        return self.radius

    def Luas(self):
        return np.pi * (self.radius ** 2)

    def Keliling(self):
        return 2 * np.pi * self.radius 

    def A(self):
        return -2 * self.pusatx

    def B(self):
        return -2 * self.pusaty
    
    def C(self):
        return self.pusatx**2 + self.pusaty**2 - self.radius**2

    def returnHasil(self):
        return f"""
Pusat                 : ({self.pusatx}, {self.pusaty})
Radius                : {self.radius}
Luas                  : {self.Luas()}
Keliling              : {self.Keliling()}
Rumus bentuk pertama  : (x - {self.pusatx})² + (y - {self.pusaty})² = {self.radius ** 2}
Rumus bentuk kedua    : x² + y² - {self.A()}x - {self.B()}y + {self.C()} = 0
        """

class LingkaranPusatO(Lingkaran):
    def __init__(self, radius):
        super().__init__(0, 0, radius)

    def returnHasil(self):
        return f"""
Pusat                 : (0, 0)
Radius                : {self.radius}
Luas                  : {self.Luas()}
Keliling              : {self.Keliling()}
Rumus bentuk pertama  : x² + y² = {self.radius ** 2}
Rumus bentuk kedua    : x² + y² - {self.radius ** 2} = 0
        """

