from tuomari import Tuomari

class KiviPaperiSakset:
    def _ensimmaisen_pelaajan_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_pelaajan_siirto(self, ensimmainen_siirto):
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto in ("k", "p", "s")

    def pelaa(self):
        tuomari = Tuomari()

        while True:
            ekan_siirto = self._ensimmaisen_pelaajan_siirto()
            if not self._onko_ok_siirto(ekan_siirto):
                break

            tokan_siirto = self._toisen_pelaajan_siirto(ekan_siirto)
            if not self._onko_ok_siirto(tokan_siirto):
                break

            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

        print("Kiitos!")
        print(tuomari)
