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


## 2022-2-19
### Changes

- Add group required to countries' pages
- Allow only ouloug admin to make CRUD operations in Countries' pages
- Allow ouloug monitors to make only Read operations in Countries' pages

## 2022-2-25
### Changes

- Change permission system from user_group to user_type in Country Pages
- Add pagination code to Country Pages

## 2022-2-27
### Changes

- Adding pages of States and its views
- Change base html page

## 2022-3-1
### Changes

- Resolving bugs related to adding new cities and new states
- Adding pages of Services and its views
- Adding change Service Status Logic

## 2022-3-7
### Changes

- Adding pages of Packages and its views
- Adding change Package Status Logic
- Resolving issues related to team pages
- Adding pages of Agent Shifts and its views


## 2022-3-12
### Changes

- complete the services 'telecom phone number'


## 2022-3-14
### Changes

- add edit.html to all masters and services 
- add views and urls 


## 2022-3-15
### Changes

- fixing bugs related to adding update functionalities to master pages which includes Countries, States, Cities, and Currencies
- the fixing process is on the run! it is not finished yet!


## 2022-3-16
### Changes

- fixing bugs related to update pages in the following maters (Countries - States - Cities - Currencies)
- removing all unrelated and not working code from address file 

## 2022-3-20
### Changes

- fixing update bugs related to the following masters (Countries - States - Cities - Currencies)
- saving automatic fields (added_by and last_modified_by) for the same masters

## 2022-3-21
### Changes

- adding pagination to the following masters  (Countries - States - Cities - Currencies)
- adding the logic and views required to add new record for the following pages (Business - AgentShift - CustomerCall )
- adding the logic and views required to add new record for the following pages (Telecom Operators - Telecom Phone Number )

## 2022-3-24
### Changes
- Completing pending teams pages (Listing data and Update Data) 

## 2022-3-25
### Changes
- Completing pending updates for masters and ouloug services pages
- adding the logic and views required for billing cycle 
- adding the logic and views required for customer payment'
- altering login to allow only staff users (admin and monitor users) to access ouloug backend