import requests
import json
import time

class LexxPlussRobot:
    def __init__(self):
        self.API_URL= 'http://192.168.20.55/v1/'
        self.headerDict = {'X-API-Key': 'lexxpluss'}

    def get_RobotInfo(self,api):
        try:
            result = None
            result = self.GET(api)
            if not result is None:
                return print(result)
            else:
                return None
        except:
            return False


    def get_RobotMaps(self, map_api):
        try:
            map_result = None
            map_result = self.GET(map_api)
            if not map_result is None:
                return print(map_result)
            else:
                return None
        except:
            return False


    def get_RobotTasks(self, task_api):
        try:
            task_result = None
            task_result = self.GET(task_api)
            if not task_result is None:
                return print(task_result)
            else:
                return None
        except:
            return False
    def GET(self,api):

        url = f'{self.API_URL}{api}'

        try:
            response = requests.get(url, headers=self.headerDict, timeout=2)

            #response = requests.get(url, headers=self.headerDict, timeout=2)

            if response.status_code == 200:
                data = response.json()
                #print(data)
                return data
            else:
                return None
        except requests.exceptions.RequestException as e:

            return None

    def POST(self,api,data):
        try:
            url = f'{self.API_URL}{api}'
            response = requests.post(url,headers=self.headerDict, json=data, timeout=2)
            # response = requests.post(api_url, json=data)
            # return True
            # Check the response status code
            if response.status_code == 200 or response.status_code == 201 :
                # Request was successful
                # result = response.json()  # Parse JSON response
                # print(f"Response data: {result}")
                print(f"Response data: {response.status_code}")
                return True
            else:
                # Handle errors here
                print(f"Request failed with status code: {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            # Handle request exceptions (e.g., network issues)
            print(f"Request error: {e}")
            return False



if __name__ == '__main__':
   lp = LexxPlussRobot()
   #lp.GET(api='robots/params')
   #lp.get_RobotInfo(api='robots/params')
   #lp.get_RobotMaps(map_api='maps')
   #lp.get_RobotTasks(task_api='tasks')

   data_stop={"enable": False}
   lp.POST(api='robots/1/emergency-stop',data=data_stop)



