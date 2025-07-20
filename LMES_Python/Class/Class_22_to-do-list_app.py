# to-do List application:

class Task:
    def __init__(self,description,priority):
        self.description = description
        self.priority = priority
        self.completed = False

    def __str__(self):
        return f"Description: {self.description} \n Priority: {self.priority} \n Completed: {'Yes' if self.completed else 'No'}"

class To_Do_List:
    def __init__(self):
        self.tasks = []

    def add_tasks(self,task):
        self.tasks.append(task)

    def display_task(self):
        if self.tasks:
            print('Tasks are available in the To_do_list: ')
            for index,task in enumerate(self.tasks, start = 1):
                print(f"{index}. {task}")
        else:
            print('no tasks in the To_do_list')

    def mark_task_completed(self,index):
        if index>=1 and index<=len(self.tasks):
            task = self.tasks[index-1]
            task.completed = True
            print(f"Task {task.description} has been completed")
        else:
            print('Invalid index value')

to_do_list =To_Do_List()
task1 = Task('Learning','High')
task2 = Task('Implementing in Project','Medium')
task3 = Task('Job selection','Low')
to_do_list.add_tasks(task1)
to_do_list.add_tasks(task2)
to_do_list.add_tasks(task3)

to_do_list.display_task()
to_do_list.mark_task_completed(1)
to_do_list.display_task()


