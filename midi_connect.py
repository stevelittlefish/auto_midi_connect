"""
Connect all midi devices to each other!
"""

import logging

__author__ = 'Stephen Brown (Little Fish Solutions LTD)'

log = logging.getLogger(__name__)

VERSION = '0.0.0'

VERBOSE = True

if __name__ == '__main__':
    if VERBOSE:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    log.info('Midi Connect v{}'.format(VERSION))
