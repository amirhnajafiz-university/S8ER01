from task import * 



class Scheduler:
    """Scheduler Class
    
    Attributes:
        task_set (TaskSet): Task set to be scheduled
    """
    def __init__(self, task_set):
        self.task_set = task_set
        
    def get_ready_tasks(self):
        """Get a list of all ready tasks in the task set
        
        Returns:
            list: List of all Task objects in the task set that are in the READY state
        """
        ready_tasks = []
        for task in self.task_set.get_all_tasks():
            if task.state == READY:
                ready_tasks.append(task)
        return ready_tasks
    
    def schedule(self):
        """Schedule the next task to run
        
        Returns:
            Task: The next task to run, or None if no tasks are ready
        """
        # complete here 

        # first check if any task is ready or not
        ready_tasks = self.get_ready_tasks()
        if not ready_tasks:
            return None
