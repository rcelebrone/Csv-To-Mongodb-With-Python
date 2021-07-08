# Python hands on 4linux
https://www.youtube.com/watch?v=JdFauzd3gFw&list=PLfrzfMwG8umbAwNQdy3y5OqTyyjJn36R4

## Build and Run MongoDB 
`Run docker-compose -f stack.yml up`

Wait for it to initialize completely, and visit http://swarm-ip:8081, http://localhost:8081, or http://host-ip:8081 (as appropriate).

## Run Setup
`python3 -m venv .venv`

## Issues
UnhandledPromiseRejectionWarning: MongoNetworkError: failed to connect to server [mongo:27017] on first connect [Error: connect ECONNREFUSED
- Solution: add in same network https://stackoverflow.com/questions/60748269/mongo-express-started-by-docker-compose-causing-error-mongoerror-failed-to-co