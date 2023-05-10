import csv
from task import Task, PERIODIC
from task_set import TaskSet
from RTOS import RTOS
from schedular import RM_MODE, DM_MODE, EDF_MODE



class Main:
    """Main class of the OS."""
    def __init__(self, duration=100):
        self.task_set = TaskSet()
        self.duration = duration

    def run(self, file, mode=RM_MODE, preemptive=False):
        # create tasks and add them to task set
        self.read_tasks_from_csv(filename=file)
        
        # creating our rtos
        rtos = RTOS(self.task_set, mode=mode, preemptive=preemptive)

        # schedule tasks using selected algorithm
        rtos.run(self.duration)

    def read_tasks_from_csv(self, filename):
        """Read tasks from CSV

        Args:
            filename (string): task set file
        """
        with open(filename, 'r') as csvfile:
            taskreader = csv.reader(csvfile)
            header = True
            
            for row in taskreader:
                priority, name, state, type, act_time, period, wcet, deadline = row
                
                # don't read headers
                if header:
                    header = False
                    continue
                
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
                
                self.task_set.add_task(task)
                
                if task.type == PERIODIC:
                    i = task.act_time + task.period
                    while i < self.duration:
                        tmp = Task(
                            priority=int(priority),
                            name=name,
                            state=int(state),
                            type=int(type),
                            act_time=i,
                            period=int(period),
                            wcet=int(wcet),
                            deadline=task.deadline
                        )
                        
                        self.task_set.add_task(tmp)
                        i = tmp.act_time + tmp.period



if __name__ == '__main__':
    main = Main()
    main.run('tasks1.csv', mode=RM_MODE, preemptive=False)
