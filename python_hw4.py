##################################################################
# 프로그램명: 영문과 숫자를 리스트로 출력하는 프로그램
# 일자: 2022 - 03 - 30
# 이름: 박규민
# 학번: 21912211
##################################################################

#각 list 생성
Upper = []
Lower = []
Digits = []

#대문자 리스트, 소문자 리스트 원소 추가
for i in range(26):
    Upper.append(chr(65+i))
    Lower.append(chr(97+i))

#숫자 리스트에 문자열 숫자 추가
for i in range(10):
    Digits.append(str(i))


print("Upper case alphabets : ")
print(Upper)
print("Lower case alphabets : ")
print(Lower)
print("Digits : ")
print(Digits)



##################################################################
# 프로그램명: 입력받은 날짜 오름차순 정렬하는 프로그램
# 일자: 2022 - 03 - 30
# 이름: 박규민
# 학번: 21912211
##################################################################

print("input 10 dates in (year month day) format : ")
ymd = []#리스트 생성

for i in range(10):
    year, month, day = input("input year, month, day : ").split()#각 변수에 입력받은 값 넣기
    list_ymd = list(map(int,(year,month, day)))#문자열을 정수형으로 바꾼 뒤 list로 합하여줌
    ymd.append(tuple(list_ymd))#ymd 리스트에 튜플 원소를 더해줌
    print("L_dates = ",ymd)


print("After input of 10 dates : ")
print("L_dates = ",ymd)
ymd.sort()#리스트 오름차순 정렬
print("After sorting, L_dates = ",ymd)



##################################################################
# 프로그램명: 시간을 입력받아 오름차순으로 정렬하는 파이썬 프로그램
# 일자: 2022 - 03 - 30
# 이름: 박규민
# 학번: 21912211
##################################################################

times = []

print("Input 10 times in (hour minute sec) format : ")

for i in range(10):
    h,m,s = input("input hour minute second : ").split()#시분초변수 값 받음
    int_times = list(map(int,(h,m,s)))#int형으로 바꾼후 list
    times.append(tuple(int_times))
    print("L_times : ",times)

times.sort()#오름차순 정렬
print("After sorting, L_times = ",times)

##################################################################
# 프로그램명: 학생 튜플 리스트 생성하여 정렬하는 프로그램
# 일자: 2022 - 03 - 30
# 이름: 박규민
# 학번: 21912211
##################################################################

student = [('Kim, S.C.',12001234,'CE', 4.10), ('Choi, Y.B.',119003234,'EE',3.78),\
    ('Hong, C.H.',21001547,'ICE',4.13), ('Yoon, Y.H',17002571,'ME',3.55),\
    ('Lee, S.H.',20003257,'ICE',4.45), ('Kim, H.Y.',19001234,'CE',4.17),\
    ('Lee, J.K.',18003234,'EE',3.78),  ('Park, S.Y.',21001643,'ICE',4.13),\
    ('Jang, S.H.',19002567,'ME',3.35), ('Yeom, C.S.',20005243,'CE',4.45)]

for i in range(len(student)):#튜플리스트 학생 열명을 순서대로 출력
    print("student[{:2}] : name({:10}), st_id({}), major({}, GPA({}))".format(i,student[i][0],student[i][1],student[i][2],student[i][3]))

print()

print("After sorting in increasing order : ")
student.sort()#기준 없이 오름차순 정렬
for i in range(len(student)):
    print("student[{:2}] : name({:10}), st_id({}), major({}, GPA({}))".format(i,student[i][0],student[i][1],student[i][2],student[i][3]))

print()

print("After sorting according to GPA in decreasing order : ")
#sort(key파라미터, reverse파라미터)
#lambda x:x[0] -> 0번째 인수를 기준으로 정렬한다.
student.sort(key = lambda x:x[3],reverse = True)#3번째 인수를 기준으로 오름차순 정렬
for i in range(len(student)):
    print("student[{:2}] : name({:10}), st_id({}), major({}, GPA({}))".format(i,student[i][0],student[i][1],student[i][2],student[i][3]))



##################################################################
# 프로그램명: 국가 이름을 입력받아 해당 국가의 수도 이름을 찾아내는 프로그램
# 일자: 2022 - 03 - 30
# 이름: 박규민
# 학번: 21912211
##################################################################
dict_na_ca ={} #딕셔너리 생성

#국가와 수도 10개 입력받기
for i in range(10):
    nation, capital = input("Input nation and its capital (. to quit)  : ").split()
    dict_na_ca[nation] = capital

print("dict_nation_capital  :  ",dict_na_ca)


while True:#'.'입력때 까지 무한으로 입력 받기
    input_nation = input("Input nation and its capital (. to quit)  : ")
    if input_nation == ".":
        break

    #입력받은 키값인 나라의 value값인 수도를 출력
    input("Input nation to find its {}".format(dict_na_ca[input_nation]))

