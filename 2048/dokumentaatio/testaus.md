# Testaus
Ohjelma on testattu automatisoidusti yksikkö- ja integraatiotesteillä, sekä manuaalisesti

## Yksikkö- ja integraatiotestaus
Pelin logiikasta vastaava `Grid` luokka on testattu laajasti, oikeanlaisesta konstruktiosta funktioiden oikealliseen toimintaan yhdessä. Lisäksi `Tile`, `Cell` ja `Border` luokat ovat testattu oikeanlaisen konstruktion
suhteen. Myös pisteidenlaskusta vastaava luokka `Score` ja asetuksista vastaava `Options` on kattavasti testattu.

### Testikattavuus
Eri käyttöliittymän ikkunoita lukuunottamatta testien haaraumakattavuus on 52%

<img width="802" height="687" alt="kuva" src="https://github.com/user-attachments/assets/d17c0402-bafe-45d7-9926-a8b844575d6c" />

Testaamatta jäivät silmukoista, sekä niiden luonnista/hallinnasta vastaavat luokat.

## Järjestelmätestaus
Sovelluksen testaus on suoritettu manuaalisesti.

### Toiminnallisuudet
Määrittelydokumentin kuvaamat toiminnallisuudet on testattu sekä Linux-, että Windows-ympäristössä. Myös odottamattomia näppäinpainalluksia on testattu.

## Sovellukseen jääneet laatuongelmat
Sovellus ei vahdi käyttäjänimen pituutta, joka saattaa aiheuttaa virheilmoituksia.
