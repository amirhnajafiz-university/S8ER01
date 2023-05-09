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
        self.scheduler = Scheduler(task_set, mode=mode, preemptive=preemptive)
        self.printer = Printer()
        self.busy = False
        self.time = 0


    def run(self, duration):
        """Run the task set on the operating system for a specified duration
        
        Args:
            duration (int): The duration to run the task set for
        
        Returns:
            List of Task: The completed task set after running on the operating system for the specified duration
        """
        completed_tasks = []
        
        for i in range(duration):
            self.scheduler.run()
            completed_tasks += self.scheduler.completed_tasks
            
        self.printer.print_schedule(completed_tasks)
        
        return completed_tasks
