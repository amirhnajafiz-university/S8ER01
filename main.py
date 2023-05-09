import csv
from task import Task
from task_set import TaskSet
from RTOS import RTOS
from schedular import Scheduler
from printer import TaskSetPrinter as Printer

class Main:
    def __init__(self):
        self.rtos = RTOS()
        self.task_set = TaskSet()
        self.scheduler = Scheduler()
        self.printer = Printer()

    def run(self):
        # create tasks and add them to task set
        self.read_tasks_from_csv('task1.csv')

        # schedule tasks using EDF algorithm
        self.scheduler.edf(self.task_set)

        # print scheduled task set
        self.printer.print_schedule(self.task_set)
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
