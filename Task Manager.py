def welcome():
    print('Welcome to Task Manager! 🗓️')

def main_menu():
    print('1. View Tasks')
    print('2. Add Task')
    print('3. Remove Completed Task')
    print('4. Quit')

    print('')

def view_tasks():
    if not tasks:
        print('No Tasks Available')
    else:
        for i, task in enumerate(tasks, start=1):
            print(f'{i}. {task}')

    print('')

def add_task():
    task = input('Add Task: ')
    tasks.append(task)
    print('')
    print(f'"{task}" Was added to your tasks')
    print('')

def remove_task(tasks):
    if not tasks:
        print('No Tasks Available')
        print('')
        return

    view_tasks()

    task_number = int(input('Enter Task Number: '))
    print('')
    try:
        if task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f'Removed Task: {removed}')

    except ValueError:
        print('Invalid Task Number')

    print('')

tasks = []

welcome()

print('')

while True:
    main_menu()
    choice = input('Enter Choice: ')

    print('')

    if choice == '1':
        view_tasks()
        continue
    elif choice == '2':
        add_task()
        continue
    elif choice == '3':
        remove_task(tasks)
    elif choice == '4':
        print('Thank you for using Task Manager!')
        break
    else:
        print('Invalid Choice')
        print('')
