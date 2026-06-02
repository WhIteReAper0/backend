from flask import Blueprint, render_template, request, redirect, url_for

from database.engine import db 
from database.models.todo import Task
from database.models.auth import User 

task_bp = Blueprint('tasks', __name__, template_folder='templates')


@task_bp.route('/')
def get_all_task():
    return render_template('tasks.html')


@tasks_bp.route('/task/<int:id>')
def detail_task(id):
    task = Task.query.filter_by(id=id).first()
    return render_template('detail.html', task_two=task)

@task_bp.route('/task/<int:id>')
def get_all_tasks(id):
    tasks = Task.query.all()
    print(tasks) 
    for task in tasks_db:
        if task.get('id') == id:
            task_two.append(task)
    return render_template('task.html', task_two=task_two)



@task_bp.route('/add', methods=['GET', 'post'])
def  add_task():
    if request.method == 'post':
        title = request.form.get('title')
        description = request.form.get('description')
        task = Task(title=title, description=description)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('tasks.get_all_tasks'))
    return render_template('add_task.html')


@task_bp.route('/update/<int:id>', methods=['GET', 'post'])
def update_task(id):
    task = Task.query.filter_by(id=id).first()
    if request.method == 'post':
        title = request.form.get('title')
        description = request.form.get('description')
        if title:
            task.title = title 
        if description: 
            task.description = description
        db.session.commit()

     
            if task == id:
                task.update({'title': title}) 
                task.update({'description': description})

            return redirect(url_for('tasks.get_all_tasks'))
        
    task_two = []
        if task.get('id') == id:
            task_two.append(task)
    return render_template('update.html', task_two=task_two)


@task_bp.route('/delete/<int:id>', methods=['post'])
def delete_task(id):
    task = Task.query.filter_by(id=id).first()
    db.session.commit()
    return redirect(url_for('tasks.get_all_tasks'))