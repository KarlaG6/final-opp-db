from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('userspace', __name__)

@bp.route('/profile')
def profile():
    rolid = g.user['rol_id']
    rol = get_db().execute(
        'SELECT name_rl FROM rol WHERE id = ?',(rolid,)
    ).fetchone()
    return render_template('userspace/profile.html', rol=rol)

class Subject:
    def __init__(self, id, nameS, type):
        self.id = id
        self.nameS = nameS
        self.professor = {}
        self.roomType = ''
        self.rooms = []
        self.date = date
        self.time = time

    def addRoom(room):
        self.rooms.append(room)

    def setProfe(id, name):
        self.professor.nameP = name
        self.professor.idP = id

    def setTime(hora):
        self.time = hora

    def setDate(dia):
        self.date = dia

    

class Schedule(Subject):
    def __init__(self):
        self.subjects = []
    
    def addSubject(self, subject):
        for subj in self.subjects:
            self.subjects.append(subject)

    def rmSubject(self, subject):
        self.subjects.remove(subject.nameS)

    def schedEmpty():
         False if len(self.subjects) == 0 else True


@bp.route('/schedule', methods=('GET', 'POST'))
@login_required
def schedule():
    db = get_db()
    subjects = db.execute(
        'SELECT id, name_s, professor_id FROM subject_'
    ).fetchall()
    user = g.user['id']
    
    print( user)
    if request.method == 'POST':
        subj = request.form['subject']
        error = None
        
        if not subj:
            error = 'Seleccione una asignatura.'
        elif db.execute(
            'SELECT id_subj FROM schedule WHERE id_subj = ? AND id_user = ?', 
            (subj, user)
        ).fetchone() is not None:
            subject = db.execute(
                'SELECT name_s FROM subject_ s WHERE id = ?', 
                (subj,)
            ).fetchone()
            error = 'La asignatura {} ya esta registrada.'.format(subject[0])
            # print(schedules)
            # mySchedule = Schedule()
            # for sch in schedules:
            #     mySchedule.addSubject(sch)
        if error is None:
            db.execute(
                'INSERT INTO schedule (id_subj, id_user) VALUES(?, ?)',
                (subj, user)
            )
            db.commit()
        else:
            flash(error)
    schedules = db.execute(
        'SELECT s.name_s FROM subject_ s, schedule sch WHERE s.id = sch.id_subj AND sch.id_user = ?', 
        (user,)
    ).fetchall()
        
    return render_template('userspace/schedule.html', subjects=subjects, schedules=schedules)