# Ohjelmistotekniikka, harjoitustyö 2048

_Koko_ perheelle sopiva hassun hauska **2048** peli

## Dokumentaatio
- [työaikakirjanpito](https://github.com/user34911/ot-harjoitustyo/blob/main/2048/dokumentaatio/tuntikirjanpito.md)
- [vaatimusmaarittely](https://github.com/user34911/ot-harjoitustyo/blob/main/2048/dokumentaatio/vaatimusmaarittely.md)
- [changelog](https://github.com/user34911/ot-harjoitustyo/blob/main/2048/dokumentaatio/changelog.md)
- [arkkitehtuuri](https://github.com/user34911/ot-harjoitustyo/blob/main/2048/dokumentaatio/arkkitehtuuri.md)

## Asennus
1. Siirry enshin hakemistoon 2048
2. Asenna sitten riippuvuudet komennolla
```
$ poetry install
```
3. Sen jälkeen voit käynnistää sovelluksen komennolla
```
$ poetry run invoke start
```
## Komentorivikomennot
### Ohjelman suoritus
```
$ poetry run invoke start
```
### Ohjelman testaus
```
$ poetry run invoke test
```
### Testikattavuus
Testikattavuusraportti löytyy htmlcow -hakemistosta
```
$ poetry run invoke coverage-report
```
