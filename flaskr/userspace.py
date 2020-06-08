from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('userspace', __name__)

@bp.route('/profile')
def profile():
    return render_template('userspace/profile.html')

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

@bp.route('/schedule')
@login_required
def schedule():
    db = get_db()
    subjects = db.execute(
        'SELECT id, name_s, professor_id FROM subject_'
    ).fetchall()
    mySchedule = Schedule()
    
    db.commit()
    return render_template('userspace/schedule.html', subjects=subjects, schedule=mySchedule)