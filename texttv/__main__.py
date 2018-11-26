import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("texttv")
[
    logging.getLogger(i).setLevel(logging.WARNING) 
    for i in logging.root.manager.loggerDict.keys()
    if not i == "texttv"
]


if __name__ == '__main__':
    logger.info("starting")
    logger.info("stopping")
