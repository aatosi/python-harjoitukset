# Roolipelaamispeli 3000

Kyseessä on konsolissa pyörivä kirjoittamalla toimiva roolipeli,
jossa hyödynnetään olio-ohjelmointia Pythonilla.

## Projektin rakenne

**properties.py** Sisältää luokat 'Esine', 'Huone' ja 'Pelaaja'.

**main.py** Sisältää pelin pääohjelman ja peliloopin.

**readme.md** Dokumentaatio projektista.

## Pelin ominaisuudet

1. **Käyttäjän tiedot ja iän tarkistus:**
    * Kysyy pelaajan nimen ja iän
    * Tarkistaa että pelaaja on yli 12-vuotias

2. **Päävalikko:**
    * **kerää** komennolla voit kerätä huoneessa olevan esineen
    * **liiku** komennolla voit siirtyä toiseen huoneeseen
    * **listaa** komennolla näet inventaarion tilanteen
    * **tiedot** komennolla näet nimesi, ikäsi sekä sijaintisi
    * **lopeta** komento sulkee pelin ja kiittää pelaajaa

3. **Virheenkäsittely ja hallinta:**
    * Ohjelma tunnistaa tuntemattomat komennot kaatumatta