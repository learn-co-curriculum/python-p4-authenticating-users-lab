# Authenticating Users Lab

## Learning Goals

- Use the session object to authenticate a user.

***

## Key Vocab

- **Identity and Access Management (IAM)**: a subfield of software engineering that
  focuses on users, their attributes, their login information, and the resources
  that they are allowed to access.
- **Authentication**: proving one's identity to an application in order to
  access protected information; logging in.
- **Authorization**: allowing or disallowing access to resources based on a
  user's attributes.
- **Session**: the time between a user logging in and logging out of a web
  application.
- **Cookie**: data from a web application that is stored by the browser. The
  application can retrieve this data during subsequent sessions.

***

## Introduction

In this lab, we'll continue working on the blog site and set up a basic login
feature.

There is some starter code in place for a Flask API backend and a React
frontend. To get set up, run:

```console
$ pipenv install && pipenv shell
$ npm install --prefix client
$ cd server
$ flask db upgrade
$ python seed.py
```

You can work on this lab by running the tests with `pytest -x`. It will also be
helpful to see what's happening during the request/response cycle by running the
app in the browser. You can run the Rails server with:

```console
$ python app.py
```

And you can run React in another terminal with:

```console
$ npm start --prefix client
```

You don't have to make any changes to the React code to get this lab working.

***

## Instructions

For our basic login feature, we'll need the following functionality:

- A user can log in by providing their username in a form.
- A user can log out.
- A user can remain logged in, even after refreshing the page.

We'll need to create the routes and controller methods to handle each of these
features. Let's get started!

### Sessions

- Generate these routes:

  - `POST /login`: run the `SessionsController#create` method.
  - `DELETE /logout`: run the `SessionsController#destroy` method.

- Create a sessions controller.

  - **Note:** If you use the generators to generate your controllers, be sure to
    pass the `--no-test-framework` flag to avoid generating unneeded files:
    `rails g controller Sessions --no-test-framework`.

- Make a `SessionsController#create` method. It should:

  - Find a user in the database using the username from `params`.
  - Save the user's ID to the session hash.
  - Return the user as a JSON object.

- Make a `SessionsController#destroy` method. It should:

  - Remove the user ID from the session hash.
  - Return an empty response with a 204 No Content status code.

### Users

- Generate these routes:

  - `GET /me`: run the `UsersController#show` method.

- Create a users controller.

  - **Note:** If you use the generators to generate your controllers, be sure to
    pass the `--no-test-framework` flag to avoid generating unneeded files:
    `rails g controller Users --no-test-framework`.

- Make a `UsersController#show` method. It should:
  - Find a user in the database using the user id from the session hash.
  - Return the user as a JSON object.

***

## Resources

- [API - Flask: class flask.session](https://flask.palletsprojects.com/en/2.2.x/api/#flask.session)
