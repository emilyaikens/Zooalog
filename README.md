# Zooalog

## Description: 

Zooalog is an animal husbandry tracking app. 

Hobbiests can use this application to log inputs and outputs of animals in their care. Logs can include parameters such as diet, behavior, and customizable abiotic factors including but not limited to temperature, humidity, salinity, pH, O2 levels and NO3. 

This app is enclosure-centric, meaning the user must create an Enclosure in order to log an animal. As such, this app is better designed for users with critters such as fish, reptiles, and contained mammals or birds. In theory a user could log their dog or cat, but they would have to do so by first creating an Enclosure. Perhaps in that case they could just call the Enclosure "House", but really this app is more catered towards the former examples. 

## Goals

The three broad user stories this app achives are:
1. AAU, I want to create new enclosures (Create)
2. AAU, I want to view my existing enclosures (Read)
3. AAU, I want to manage my existing enclosures (Update and Delete)

Of course each of these can be broken down quite a bit, but these overaching user stories boil down to the idea that this app needs to be full CRUD.

Responsive interface

User-friendly interface

User authentication

Page authorization

## Technologies Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) 
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) 
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) 

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)

## Getting Started!

App is under construction so link is not yet available! Stay tuned.

Mockup for home page 

![UI Design for home page](https://i.imgur.com/lyHg81S.png)

## Planning Links

[Wireframe: Whimsical](https://whimsical.com/zooalog-D5avFK95o1bgy94H4kbUSd@3CRerdhrAw89dQ8hhdkVHFp1)

[User Stories: Trello](https://trello.com/invite/b/MhlMC0Qn/c32c891202deb797028f567e7c5d68d3/zooalog)
<details>
<summary> ERD created with Lucidchart </summary>
<img src="main_app/static/images/erd.png">
</details>

## Progress Report

* Dec 11 2022: Set up user authentication and authorization. Signup, login, and logout functionality are all up and running.
* Dec 8 2022: Implement full CRUD for Test. Form to create new Tests and ability to update and delete. Add Sub Model to models.py, migrate and can view. Form to create new Sub.
* Dec 7 2022: Create Test model and migrate to postgreSQL. Set up templates (base.html, about.html, test/detail.html, test/index.html), set up some basic CSS, and config routes (urls.py and views.py) for each
* Dec 6 2022: Initial commit. Deploy to Heroku and create blank home page with URL/Views route config