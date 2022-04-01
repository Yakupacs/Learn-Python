import requests

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = 
    def getUser(self, username):
        response = requests.get(self.api_url + '/users/' + username)
        return response.json()

    def getRepositories(self, username):
        response = requests.get(self.api_url + '/users/' + username + '/repos')
        return response.json()

    def createRepository(self, name):
        response = requests.post(self.api_url + '/user/repos?acces_token='+ self.token, json = {
        "name": name,
        "description": "This is your first repository",
        "homepage": "https://github.com",
        "private": False,
        "has_issues": True,
        "has_project": True,
        "has_wiki": True 
        })
        return response.json()
        


github = Github()

while True:
    secim = input('1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçim: ')

    if secim == '4':
        break
    else:
        if secim == '1':
            try:
                username = input('Username: ')
                result = github.getUser(username)
                print(f"Name: {result['name']}\nPublic Repos: {result['public_repos']}\nFollowers: {result['followers']}")
            except:
                print("Böyle Bir Kullanıcı Bulunamadı!")
        elif secim == '2':
            try:
                username = input('Username: ')
                result = github.getRepositories(username)
                for repo in result:
                    print(repo['name'])
            except:
                print("Böyle Bir Kullanıcı Bulunamadı!")
        elif secim == '3':
            name = input('Resository Name: ')
            result = github.createRepository(name)
            print(result)
        else:
            print("Geçersiz Argüman Girildi!")