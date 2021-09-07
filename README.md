## EMOJI API

this api allow one with just a query to get emoji relating to a certain words.
you can also add emoji relating to certain words.

words like:

* happy
* sad
* animal
* car
* walking
* angry
* sick
* laughing
* e.t.c

by just doing http://127.0.0.1:8000/api/s/happy will give :

------------------------------------

HTTP 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "symbol": "😄"
    },
    {
        "id": 3,
        "symbol": "😊"
    }
]

-------------------------------------