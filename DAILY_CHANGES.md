# Change Log

## 2022-2-06
### Changes

- Adding new superuser 
- Adding favicon to pages
- change side bar image to ouloug logo
- change sidebar title style
- Adding new Model User_Country to Address app

## 2022-2-07
### Changes

- Resolving issues related to user country model foreign keys

## 2022-2-08
### Changes

- Deploy all models 
- With one error with import models from other apps
- Register all models in an admin
- Handling issues related to deploying new models , hint there are still some errors needs to be delt with

## 2022-2-09
### Changes

- Make-migrations for all models
- Resolving all issues related to models



## 2022-2-12
### Changes

- Add some code in views.py for dahborad use it's with comment
- Make some empty html files for all dashboard related 

## 2022-2-14
### Changes

- Add check validation for form registration 


## 2022-2-15
### Changes

- Create forms for the apps and make the views of those forms with empty html pages

## 2022-2-17
### Changes

- Add messages section in base html file
- Add Countries Master Page with its subpages (All Countries - Add Countries - Edit Country - Remove Countries)
- Remove the sing up link from the login page (The signup process will be conducted from within the system ,by Ouloug admin only)
- Customize authorization groups to 'ouloug_admin' and 'ouloug_monitor'
- Customize User model and add Groups model inheritance to it
- Adding Group Required Mixin to Countries View List 
