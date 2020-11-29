import logging
import datetime

def showTime():
    logging.basicConfig(filename="showTime.log")
    logging.debug("debug log")
    

logging.basicConfig(filename="time.log",
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S',
        format='%(asctime)s %(name)-8s %(levelname)-8s [line:%(lineno)d] %(message)s')
logging.debug(datetime.date)

showTime()
