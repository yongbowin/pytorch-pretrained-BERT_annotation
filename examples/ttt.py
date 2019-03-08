import logging


logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                    datefmt = '%m/%d/%Y %H:%M:%S',
                    level = logging.INFO)
logger = logging.getLogger(__name__)

ss="This is a test sentence."
sss="The same to last one."

logger.info("111 %s" % ss)
logger.info("111")