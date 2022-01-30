# Scratch Notes
Just some scratch notes that I want to save for later

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

## I(q) Genetation Stuff
I'm going to need to compartmentalize much of the workflow into different functions. So here is a running list of them:
- alpha()
    - converts a domain area fraction (ad) value into alphad
- e26()
    - used for generating the "w" vector
    - based on Fred's equation 26
- legendre()
    - not yet implemented
    - uses the above two functions to generate the "w" vector
- readData()
    - not yet implemented
    - returns the F matrix
- functions used for fitting:
    - f_bs()
        - float version of binary search
        - helper function used to transform a y curve to a particular x vector
        - rather than using equals to return the index, I check against a threshhold by which the elements can differ
    - change_x()
        - used to transform a y curve to a particular x vector
        - this is what allows me to do things like chi squared calculations and goodness of fit evaluation
    - evaluate()
        - may or may not be used
        - the idea is to evaluate the goodness of fit of a particular I(q)
- generate()
    - uses the readData() and legendre(), among possibly others, to generate and return an I(q) vector
    - this one will likely be the longest and the most important function
- fit()
    - this would continuously apply steps 2.5 and 3 of the workflow, as well as calling evaluate() to find the best combination of ad and number of domains
    - would be called in generate()
- generateMatrices()
    - not entirely sure how I want to implement this one, but essentially this would be for the D, M, Omega, and Theta matrices
    - Generating these is far from quick so it may be a bit weird to use a function call each time I need them
    - maybe return a tuple of all 4 of them and use that?
- homogeneous stuff
    - I'll need to ask Fred how the homogeneous I(q) fits together with the heterogeneous stuff
    - If they are kept separate, then I'll just need to do this in somewhere else, but if they are used together and combined at some point, this will likely exist as something called by generate()  

### Note: I may not use the same exact function names in production, the idea is more important than the actual names

## Redis Stuff
- use a "numprocs" var for number of processes running (when I eventually implement multiprocessing)
    - running processes decrement it when they finish
    - scheduler thing increments it when it spins up a new process
    - scheduler also monitors it to know when to spin up a new process
- pass in the id of the dataset into a queue via redis
    - flask app pushes onto the queue
    - scheduler pops from the queue and uses the sql db to get the rest of the info
    - scheduler then performs the calculations, and writes them to the db
    - flask app reads from the db

## Goodness of fit stuff
- currently the y_experimental and y_theoretical vectors have different corresponding x vectors
    - this is solved by transforming the y_theoretical into a new vector which uses the same x vector as y_experimental
- with this solved, we can actually evaluate the goodness of fit
- currently I'm using chi squared to do this (scipy.stats.chisquare or smth)
    - I'm a bit scared that chi squared won't work how I want it to, but we'll see...
- the lower the chi squared, the better
- I iteratively find the combination of ad (domain area fraction) and nd (number of domains) which gets the lowest chi squared value
- NOTE: currently, I have an issue where the two datasets are off by some factor of 10, so I'll need to find a way of fixing this
    - either that or I could ignore it and see what happens...
    - perhaps taking the log base 10 of the data can solve this, which essentially converts from a 'logarithmic graph' to a 'linear graph'
        - what this would mean is the different sections of the curve could be compared more evenly, such that the upper sections don't contribute way more than the lower sections
        - the problem is I don't know if that is what we want, so I'll have to see

    