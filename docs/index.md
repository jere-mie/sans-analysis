# SANS-Analysis Software
### Developer notes and documentation
The purpose of this document is to explain a bit about how this project is layed out.
This is to help both future developers understand my code, as well as myself when coming back to maintain it.

## NOTE: Since this specific web interface is still in early development, I may have things written in here which I plan to implement, but have not yet implemented

## How does the backend work?
Essentially, there are two parts to the backend:
1. The Flask web app
2. The server side job scheduler/maintainer

### 1. The Flask App
The purpose of the flask app is entirely to deal with handling requests from clients, and storing/managing data. None of the actual calculations are done by the 'flask' portion of the web app

### 2. The Job Scheduler
The purpose of this is to take jobs from the flask app, decide how to schedule/run these tasks, then run the necessary calculations and send the data back to the db.

### How are these two connected?
These two communicate via a simple Redis queue. The flask app adds 'jobs' to the queue for different datasets, and the scheduler pops these from the queue to run them. They both are connected to the same SQL db and have access to the same files.

