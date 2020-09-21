### Example project for exploring capabilities of Schemathesis

A simple web app, built with Connexion, AioHTTP, attrs and asyncpg. Contains many intentional errors, which should be found by running Schemathesis against the running example app.

Schemathesis repo: https://github.com/kiwicom/schemathesis

Start the application via `docker-compose`:

```shell script
$ docker-compose up
```

For the further actions the app should be running (by default on `127.0.0.1:5000`)

Run Schemathesis CLI:

```shell script
$ schemathesis run http://0.0.0.0:5000/api/openapi.json
```

Run Schemathesis-based tests:

```shell script
$ pytest -v test
```
