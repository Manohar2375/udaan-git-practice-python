import requests as rs

# url = "http://127.0.0.1:8000/getall"
# response = rs.get(url)
# students = response.json()
# # for stu in students:
# #     print(stu)
# print(students)

baseurl = "http://127.0.0.1:8000"
stuID = "002" 
url = f"{baseurl}/search/{stuID}"
# "http://127.0.0.1:8000/search/002"
response = rs.get(url)
print(response.status_code)
try:
    if response.status_code == 200 :
        students = response.json()
        print(students)
    elif response.status_code == 404:
        print("")
except:
    print("")