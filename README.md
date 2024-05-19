# wallet_api_test_task

## Task requirements

### Task

Develop REST API server using django-rest-framework with pagination, sorting and filtering for two models:

- **Transaction** (id, wallet_id (fk), txid, amount);
- **Wallet** (id, label, balance);

Where *txid* is required unique string field, amount is a number with 18-digits precision, *label* is a string field, *balance* is a summary of all transactions’s amounts. Transaction amount may be negative. Wallet balance should **NEVER** be negative

### Tech Stack

- Python – 3.11+
- Database – mysql

### Other

API specification – JSON:API — A specification for building APIs in JSON (you are free to use plugin https://django-rest-framework-json-api.readthedocs.io/en/stable/)

Will be your advantage:

- Test coverage
- SQLAlchemy migrations is an option
- Any linter usage
- Quick start app guide if you create your own docker-compose or Dockerfiles
- Comments in non-standart places in code
- Use database indexes if you think it's advisable

## Implementation details

I decided to use Django-Ninja as a framework to make this test assignment more interesting for me since I have never worked with it before. The API includes the following functionalities:

- Creation of transactions
- Searching transactions by wallet label and txid
- Creation of a wallet
- Listing wallets

There is validation to prohibit the creation of a transaction if its negative amount exceeds the wallet balance. Additionally, there are tests for the transactions API. I also added GitHub Actions with tests and a Ruff linter and formatter (though I am not sure if the linter and formatter will fail the build, as I haven't had time to check it).

## How to run

```sh
docker-compose build
docker-compose up -d
docker-compose exec wallet_api sh -c "./manage.py migrate"
```

then go to: http://localhost:8100/api/docs
