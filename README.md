
# Project Title

Flask written API that mades the basic operations and validations for the breakable toy activity "contacts-app".

## Authors

- [@gibranhl](https://twitter.com/gibranhl)

  
## Tech Stack

**Server:** Flask, Gunicorn, PostgreSQL

  
## API Reference

#### Get all contacts

```http
  GET /contacts
```

#### Add a new contact

```http
  POST /contacts
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required**. Should be a valid email (eg. "gibran@encora.com") and **unique**|
| `name` | `string` | **Required**. Should be a valid name (eg. "Gibran") no special characters or numbers|
| `last_name` | `string` | **Required**. Should be a valid last name (eg. "Herrera Lopez") no special characters or numbers|
| `company` | `string` | **Required**. In the case of being optional it has to be provided as ""|
| `phone` | `string` | **Required**. In the case of being optional it has to be provided as ""|


#### Update a contact

```http
  PUT /contacts
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required**. Should be a valid email (eg. "gibran@encora.com") and be in the DB|
| `name` | `string` | **Required**. Should be a valid name (eg. "Gibran") no special characters or numbers|
| `last_name` | `string` | **Required**. Should be a valid last name (eg. "Herrera Lopez") no special characters or numbers|
| `company` | `string` | **Required**. In the case of being optional it has to be provided as ""|
| `phone` | `string` | **Required**. In the case of being optional it has to be provided as ""|


#### Delete a contact

```http
  DELETE /contacts/${email}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email`      | `string` | Should be a valid email (eg. "gibran@encora.com") and be in the DB|

  
## Installation 

Install contacts-api with pip and flask

```bash 
  pip install -r requirements.txt
  export FLASK_APP=app.py
  flask run
```
    
## Deployment

To deploy this project on Heroku run

```bash
  heroku login
  heroku addons:create heroku-postgresql:hobby-dev --app app_name
  heroku config --app app_name
  git init
  git add .
  git commit -m "initial commit"
  heroku git:remote -a app_name
  git push heroku master
```

**Notes:** app_name is the name of the app you create in Heroku. After using **heroku cofig** copy the URI, put it into config and add **sql** after postgres
  
## Acknowledgements
Thank you for all the help and tips
 - Dan Portillo
 - Moy Morales