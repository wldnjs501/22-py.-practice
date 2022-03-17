#%% dict test 학생관리
# 학생 이름과 학생 점수를 입력받고
# 추가, 수정, 삭제, 목록 print("[" + i + "]")

title = "학생 성적 관리 프로그램\n"
msg = "1.추가\n2.수정\n3.삭제\n4.목록\n5.나가기\n"
errMsg = "다시 시도해주세요"

studentDict = {}
subjectList = ["국어","영어","수학"]

while True:
    choice = int(input(title + msg))
    #추가
    if choice == 1:
        name = input("학생 이름:")
        if name not in studentDict:
            studentDict[name] = input("해당학생 점수를 입력해주세요. 예)국어,영어,수학").split(",")
        else:
            print("이미 등록된 학생입니다.")
    #수정
    elif choice == 2:
        cho = int(input("1.학생명\n2.점수\n"))
        name = input("학생이름:")
        if cho == 1:
            if name in studentDict:
                new = input("새로운 학생명:")
                scoreList = studentDict[name]
                del studentDict[name]
                studentDict[new] = scoreList
            else:
                print("존재하지 않는 학생입니다.")
                
        if cho == 2:
            if name in studentDict:
                studentDict[name] = input("해당학생 점수를 입력해주세요. 예)국어,영어,수학").split(",")
            else:
                print("존재하지 않는 학생입니다.")
                
    #삭제
    elif choice == 3:
        name = input("삭제할 학생명:")
        if name in studentDict:
            del studentDict[name]
        else:
            print("존재하지 않는 학생입니다.")
    #목록
    elif choice == 4:
        for i in studentDict.keys():
            print(i)
            cnt = 0
           
                
            for j in studentDict[i]:
                print(subjectList[cnt] + ":" + str(j) + "점" )
                cnt += 1
                
        
       
    #나가기
    elif choice == 5:
        break
    #오류
    else:
        print(errMsg)
        