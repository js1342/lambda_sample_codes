| 함수 이름         | 함수 설명                                    | Method | Request Body (Vue --> lambda)            | Response Body (lambda --> Vue)  |
| ------------- | ---------------------------------------- | ------ | ---------------------------------------- | ------------------------------- |
| getClothes    | 사용자의 옷 전체 불러오기                           | GET    | user_id (cognito) / name                 | clothes 테이블 정보 전체               |
| getOutfit     | 사용자의 코디 전체 불러오기                          | GET    | user_id (cognito) / name                 | outfit 테이블 전체                   |
| putClothes    | 옷 새로 등록하기                                | POST   | user_id(cognito), category(AI), color(AI), s3_bucket_url, file_name(IoT) | clothes 테이블 업데이트된 정보            |
| putOutfit     | event['button_id']=등록<br />1. 등록하기를 누른 상황: saved=1, worndate=[], 나머지 정보 추가<br />event['button_id']=오늘의코디<br />2-1. 이미 등록된 옷: worndate=추가<br />2-2. 아직 등록 안된 옷:<br />saved=0, worndate=추가, 나머지 정보도 추가<br />event['button_id']=코디보내기<br />3-1. 이미 등록된 옷:이미 있는 옷입니다!<br />3-2. 새로운 옷<br />saved=1, sender_id=내 아이디 | POST   | user_id(cognito), outfit(dict), eventtype,  wornddate=today() *람다에서 처리, sender_id **optional | outfit 테이블에서 saved = 1 업데이트된 정보 |
| getCategories | 카테고리 전체 불러오기                             | GET    |                                          | category 테이블 이름 전체              |
| getWeather    | 날씨정보 불러오기                                | GET    |                                          | 날씨 api 사용해서 온도, 날씨, 습도..?       |
| getUser       | 유저정보 불러오기                                | GET    | user_id(cognito)                         | user 테이블 전체                     |
| filterClothes | 카테고리 별로 옷 조회                             | GET    | user_id(cognito), category               | category별로 필터된 clothes          |
| searchFriend  | 친구 아이디를 검색하면 검색 query를 포함한 결과 출력         | GET    | q                                        | name에 맞는 사용자 리스트                |
| addFriend     | 친구 추가하기                                  | POST   | user_id(cognito), receiver_id            | 친구 리스트                          |
| acceptFriend  | 친구 추가 승낙하기                               | POST   | receiver_id(cognito), user_id            | 친구 리스트                          |
| likeClothes   | 친구의 옷장에서 옷 좋아요 / 좋아요 취소 하기               | POST   | user_id(cognito), clothes_id             |                                 |

