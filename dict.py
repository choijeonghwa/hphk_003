"""
파이썬 dictionary 활용 기초!
"""

# 1. 평균을 구하세요.
iu_score = {
    "수학": 80,
    "국어": 90,
    "음악": 100
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q1=====")
# 1. iu_score라고 하는 dic 변수에서 value값만 뽑아내보자.
total_score = 0
count = 0

# 2. 뽑아낸 값들의 총 합을 구한다.
for score in iu_score:
    total_score = total_score + iu_score[score]
    count+=1
print(total_score/count)

###--------------------------------------------------------

### 검색 : python get values in dictionary
scores = list(iu_score.values())

### 검색 : python get sum of list
print(sum(scores)/len(scores))



###############################################################

# 2. 반 평균을 구하세요.
score = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}
# 답변 코드는 아래에 작성해주세요.
print("=====Q2=====")
sum = 0
print(score.keys())
for j in score.keys():
    for i in score["iu"].values():
        sum += i
average = sum/(len(score.keys())*len(score["iu"].values()))
print(average)

###--------------------------------------------------------

print("=====Q2=====")

# 1. 각 반을 순회하는 반복문을 작성한다.

# 2. 한 반 순회를 할 때 1번에서 작성한 코드를 활용한다.

# 3. 출력한다.

for cl in score:
    print(score[cl])
    tmp = list(score[cl].values())
    print("{}: {}" .format(cl, sum(tmp)/len(tmp)))



###############################################################

# 3. 도시별 최근 3일의 온도 평균은?
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""



###############################################################

# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
city = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9],
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q3=====")

print((city.values()))

for citys,day in city.items():
    average = sum(day)/len(city[citys])
    print("{} : {}값" .format(citys, round(average,1)))

###------------------------------------------------

# 1. 각 도시를 순회하는 반복문을 작성한다.

# 2. 1번의 코드를 활용하여 순회할 때마다 평균 값을 출력한다.


# 검색 : python get round(반올림) / ceil(올림) / floor(내림) value
for cities in city:
    temp = city[cities]
    print("{}의 평균 기온: {:0.1f}".format(cities, sum(temp)/len(temp)))



###############################################################

# 답변 코드는 아래에 작성해주세요.
print("=====Q3-1=====")

tem=100

for cold in city.keys():
    for i in city[cold]:
        if i < tem:
            tem = i

for city, temp in city.items():
    for i in (temp):
        if i == tem:
            print(city)


###--------------------------------------------
# 1. 각 도시를 순회하는 반복문을 만든다.

# 2. 최저기온, 최고기온을 저장할 수 있는 변수를 선언한다.

# 3. 각 도시의 기온 정보를 순회하는 반복문을 만든다.

# 4. 순회하다가 최저기온의 경우에는 현재 저장된 값보다 작은 값이,
#    최고 기온의 경우에는 현재 저장된 값보다 큰 값이 있는 경우
#    현재 저장되어 있는 값을 바꾼다.

#           최고기온에 해당하는 조건문
#           최저기온에 해당하는 조건문

#검색 :  python change key of value

minimum = ["도시명", 1000]
maximum = ["도시명", -1000]

print(city)
for cities in city:
    for temp in city[cities]:
        if(maximum[1] < temp):
            maximum[0] = cities
            maximum[1] = temp
        if(minimum[1] > temp):
            minimum[0] = cities
            minimum[1] = temp
print("최고 기온은 {}의 {}도이며, 최저 기온은 {}의 {}도 입니다." .format(maximum[0], maximum[1], minimum[0], minimum[1]))




###############################################################

# 4. 위에서 서울은 영상 2도였던 적이 있나요?
# 답변 코드는 아래에 작성해주세요.
print("=====Q4=====")

count = 0
for tem in city["서울"]:
    if tem == 2:
        count+=1

if count > 0:
    print("서울은 영상 2도였던 적이 있었습니다.")
else:
    print("서울은 영상 2도였던 적이 없었습니다.")
    
###----------------------------------------------------------------

# 1. cities 변수에서 서울부분만 추출해서 seoul 변수에 저장한다.

# 1-1. flag 라고 하는 변수에 false를 저장한다. 

# 2. seoul 변수(list)를 순회하며 요소가 2와 같았던 적이 있는지 확인한다.

# 3. 2도 같았던 적이 있다면 flag 변수를 true로 바꿔준다.

# 4. flag 변수에 따라 출력문을 작성한다.

seoul = city["서울"]
flag = False

for tem in seoul:
    if tem == 2:
        flag = True

if flag == True:
    print("서울은 영상 2도였던 적이 있었습니다.")
else:
    print("서울은 영상 2도였던 적이 없었습니다.")
