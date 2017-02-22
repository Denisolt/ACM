# ACM NYIT Chapter
<h3> Official website build on Django </h3>
This is the website created by the president <a href="https://github.com/denisolt">Denisolt Shakhbulatov</a> and founder <a href="https://github.com/msdocs">Mahmoud Saleh</a>
of Association for Computing Machinery at NYIT manhattan campus <br/>
Website is build on Django, users are capable of adding events to the calendar, add blog posts and has a custom form for signup <br/>
Signedup users are being stored in the DB together with Events and Posts. </br>

Check out the website: <a href="http://acm-nyit.org">acm-nyit.org</a> </br></br>
![alt tag](https://github.com/Denisolt/acm/blob/master/readmeimage2.png?raw=true)
![alt tag](https://github.com/Denisolt/acm/blob/master/readmeimage.png?raw=true)

Installation
-----------------------------------------
Activation of virtual environment:
```
source local/bin/activate
pip install -r /path/to/requirements.txt
```
Configuring and running Django:
```
#creating a super user
./manage.py createsuperuser 
#creating a migration
./manage.py makemigrations
#run the server
./manage.py runserver
```
Capabilities
-----------------------------------------
By going to the admin page (localhost/admin) and entering superuser login and password </br>
Admin can create events, posts, and access the db of signedup users </br>
Creation of the event:</br>
![alt tag](https://github.com/Denisolt/acm/blob/master/page2.png?raw=true)</br>
Creation of the blog post:</br>
![alt tag](https://github.com/Denisolt/acm/blob/master/page1.png?raw=true)</br>
Accessing the db of signed up users:</br>
![alt tag](https://github.com/Denisolt/acm/blob/master/page3.png?raw=true)</br>

