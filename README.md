## Instructions

1) Start a local Postgres database


2) Create `.env` with the postgres database uri:
```bash
DATABASE_URL=postgresql://postgres:password@localhost:5433/smarkets
```


3) Run the Python API:

```bash
python3 main.py
```


## Development

I primarily build my API's with nestJS so this was a new experience for me. I heard Flask was a good choice, so I decided to go with that. I had to figure out how to organise my routes as it was quite cluttered in one file. I added some basic error handling and cover all endpoints.

I'd need to do some research into how to handle migrations with Python and Flask. As it's a demo task, I have no authentication. The models contains the schemas for each table. The routes are organised into events, markets, contracts.