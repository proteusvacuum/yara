# yara
Yet Another Recipe Aggregator


# Installing

```sh
mkvirtualenv -p $(which python3) yara
pip install -r requirements.txt
cp yara/localsettings.example yara/localsettings.py
```
Download the latest jdbc driver for postgres, and put it into `./config`
```sh
wget -P ./config/ https://jdbc.postgresql.org/download/postgresql-42.2.2.jar 
```
and update the line in `docker-compose` to point to this file.

# Updating Recipes

Run the scrapers in the `./spiders` folder, with output into an `output` directory:
```sh
$ scrapy runspider ./spiders/pressurecookrecipes.com/spider.py -o spiders/output/pressurecookrecipes1.json
```

Add these to the postgres DB:
```sh
$ ./manage.py update_db
```

Logstash should ~immediately put these into the ES index.
