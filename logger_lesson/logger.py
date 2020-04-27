import logging
import time

logger = logging.getLogger("logger_root")
log_entry_format = "%(asctime)s %(levelname)-8s %(name)s [%(filename)s:%(lineno)d] %(message)s"
logging.basicConfig(level=logging.DEBUG, format=log_entry_format)
logging.Formatter.converter = time.gmtime


logger.info("Here is some info...")
logger.warning("WARNING!")
logger.debug("Debug message.")
logger.error("ERROR!")
logger.critical("NOT GOOD!")

child_logger = logging.getLogger("logger_root.child")
child_logger.critical("Child logger info...")
