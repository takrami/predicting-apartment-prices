# Divar scraping and machine learning

This is a simple app for predict apartment price from data provided by divar.ir.

### Getting started

First you should create a table with the command below:

```sql
CREATE TABLE `apartment` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`region` VARCHAR(4),
	`size` VARCHAR(10),
	`date` VARCHAR(6),
	`price` VARCHAR(50),
	`link` VARCHAR(200),
	PRIMARY KEY (`id`)
);
```

Config your mysql connection by changing connector's parameters in `predict.py` and `scrap.py`. Like:

```python
cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='learn')
```

## Scraping data

To start scraping run `scrap.py`. You need to scrap all cities before predicting.

## Predicting

To predict data you need to configure this line on `predict.py` before running:

```python
new_data = [['10', '150', '1380']]
```

> 10 => region code (Look into `cities-code.txt`) <br>
> 150 => size of the apartment (in meters) <br>
> 1380 => date of production of the apartment (It can be between 1370 to 1398)
