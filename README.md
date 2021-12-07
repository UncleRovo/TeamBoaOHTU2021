# TeamBoaOHTU2021
[Klikkaa tästä päästäksesi käyttämään sovellusta](https://lukuvinkki-boa.herokuapp.com/)

---

![GitHub Actions](https://github.com/UncleRovo/TeamBoaOHTU2021/workflows/CI/badge.svg)

[Backlog (Team use)](https://helsinkifi-my.sharepoint.com/:x:/g/personal/karhelmi_ad_helsinki_fi/EUyjfZObbRtEktjglZIfjqkBznpw83N5DPR699B00N6RFQ?e=fe2MUZ)

[Product Backlog and Burndown Chart](https://helsinkifi-my.sharepoint.com/:x:/g/personal/karhelmi_ad_helsinki_fi/EUyjfZObbRtEktjglZIfjqkB4lAZh1uDpnCF3pvPSApGeQ?e=XD0BRH) (public)

---

## Definition of Done:
- pylintin 8/10 mukaisesti kirjoitettu Sprintistä 2 eteenpäin
- yksikkötestit ominaisuudelle tehty ja ne menevät paikallisesti läpi
- GitHub Actionit menevät läpi (ehkä toisesta sprintistä lähtien?)
- toimii user storyn sanallisen kuvauksen mukaisesti selaimessa Herokun kautta
- testikattavuus 80 % - käyttöliittymää ei lasketa mukaan. Sprintistä 2 eteenpäin

---

[Sprint 2 release](https://github.com/UncleRovo/TeamBoaOHTU2021/releases/tag/sprint2)

---
## Sovelluksen paikallinen käyttö

Lataa koodi kloonaamalla projekti tai lataamalla ja purkamalla releasessa oleva lähdekoodi. 

Tietokanta tulee alustaa ennen sovelluksen käyttöä käskyllä
`psql < schema.sql`.

Jotta kirjautuminen ja rekisteröityminen toimisi, tulee sovelluksen juureen luoda tiedosto .env, jonka sisälle on määriteltävä haluamansa salainen avain, tyyliin
`SECRET_KEY=haluamasisalainenmerkkijonotähän`.

---

## Testikattavuusraportti
<p>
Coverage-raportin voit nähdä paikallisesti omalla koneellasi. Tee seuraavasti:
<p>
1) Kloonaa tämä projekti GitHubista omalle koneellesi (<b>git clone git@github.com:UncleRovo/TeamBoaOHTU2021.git</b>)
<p>
2) Kirjoita toiseen terminaali-ikkunaan <b>start-pg.sh</b> ja jätä se taustalle.

Suorita projektin juurihakemistossa seuraavat komennot:
<p>
3) <b>Poetry install</b> (asenna riippuvuudet. Huomaa, että sinulla tulee olla Python-versio 3.8.12. Jos sinulla on muu versio, mutta ko. versio toivotuksi ensin pyproject.toml-tiedostossa)
<p>
4) <b>poetry run invoke initialize</b> (alustaa tietokannann)
<p>
5) <b>poetry run invoke coverage</b> (luo testikattavuusraportin) > testikattavuusraportti on nimeltään "index.html"-tiedosto juurihakemiston kansiossa "htmlcov".

  ---
  
  ## License
  [MIT License](https://github.com/UncleRovo/TeamBoaOHTU2021/blob/main/LICENSE)
