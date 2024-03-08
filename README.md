![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

<img src="static/images/article3.jpg" >

# Title: Learner Wellness

## Overview:
- Foster a healthy university campus environment by centralising wellness resources.

## Features:

### Enable Students to: 
- Access resources and services that promote mental and physical well-being. 
- Book sessions or join classes easily.
- Encourage healthy eating. Profile healthy options.

### Enable Therapists/Instructors to showcase their value: 
- Create profiles, offer services, and manage bookings. 
- Engage with the student community and get feedback.

### Enable Food Vendors to showcase their produce:
- List healthy food options and attract health-conscious students.

# Detailed Description

## User/student registration.
- (i) Therapist/Instructor profiles: allow students to read about available professional and book sessions or classes.
- (ii) Event/Session booking: For therapy, yoga, meditation, or fitness classes.
- (iii) Food section: Highlighting healthy dining options on campus with ratings, reviews, and menu options.
- (iv) Resources: Articles, videos, and podcasts related to mental and physical wellness.


### 1. Technical Project Overview

Full Stack Web Development Hackathon: Application built using a Full Stack Django Framework.

Activities: Development using Django, Python, HTML, CSS and JavaScript, UX Design, and Agile Project Management.

Hackathon Objectives:
- Use an Agile methodology to plan and design a Full-Stack Web application using an MVC framework and related contemporary technologies.
- Implement a data model, application features and business logic to manage, query and manipulate data to meet given needs in a particular real-world domain.
- Identify and apply authorisation, authentication and permission features in a Full-Stack web application solution.
- Create manual and/or automated tests for a Full-Stack Web application using an MVC framework and related contemporary technologies.
- Use a distributed version control system and a repository hosting service to document, develop and maintain a Full-Stack Web application using an MVC framework and related contemporary technologies.
- Deploy a Full-Stack Web application using an MVC framework and related contemporary technologies to a cloud-based platform


### 2. Explain the Design and Thinking Process
### 2. List of features

- feature name
- description of the feature
- screenshot

- Project Idea:	Learner Wellness
- Team name:	Healthy Hustlers
- Wireframing Tool: Balsamiq
- Project Management Kanban Board Tool: GitHub
- Leverage Bootstrap: Yes
- Leverage external APIs:	Cloudinary
- Feedback from Hackathon 1 and 2:	Code review check for commented out code, logs, test data. Ensure all Git commit messages relevant
- Define roles and responsibilities
--  Potential Roles: 
Developer (Frontend and Backend), 
Product Owner, 
Scrum Master,
Branch Manager (Forking), 
Documenter,
Environment Owner,
ERD Designer (Models).

### 3. UX with user stories
- site goals
- design thought process
- planning and wireframe design
- design choices
- user stories
- wireframes

### 4. Deployment
- demonstrate how to deploy project
- record to self and others of how to deploy and use our software
- detailed list of deployment steps
- heroku
- elephantsql
- cloudinary

## Heroku
- Activate your Heroku Student Pack
- Get the student offer”
- Heroku dashboard
- Account settings
- Billings
- Subscribe to Eco
- Eco dyno
- Your Eco dyno subscription is now active
- DISABLE_COLLECTSTATIC key has a value of 1
- pip3 to install webserver gunicorn~=20.1
- Procfile: add a command using gunicorn and codestar wsgi: web: gunicorn codestar.wsgi
- DEBUG constant to False
- Heroku dashboard: go to your app. Click on the Deploy tab
- Reveal Config Vars in the Settings
- DATABASE_URL = add the value of the ElephantSQL URL

 ## Elephant SQL
- ElephantSQL is a PostgreSQL database hosting service that uses several cloud-hosted platforms
- Log into ElephantSQL to access your dashboard
- Create New Instance.
- Tiny Turtle plan
- Select a data centre near you
- Create instance
- Click on your newly named instance
- Click on STATS.
- Verify the version of PostgreSQL is 12 or higher
- Create a file named env.py,
- .gitignore file: add env.py
- os.environ.setdefault("DATABASE_URL", "<your-database-URL>")
- pip3 install dj-database-url~=0.5 psycopg2~=2.9, pip3 freeze --local > requirements.txt
- settings.py: import os; import dj_database_url if os.path.isfile('env.py'):     import env
- python3 manage.py createsuperuser

## Cloudinary
- A persistent file store
- Cloudinary is an API, so we will need an API key to connect the Django project to it securely
- pip3 install cloudinary~=1.36.0 dj3-cloudinary-storage~=0.0.6 urllib3~=1.26.15
- pip3 freeze --local > requirements.txt
- Sign up to Cloudinary
- env.py: os.environ.setdefault("CLOUDINARY_URL", "<URL copied from Cloudinary in last step>")
- settings.py: INSTALLED_APPS
- Update the app to use Cloudinary
- import the CloudinaryField from the cloudinary/models.py
- python3 manage.py makemigrations
- python3 manage.py migrate

## Deployment with static files
- whitenoise server
- pip3 install whitenoise~=5.3.0
- pip3 freeze --local > requirements.txt
- settings.py: 'whitenoise.middleware.WhiteNoiseMiddleware',
- 



### 5. Demonstrate Testing
- demostrate it has been tested well
- demostrate it is responsive on multiple dcevices
- show that code passes validation
- list known bugs

Validator Testing
HTML: No errors were returned when passing through the official W3C validator
https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html
CSS: No errors were found when passing through the official (Jigsaw) validator
https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css



### 6. Future Features
- ran out of time
- not sure if viable
- not confortable implementing

### 7. Credit our Sources
- images
- code
- text 
- link to relevant sites
- authors name










pip install -r requirements.txt
Successfully installed django-ckeditor-6.7.1 django-js-asset-2.2.0
pip install django-ckeditor

https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=1





