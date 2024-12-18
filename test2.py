# from datetime import datetime

# json = {
#   "bound": "O",
#   "startPlcNameSel": ["BUSAN"],
#   "destPlcNameSel": ["JEBEL ALI"],
#   "startCtrNameSel": ["KOREA"],
#   "destCtrNameSel": ["UNITED ARAB EMIRATES"],
#   "arrayStartCtrCd": ["KR"],
#   "arrayStartPlcCd": ["PUS"],
#   "arrayDestCtrCd": ["AE"],
#   "arrayDestPlcCd": ["JEA"],
#   "listSchedule": [
#     {
#       "vslCd": "JESN",
#       "vslNm": "ESL SANA",
#       "voyNo": "02443W",
#       "pol": "PNC",
#       "polCtrCd": "KR",
#       "polNm": "BUSAN NEW PORT, KOREA",
#       "pod": "JEA",
#       "podCtrCd": "AE",
#       "podNm": "JEBEL ALI,UNITED ARAB EMIRATES",
#       "etd": "20241030",
#       "etdTm": "1200",
#       "eta": "20241125",
#       "etaTm": "2100",
#       "polEtb": "20241029",
#       "polEtbTm": "1500",
#       "polTml": "PNCT",
#       "podTml": "JBAI1",
#       "itrmlNm": "JEBEL ALI TMNL 1",
#       "otrmlNm": "Pusan New Port",
#       "ts": "N",
#       "cct": "202410281900",
#       "closeTime": "202410281900",
#       "transitTime": "26\uc77c 9\uc2dc\uac04 ",
#       "callSign": "CQ2152",
#       "mrnNo": "24EMSK0029E",
#       "apoTcnt": "6",
#       "bound": "O",
#       "rteCd": "AIM",
#       "rteCdNm": "ASIAN INDIA MIDDLE-EAST SERVICE",
#       "targetVoy": "02443W",
#       "vslCd1": "JESN",
#       "vslNm1": "ESL SANA",
#       "vslType1": "03",
#       "pol1": "PNC",
#       "polEtb1": "20241029",
#       "polEtd1": "20241030",
#       "pod1": "JEA",
#       "pod1Nm": "JEBEL ALI,UNITED ARAB EMIRATES",
#       "podEtd1": "20241125",
#       "polTrml1": "PNCT",
#       "podTrml1": "JBAI1",
#       "podTrml1Nm": "JEBEL ALI TMNL 1",
#       "etdTm1": "1200",
#       "etaTm1": "2100",
#       "transitTime1": "26\uc77c 9\uc2dc\uac04 ",
#       "bkgMfCls": "202410251700",
#       "bkgDocCls": "202410251300",
#       "bkgDocPic": "",
#       "bkgCgoCls": "202410281900",
#       "bkgAsPolTrmlCd": "PNCT",
#       "bkgCgoPic": "\ud130\ubbf8\ub110   051-6018114",
#       "cfsCls": "202410250900",
#       "bkgCfsPic": "",
#       "bkgVslCd": "JESN",
#       "bkgVoyNo": "02443W",
#       "tsDegree": "0",
#       "portCd": "PNC",
#       "targetVsl": "JESN",
#       "closeInfoVO": {
#         "bkgDocCls": "202410251300",
#         "bkgCgoCls": "202410281900",
#         "bkgCgoPic": "\ud130\ubbf8\ub110   051-6018114",
#         "bkgAsPolTrmlCd": "PNCT",
#         "bkgMfCls": "202410251700",
#         "bkgMrnNo": "24EMSK0029E",
#         "bkgCallSign": "CQ2152",
#         "bkgApoTcnt": "6",
#         "cfsCls": "202410250900",
#         "vslCls": "0",
#         "salesCls": "1",
#         "seq": "0",
#         "bkgClosed": "CLOSED",
#         "vgmCgoCls": "202410251300"
#       },
#       "bkgClose": "Y",
#       "bkgClosed": "WCLOSED",
#       "bkgDocTime": "202410251300",
#       "info": "ESL SANA:JESN:02443W:PNC:PNCT:202410301200:JEA:JBAI1:202411252100:202410281900:CQ2152:N:@_@ESL SANA:PNC:202410301200:JEA:202411252100:02443W:9478518:9478529:03:02443W:02443W:PNCT:JBAI1:9478518:9478529:0:0:JESN@_@",
#       "ordType": 0,
#       "prrmSgEtd": "20241017",
#       "schSeq": "9478518",
#       "vgmDocCls": "202410251300",
#       "filterChkYN": "Y",
#       "prfmEtd": "20241023",
#       "prfmEtdTm": "0600",
#       "prfmEtdWd": "4",
#       "prfmEta": "20241116",
#       "prfmEtaTm": "0500",
#       "prfmEtaWd": "7",
#       "itrmlCd": "JBAI1",
#       "otrmlCd": "PNCT",
#       "eirCloCls": "",
#       "eirOpenCls": "",
#       "rteCdVo": {
#         "vslCd": "JESN",
#         "polCd": "PNC",
#         "polTrml": "PNCT",
#         "voyNo": "02443W",
#         "polSeq": "9478518"
#       },
#       "priority": "N",
#       "mcOpenYn": "N",
#       "rfYn": "",
#       "kmtcPremiumLineYn": "N",
#       "ttransDds": "26"
#     },
#     {
#       "vslCd": "JGGX",
#       "vslNm": "GFS GALAXY",
#       "voyNo": "02444W",
#       "pol": "PNC",
#       "polCtrCd": "KR",
#       "polNm": "BUSAN NEW PORT, KOREA",
#       "pod": "JEA",
#       "podCtrCd": "AE",
#       "podNm": "JEBEL ALI,UNITED ARAB EMIRATES",
#       "etd": "20241102",
#       "etdTm": "1500",
#       "eta": "20241126",
#       "etaTm": "0500",
#       "polEtb": "20241101",
#       "polEtbTm": "1200",
#       "polTml": "PNCT",
#       "podTml": "JBAI1",
#       "itrmlNm": "JEBEL ALI TMNL 1",
#       "otrmlNm": "Pusan New Port",
#       "ts": "N",
#       "cct": "202411010300",
#       "closeTime": "202411010300",
#       "transitTime": "23\uc77c 14\uc2dc\uac04 ",
#       "callSign": "V7A4687",
#       "mrnNo": "24SJLU1006E",
#       "apoTcnt": "6",
#       "bound": "O",
#       "rteCd": "AIM",
#       "rteCdNm": "ASIAN INDIA MIDDLE-EAST SERVICE",
#       "targetVoy": "02444W",
#       "vslCd1": "JGGX",
#       "vslNm1": "GFS GALAXY",
#       "vslType1": "03",
#       "pol1": "PNC",
#       "polEtb1": "20241101",
#       "polEtd1": "20241102",
#       "pod1": "JEA",
#       "pod1Nm": "JEBEL ALI,UNITED ARAB EMIRATES",
#       "podEtd1": "20241126",
#       "polTrml1": "PNCT",
#       "podTrml1": "JBAI1",
#       "podTrml1Nm": "JEBEL ALI TMNL 1",
#       "etdTm1": "1500",
#       "etaTm1": "0500",
#       "transitTime1": "23\uc77c 14\uc2dc\uac04 ",
#       "bkgMfCls": "202410301700",
#       "bkgDocCls": "202410301300",
#       "bkgDocPic": "",
#       "bkgCgoCls": "202411010300",
#       "bkgAsPolTrmlCd": "PNCT",
#       "bkgCgoPic": "\ud130\ubbf8\ub110   051-6018114",
#       "cfsCls": "202410290900",
#       "bkgCfsPic": "",
#       "bkgVslCd": "JGGX",
#       "bkgVoyNo": "02444W",
#       "tsDegree": "0",
#       "portCd": "PNC",
#       "targetVsl": "JGGX",
#       "closeInfoVO": {
#         "bkgDocCls": "202410301300",
#         "bkgCgoCls": "202411010300",
#         "bkgCgoPic": "\ud130\ubbf8\ub110   051-6018114",
#         "bkgAsPolTrmlCd": "PNCT",
#         "bkgMfCls": "202410301700",
#         "bkgMrnNo": "24SJLU1006E",
#         "bkgCallSign": "V7A4687",
#         "bkgApoTcnt": "6",
#         "cfsCls": "202410290900",
#         "vslCls": "1",
#         "salesCls": "1",
#         "seq": "1",
#         "bkgClosed": "CLOSED",
#         "vgmCgoCls": "202410301300"
#       },
#       "bkgClose": "Y",
#       "bkgClosed": "CLOSED",
#       "bkgDocTime": "202410301300",
#       "info": "GFS GALAXY:JGGX:02444W:PNC:PNCT:202411021500:JEA:JBAI1:202411260500:202411010300:V7A4687:N:@_@GFS GALAXY:PNC:202411021500:JEA:202411260500:02444W:9539290:9539299:03:02444W:02444W:PNCT:JBAI1:9539290:9539299:0:0:JGGX@_@",
#       "ordType": 0,
#       "prrmSgEtd": "20241024",
#       "schSeq": "9539290",
#       "vgmDocCls": "202410301300",
#       "filterChkYN": "Y",
#       "prfmEtd": "20241030",
#       "prfmEtdTm": "0600",
#       "prfmEtdWd": "4",
#       "prfmEta": "20241123",
#       "prfmEtaTm": "0500",
#       "prfmEtaWd": "7",
#       "itrmlCd": "JBAI1",
#       "otrmlCd": "PNCT",
#       "eirCloCls": "",
#       "eirOpenCls": "",
#       "rteCdVo": {
#         "vslCd": "JGGX",
#         "polCd": "PNC",
#         "polTrml": "PNCT",
#         "voyNo": "02444W",
#         "polSeq": "9539290"
#       },
#       "priority": "N",
#       "mcOpenYn": "N",
#       "rfYn": "",
#       "kmtcPremiumLineYn": "N",
#       "ttransDds": "24"
#     },
#     {
#       "vslCd": "JEWF",
#       "vslNm": "ESL WAFA",
#       "voyNo": "02445W",
#       "pol": "PNC",
#       "polCtrCd": "KR",
#       "polNm": "BUSAN NEW PORT, KOREA",
#       "pod": "JEA",
#       "podCtrCd": "AE",
#       "podNm": "JEBEL ALI,UNITED ARAB EMIRATES",
#       "etd": "20241109",
#       "etdTm": "2357",
#       "eta": "20241202",
#       "etaTm": "0900",
#       "polEtb": "20241108",
#       "polEtbTm": "1900",
#       "polTml": "PNCT",
#       "podTml": "JBAI1",
#       "itrmlNm": "JEBEL ALI TMNL 1",
#       "otrmlNm": "Pusan New Port",
#       "ts": "N",
#       "cct": "202411080600",
#       "closeTime": "202411080600",
#       "transitTime": "22\uc77c 9\uc2dc\uac04 3\ubd84",
#       "callSign": "CQ2247",
#       "mrnNo": "24EMSK0030E",
#       "apoTcnt": "7",
#       "bound": "O",
#       "rteCd": "AIM",
#       "rteCdNm": "ASIAN INDIA MIDDLE-EAST SERVICE",
#       "targetVoy": "02445W",
#       "vslCd1": "JEWF",
#       "vslNm1": "ESL WAFA",
#       "vslType1": "03",
#       "pol1": "PNC",
#       "polEtb1": "20241108",
#       "polEtd1": "20241109",
#       "pod1": "JEA",
#       "pod1Nm": "JEBEL ALI,UNITED ARAB EMIRATES",
#       "podEtd1": "20241202",
#       "polTrml1": "PNCT",
#       "podTrml1": "JBAI1",
#       "podTrml1Nm": "JEBEL ALI TMNL 1",
#       "etdTm1": "2357",
#       "etaTm1": "0900",
#       "transitTime1": "22\uc77c 9\uc2dc\uac04 3\ubd84",
#       "bkgMfCls": "202411071700",
#       "bkgDocCls": "202411071000",
#       "bkgDocPic": "",
#       "bkgCgoCls": "202411080600",
#       "bkgAsPolTrmlCd": "PNCT",
#       "bkgCgoPic": "\ud130\ubbf8\ub110   051-6018114",
#       "cfsCls": "202411061000",
#       "bkgCfsPic": "",
#       "bkgVslCd": "JEWF",
#       "bkgVoyNo": "02445W",
#       "tsDegree": "0",
#       "portCd": "PNC",
#       "targetVsl": "JEWF",
#       "closeInfoVO": {
#         "bkgDocCls": "202411071000",
#         "bkgCgoCls": "202411080600",
#         "bkgCgoPic": "\ud130\ubbf8\ub110   051-6018114",
#         "bkgAsPolTrmlCd": "PNCT",
#         "bkgMfCls": "202411071700",
#         "bkgMrnNo": "24EMSK0030E",
#         "bkgCallSign": "CQ2247",
#         "bkgApoTcnt": "7",
#         "cfsCls": "202411061000",
#         "vslCls": "1",
#         "salesCls": "1",
#         "seq": "2",
#         "bkgClosed": "CLOSED",
#         "vgmCgoCls": "202411071000"
#       },
#       "bkgClose": "Y",
#       "bkgClosed": "CLOSED",
#       "bkgDocTime": "202411071000",
#       "info": "ESL WAFA:JEWF:02445W:PNC:PNCT:202411092357:JEA:JBAI1:202412020900:202411080600:CQ2247:N:@_@ESL WAFA:PNC:202411092357:JEA:202412020900:02445W:9539402:9539411:03:02445W:02445W:PNCT:JBAI1:9539402:9539411:0:0:JEWF@_@",
#       "ordType": 0,
#       "prrmSgEtd": "20241031",
#       "schSeq": "9539402",
#       "vgmDocCls": "202411071000",
#       "filterChkYN": "Y",
#       "prfmEtd": "20241106",
#       "prfmEtdTm": "0600",
#       "prfmEtdWd": "4",
#       "prfmEta": "20241130",
#       "prfmEtaTm": "0500",
#       "prfmEtaWd": "7",
#       "itrmlCd": "JBAI1",
#       "otrmlCd": "PNCT",
#       "eirCloCls": "",
#       "eirOpenCls": "",
#       "rteCdVo": {
#         "vslCd": "JEWF",
#         "polCd": "PNC",
#         "polTrml": "PNCT",
#         "voyNo": "02445W",
#         "polSeq": "9539402"
#       },
#       "priority": "N",
#       "mcOpenYn": "N",
#       "rfYn": "",
#       "kmtcPremiumLineYn": "N",
#       "ttransDds": "23"
#     },
#     {
#       "vslCd": "JEPU",
#       "vslNm": "ESL BUSAN",
#       "voyNo": "02446W",
#       "pol": "PNC",
#       "polCtrCd": "KR",
#       "polNm": "BUSAN NEW PORT, KOREA",
#       "pod": "JEA",
#       "podCtrCd": "AE",
#       "podNm": "JEBEL ALI,UNITED ARAB EMIRATES",
#       "etd": "20241116",
#       "etdTm": "0200",
#       "eta": "20241207",
#       "etaTm": "0430",
#       "polEtb": "20241115",
#       "polEtbTm": "0600",
#       "polTml": "PNCT",
#       "podTml": "JBAI1",
#       "itrmlNm": "JEBEL ALI TMNL 1",
#       "otrmlNm": "Pusan New Port",
#       "ts": "N",
#       "cct": "202411141800",
#       "closeTime": "202411141800",
#       "transitTime": "21\uc77c 2\uc2dc\uac04 30\ubd84",
#       "callSign": "CQCZ",
#       "mrnNo": "24EMSK0031E",
#       "apoTcnt": "2",
#       "bound": "O",
#       "rteCd": "AIM",
#       "rteCdNm": "ASIAN INDIA MIDDLE-EAST SERVICE",
#       "targetVoy": "02446W",
#       "vslCd1": "JEPU",
#       "vslNm1": "ESL BUSAN",
#       "vslType1": "03",
#       "pol1": "PNC",
#       "polEtb1": "20241115",
#       "polEtd1": "20241116",
#       "pod1": "JEA",
#       "pod1Nm": "JEBEL ALI,UNITED ARAB EMIRATES",
#       "podEtd1": "20241207",
#       "polTrml1": "PNCT",
#       "podTrml1": "JBAI1",
#       "podTrml1Nm": "JEBEL ALI TMNL 1",
#       "etdTm1": "0200",
#       "etaTm1": "0430",
#       "transitTime1": "21\uc77c 2\uc2dc\uac04 30\ubd84",
#       "bkgMfCls": "202411131700",
#       "bkgDocCls": "202411131400",
#       "bkgDocPic": "",
#       "bkgCgoCls": "202411141800",
#       "bkgAsPolTrmlCd": "PNCT",
#       "bkgCgoPic": "\ud130\ubbf8\ub110   051-6018114",
#       "cfsCls": "202411121600",
#       "bkgCfsPic": "",
#       "bkgVslCd": "JEPU",
#       "bkgVoyNo": "02446W",
#       "tsDegree": "0",
#       "portCd": "PNC",
#       "targetVsl": "JEPU",
#       "closeInfoVO": {
#         "bkgDocCls": "202411131400",
#         "bkgCgoCls": "202411141800",
#         "bkgCgoPic": "\ud130\ubbf8\ub110   051-6018114",
#         "bkgAsPolTrmlCd": "PNCT",
#         "bkgMfCls": "202411131700",
#         "bkgMrnNo": "24EMSK0031E",
#         "bkgCallSign": "CQCZ",
#         "bkgApoTcnt": "2",
#         "cfsCls": "202411121600",
#         "vslCls": "1",
#         "salesCls": "0",
#         "seq": "3",
#         "bkgClosed": "CLOSED",
#         "vgmCgoCls": "202411131400"
#       },
#       "bkgClose": "Y",
#       "bkgClosed": "CLOSED",
#       "bkgDocTime": "202411131400",
#       "info": "ESL BUSAN:JEPU:02446W:PNC:PNCT:202411160200:JEA:JBAI1:202412070430:202411141800:CQCZ:N:@_@ESL BUSAN:PNC:202411160200:JEA:202412070430:02446W:9539514:9539523:03:02446W:02446W:PNCT:JBAI1:9539514:9539523:0:0:JEPU@_@",
#       "ordType": 0,
#       "prrmSgEtd": "20241107",
#       "schSeq": "9539514",
#       "vgmDocCls": "202411131400",
#       "filterChkYN": "Y",
#       "prfmEtd": "20241113",
#       "prfmEtdTm": "0600",
#       "prfmEtdWd": "4",
#       "prfmEta": "20241207",
#       "prfmEtaTm": "0500",
#       "prfmEtaWd": "7",
#       "itrmlCd": "JBAI1",
#       "otrmlCd": "PNCT",
#       "eirCloCls": "",
#       "eirOpenCls": "",
#       "rteCdVo": {
#         "vslCd": "JEPU",
#         "polCd": "PNC",
#         "polTrml": "PNCT",
#         "voyNo": "02446W",
#         "polSeq": "9539514"
#       },
#       "priority": "N",
#       "mcOpenYn": "N",
#       "rfYn": "",
#       "kmtcPremiumLineYn": "N",
#       "ttransDds": "21"
#     },
#     {
#       "vslCd": "JEDN",
#       "vslNm": "ESL DANA",
#       "voyNo": "02447W",
#       "pol": "PNC",
#       "polCtrCd": "KR",
#       "polNm": "BUSAN NEW PORT, KOREA",
#       "pod": "JEA",
#       "podCtrCd": "AE",
#       "podNm": "JEBEL ALI,UNITED ARAB EMIRATES",
#       "etd": "20241128",
#       "etdTm": "2300",
#       "eta": "20241219",
#       "etaTm": "0800",
#       "polEtb": "20241127",
#       "polEtbTm": "1600",
#       "polTml": "PNCT",
#       "podTml": "JBAI1",
#       "itrmlNm": "JEBEL ALI TMNL 1",
#       "otrmlNm": "Pusan New Port",
#       "ts": "N",
#       "cct": "202411270200",
#       "closeTime": "202411270200",
#       "transitTime": "20\uc77c 9\uc2dc\uac04 ",
#       "callSign": "CQ2136",
#       "mrnNo": "24EMSK0032E",
#       "apoTcnt": "6",
#       "bound": "O",
#       "rteCd": "AIM",
#       "rteCdNm": "ASIAN INDIA MIDDLE-EAST SERVICE",
#       "targetVoy": "02447W",
#       "vslCd1": "JEDN",
#       "vslNm1": "ESL DANA",
#       "vslType1": "03",
#       "pol1": "PNC",
#       "polEtb1": "20241127",
#       "polEtd1": "20241128",
#       "pod1": "JEA",
#       "pod1Nm": "JEBEL ALI,UNITED ARAB EMIRATES",
#       "podEtd1": "20241219",
#       "polTrml1": "PNCT",
#       "podTrml1": "JBAI1",
#       "podTrml1Nm": "JEBEL ALI TMNL 1",
#       "etdTm1": "2300",
#       "etaTm1": "0800",
#       "transitTime1": "20\uc77c 9\uc2dc\uac04 ",
#       "bkgMfCls": "202411251700",
#       "bkgDocCls": "202411251500",
#       "bkgDocPic": "",
#       "bkgCgoCls": "202411270200",
#       "bkgAsPolTrmlCd": "PNCT",
#       "bkgCgoPic": "\ud130\ubbf8\ub110   051-6018114",
#       "cfsCls": "202411250900",
#       "bkgCfsPic": "",
#       "bkgVslCd": "JEDN",
#       "bkgVoyNo": "02447W",
#       "tsDegree": "0",
#       "portCd": "PNC",
#       "targetVsl": "JEDN",
#       "closeInfoVO": {
#         "bkgDocCls": "202411251500",
#         "bkgCgoCls": "202411270200",
#         "bkgCgoPic": "\ud130\ubbf8\ub110   051-6018114",
#         "bkgAsPolTrmlCd": "PNCT",
#         "bkgMfCls": "202411251700",
#         "bkgMrnNo": "24EMSK0032E",
#         "bkgCallSign": "CQ2136",
#         "bkgApoTcnt": "6",
#         "cfsCls": "202411250900",
#         "vslCls": "1",
#         "salesCls": "1",
#         "seq": "4",
#         "bkgClosed": "CLOSED",
#         "vgmCgoCls": "202411251500"
#       },
#       "bkgClose": "Y",
#       "bkgClosed": "CLOSED",
#       "bkgDocTime": "202411251500",
#       "info": "ESL DANA:JEDN:02447W:PNC:PNCT:202411282300:JEA:JBAI1:202412190800:202411270200:CQ2136:N:@_@ESL DANA:PNC:202411282300:JEA:202412190800:02447W:9539626:9539635:03:02447W:02447W:PNCT:JBAI1:9539626:9539635:0:0:JEDN@_@",
#       "ordType": 0,
#       "prrmSgEtd": "20241114",
#       "schSeq": "9539626",
#       "vgmDocCls": "202411251500",
#       "filterChkYN": "Y",
#       "prfmEtd": "20241120",
#       "prfmEtdTm": "0600",
#       "prfmEtdWd": "4",
#       "prfmEta": "20241214",
#       "prfmEtaTm": "0500",
#       "prfmEtaWd": "7",
#       "itrmlCd": "JBAI1",
#       "otrmlCd": "PNCT",
#       "eirCloCls": "",
#       "eirOpenCls": "",
#       "rteCdVo": {
#         "vslCd": "JEDN",
#         "polCd": "PNC",
#         "polTrml": "PNCT",
#         "voyNo": "02447W",
#         "polSeq": "9539626"
#       },
#       "priority": "N",
#       "mcOpenYn": "N",
#       "rfYn": "",
#       "kmtcPremiumLineYn": "N",
#       "ttransDds": "21"
#     },
#     {
#       "vslCd": "HKS",
#       "vslNm": "HAKATA SEOUL",
#       "voyNo": "2407W",
#       "pol": "PNC",
#       "polCtrCd": "KR",
#       "polNm": "BUSAN NEW PORT, KOREA",
#       "pod": "JEA",
#       "podCtrCd": "AE",
#       "podNm": "JEBEL ALI,UNITED ARAB EMIRATES",
#       "etd": "20241206",
#       "etdTm": "1000",
#       "eta": "20241226",
#       "etaTm": "1300",
#       "polEtb": "20241205",
#       "polEtbTm": "0100",
#       "polTml": "PNCT",
#       "podTml": "JBAI1",
#       "itrmlNm": "JEBEL ALI TMNL 1",
#       "otrmlNm": "Pusan New Port",
#       "ts": "N",
#       "cct": "202412041300",
#       "closeTime": "202412041300",
#       "transitTime": "20\uc77c 3\uc2dc\uac04 ",
#       "callSign": "3FOE7",
#       "mrnNo": "24KMTC4896E",
#       "apoTcnt": "7",
#       "bound": "O",
#       "rteCd": "AIM",
#       "rteCdNm": "ASIAN INDIA MIDDLE-EAST SERVICE",
#       "targetVoy": "2407W",
#       "vslCd1": "HKS",
#       "vslNm1": "HAKATA SEOUL",
#       "vslType1": "02",
#       "pol1": "PNC",
#       "polEtb1": "20241205",
#       "polEtd1": "20241206",
#       "pod1": "JEA",
#       "pod1Nm": "JEBEL ALI,UNITED ARAB EMIRATES",
#       "podEtd1": "20241226",
#       "polTrml1": "PNCT",
#       "podTrml1": "JBAI1",
#       "podTrml1Nm": "JEBEL ALI TMNL 1",
#       "etdTm1": "1000",
#       "etaTm1": "1300",
#       "transitTime1": "20\uc77c 3\uc2dc\uac04 ",
#       "bkgMfCls": "202412031700",
#       "bkgDocCls": "202412031300",
#       "bkgDocPic": "",
#       "bkgCgoCls": "202412041300",
#       "bkgAsPolTrmlCd": "PNCT",
#       "bkgCgoPic": "\ud130\ubbf8\ub110   051-6018114",
#       "cfsCls": "202412020900",
#       "bkgCfsPic": "",
#       "bkgVslCd": "HKS",
#       "bkgVoyNo": "2407W",
#       "tsDegree": "0",
#       "portCd": "PNC",
#       "targetVsl": "HKS",
#       "closeInfoVO": {
#         "bkgDocCls": "202412031300",
#         "bkgCgoCls": "202412041300",
#         "bkgCgoPic": "\ud130\ubbf8\ub110   051-6018114",
#         "bkgAsPolTrmlCd": "PNCT",
#         "bkgMfCls": "202412031700",
#         "bkgMrnNo": "24KMTC4896E",
#         "bkgCallSign": "3FOE7",
#         "bkgApoTcnt": "7",
#         "cfsCls": "202412020900",
#         "vslCls": "0",
#         "salesCls": "0",
#         "seq": "5",
#         "bkgClosed": "OPEN",
#         "vgmCgoCls": "202412031300"
#       },
#       "bkgClose": "N",
#       "bkgClosed": "OPEN",
#       "bkgDocTime": "202412031300",
#       "info": "HAKATA SEOUL:HKS:2407W:PNC:PNCT:202412061000:JEA:JBAI1:202412261300:202412041300:3FOE7:N:@_@HAKATA SEOUL:PNC:202412061000:JEA:202412261300:2407W:9669768:9669777:02:2407W:2407W:PNCT:JBAI1:9669768:9669777:0:0:HKS@_@",
#       "ordType": 0,
#       "prrmSgEtd": "20241121",
#       "schSeq": "9669768",
#       "vgmDocCls": "202412031300",
#       "filterChkYN": "Y",
#       "prfmEtd": "20241127",
#       "prfmEtdTm": "0600",
#       "prfmEtdWd": "4",
#       "prfmEta": "20241221",
#       "prfmEtaTm": "0500",
#       "prfmEtaWd": "7",
#       "itrmlCd": "JBAI1",
#       "otrmlCd": "PNCT",
#       "eirCloCls": "",
#       "eirOpenCls": "",
#       "rteCdVo": {
#         "vslCd": "HKS",
#         "polCd": "PNC",
#         "polTrml": "PNCT",
#         "voyNo": "2407W",
#         "polSeq": "9669768"
#       },
#       "priority": "N",
#       "mcOpenYn": "N",
#       "rfYn": "",
#       "kmtcPremiumLineYn": "Y",
#       "ttransDds": "20"
#     },
#     {
#       "vslCd": "JTSA",
#       "vslNm": "TS SHANGHAI",
#       "voyNo": "02449W",
#       "pol": "PNC",
#       "polCtrCd": "KR",
#       "polNm": "BUSAN NEW PORT, KOREA",
#       "pod": "JEA",
#       "podCtrCd": "AE",
#       "podNm": "JEBEL ALI,UNITED ARAB EMIRATES",
#       "etd": "20241208",
#       "etdTm": "0247",
#       "eta": "20241229",
#       "etaTm": "2317",
#       "polEtb": "20241207",
#       "polEtbTm": "0547",
#       "polTml": "PNCT",
#       "podTml": "JBAI1",
#       "itrmlNm": "JEBEL ALI TMNL 1",
#       "otrmlNm": "Pusan New Port",
#       "ts": "N",
#       "cct": "202412061747",
#       "closeTime": "202412061747",
#       "transitTime": "21\uc77c 20\uc2dc\uac04 30\ubd84",
#       "callSign": "V7A6435",
#       "mrnNo": "",
#       "apoTcnt": "0",
#       "bound": "O",
#       "rteCd": "AIM",
#       "rteCdNm": "ASIAN INDIA MIDDLE-EAST SERVICE",
#       "targetVoy": "02449W",
#       "vslCd1": "JTSA",
#       "vslNm1": "TS SHANGHAI",
#       "vslType1": "03",
#       "pol1": "PNC",
#       "polEtb1": "20241207",
#       "polEtd1": "20241208",
#       "pod1": "JEA",
#       "pod1Nm": "JEBEL ALI,UNITED ARAB EMIRATES",
#       "podEtd1": "20241229",
#       "polTrml1": "PNCT",
#       "podTrml1": "JBAI1",
#       "podTrml1Nm": "JEBEL ALI TMNL 1",
#       "etdTm1": "0247",
#       "etaTm1": "2317",
#       "transitTime1": "21\uc77c 20\uc2dc\uac04 30\ubd84",
#       "bkgMfCls": "202412051700",
#       "bkgDocCls": "202412051300",
#       "bkgDocPic": "",
#       "bkgCgoCls": "202412061747",
#       "bkgAsPolTrmlCd": "PNCT",
#       "bkgCgoPic": "\ud130\ubbf8\ub110   051-6018114",
#       "cfsCls": "202412040900",
#       "bkgCfsPic": "",
#       "bkgVslCd": "JTSA",
#       "bkgVoyNo": "02449W",
#       "tsDegree": "0",
#       "portCd": "PNC",
#       "targetVsl": "JTSA",
#       "closeInfoVO": {
#         "bkgDocCls": "202412051300",
#         "bkgCgoCls": "202412061747",
#         "bkgCgoPic": "\ud130\ubbf8\ub110   051-6018114",
#         "bkgAsPolTrmlCd": "PNCT",
#         "bkgMfCls": "202412051700",
#         "bkgCallSign": "V7A6435",
#         "bkgApoTcnt": "0",
#         "cfsCls": "202412040900",
#         "vslCls": "0",
#         "salesCls": "0",
#         "seq": "6",
#         "bkgClosed": "OPEN",
#         "vgmCgoCls": "202412051300"
#       },
#       "bkgClose": "N",
#       "bkgClosed": "OPEN",
#       "bkgDocTime": "202412051300",
#       "info": "TS SHANGHAI:JTSA:02449W:PNC:PNCT:202412080247:JEA:JBAI1:202412292317:202412061747:V7A6435:N:@_@TS SHANGHAI:PNC:202412080247:JEA:202412292317:02449W:9539930:9539939:03:02449W:02449W:PNCT:JBAI1:9539930:9539939:0:0:JTSA@_@",
#       "ordType": 0,
#       "prrmSgEtd": "20241128",
#       "schSeq": "9539930",
#       "vgmDocCls": "202412051300",
#       "filterChkYN": "Y",
#       "prfmEtd": "20241204",
#       "prfmEtdTm": "0600",
#       "prfmEtdWd": "4",
#       "prfmEta": "20241228",
#       "prfmEtaTm": "0500",
#       "prfmEtaWd": "7",
#       "itrmlCd": "JBAI1",
#       "otrmlCd": "PNCT",
#       "eirCloCls": "",
#       "eirOpenCls": "",
#       "rteCdVo": {
#         "vslCd": "JTSA",
#         "polCd": "PNC",
#         "polTrml": "PNCT",
#         "voyNo": "02449W",
#         "polSeq": "9539930"
#       },
#       "priority": "N",
#       "mcOpenYn": "N",
#       "rfYn": "",
#       "kmtcPremiumLineYn": "Y",
#       "ttransDds": "21"
#     }
#   ],
#   "weeks": "5",
#   "pol": "PUS",
#   "pod": "JEA",
#   "type": "",
#   "legIdx": "0",
#   "etaBookingMsg": "",
#   "etaCtrCd": "KR",
#   "main": "N",
#   "bkgNotCnt": "56",
#   "filterYN": "N",
#   "filterDirect": "Y",
#   "filterTS": "Y",
#   "filterTranMin": 0,
#   "filterTranMax": 0,
#   "polTrmlStr": "",
#   "podTrmlStr": "",
#   "directYn": "Y",
#   "tsYn": "N",
#   "filterPolTrmlList": ["PNCT@@(Pusan New Port)"],
#   "filterPodTrmlList": ["JBAI1@@(JEBEL ALI TMNL 1)"],
#   "filterPolTrmlListSize": 1,
#   "filterPodTrmlListSize": 1,
#   "filterPolCd": "PUS",
#   "filterPodCd": "JEA",
#   "pointLength": "",
#   "today": "2024. 11",
#   "todayStr2": "202411",
#   "startDay": 1,
#   "endDay": 30,
#   "week": 5,
#   "firstDayOfWeek": 6,
#   "prevMonth": "202410",
#   "nextMonth": "202412",
#   "viewType": "C",
#   "tdColor": ["R", "R", "R", "R", "R", "B", "B"],
#   "toDate": "20241127",
#   "effectDate": "20250126",
#   "sunCnt": 0,
#   "monCnt": 0,
#   "tueCnt": 0,
#   "wedCnt": 1,
#   "thuCnt": 0,
#   "friCnt": 0,
#   "satCnt": 0,
#   "voyCntSum": 1,
#   "rteCd": "AIM@@(ASIAN INDIA MIDDLE-EAST SERVICE)",
#   "insertCnt": 0,
#   "holidayList": [
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241101",
#       "bascDt2": "01",
#       "wdayCd": "6",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241102",
#       "bascDt2": "02",
#       "wdayCd": "7",
#       "hldYn": "Y",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241103",
#       "bascDt2": "03",
#       "wdayCd": "1",
#       "hldYn": "Y",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241104",
#       "bascDt2": "04",
#       "wdayCd": "2",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241105",
#       "bascDt2": "05",
#       "wdayCd": "3",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241106",
#       "bascDt2": "06",
#       "wdayCd": "4",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241107",
#       "bascDt2": "07",
#       "wdayCd": "5",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241108",
#       "bascDt2": "08",
#       "wdayCd": "6",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241109",
#       "bascDt2": "09",
#       "wdayCd": "7",
#       "hldYn": "Y",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241110",
#       "bascDt2": "10",
#       "wdayCd": "1",
#       "hldYn": "Y",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241111",
#       "bascDt2": "11",
#       "wdayCd": "2",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241112",
#       "bascDt2": "12",
#       "wdayCd": "3",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241113",
#       "bascDt2": "13",
#       "wdayCd": "4",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241114",
#       "bascDt2": "14",
#       "wdayCd": "5",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241115",
#       "bascDt2": "15",
#       "wdayCd": "6",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241116",
#       "bascDt2": "16",
#       "wdayCd": "7",
#       "hldYn": "Y",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241117",
#       "bascDt2": "17",
#       "wdayCd": "1",
#       "hldYn": "Y",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241118",
#       "bascDt2": "18",
#       "wdayCd": "2",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241119",
#       "bascDt2": "19",
#       "wdayCd": "3",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241120",
#       "bascDt2": "20",
#       "wdayCd": "4",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241121",
#       "bascDt2": "21",
#       "wdayCd": "5",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241122",
#       "bascDt2": "22",
#       "wdayCd": "6",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241123",
#       "bascDt2": "23",
#       "wdayCd": "7",
#       "hldYn": "Y",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241124",
#       "bascDt2": "24",
#       "wdayCd": "1",
#       "hldYn": "Y",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241125",
#       "bascDt2": "25",
#       "wdayCd": "2",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241126",
#       "bascDt2": "26",
#       "wdayCd": "3",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241127",
#       "bascDt2": "27",
#       "wdayCd": "4",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241128",
#       "bascDt2": "28",
#       "wdayCd": "5",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241129",
#       "bascDt2": "29",
#       "wdayCd": "6",
#       "hldYn": "N",
#       "hldNm": "NOT"
#     },
#     {
#       "ordType": 0,
#       "filterChkYN": "Y",
#       "bascDt": "20241130",
#       "bascDt2": "30",
#       "wdayCd": "7",
#       "hldYn": "Y",
#       "hldNm": "NOT"
#     }
#   ],
#   "insertRateMngResult": 0,
#   "strchange": "PUS",
#   "desrchange": "JEA"
# }


