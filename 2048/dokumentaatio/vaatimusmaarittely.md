# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on 2048 peli.

## Perusversion toiminnallisuus
- 4x4 ruudukko, jossa peli toimii
  - Jokaisella liikkeellä syntyy ruudukkoon uusi 2- tai 4-laatta :heavy_check_mark:
  - Laatat liikkuvat syötettä vastaavaan reunaan :heavy_check_mark:
  - Laatat yhdistyvät törmätessä toiseen samanarvoiseen :heavy_check_mark:
  - Kun ruudukkoo täyttyy on peli ohi :heavy_check_mark:
- Peli pitää kirjaa pisteistä :heavy_check_mark:
  - Pisteet lasketaan kaavalla laatta $2^n$ antaa $(n-1)2^n$ lisää pisteitä :heavy_check_mark:
- Pelissä on tulostaulukko :heavy_check_mark:
  - Käyttäjä voi asettaa kirjautumatta nimimerkin, jolla tuloksia tallenetaan
  - Käyttäjä voi nähdä tulostaulukon käyttöliittymästä :heavy_check_mark:
  - Peli tallentaa tuloksen tulostaulukkoon automaattisesti :heavy_check_mark:

## Jatkokehitys (jos aikaa niin)
- Ajastettu pelimuoto, jossa tavoite saadaa 2048 mahdollisimman nopeasti
- Itse valittava ruudukon koko
- "Undo" toiminallisuus, joka kumoaa edellisen siirron
- "Katkaisuhoito" toiminallisuus, joka poistaa ruudukosta pienet laata
- Laajennettu tulostaulukko sisältämään ajastetun pelimuodon
