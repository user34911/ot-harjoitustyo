import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)
        self.koyhakortti = Maksukortti(100)

    def test_luotu_kassapaate_olemassa(self):
        self.assertIsNotNone(self.kassapaate)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_myytyjen_lounaiden_maara_alussa_oikein(self):
        maara = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(maara, 0)
    
    def test_lounaiden_maara_kasvaa_kun_syodaan_edullisesti_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_lounaiden_maara_kasvaa_kun_syodaan_edullisesti_kortilla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_lounaiden_maara_kasvaa_kun_syodaan_maukkaasti_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_lounaiden_maara_kasvaa_kun_syodaan_maukkaasti_kortilla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_edullinen_kateismaksu_antaa_oikean_vaihtorahan(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(vaihto, 10)
    
    def test_maukas_kateismaksu_antaa_oikean_vaihtorahan(self):
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(vaihto, 10)

    def test_edullinen_kateismaksu_kasvattaa_kassan_saldoa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
    
    def test_maukas_kateismaksu_kasvattaa_kassan_saldoa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)

    def test_jos_edullinen_kateismaksu_ei_riita_kassa_saldo_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_jos_maukas_kateismaksu_ei_riita_kassa_saldo_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_jos_edullinen_kateismaksu_ei_riita_myytyjen_maara_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_jos_maukas_kateismaksu_ei_riita_myytyjen_maara_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_jos_edullinen_kateismaksu_ei_riita_palautetaan_se(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(50)
        self.assertAlmostEqual(vaihto, 50)

    def test_jos_maukas_kateismaksu_ei_riita_palautetaan_se(self):
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(50)
        self.assertAlmostEqual(vaihto, 50)

    def test_jos_kortilla_rahaa_edulliseen_veloitetaan_se(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertAlmostEqual(self.kortti.saldo_euroina(), 7.6)

    def test_jos_kortilla_rahaa_maukkaaseen_veloitetaan_se(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertAlmostEqual(self.kortti.saldo_euroina(), 6.0)
    
    def test_jos_kortilla_rahaa_edulliseen_palautetaan_true(self):
        arvo = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertTrue(arvo)

    def test_jos_kortilla_rahaa_maukkaaseen_palautetaan_true(self):
        arvo = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertTrue(arvo)
    
    def test_jos_kortilla_rahaa_edulliseen_kasvaa_myyty_maara(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_jos_kortilla_rahaa_maukkaaseen_kasvaa_myyty_maara(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_jos_kortilla_ei_varaa_edulliseen_pysyy_saldo(self):
        self.kassapaate.syo_edullisesti_kortilla(self.koyhakortti)
        self.assertAlmostEqual(self.koyhakortti.saldo_euroina(), 1)

    def test_jos_kortilla_ei_varaa_maukkaaseen_pysyy_saldo(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.koyhakortti)
        self.assertAlmostEqual(self.koyhakortti.saldo_euroina(), 1)
    
    def test_jos_kortilla_ei_varaa_edulliseen_pysyy_myyty_maara(self):
        self.kassapaate.syo_edullisesti_kortilla(self.koyhakortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_jos_kortilla_ei_varaa_maukkaaseen_pysyy_myyty_maara(self):
        self.kassapaate.syo_edullisesti_kortilla(self.koyhakortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_jos_kortilla_ei_varaa_edulliseen_palauttaa_false(self):
        arvo = self.kassapaate.syo_edullisesti_kortilla(self.koyhakortti)
        self.assertFalse(arvo)

    def test_jos_kortilla_ei_varaa_maukkaaseen_palauttaa_false(self):
        arvo = self.kassapaate.syo_maukkaasti_kortilla(self.koyhakortti)
        self.assertFalse(arvo)
    
    def test_kassaan_rahamaara_ei_muutu_ostaessa_kortilla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_kortille_ladatessa_saldo_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 100)
        self.assertAlmostEqual(self.kortti.saldo_euroina(), 11.0)
    
    def test_kortille_ladattaessa_kassa_saldo_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1001.0)
    
    def test_kortille_negatiivisen_summan_lataus_ei_muuta_kassaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -100)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_kortille_negatiivisen_summan_lataus_ei_muuta_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -100)
        self.assertAlmostEqual(self.kortti.saldo_euroina(), 10.0)