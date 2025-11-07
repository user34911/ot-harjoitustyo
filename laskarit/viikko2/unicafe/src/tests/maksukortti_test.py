import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertAlmostEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahan_lataus_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertAlmostEqual(self.maksukortti.saldo_euroina(), 15.0)

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(500)
        self.assertAlmostEqual(self.maksukortti.saldo_euroina(), 5.0)

    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertAlmostEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_ottaminen_palauttaa_true_jos_riittää(self):
        palautus = self.maksukortti.ota_rahaa(500)
        self.assertEqual(palautus, True)

    def test_ottaminen_palauttaa_false_jos_ei_riita(self):
        palautus = self.maksukortti.ota_rahaa(1500)
        self.assertFalse(palautus)

    def test_str_palauttaa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
