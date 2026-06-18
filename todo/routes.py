from flask import Blueprint, render_template, request, redirect, url_for

from flask_login import login_required, current_user

from database.engine import db 
from database.models.todo import Task
from database.models.auth import User 

task_bp = Blueprint('task_bp', __name__, template_folder='templates')


@task_bp.route('/')
def get_all_task():
    return render_template('tasks.html')


@task_bp.route('/task/<int:id>')
@login_required
def detail_task(id):
    task = Task.query.filter_by(id=id).first()
    return render_template('detail.html', task_two=task)


@task_bp.route('/')
@login_required
def get_all_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', tasks_db=tasks)



@task_bp.route('/add', methods=['GET', 'post'])
@login_required
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