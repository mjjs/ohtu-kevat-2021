from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_tekoaly import KPSTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja

class KPSTehdas:
    @staticmethod
    def PelaaMestariTekoalyaVastaan():
        return KPSParempiTekoaly()

    @staticmethod
    def PelaaTekoalyaVastaan():
        return KPSTekoaly()

    @staticmethod
    def PelaaToistaPelaajaaVastaan():
        return KPSPelaajaVsPelaaja()
