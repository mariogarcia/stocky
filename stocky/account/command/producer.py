import time
import functools

def evecons(app):
    import time
    time.sleep(2)        
    section = app.log["1,10"]
    for item in section.items:
        print(item)    

import functools

def account_producer(app):
    def outer(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            info  = kwargs['info']
            tasks = kwargs['tasks']
            result = await func(**kwargs)
            tasks.add_task(evecons, app=app)
            return result
        return wrapper
    return outer

