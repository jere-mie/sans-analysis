# Notes
Just some scratch notes that I want to save for later

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

    