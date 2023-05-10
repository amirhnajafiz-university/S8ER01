from task import * 



RM_MODE = 1
DM_MODE = 2
EDF_MODE = 3



class Scheduler:
    """Scheduler Class
    
    Attributes:
        task_set (TaskSet): Task set to be scheduled
        mode (int): Mode will choose the algorithm
        preemptive (bool): Algorithm is preemptive or not
    """
    def __init__(self, task_set, mode=RM_MODE):
        self.task_set = task_set
        
        # arrange tasks based on mode
        if mode == RM_MODE:
            self.rm()
        elif mode == DM_MODE:
            self.dm()
        elif mode == EDF_MODE:
            self.edf()


    def schedule(self, time):
        """Schedule the next task to run
        
        Args:
            time (int): Current time.
        
        Returns:
            Task: The next task to run, or None if no tasks are ready
        """

        ready_tasks = self.task_set.get_ready_tasks(time)
        
        # first check if any task is ready or not
        if len(ready_tasks) == 0:
            return None
        
        # return the top
        return ready_tasks[0]


    def edf(self):
        """EDF
        
        Sort tasks based on the nearest deadline.
        """
        # get interrupts first
        interrupts = [task for task in self.task_set.get_all() if task.is_interrupt()].sort(key=lambda x: x.deadline)
        # get other tasks
        others = [task for task in self.task_set.get_all() if not task.is_interrupt()].sort(key=lambda x: x.deadline)
        # set new tasks
        self.task_set.set_tasks(interrupts+others)
    

    def dm(self):
        """DM
        
        Sort tasks based on the deadline monotonic.
        """
        # get interrupts first
        interrupts = [task for task in self.task_set.get_all() if task.is_interrupt()].sort(key=lambda x: x.deadline)
        # get other tasks by deadline monotonic
        others = [task for task in self.task_set.get_all() if not task.is_interrupt()].sort(key=lambda x: 1/x.deadline, reverse=True)
        # set new tasks
        self.task_set.set_tasks(interrupts+others)


    def rm(self):
        """RM
        
        Sort tasks based on the rate monotonic.
        """
        # get interrupts first
        interrupts = [task for task in self.task_set.get_all() if task.is_interrupt()].sort(key=lambda x: x.deadline)
        # get periodic tasks by rate monotonic
        periodic = [task for task in self.task_set.get_all() if not task.is_interrupt() and task.period != 0].sort(key=lambda x: 1/x.period, reverse=True)
        # get other tasks
        others = [task for task in self.task_set.get_all() if not task.is_interrupt() and task.period == 0].sort(key=lambda x: x.deadline)
        # set new tasks
        self.task_set.set_tasks(interrupts+periodic+others)
