# TeamBoaOHTU2021
[Klikkaa tästä päästäksesi käyttämään sovellusta](https://lukuvinkki-boa.herokuapp.com/)

---

![GitHub Actions](https://github.com/UncleRovo/TeamBoaOHTU2021/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/UncleRovo/TeamBoaOHTU2021/branch/main/graph/badge.svg?token=RVVXELLER4)](https://codecov.io/gh/UncleRovo/TeamBoaOHTU2021)

[Backlog (Team use)](https://helsinkifi-my.sharepoint.com/:x:/g/personal/karhelmi_ad_helsinki_fi/EUyjfZObbRtEktjglZIfjqkBznpw83N5DPR699B00N6RFQ?e=fe2MUZ)

[Product Backlog and Burndown Chart](https://helsinkifi-my.sharepoint.com/:x:/g/personal/karhelmi_ad_helsinki_fi/EUyjfZObbRtEktjglZIfjqkB4lAZh1uDpnCF3pvPSApGeQ?e=XD0BRH) (public)

---

Definition of Done:
- pylintin 10/10 mukaisesti kirjoitettu Sprintistä 2 eteenpäin
- yksikkötestit ominaisuudelle tehty ja ne menevät paikallisesti läpi
- GitHub Actionit menevät läpi (ehkä toisesta sprintistä lähtien?)
- toimii user storyn sanallisen kuvauksen mukaisesti selaimessa Herokun kautta
- testikattavuus 80 % - käyttöliittymää ei lasketa mukaan. Sprintistä 2 eteenpäin

---
Unittestit
Coverage-raportin voit nähdä paikallisesti omalla koneellasi. Tee seuraavasti:
1) Kloonaa tämä projekti GitHubista omalle koneellesi (<b>git clone git@github.com:UncleRovo/TeamBoaOHTU2021.git</b>)

Suorita projektin juurihakemistossa seuraavat komennot:
2) <b>Poetry install</b> (asenna riippuvuudet. Huomaa, että sinulla tulee olla Python-versio 3.8.12. Jos sinulla on muu versio, mutta ko. versio toivotuksi ensin pyproject.toml-tiedostossa)
3) Poetry shell ??
4) poetry run invoke initialize (alusta ja luo tietokanta)
5) poetry run invoke test
6) poetry run invoke coverage (luo testikattavuusraportin) > testikattavuusraportti on nimeltään "index.html"-tiedosto juurihakemiston kansiossa "htmlcov".