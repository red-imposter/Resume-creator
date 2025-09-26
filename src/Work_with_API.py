import requests


with open("Data.txt","r",encoding="utf-8") as file:
    for line in file:
        token = line

git_url = 'https://git.miem.hse.ru/api/v4'

def get_main_info():
    url = f"{git_url}/user"
    response = requests.get(url, headers={"PRIVATE-TOKEN": token})
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Ошибка {response.status_code}(при получении основной информации): {response.text}')
        quit()

def get_achievements(id):
    url = f'{git_url}/users/{id}/events'
    response = requests.get(url,headers={'Private-Token': token})
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Ошибка {response.status_code}(при получении достижений): {response.text}')
        quit()

