import os
from Module import functions
from Module.logger import logger


def main():

    #log = logger.GetLogger()
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # read Xlsx
    InputFileNm = base_dir + "\Files\INPUT.xlsx"
    logger.info("input file : "+InputFileNm)

    # setting result file
    OutputFileNm = base_dir + "\Files\OUTPUT.txt"
    logger.info("output file : "+OutputFileNm)

    try:
        functions.makeOutput(InputFileNm, OutputFileNm)
    except Exception as ex:
        logger.info(ex)
        logger.info(ex.with_traceback())


if __name__ == "__main__":
    main()