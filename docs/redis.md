# Redis Info
## Setting up Redis on System
Installing Redis:
> `sudo apt install redis`

Starting Redis Server:
> `redis-server --port <PORT NUMBER> &`

Shutting Down Redis:
> `redis-cli shutdown`

Starting CLI:
> `redis-cli` 

## Interating with Redis via CLI:
Get the Value Associated With "key"
> `get key`

Set the Value Associated With "key" to "value"
> `set key value`

Pushing Onto List (Left and Right Push)
- > `lpush mylist value`
- > `rpush mylist value`

Popping From List (Left and Right Push)
- > `lpop mylist`
- > `rpop mylist`

Getting List Values From Left (Ending Num is Inclusive)
- > `lrange 0 10`  
- > `lrange 0 -1`

## Using Redis With Python
Installing:
> `pip install redis`

Quickstart:
```py
>>> import redis
>>> r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
>>> r.set('foo', 'bar')
True
>>> r.get('foo')
'bar'
```
