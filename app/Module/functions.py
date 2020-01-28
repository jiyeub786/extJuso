import pandas as pd
import xml.etree.ElementTree as ET
import os
import time
from urllib.request import urlopen
from urllib import parse
from .logger import logger
base_dir = os.path.dirname( os.path.abspath( __file__ ) )



def searchJuso(param):
    #local juso api server url
    url = "http://127.0.0.1:8983/app/search/addrSearchApi.do?resultType=xml&countPerPage=1&keyword="+param
    response = urlopen(url).read().decode("utf-8")
    return response


def makeOutput(InputFileNm,OutputFileNm):
    logger.info("Start Juso Extract-makeOutput")
    df = pd.read_excel(InputFileNm, sheet_name='Sheet1')

    header = ""
    header_strings =["no"
                    ,"key"
                    ,"keyword"
                    ,""
                    ,""
                    ,"totalcount"
                    ,"currentpage"
                    ,"countperpage"
                    ,"errorcode"
                    ,"errormessage"
                    ,""
                    ,"roadAddr"
                    ,"roadAddrPart1"
                    ,"roadAddrPart2"
                    ,"jibunAddr"
                    ,"engAddr"
                    ,"zipNo"
                    ,"admCd"
                    ,"rdMgtSn"
                    ,"bdMgtSn"
                    ,"detBdNmList"
                    ,"bdNm"
                    ,"siNm"
                    ,"sggNm"
                    ,"emdNm"
                    ,"liNm"
                    ,"rn"
                    ,"buldMnnm"
                    ,"buldSlno"
                    ,"lnbrMnnm"
                    ,"lnbrSlno"
                    ,"bdKdcd"
                    ,"udrtYn"
                    ,"mtYn" ]

#make header
    for i in header_strings:
        header = header + i + "\t"


    f = open(OutputFileNm, mode='wt', encoding='utf-8')
#write header
    f.write(header)
    f.write("\n")

    start_time = "start time : " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    logger.info(start_time)
    end_time = ''

    for c in df.index:
        time.sleep(0.007) # 요청 주기를 조정하지 않으면 서버에서 오류발생
        key = str(df.loc[c, "key"])
        keyword = str(df.loc[c, "keyword"])
        root = ET.fromstring(searchJuso(parse.quote(keyword, encoding='utf-8')))
        result = ''
        result += str(c) + "\t" + str(key) + "\t" + str(keyword) + "\t"
        for child in root.iter():
            result += str(child.text) + "\t"
        logger.info(result)
        f.write(result)
        f.write("\n")

    end_time = "end time : " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    f.write(start_time)
    f.write("\n")
    f.write(end_time)

    # end Write result
    f.close()
    logger.info("End Juso Extract")