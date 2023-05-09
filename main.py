import csv
from task import Task
from task_set import TaskSet
from RTOS import RTOS



class Main:
    def __init__(self):
        self.task_set = TaskSet()

    def run(self):
        # create tasks and add them to task set
        self.read_tasks_from_csv('task1.csv')
        
        # creating our rtos
        self.rtos = RTOS(self.task_set)

        # schedule tasks using selected algorithm
        self.rtos.run(100)

    def read_tasks_from_csv(self, filename):
        with open(filename, 'r') as csvfile:
            taskreader = csv.reader(csvfile)
            for row in taskreader:
                name, priority, state, type, act_time, period, wcet, deadline = row
                task = Task(
                    priority=int(priority),
                    name=name,
                    state=int(state),
                    type=int(type),
                    act_time=int(act_time),
                    period=int(period),
                    wcet=int(wcet),
                    deadline=int(deadline)
                )
                self.taskset.add_task(task)



if __name__ == '__main__':
    main = Main()
    main.run()
