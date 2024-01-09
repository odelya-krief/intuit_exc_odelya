<h1>Intuit Home Exercise - Players RestAPI</h1>

<h3>Deployed Server:</h3>
Deployed service here : https://intuit-exc-odelya.vercel.app/

**Note**: The endpoint `/api/players` will not work due returned data size limit (Explained below).
This endpoint can be ran locally to make sure it works.

<h3> Local Execution: </h3>

 1. Create a `venv` in the project directory, activate it and install the requirements. (instructions: https://sourabhbajaj.com/mac-setup/Python/virtualenv.html)
 2. Add these lines at the end of the "main.py" file:
```
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=800)

```
3. Add `PLAYERS_FILE_PATH = player_manager/player.csv` as an environment variable, 
or just override it in the settings file (I left the name commented).
4. Run`main.py`, the server should be up and running on port `8000`.
5. Explore http://localhost:8000/api/players or http://localhost:8000/api/players/ackerto01 on the browser.
6. Explore the documentation provided by `FastAPI` on http://localhost:8000/docs.


<h3> Testing: </h3>

1. Open the terminal in the root directory of the project and activate the `venv`.
2. Run: 
```
cd unit_tests
pytest
```

<h3> Things I would have changed If I had infinite time: </h3>

1. Add integration tests, that are creating HTTP requests to the server, and asserting on the results.
2. Add dummy unit tests for the Fast API server. (To make sure things will not break in the future.)
3. Currently, the `/api/players` endpoint is not working on `Vercel`, because the amount of data an AWS
   lambda can return is limited, so if I had time I would add pagination or some sort 
   of chunking of the data.
4. CSV is a fragile, not secure and not scalable format, storing the data in a database 
   will be a lot better, in terms of security, future updates and changes, scale, speed, tests
   and deployment. 
5. Add a better configuration management.
6. Add `github actions` on the repo, for testing and deploying.

