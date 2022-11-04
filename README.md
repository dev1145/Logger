# loggerdev
o This is a simple logger getter.
 - use get_logger(...) 
 - Installation
 - Using example


## Installation
```sh
# pip install git+https://github.com/dev1145/loggerdev.git
```

## Using example
```python
import logging
from loggerdev import get_logger
logger=get_logger(logger_name="myJob.subjob", log_filename=None)
logger.info("default logging level is INFO = %s", logging.INFO)
logger.setLevel(logging.INFO-1)
logger.log(logging.INFO-1 , "more info=%s \n %s", dir(loggerdev), loggerdev.__spec__)
```

### by dev1145
