# Käyttöohje
Lataa projektin lähdekoodi kohdasta [releases](https://github.com/user34911/ot-harjoitustyo/releases)

## Ohjelman käynnistys
Purettua ohjelman lähdekoodin sopivaan hakemistoon siirry kansioon `\2048\`.

Tämän jälkeen suorita hakemistossa komento
```
poetry install
```
Jonka jälkeen ohjelma käynnistyy komennolla
```
poetry run invoke start
```

## Ohjelman käyttö
Pelin tavoite normaalissa pelimuodossa yhdistää samanarvoisia laattoja saaden mahdollisimman suuren määrän pisteitä ennen ruudukon täyttymistä. Ajastetussa pelimuodossa tavoite on saada **2048** mahdollisimman nopeasti.

### Päävalikko
Päävalikossa on kolme painikitta `Exit` painike sulkee pelin, `Leaderboards` painike avaa tulostaulukon ja `Start` avaa pelin aloitusasetukset. Tulostaulukosta ja aloitusasetuksista takaisin päävalikkoon pääsee painamalla
`Esc` näppäintä tai `Back` painiketta.

### Tulostaulukko
Tulostaulukossa voit hiiren rullalla, tai sivupalkkia vetämällä mennä taulukkoa ylös tai alas. `Esc` näppäin sulkee taulukon.

### Aloitusasetukset
Aloitusasetuksissa on `Timed mode` valintaruutu, jonka aktivoimalla peli alkaa ajastetussa pelimuodossa. Lisäksi valittavan on `Grid size` pudotusvalikko, josta ruudukon koon voi valita.
Peli alkaa painamalla `Start` nappia.

### Peli
Itse pelissa laattoja voi liikutta joko `WASD` näppäimillä, tai nuolinäppäimillä. Pelistä voi palata päävalikkoon painamalla `Esc` näppäintä, tällöin tulos ei tallennu tulostaulukkoon.

### Peli ohi
Kun ruudussa lukee _Game Over_ on peli tallentanut tuloksen tulostaulukkoon ja `Esc` näppäin palauttaa takaisin päävalikkoon.

