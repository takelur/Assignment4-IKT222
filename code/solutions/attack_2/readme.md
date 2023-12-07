# Attack 2

## Background

This second attack was performed to gain access to the secondary dashboard behind yet another authentication wall. This login page was located at the [inner portal](https://inner.portal.regjeringen.uiaikt.no/).

The image on this login page (a needle) strongly suggested that some sort of injection should be performed here.

## Solution

The query for the login form check was 
```SQL
SELECT * FROM users WHERE username='{username}' AND password='{password}'
```
as given by a Flask debug error page when trying a simple injection.

To match the query an injection on the form: `' OR 1=1 OR '` can be performed to make the password field always true. The resulting query will then be
```SQL
SELECT * FROM users WHERE username='{username}' AND password='' OR 1=1 OR ''
```
which should obviously always be true for the password field.

The result was that I got successfully logged in on Intranett level 1 as the user Jonas Dahl.