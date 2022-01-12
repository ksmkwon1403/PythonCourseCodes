import requests

indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&l&vjk=112db0c64f7899b8")

print(indeed_result.text)

#test
#test2