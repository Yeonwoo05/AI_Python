# open API와 JSON 타입의 파일


# 닥셔너리 자료형
# 서로 대응관계를 가진 데이터로 이루어진 자료형
# 대응관계는 키와 값으로 표현
# 키로 인덱싱 하여 접근 가능


# JSON
# Java Script Object Notation의 약자
# 자바스크립트의 프로그래밍 언어부분에 기반하고 있으며
# 데이터를 효율적으로 저장하고 교환하는데 사용하는 텍스트
# 데이터 형식 중 하나

# 파이썬의 list와 JSON이
# JSON으로 변환하게 되면
# array로 바뀌며,
# 반대로 array는 list로 변환 된다


# 파이썬에서 JSON을 다룰려면
# import json으로 모듈을 불러와야 한다

import json

with open('student_file.json') as json_file:
    json_data = json.load(json_file)

json_data



# open API
# 인터넷 이용자가 웹 검색 결과 및 사용자 인터페이스 등을
# 수동적으로 제공받는데 그치지 않고
# 직접 응용 프로그램과 서비스를 개발할 수 있도록
# 공개된 API

# 인터넷 이용자가 웹 검색결과, 즉 데이터를
# 우리가 지정한 조건에 맞게끔 가져올 수 있는 도구

# open API를 활용하려면
# 해당업체에서 제공해 주는 '키'라는 것이 필요하다
# 종종 키가 필요없는 경우도 있음

# 필요한 데이터 확인
# 데이터 공급형태 확인
# 데이터 정제
