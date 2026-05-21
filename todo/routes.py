from flask import Blueprint, render_template


task_bp = Blueprint('tasks', __name__, template_folder='templates')

tasks_db = [
    {'id': 1, 'title': 'Buy a bread', 'description': 'before shop closed'},
    {'id': 1, 'title': 'do flip', 'description': 'just do it'},
    {'id': 1, 'title': 'training', 'description': 'HELL YEAH'}
]

@task_bp.route('/tasks')
def get_all_task():
    return render_template('tasks.html', tasks_db=tasks_db)



@task_bp.route('/task/<int: id>')
def get_all_tasks(id):
    task_two = []
    for task in tasks_db:
        if task.get('id') == id:
            task_two.append(task)
    return render_template('task.html', tasks_two=task_two)


