#DemoDict.py
device ={"아이폰":5, "아이패드":10, "윈도우타블렛":20}

print(len(device))
print(device)

#검색
print(device["아이폰"])
#입력
device["맥북"] = 15
#삭제
del device["아이패드"]
#수정
device["아이폰"] = 6

for item in device.items():
    print(item)


for k,v in device.items():
    print(k,v)

#전화번호
phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print("kim" in phone)
print("kang" not in phone)
#참조를 전달
p = phone
p["kang"] = "1234"
print(phone)
print(p)
print(id(phone))
print(id(p))
