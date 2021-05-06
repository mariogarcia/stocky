import time
import functools

def producer(app):
    '''
    this function represents a producer taking notification logs
    and creating an application state that can be queried by users
    in a more performant way than the event log.
    '''
    time.sleep(2)        
    section = app.log["1,10"]
    for item in section.items:
        print(item)    

import functools

def account_producer(app):
    '''
    decorator for handling event sourcing notification logs and
    maybe create a query-driven-state of the application
    '''
    def outer(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # executes original function
            result = await func(**kwargs)
            # adds the producer tasks to be executed in the background
            tasks.add_task(producer, app=app)
            # returns the result of executing the original function
            return result
        return wrapper
    return outer

