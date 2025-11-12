# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on 2048 peli.

## Perusversion toiminnallisuus
- 4x4 ruudukko, jossa peli toimii
  - Jokaisella liikkeellä syntyy ruudukkoon uusi 2- tai 4-laatta
  - Laatat liikkuvat syötettä vastaavaan reunaan
  - Laatat yhdistyvät törmätessä toiseen samanarvoiseen
  - Kun ruudukkoo täyttyy on peli ohi
- Peli pitää kirjaa pisteistä
  - Pisteet lasketaan kaavalla laatta $2^n$ antaa $(n-1)2^n$ lisää pisteitä
- Pelissä on tulostaulukko
  - Käyttäjä voi asettaa kirjautumatta nimimerkin, jolla tuloksia tallenetaan
  - Käyttäjä voi nähdä tulostaulukon käyttöliittymästä
  - Peli tallentaa tuloksen tulostaulukkoon automaattisesti

## Jatkokehitys (jos aikaa niin)
- Ajastettu pelimuoto, jossa tavoite saadaa 2048 mahdollisimman nopeasti
- Itse valittava ruudukon koko
- "Undo" toiminallisuus, joka kumoaa edellisen siirron
- "Katkaisuhoito" toiminallisuus, joka poistaa ruudukosta pienet laata
- Laajennettu tulostaulukko sisältämään ajastetun pelimuodon
