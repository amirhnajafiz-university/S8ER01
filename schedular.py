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
    def __init__(self, task_set, mode=RM_MODE, preemptive=False):
        self.task_set = task_set
        self.mode = mode
        self.preemptive = preemptive


    def run(self):
        """Schedule the next task to run
        
        Returns:
            Task: The next task to run, or None if no tasks are ready
        """
        # complete here 

        # first check if any task is ready or not
        ready_tasks = self.get_ready_tasks()
        if not ready_tasks:
            return None
        
        # call a method based of the algorithm
