from printer import TaskSetPrinter as Printer
from schedular import *



class RTOS:
    """Real-Time Operating System Class"""
    def __init__(self, task_set, mode=RM_MODE, preemptive=False):
        """Initialize the RTOs instance
        
        Args:
            task_set (TaskSet): The task set to run on the operating system
            mode (int): Mode will choose the algorithm
            preemptive (bool): Algorithm is preemptive or not
        """
        self.task_set = task_set
        self.scheduler = Scheduler(task_set, mode=mode)
        self.printer = Printer()
        self.preemptive = preemptive
        self.busy = False


    def run(self, duration):
        """Run the task set on the operating system for a specified duration
        
        Args:
            duration (int): The duration to run the task set for
        
        Returns:
            List of Task: The completed task set after running on the operating system for the specified duration
        """
        completed_tasks = []
        task = None
        
        for i in range(duration):
            if not self.preemptive: # if we are not preemptive
                if not self.busy:
                    # get a task to start
                    task = self.scheduler.schedule(i)
                    self.busy = True
                elif task.done():
                    # move to done tasks
                    completed_tasks.append(task)
                    task = None
                    self.busy = False
                if task != None: # update task downtime
                    task.do()
            else:
                pass
            
        self.printer.print_schedule(completed_tasks)
        
        return completed_tasks
