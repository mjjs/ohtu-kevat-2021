OLETUS_KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=OLETUS_KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")

        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.lukujoukko = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.lukujoukko

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        self.lukujoukko[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1

        if self.taynna():
            self.kasvata_taulukkoa()

        return True

    def poista(self, n):
        if self.kuuluu(n) is False:
            return False

        self.lukujoukko = [num for num in self.lukujoukko if num is not n]
        self.alkioiden_lkm -= 1

        return True

    def kasvata_taulukkoa(self):
        uusi_taulukko = [n for n in self.lukujoukko] + [0] * self.kasvatuskoko
        self.lukujoukko = uusi_taulukko

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujoukko[i]

        return taulu

    def taynna(self):
        return self.alkioiden_lkm == len(self.lukujoukko)

    @staticmethod
    def yhdiste(a, b):
        yhdistetty_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            yhdistetty_joukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            yhdistetty_joukko.lisaa(b_taulu[i])

        return yhdistetty_joukko

    @staticmethod
    def leikkaus(a, b):
        leikattu_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for n in a_taulu:
            if b.kuuluu(n):
                leikattu_joukko.lisaa(n)

        for n in b_taulu:
            if a.kuuluu(n):
                leikattu_joukko.lisaa(n)

        return leikattu_joukko

    @staticmethod
    def erotus(a, b):
        joukon_erotus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            joukon_erotus.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            joukon_erotus.poista(b_taulu[i])

        return joukon_erotus

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"

        numerot = ", ".join([str(n) for n in self.to_int_list()])
        return f"{{{numerot}}}"
