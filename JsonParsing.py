import json
json_text1 ='{"first message": {"message": "This is the first message", "timestamp":"2021-06-04 16:40:53"}}'
json_text2 = '{"second message": {"message": "And this is a second message", "timestamp":"2021-06-04 16:41:01"}}'
obj1 = json.loads(json_text1)
obj2 = json.loads(json_text2)
key ="second message"
if key in obj1:
    print(obj1[key])
elif key in obj2:
    print(obj2[key])
else:
    print(f"Ключа {key} в JSON нет")