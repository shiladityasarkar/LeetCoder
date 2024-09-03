# created by Shiladitya©
import http.client
import json
import os
from dotenv import load_dotenv
load_dotenv()

class Retrieve:
    conn = [http.client.HTTPSConnection("google.serper.dev"),
            http.client.HTTPSConnection("scrape.serper.dev")]
    flag = 1
    def get_problem(self, num: int):
        self.flag = 1
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'Content-Type': 'application/json'
        }
        payload = json.dumps({
            "q": f"leetcode problem {num}"
        })
        self.conn[0].request("POST", "/search", payload, headers)
        res = self.conn[0].getresponse()
        data = res.read()
        link = json.loads(data.decode("utf-8"))['organic'][0]['link'] + 'description'
        payload = json.dumps({
            "url": link
        })
        self.conn[1].request("POST", "/", payload, headers)
        res = self.conn[1].getresponse()
        data = res.read()
        problem = json.loads(data.decode("utf-8"))['text']
        if 'Subscribe to unlock' in problem:
            self.flag = 0
            return 'This is a premium problem. Subscribe to unlock 🙃'
        return problem