# now = datetime.now()
# date_str = now.strftime("%Y%m%d%H%M")
# # 조건에 맞는 첫 번째 객체 찾기
# first_valid_schedule = next(
#     (schedule for schedule in json.get('listSchedule') if date_str < schedule.get('closeTime')),
#     None
# )
# # 결과 출력
# print(json.get('arrayStartCtrCd')[0]) # KR
# print(json.get('arrayStartPlcCd')[0]) # PUS
# print(json.get('arrayDestCtrCd')[0]) # AE
# print(json.get('arrayDestPlcCd')[0]) # JEA
# print('porPlcCd', first_valid_schedule.get("etd")) # etd: 20241206
# print("Vessel Name:", first_valid_schedule.get('vslNm'))  # 특정 키 출력



# a = 1;
# b = 'str'
# def fc():
#     if a:
#         return (a, None)
#     else:
#         return a, b

# result1, result2 = fc()
# print(result1, result2)


param = {
        "polNm" : "BUSAN NEW PORT, KOREA",
        "podNm" : "JEBEL+ALI,UNITED+ARAB+EMIRATES"
    }
# 공백을 '+'로 대체하는 함수
def replace_space_with_plus(param):
    for key, value in param.items():
        if isinstance(value, str):  # 값이 문자열인 경우에만 처리
            param[key] = value.replace(" ", "+")
    return param

# param 딕셔너리 처리
param = replace_space_with_plus(param)

# 결과 출력
print(param)
