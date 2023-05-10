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
        
        if mode == RM_MODE:
            self.mode = "RM"
        elif mode == DM_MODE:
            self.mode = "DM"
        elif mode == EDF_MODE:
            self.mode = "EDF"
        
    
    def compute_missed_tasks(self):
        """Count the number of missed tasks.

        Returns:
            int: number of missed tasks.
        """
        count = 0;
        
        for task in self.task_set.get_all():
            if task.is_missed():
                count = count + 1
        
        return count


    def run(self, duration):
        """Run the task set on the operating system for a specified duration
        
        Args:
            duration (int): The duration to run the task set for
        
        Returns:
            float: Utility of CPU
        """
        completed_tasks = []
        
        task = None
        cpu_busy_time = 0
        
        for i in range(duration):
            if not self.preemptive: # if we are not preemptive
                if not self.busy:
                    # get a task to start
                    task = self.scheduler.schedule(i)
                    if task != None:
                        self.busy = True
                elif task.done():
                    task = None
                    self.busy = False
                if task != None: # update task downtime
                    if not task.do(i):
                        self.busy = False
                        task = None
            else: # if we are preemptive
                # take a task and do it
                task = self.scheduler.schedule(i)
                if task != None:
                    task.do(i)
            
            # update cpu busy time
            if task != None:
                cpu_busy_time = cpu_busy_time+1
            
            completed_tasks.append(task)
            
        # print tasks
        self.printer.print_schedule(completed_tasks)
        
        # compute missed tasks
        missed = self.compute_missed_tasks()
        
        # print extra information
        print()
        print("\n==========================================\n")
        print(f'Total time: {duration}s')
        print(f'CPU Utilization: {100 * cpu_busy_time/duration}')
        print(f'Total tasks: {self.task_set.status()}')
        print(f'Missed tasks: {missed}')
        print('Scheduling Algorithm:')
        print(f'\tFeasible: {missed == 0}')
        print(f'\tPreemptive: {self.preemptive}')
        print(f'\tMode: {self.mode}')
        print("\n==========================================\n")
        print()
