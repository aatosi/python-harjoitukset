# - Roskaralli 3000 -

Roskaralli 3000 on pythonilla olio-ohjelmointia hyödyntävä konsolissa pyörivä tekstipohjainen peli.

Pelissä pelaaja on roskannut luontoa ja tuomitaan siksi yhteiskuntapalvelukseen.

Yhteiskuntapalveluksessa pelaajan täytyy siivota kaikki kaupungin ulkoilualueiden roskat.

## Projektin rakenne

**properties.py** Sisältää luokat 'Esine', 'Alue' ja 'Pelaaja'.

**main.py** Sisältää pelin pääohjelman ja peliloopin.

**readme.md** Dokumentaatio projektista.

**ohjeet.txt** Sisältää ohjeet pelin pelaamiseen.

**intro.txt** Sisältää pelin intron tekstin ja ASCII kuvan oikeudenkäynnistä.

**outro.txt** Sisältää pelin lopetuksen tekstin ja ASCII hymiön.

## Pelin ominaisuudet

1. **Käyttäjän tiedot ja iän tarkistus:**
    * Kysyy pelaajan nimen ja iän
    * Tarkistaa että pelaaja on yli 12-vuotias
    * Tallentaa nimen perusteella pelin tilanteen

2. **Päävalikko:**
    * **kerää** komennolla voit kerätä roskia alueeltasi
    * **liiku** komennolla voit siirtyä toiselle ulkoilualueelle
    * **listaa** komennolla näet mitä roskia olet jo kerännyt
    * **tiedot** komennolla näet nimesi, ikäsi, sekä sijaintisi
    * **lopeta** komento sulkee pelin ja tallentaa nykyisen tilanteen

3. **Virheenkäsittely ja hallinta:**
    * Ohjelma tunnistaa tuntemattomat komennot kaatumatta