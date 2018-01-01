"""
Lambda example with external dependency
"""

import logging

from wu import tang


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handle(event, context):
    """
    Lambda handler
    """
    logger.info("%s - %s", event, context)

    logger.info("Wu-Tang %s", tang().capitalize())

    return event
