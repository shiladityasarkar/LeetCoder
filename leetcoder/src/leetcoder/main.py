from leetcoder.crew import LeetcoderCrew
from leetcoder.retrieve import Retrieve

leet = LeetcoderCrew().crew()
retr = Retrieve()
inp = None
llm_result = None

class Run:
    prm = 0
    def run(self, q: int):
        problem = retr.get_problem(q)
        if not retr.flag:
            self.prm = 1
            return "print('Nothing to show hehe')", problem
        leet.kickoff(inputs = {'problem_statement':problem})
        ans = []
        for _ in range(len(leet.agents)):
            ans.append(leet.logs[_][0])
        self.prm = 0
        return ans


testing = False

if testing:
    try:
        inp = int(input('Enter the problem number: '))
    except ValueError:
        print('Enter an integer!')

    if inp:
        llm_result = Run.run(inp)

    for i in llm_result:
        print(i)


