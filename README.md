# Apartments Scraper

This is a python program that was build to get apartments information like `name`, `price` and `bed` out of a specific [Apartment Website](https://www.apartments.com/) using `scrapy` python module and saved the data into a `json` file.
<br/>
<br/>

## :hammer_and_wrench: Setting Up:

---

Windows:

```
pip install scrapy
pip install colorama
```

iOS:

```
pip3 install scrapy
pip3 install colorama
```

## To run the application:

---

In the root directory of the project, run `main.py` file.
<br/>
<br/>

:heavy_exclamation_mark: :heavy_exclamation_mark: <span>Note </span>:heavy_exclamation_mark: :heavy_exclamation_mark:

<span style="color:orange">Not ALL APARTMENTS</span>
have results for `price` and `bed`</p>
due to the [css selectors](https://www.w3schools.com/cssref/css_selectors.php) used in the site (Also noted in the program).
<br/>
<br/>

![Display in program](./assets/Disclaimer.png)

<br/>

## Resources used to build this app

---

- Scrapy:</br>
  https://scrapy.org/

- Colorama:</br>
  https://pypi.org/project/colorama/

- CSS Selectors:</br>
  https://www.w3schools.com/cssref/css_selectors.php

- States Letter for `states.txt`:</br>
  https://www.faa.gov/air_traffic/publications/atpubs/cnt_html/appendix_a.html
