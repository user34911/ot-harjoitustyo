# Changelog

## Viikko 3
- Lisätty Grid-luokka, joka luo ruudukon ja vastaa laattojen liikuttamisesta
- Mahdollistettu laattojen liikuttaminen jokaiseen suuntaan
- Luotu GameLoop-luokka, joka vastaa pelin silmukasta
- Luoto ruuduille, laatoille ja reunoille jokaiselle oma Sprite luokka, jotka vastaavat väristä ja sijainnista
- Testattu, että Grid luokka luo oikean kokoisen ruudukoin ruudut oikeissa paikossa ja kaksi laattaa

## Viikko 4
- Liike jatkuu nyt niin kauan kunnes osuu toiseen laattaan tai ruudukon reunaan
- Jokaisen liikkeen jälkeen syntyy nyt uusi laatta
- Samanarvoisten laattojen törmätessä toisiinsa ne yhdistyvät
  - Laatat voivat yhdistyä vain kerran liikeessä
- Laatoissa näkyy niiden arvo
- Peli pitää kirjaa pisteistä
- Testejä liikeen toimimisesta ja spritejen konstruktiosta
