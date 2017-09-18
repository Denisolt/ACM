## Exporting the heroku database into csv file

1. Open terminal and install heroku on your CLI:
   1. More info here: https://devcenter.heroku.com/articles/heroku-cli
2. Login into heroku
3. Enter: ```heroku pg:psql --app acm-nyit DATABASE```
4. Enter: ```bash \COPY blog_user TO 'acm-users.csv' WITH (FORMAT csv, DELIMITER ',', HEADER true);```
5. make sure you are allowed to access the db and the heroku website. 

