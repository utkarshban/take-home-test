## Intro
This is an application that uses Flask and Python. Docker is used to make this
project platform independent.
The routes that this application serves are:
- `/user/add/transaction` (POST request)
  - consumes JSON data
  - example JSON data:
  ```
  { "payer": "DANNON", "points": 10000, "timestamp": "2020-11-02T14:00:00Z" }
  ```

- `/user/spend` (POST request)
  - consumes JSON data
  - example JSON data:
  ```
  { "points": 5000 }
  ```

- `/user/balance` (GET request)

## Setup
There are two ways to get this project working.

### 1 If you have Docker installed and setup, follow these steps to use the docker image from the repo:
 - download the zipped docker image `take-home-test.tar`
 - `cd` into the directory where the zipped image is downloaded
 - run `docker load < take-home-test.tar` (Use Command Prompt, not PowerShell)
 - run `docker run -p 5000:5000 take-home-test`

 Now the project is setup and you should see
 ```
* Serving Flask app "app" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on all addresses.
  WARNING: This is a development server. Do not use it in a production deployment.
* Running on http://172.17.0.2:5000/ (Press CTRL+C to quit)
 ```
 - Use Postman to send requests to the server hosted locally on port 5000.
   - To send POST requests to add a transaction select `POST` from the dropdown
     menu and set the request URL to `localhost:5000/user/add/transaction`.
   - Click on `Body`, select `raw`, and select `JSON` from the dropdown menu at
     the right.
   - Paste the example JSON data for the add transaction request from above.
   - You have successfully called the add transaction request if you see
     `{"message": "Successfully added!"}` in the response body.
   - Similarly, you can send POST requests to spend points by setting the request
     URL to `localhost:5000/user/spend` and using the example JSON data from above.
   - You should see `[{ "payee": "DANNON", "points": -5000 }]` in the response body.
   - To send a GET request to see payer points balances, set the request type to
     `GET`, and the request URL to `localhost:5000/user/balance`.
   - You should see `{ "DANNON": 5000 }` in the response body.

  ### 2 If you do not have Docker installed, you can clone the repo and follow these steps:
  - Install Python using [this link](https://wiki.python.org/moin/BeginnersGuide/Download).
  - Install pip if it is not installed already using [this link](https://pip.pypa.io/en/stable/installing/).
  - Install Flask and its dependencies using `pip install -r requirements.txt`.
  - Run the command `python app.py` or `flask run`.
  - Now use Postman exactly as described above.

## Installing Docker on Windows for Method 1 
### (Warning: Need patience for the entire setup!)
 - Download Docker from [this link](https://docs.docker.com/docker-for-windows/install/).
 - After installing Docker (and restarting your computer), follow [this link](https://docs.microsoft.com/en-us/windows/wsl/install-win10#manual-installation-steps) all the way to Step 6.
 - You should now be able to use Method 1 described above.

## Create the Docker image using the Dockerfile
### (Optional!)
 - Install Docker.
 - Clone the repo.
 - `cd` into the folder containing Dockerfile.
 - Run `docker image build -t <image-name> .`. (Do not forget the `.` near the end of the command!)
 - You should now see the image in the Docker Hub application under Images.
 - Run `docker run -p 5000:5000 <image-name>` and start using Postman to interact with the APIs.
