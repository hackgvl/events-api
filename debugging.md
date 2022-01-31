This is an example of debugging the data results used in app.py and outputting errors to the error log.


```
    import sys
    from pprint import pformat

    # logger.error("-------");
    logger.error(pformat(data.get('events')));
    logger.error("-------");
    # logger.error(events);

    sys.exit()
```
