SELECT SCHUL_LAND_BULD_CODE KEY
       ,NVL(JIBUN_ADDR,ROAD_FULL_ADDR ) KEYWORD
FROM API_ADDR_INFO T1
WHERE NVL(JIBUN_ADDR,ROAD_FULL_ADDR ) IS  NOT NULL