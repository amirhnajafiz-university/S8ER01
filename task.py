RUNNING   = 0   # Currently executing on the processor
READY     = 1   # Ready to run but task of higher or equal priority is currently running
BLOCKED   = 2   # Task is waiting for some condition to be met to move to READY state
SUSPENDED = 3   # Task is waiting for some other task to unsuspend

INTERRUPT = 0  # Task type is interrupt
PERIODIC  = 1  # Task type is periodic
APERIODIC = 2  # Task type is aperiodic
SPORADIC  = 3  # Task type is sporadic



class Task (object):
    """Task Object Class

    Attributes:
        priority (int): Priority of the task
        name (str): Name of the task
        state (int): State of the task
        type (int): Type of the task
        act_time (int): Activation time of the task
        period (int): Period of the task
        wcet (int): Worst case execution time of the task
        deadline (int): Deadline of the task
    """
    def __init__(self,priority=255,name=None,state=SUSPENDED,type=None,act_time=0,period=0,wcet=0,deadline=1000):
        self.priority = priority
        self.name = name
        self.state = state
        self.type = type
        self.act_time = act_time
        self.period = period
        self.wcet = wcet
        self.deadline = deadline
        self.work = 0
        
    
    def do(self, time):
        """Make the task work 1 period.
        
        Returns:
            bool: true if everything is set, false if something goes wrong
        """
        if not self.is_ready(time):
            return False
        
        self.work = self.work + 1    
        
        return True
        

    def done(self):
        """Check if the task is done or not.

        Returns:
            bool: done or not
        """
        return self.work == self.wcet

        
    def is_ready(self, time) -> None:
        """Check if the task is ready or not.

        Args:
            time (int): Current time.

        Returns:
            true or false.
        """
        return self.act_time <= time and self.act_time + self.deadline > time and not self.done()
       
 
    def is_interrupt(self):
        """Check the interrupt type.

        Returns:
            bool: interrupt or not
        """
        return self.type == INTERRUPT


    def is_missed(self):
        """Check if the task is missed or not.

        Returns:
            bool: Missed task.
        """
        return self.wcet != self.work
