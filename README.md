# transform-utf8mb4
python script to set mysql db characters in utf8mb4

I had several problems to store emojis into database few weeks ago
from ``(1709, 'Index column size too large. The maximum column size is 767 bytes.')``

to ``Incorrect string value: for column '' at row 1 python``

please before using it, backup your database, it's always good to backup before modifications

the script is absolutely inspired but an answer found on SO, I'll post the link soon

I'm not saying that it's the best solutions to set your database up to store emojis or chinese character but it might help you. Not sure it's the best things to do either. 

# QUESTIONS 

why UTF8MB4 ? http://stackoverflow.com/questions/30074492/what-is-the-difference-between-utf8mb4-and-utf8-charsets-in-mysql

why utf8mb4_unicode_ci ? http://stackoverflow.com/questions/766809/whats-the-difference-between-utf8-general-ci-and-utf8-unicode-ci/766996#766996

If you still have trouble to store emojis / chinese characters give a look at your mysql files over /etc/mysql

i had to add this in my.cnf

```
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci
```
and in mariadb.cnf

```
character-set-server  = utf8mb4
collation-server      = utf8mb4_unicode_ci
```
