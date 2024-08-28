# test_django_task

## Installation
To install the project it is necessary to:
1. Clone the repository
2. Build and run docker containers
```bash
docker-compose up
```

During the container building, **startup.sh** file will automatically execute the following actions:
- make migrations;
- load testing data to database (from db.json file);
- collect static content (for django admin);
- run server.


## Usage
For the convenience of data manipulation you can use [django admin panel](http://127.0.0.1:8080/admin/).
Use the following credentials for log in:
```bash
login: admin
password: admin
```

To get the id of producers, based on the contract_id, use the [producers](http://127.0.0.1:8080/producers?contract_id=1) endpoint
```bash
http://{HOST}/producers?contract_id={contract_id}
```
