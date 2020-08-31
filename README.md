### Example project for exploring capabilities of Schemathesis

A simple web app, built with Connexion, AioHTTP, attrs and asyncpg. Contains many intentional errors, which should be found by running Schemathesis against the running example app.

Schemathesis repo: https://github.com/kiwicom/schemathesis

Install dependencies:

```shell script
$ pip install -r requirements.txt -r requirements-test.txt
```

Setup the database via `docker-compose`:

```shell script
$ docker-compose up
```

To run the app:

```shell script
$ python -m example
```

For the further actions the app should be running (by default on `127.0.0.1:8080`)

Run Schemathesis CLI:

```shell script
$ schemathesis run http://0.0.0.0:8080/api/openapi.json
```

Run Schemathesis-based tests:

```shell script
$ pytest -v test_example.py
```
