import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

file_handler = logging.FileHandler('logfile.log')

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)

logging.getLogger().addHandler(file_handler)

def log_activity(func, *dec_args, **dec_kwargs):

    def wrapper(*args, **kwargs):
        logging.info(f'Calling function : {func.__name__}')
        result = func(*args, **kwargs)
        logging.info(f'Function {func.__name__} finished')
        return result
    
    return wrapper

@log_activity
def subtract(a, b):
    return abs(a-b)

@log_activity
def add (a, b):
    return a + b

print(add(10, 20))