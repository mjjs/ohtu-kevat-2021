from tuomari import Tuomari
from kps import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_pelaajan_siirto(self, ensimmainen_siirto):
        return input("Toisen pelaajan siirto: ")
