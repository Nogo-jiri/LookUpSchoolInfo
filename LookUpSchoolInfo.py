import json
import requests

#학교 정보를 출력하는 함수 선언
def PrintData(x):
    for key in APIData:
        if key in SchoolData[x-1]:
            print(APIData[key],":",SchoolData[x-1][key])

#학교명 입력받고 API 조회해서 json 파일 저장
SchoolName=input("정보를 조회하고자 하는 학교의 이름을 입력하세요: ")
url="https://open.neis.go.kr/hub/schoolInfo?SCHUL_NM={m}&Type=json".format(m=SchoolName)
JsonData=requests.get(url).json()

#API 출력명과 출력 설명 대치
APIData={
    "SCHUL_NM": "학교명",
    "FOND_SC_NM": "설립명",
    "ENG_SCHUL_NM": "학교 영문명",
    "SD_SCHUL_CODE": "표준 학교 코드",
    "SCHUL_KND_SC_NM": "학교급",
    "HS_SC_NM": "고등학교 구분",
    "COEDU_SC_NM": "성별 구분",
    "LCTN_SC_NM": "소재지명",
    "ORG_RDNZC": "우편번호(도로명)",
    "ORG_RDNMA": "도로명주소",
    "ORG_RDNDA": "상세주소",
    "HMPG_ADRES": "홈페이지 주소",
    "ORG_TELNO": "전화번호",
    "ORG_FAXNO": "팩스 번호",
    "ATPT_OFCDC_SC_NM": "시도교육청명",
    "ATPT_OFCDC_SC_CODE": "시도교육청 코드",
    "JU_ORG_NM": "관할 조직(교육청)명",
    "INDST_SPECL_CCCCL_EXST_YN": "산업체특별학급 존재 여부",
    "HS_GNRL_BUSNS_SC_NM": "고등학교 일반/실업 구분",
    "SPCLY_PURPS_HS_ORD_NM": "특수목적고등학교 계열명",
    "ENE_BFE_SEHF_SC_NM": "입시 전후기 구분",
    "DGHT_SC_NM": "주야 구분",
    "FOND_YMD": "설립일자",
    "FOAS_MEMRD": "개교기념일",
    "LOAD_DTM": "적재일시"
}

#json 파일에 학교 정보가 제대로 있는 경우
if "schoolInfo" in JsonData:
    #동명의 학교 개수를 SchoolCount에 저장
    SchoolCount=JsonData["schoolInfo"][0]["head"][0]["list_total_count"]

    #학교 정보를 모두 담을 배열 선언
    SchoolData=[]

    #SchoolCount 수만큼 SchoolData 배열에 학교 정보 모두 저장
    for n in range(0,SchoolCount):
        SchoolData.append(JsonData["schoolInfo"][1]["row"][n])

    #동명의 학교 있음
    if SchoolCount>=2:
        #동명의 학교 출력 후 조회하고자 하는 학교의 번호를 DataNumber에 저장
        for n in range(0,SchoolCount):
            print(str(n+1)+". "+SchoolData[n]["ATPT_OFCDC_SC_NM"]+"의 "+SchoolData[n]["SCHUL_NM"])
        DataNumber=int(input("어느 학교의 정보를 조회하시겠습니까? 번호를 입력해주세요: "))
    #동명의 학교가 없음
    else:
        DataNumber=1

    #조회된 정보 출력
    PrintData(DataNumber)

#json 파일에 학교 정보가 제대로 있지 않은 경우
else:
    print("학교 이름을 잘못 입력하셨거나 네트워크에 연결되어있지 않습니다. 다시 확인해주시기 바랍니다.")
