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

## Viikko 5
- Paranneltu ulkonäköä
- Lisätty Main Menu, jossa aloitus-, tulostaulukko- ja positumisnappi
- Pelissä on tulostaulukko, joka kirjaa automaattisesti tulokset
- Lisätty testejä laattojen yhdistymiseen ja lisäämiseen littyen

## Viikko 6
- Peli ei enään heitä suoraan päävalikkoon kun peli ohi
- Liästty ikkuna pelin aloitusasetusten valinnalle
- Lisätty ajastettu pelimuoto