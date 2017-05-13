import logging
import hepshell.SETTINGS as s

logger = logging.getLogger(s.LOG['name'])
logger.setLevel(logging.INFO)
if s.LOG['logToFile']:
    formatter = logging.Formatter(
        '%(asctime)s [%(name)s]  %(levelname)s: %(message)s')

    logfile = s.LOG['logFile']
    fh = logging.FileHandler(logfile)
    fh.setFormatter(formatter)
    fh.setLevel(s.LOG['logLevelFile'])
    logger.addHandler(fh)

if s.LOG['logToConsole']:
    # logging to the console
    formatter = logging.Formatter('%(message)s')
    ch = logging.StreamHandler()
    ch.setLevel(s.LOG['logLevelConsole'])
    ch.setFormatter(formatter)
    logger.addHandler(ch)
