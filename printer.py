class Printer:
    """Printer Class"""
    def print_task(self, task):
        """Print the details of a scheduled task
        
        Args:
            task (Task): The scheduled task to print
        """
        if task is None:
            print("No task scheduled")
            return
        
        print(f"Scheduled Task: {task.name}")
        print(f"  Priority: {task.priority}")
        print(f"  State: {task.state}")
        print(f"  Type: {task.type}")
        print(f"  Activation Time: {task.act_time}")
        print(f"  Period: {task.period}")
        print(f"  WCET: {task.wcet}")
        print(f"  Deadline: {task.deadline}")

class TaskSetPrinter:
    """TaskSetPrinter Class"""
    def __init__(self):
        """Initialize the TaskSetPrinter instance."""
        self.printer = Printer()
        
    def print_schedule(self, schedule):
        """Print the scheduled tasks
        
        Args:
            schedule (List[Task]): A list of scheduled tasks
        """
        for i, task in enumerate(schedule):
            print(f'Time: {i}')
            self.printer.print_task(task)
