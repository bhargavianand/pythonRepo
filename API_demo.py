import json
import requests as reqs

api = "https://reqres.in/api/users/"

print("============GET request===============")
queryparam = {"id":"4"}
response = reqs.request("GET", api, params=queryparam)
print(response.text)

print("--------------------------------content printing -= bytes instance --------------------------")
print(response.content)

response_dict = json.loads(response.text)
for i in response_dict:
     print( "Key: ", i , " : value: " , response_dict[i])
     print("\n")


print("###################read any particular entity of json response ########################")

print("*******************printing a particular entity***************************")
support = response_dict.get('support')
print(type(support))
print("************************retrieving inner values from inner dict*************")
for i in support:
    print("key:" , i , " :value : " , support[i])

##or just print one value
print(support.get('url'))

##same way as above print values of data object

data = response_dict.get('data')
print("Value of id retreived is " , data.get('id'))
print("Value of email retreived is " , data.get('email'))
print("Value of first_name retreived is " , data.get('first_name'))
print("Value of last_name retreived is " , data.get('last_name'))
print("Value of avatar retreived is " , data.get('avatar'))

print(response.status_code)
print(response.url)

#prints response the headers details,cookies, encoding etc details
print(response.__dict__)

print("============POST request===============")
queryparam_post = {"name":"Bhargavi","job":"Leader"}

response_post = reqs.request("POST", api, params=queryparam_post)
print(response_post.text)
print(response_post.status_code)
print(response_post.url)
print("content of response is ###################")
print(response_post.content)

#as response.content is a bytes instance we cant compare below
#print(str(response_post.content) == response_post.text)



print("################JSON response values retrieval ########################################")

response_get = reqs.get(api)
#If the response is in json you could do something like (python3):

response_dict = json.loads(response_get.text)

# print("###################response_dict##################")
# print(response_dict)
# print("###################response_dict##################")

print(type(response_dict))

#print the key- value pairs of json response
for i in response_dict:
    print( "Key: ", i , " : value: " , response_dict[i])



print("#############using response.__dict__######################")

print(response.__dict__)


print("++++++++++++++++without loads() directly calling json() on response ++++++++++++++++")
response_json = response.json()
for i in response_json:
    print("key: ", i, "val: ", response_json[i])

print("+++++++++++++++++++++++++++++++++with json loads()+++++++++++++++++++++++++++++++++++++")
response_json1 = json.loads(response.text)
for i in response_json1:
    print("key: ", i, "val: ", response_json1[i])
