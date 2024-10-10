from datetime import datetime
from test_case_cadastro_growth import test_case_casdastro_growth
import logging

def main():

    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='log_file.log', encoding='utf-8', level=logging.DEBUG)

    if test_case_casdastro_growth(logger):
        logger.info("Passou no teste")
        return

    logger.error("Não completou o teste")


if __name__ == '__main__':
    main()

