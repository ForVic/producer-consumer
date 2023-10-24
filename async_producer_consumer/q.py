class Queue:
    def __init__(self):
        self.tasks = []
    
    def push(self, task):
        self.tasks.append(task)

    def pop(self):
        if self.tasks:
            return self.tasks.pop()

class Processable:
    def __init__(self):
        pass
    def process(self):
        pass


class QueueTask:
    def __init__(self, func: Processable):
        self.processor = func
    
    def process(self):
        self.processor.process()
        print("Processing succeeded")
        

