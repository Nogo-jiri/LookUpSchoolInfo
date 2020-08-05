# LookUpSchoolInfo

Just by typing school name, look up school's informations (Use NEIS OpenAPI)

학교 이름을 입력해서 학교의 정보를 조회합니다. (나이스 교육정보 개방 포털 OpenAPI 이용)

조회 가능한 정보는 다음과 같습니다.
- 학교명, 학교 영문명, 설립명, 표준 학교 코드
- 시도교육청명, 시도교육청 코드
- 주소 (도로명 우편번호, 도로명주소, 상세주소)
- 전화번호, 팩스번호, 홈페이지 주소
- 학교 구분명 (고등학교 구분명, 특목고 계열명, 전후기 구분명 등)
- 이외 기타 정보

# Usage

1. `requirements.txt` 파일이 있는 위치에서 `pip install -r requirements.txt` 명령어를 입력하여 필요한 모듈을 다운로드받습니다.

2. `LookUpSchoolInfo.py` 파일을 실행합니다.

3. 학교 이름을 입력합니다. 예) 학교 이름이 '성남고등학교'라면 '성남고등학교' 또는 '성남고' 입력

3-1. 동명의 학교가 존재한다면 다음과 같이 출력됩니다.

>1. 서울특별시교육청 성남고등학교
>2. ?????교육청 성남고등학교
>동명의 학교가 존재합니다. 숫자를 입력해주세요: 

번호를 입력해 학교를 선택해주세요. 예) 서울특별시에 소재한 성남고등학교에 대한 정보를 조회하려면 숫자 '1' 한자리만 입력

4. 학교 정보가 다음과 같이 출력됩니다.
>
>
>5

5. 동명의 학교가 5개보다 많이 존재하면 3-1 과정에서 6번째부터는 출력되지 않습니다. 이는 OpenAPI 샘플 URL에 인증키가 없어 5건만 샘플로 출력되는 것으로, [나이스 교육정보 개방 포털](https://open.neis.go.kr)에 접속하여 인증키를 발급받으신 후 `OpenAPIKey.json` 파일을 수정하시기 바랍니다.

# ToDoList
키에 해당하는 값이 "None"일 때 출력하지 않게 만들기
