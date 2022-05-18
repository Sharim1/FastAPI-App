

# FastAPI App

A small app for sentiment analysis and key-phrase extraction built using [FastAPI](https://fastapi.tiangolo.com/) and Azure Text Analytics Service.

<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" align="right"
     alt="Size Limit logo by Anton Lovchikov" width="170" height="90">

Note - You must have an active Azure account to use/test this app.

## Quickstart
* Clone the repository.
* `pip install -r requirements.txt`
* Create env file - "fastapi.env" at the same location as requirements.txt.
* ENV file requires 3 values -
	* APIKEY="Get it from the from Text Analytics resource once you have successfully created and deployed the same."
	* ENDPOINT="Get it from exactly the same section as the API Key."
	* INSTRUMENTATIONKEY="Get it from Application Insights Rescource Dashboard once you have successfully created and deployed the same."
* `uvicorn main:app` to run and `uvicorn main:app --reload` to reload after some changes.
* Visit `http://localhost:8000/docs` and you can start making request in below format -
		`{"text_to_analyze":[
												"Elon musk to acquire twitter for 44 billion dollars.",
												"Today was the best day of my life."]
                                                            }`


