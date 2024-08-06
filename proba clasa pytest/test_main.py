class Mama:
    def __init__(self, cas, mas):
        self.cas = cas
        self.mas = mas

    def calc(self):
        suma = self.cas + self.mas
        return suma

    def test_calc(self):
        assert self.calc() == 12


def test_cal():
    mama = Mama(5, 7)
    mama.test_calc()