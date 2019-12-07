"""
Challenge Description
"""

import logging
import sys

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, format='[%(levelname)s] %(message)s', level=logging.INFO)
    log = logging.getLogger(__name__)

    # log.info(f"Part 1: {}")
    # log.info(f"Part 2: {}")