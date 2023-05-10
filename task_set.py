from task import Task



class TaskSet:
    """Task Set Class
    
    Attributes:
        tasks (list): List of Task objects
        utility (float): Utility of the task set
        self.feasible (bool): Whether the task set is feasible
    """
    def __init__(self, tasks=[]):
        self.tasks = tasks
        self.utility = 0
        self.feasible = False
    
    
    def get_ready_tasks(self, time):
        """Get ready tasks of task set.
        
        Returns:
            a list of ready tasks.
        """
        array = []
        
        for task in self.tasks:
            if task.is_ready(time):
                array.append(task)
        
        return array
                
        
    def add_task(self, task):
        """Add a task to the task set
        
        Args:
            task (Task): Task object to add
        """
        self.tasks.append(task)
    
    
    def status(self):
        """Return an status of task set.

        Returns:
            int: Number of tasks
        """
        return len(self.tasks)    
