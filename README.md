# TeamBoaOHTU2021
[Klikkaa tästä päästäksesi käyttämään sovellusta](https://lukuvinkki-boa.herokuapp.com/)

Herkussa tietokanta on alustettu tyhjäksi. Tiimi on käyttänyt demoamiseen käyttäjätunnusta *TeamBoa* salasanalla *boa123*, joita voi käyttää halutessaan testailuun jo joillain lisätyillä vinkeillä.

---

![GitHub Actions](https://github.com/UncleRovo/TeamBoaOHTU2021/workflows/CI/badge.svg)

[Backlog (Team use)](https://helsinkifi-my.sharepoint.com/:x:/g/personal/karhelmi_ad_helsinki_fi/EUyjfZObbRtEktjglZIfjqkBznpw83N5DPR699B00N6RFQ?e=fe2MUZ)

[Product Backlog and Burndown Chart](https://helsinkifi-my.sharepoint.com/:x:/g/personal/karhelmi_ad_helsinki_fi/EUyjfZObbRtEktjglZIfjqkB4lAZh1uDpnCF3pvPSApGeQ?e=XD0BRH) (public)

[Sprint Backlogs also in Projects (Team use)](https://github.com/UncleRovo/TeamBoaOHTU2021/projects?query=is%3Aclosed)

[Raportti](https://github.com/UncleRovo/TeamBoaOHTU2021/blob/main/documents/raportti_TeamBoa.pdf)

---

## Definition of Done:
- pylintin 8/10 mukaisesti kirjoitettu Sprintistä 2 eteenpäin
- yksikkötestit ominaisuudelle tehty ja ne menevät paikallisesti läpi
- GitHub Actionit menevät läpi (ehkä toisesta sprintistä lähtien?)
- toimii user storyn sanallisen kuvauksen mukaisesti selaimessa Herokun kautta
- testikattavuus 80 % - käyttöliittymää ja palvelutasoa ei lasketa mukaan. Sprintistä 2 eteenpäin

---
[Sprint 3 release](https://github.com/UncleRovo/TeamBoaOHTU2021/releases/tag/final)

[Sprint 2 release](https://github.com/UncleRovo/TeamBoaOHTU2021/releases/tag/sprint2)

---
## Sovelluksen paikallinen käyttö

Lataa koodi kloonaamalla projekti tai lataamalla ja purkamalla releasessa oleva lähdekoodi. 

Asenna projektin riippuvuudet komennolla `poetry install`. Paikallinen käyttö edellyttää, että koneellasi on asennettuna postgresql ja, että se on toiminnassa. 

Tietokanta tulee alustaa ennen sovelluksen käyttöä käskyllä
`psql < schema.sql` (tai komennolla `poetry run invoke initialize`).

Jotta kirjautuminen ja rekisteröityminen toimisi, tulee sovelluksen juureen luoda tiedosto .env, jonka sisälle on määriteltävä haluamansa salainen avain, tyyliin
`SECRET_KEY=haluamasisalainenmerkkijonotähän`.

Tämän jälkeen voit käynnistää sovelluksen ajamalla komennon `poetry run invoke start`.

Tietokannassa olevaa testikäyttäjää voi paikallisesti käyttää tunnuksella "Kasper123" ja salasanalla "Jesper123".

---

## Testikattavuusraportti (unittests)

Linkit testikattavuusraportteihin:

* [Coverage report (main)](https://github.com/UncleRovo/TeamBoaOHTU2021/blob/main/documents/Coverage_report.pdf)

Detailed coverage reports:
* [app.py](https://github.com/UncleRovo/TeamBoaOHTU2021/blob/main/documents/Coverage%20for%20src_app.py_%2076%25.pdf)
* [articles.py](https://github.com/UncleRovo/TeamBoaOHTU2021/blob/main/documents/Coverage%20for%20src_articles.py_%2094%25.pdf)
* [blogs.py](https://github.com/UncleRovo/TeamBoaOHTU2021/blob/main/documents/Coverage%20for%20src_blogs.py_%20100%25.pdf)
* [books.py](https://github.com/UncleRovo/TeamBoaOHTU2021/blob/main/documents/Coverage%20for%20src_books.py_%20100%25.pdf)
* [user.py](https://github.com/UncleRovo/TeamBoaOHTU2021/blob/main/documents/Coverage%20for%20src_user.py_%2057%25.pdf)
* [videos.py](https://github.com/UncleRovo/TeamBoaOHTU2021/blob/main/documents/Coverage%20for%20src_videos.py_%20100%25.pdf)
<p>
Coverage-raportin voit nähdä myös paikallisesti omalla koneellasi. Tee seuraavasti:
<p>
1. Kloonaa tämä projekti GitHubista omalle koneellesi (<b>git clone git@github.com:UncleRovo/TeamBoaOHTU2021.git</b>)
<p>
2. Kirjoita toiseen terminaali-ikkunaan <b>start-pg.sh</b> ja jätä se taustalle.

Suorita projektin juurihakemistossa seuraavat komennot:
<p>
3. <b>Poetry install</b> (asenna riippuvuudet. Huomaa, että sinulla tulee olla Python-versio 3.8.12. Jos sinulla on muu versio, muuta ko. versio toivotuksi ensin pyproject.toml-tiedostossa)
<p>
4. <b>poetry run invoke initialize</b> (alustaa tietokannan)
<p>
5. <b>poetry run invoke coverage</b> (luo testikattavuusraportin) > testikattavuusraportti on nimeltään "index.html"-tiedosto juurihakemiston kansiossa "htmlcov".

  ---
  
  ## License
  [MIT License](https://github.com/UncleRovo/TeamBoaOHTU2021/blob/main/LICENSE)
