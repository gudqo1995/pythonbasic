#flag 변수는 상반된 걸로 전환시키는 용도로 쓰임/True-False, +- 등
# i = 0
# flag = True
# while flag:
#     print(i, "종속 문장", end=" ")
#     if i == 10:
#         flag = False
#     i+=1

## break, continue
# while 조건식:
#     while 조건식:
#         break #전체가 아닌 종속 조건문에서만 빠져나옴

# i = 0
# while True:
#     if i == 3:
#         break
#         print("3 출력") #break 하위는 생략됨
#     print(i, "출력")
#     i+=1
# print("다음 문장")

# i = 0
# while i < 5:
#     i+=1
#     if i == 3:
#         continue
#         print("3 출력") #continue 하위는 생략됨
#     print(i, "촐력")
# print("다음 문장")

# for i in range(1,6,1):
#     if i == 3:
#         continue
#         print("3 출력")
#     print(i, "출력")
# print("다음 문장")

# else 버그 고치기
# num, result, i = 0, 0, 1
# while True:
#     num = int(input("1~10 사이의 숫자 입력:"))
#     if num < 1 or num > 10:
#         print("잘못 입력, 다시입력")
#         continue
#     break
# # else:
# print("next..")
# while i <= num:
#     result += i
#     i += 1
# else:
#     print("1~", num, "까지의 합:", result)
#flag로 고치기
# num, result, i = 0, 0, 1
# flag = True
# while flag:
#     num = int(input("1~10 사이의 숫자 입력:"))
#     if num < 1 or num > 10:
#         print("잘못 입력, 다시입력")
#         continue
#     else:
#         flag = False
# else:
#     print("next..")
# while i <= num:
#     result += i
#     i += 1
# else:
#     print("1~", num, "까지의 합:", result)
#break 위에 넣어주는 방법
# num, result, i = 0, 0, 1
# while True:
#     num = int(input("1~10 사이의 숫자 입력:"))
#     if num < 1 or num > 10:
#         print("잘못 입력, 다시입력")
#         continue
#     print("next..")
#     break
# while i <= num:
#     result += i
#     i += 1
# else:
#     print("1~", num, "까지의 합:", result)

# result = 0
# while True:
#     num = int(input("10~20사이의 숫자 입력:"))
#     if num < 10 or num > 20:
#         print("잘못된 숫자 입력, 다시 입력")
#         continue
#     break
# print("next..")
# for i in range(num+1):
#     result += i
# print("1~", num, "까지의 합:", result)

# for i in range(0,3,1):
#     for k in range(0,5,1):
#         if k == 3:
#             break
#         print("(i: %d\tk: %d)" % (i, k))
# print()
# #위에꺼 while문으로 바꾸기
# i = 0
# while i < 3:
#     k = 0
#     while k < 5:
#         if k == 3:
#             break
#         print("(i: %d\tk: %d)" % (i, k))
#         k += 1
#     i+=1


# 쌀 100통이 저장되어 있는 창고에 암수 1쌍의 쥐가 있다. 쥐 한마리가 하루에
# 20g씩의 쌀을 먹고, 10일(10,20,30)마다 쥐의 수가 2배씩 증가한다. 며칠만에
# 창고의 쌀이 모두 쥐의 먹이가 될까. 그리고 쥐는 총 몇마리 인가?
# (쌀 한통 = 1kg, 쌀을 먹은 후 2배 증가하는 조건)
# 총 10만그람 쌀

rice = 100000
eat_oneday = 20
mouse = 2
day = 1

print("1번째", rice - (2 * eat_oneday) * 1)
print("10번째", rice - (4 * eat_oneday) * 10)
print("20번째", rice - (8 * eat_oneday) * 20)
print("30번째", rice - (16 * eat_oneday) * 30)
print("40번째", rice - (32 * eat_oneday) * 40)
print("50번째", rice - (64 * eat_oneday) * 50)
print("59번째", rice - (64 * eat_oneday) * 59)
print("60번째", rice - (128 * eat_oneday) * 60)
print()

eat_sum = rice - (mouse * eat_oneday) * day
while eat_sum >= 0:
    if day % 10 == 0:
        mouse = mouse * 2
    eat_sum = rice - (mouse * eat_oneday) * day
    day += 1
print("{}번째날 남은 쌀: {:,}".format(day-1, eat_sum))
print("%d번째 모두 쥐의 먹이가 됨" % (day-1))
print("총 쥐 마리: %d" % mouse)


# eat_sum = rice - (mouse * eat_oneday) * day
# print("총 쌀: {:,}".format(eat_sum))
# # print("남은 쌀: {:,}".format(eat_sum))
# while eat_sum >= 0:
#     if day % 10 == 0:
#         mouse = mouse * 2
#     eat_sum = rice - (mouse * eat_oneday) * day
#     day += 1
# print("{}번째날 남은 쌀: {:,}".format(day, eat_sum))
# print("%d번째 모두 쥐의 먹이가 됨" % day)
# print("총 쥐 마리: %d" % mouse)
