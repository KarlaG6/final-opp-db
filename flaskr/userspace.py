from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
import abc

bp = Blueprint('userspace', __name__)

@bp.route('/profile')
def profile():
    rolid = g.user['rol_id']
    rol = get_db().execute(
        'SELECT name_rl FROM rol WHERE id = ?',(rolid,)
    ).fetchone()
    return render_template('userspace/profile.html', rol=rol)

class Subject:
    # falta el , id, nameS, type en init
    def __init__(self):
        self.id = None
        self.nameS = ''
        self.professor = {}
        self.roomType = ''
        self.rooms = []
        self.date = None
        self.time = None

    def setNameS(name):
        self.nameS = name

    def setId(i):
        self.id = i

    def addRoom(self, room):
        self.rooms.append(room)

    def setProfe(self, id):
        self.professor.idP = id

    def setTime(self, hora):
        self.time = hora

    def setDate(self, dia):
        self.date = dia
        setNameS(name) 
            

    def delSubject(self):
        pass



class Schedule(Subject):
    def __init__(self):
        self.subjects = []
        self.schedules = []
        self.owner = None

    def getSbjcts(self):
        return self.subjects

    def getSchdls(self):
        return self.schedules
    
    def addSbjct(self):
        db = get_db()
        self.subjects = db.execute(
            'SELECT id, name_s FROM subject_'
        ).fetchall()
        self.owner = g.user['id']
        owner = self.owner
        if request.method == 'POST':
            subj = request.form['subject']
            error = None
            
            if not subj:
                error = 'Seleccione una asignatura.'
            elif db.execute(
                'SELECT id_subj FROM schedule WHERE id_subj = ? AND id_user = ?', 
                (subj, owner)
            ).fetchone() is not None:
                subject = get_subject(subj)
                error = 'La asignatura {} ya esta registrada.'.format(subject[0])
                # print(schedules)
                # mySchedule = Schedule()
                # for sch in schedules:
                #     mySchedule.addSubject(sch)
            if error is None:
                db.execute(
                    'INSERT INTO schedule (id_subj, id_user) VALUES(?, ?)', (subj, owner)
                )
                db.commit()
            else:
                flash(error)
        self.schedules = db.execute(
            'SELECT s.name_s FROM subject_ s, schedule sch WHERE s.id = sch.id_subj AND sch.id_user = ?', 
            (owner,)
        ).fetchall()



    def rmSubject(self, subject):
        pass
        # self.subjects.remove(subject.nameS)
        

    def schedEmpty():
        #  False if len(self.subjects) == 0 else True
        pass


class User(metaclass=abc.ABCMeta):
    def __init__(self):
        self.id = None
        self.name = ''
        self.rol = None

    @abc.abstractmethod
    def registrarse(self):
        pass

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setRol(self, rol):
        self.rol = rol

    def getRol(self):
        return self.rol
        

class Professor( User):
    def __init__(self):
        User.__init__(self)

    def registrarse(self):
        return 'Profesor'

class Student( User):
    def __init__(self):
        User.__init__(self)

    def registrarse(self):
        return 'Estudiante'

def get_subject(id):
    db = get_db()
    subject = db.execute(
        'SELECT name_s FROM subject_  WHERE id = ?', 
        (id,)
    ).fetchone()
    db.commit()
    return subject 

def newSubject():
        db = get_db()
        user = g.user['id']
        
        if request.method == 'POST':
            # subj = request.form['subject']
            name = request.form['name_s']
            error = None
            
            if not name or name == '':
                error = 'Ingrese el nombre de la asignatura.'
            elif db.execute(
                'SELECT name_s FROM subject_ WHERE name_s = ?', 
                (name,)
            ).fetchone() is not None:
                error = 'La asignatura {} ya esta registrada.'.format(name)
                
            if error is None:
                db.execute(
                    'INSERT INTO subject_ (name_s) VALUES(?)',(name,)
                )
                db.commit()
                return redirect(url_for('userspace.schedule'))
            else:
                flash(error)
            id = db.execute(
                'SELECT id FROM subject_ WHERE name_s = ?', (name,)
            ).fetchone()


mySchedule = Schedule()

@bp.route('/schedule', methods=('GET', 'POST'))
@login_required
def schedule():
    mySchedule.addSbjct()
    subjects = mySchedule.getSbjcts()
    schedules = mySchedule.getSchdls()
    return render_template('userspace/schedule.html', subjects=subjects, schedules=schedules)

# Eliminar un grupo de una asignatura que corresponde a un profesor
@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_subject(id)
    db = get_db()
    user = g.user['id']
    db.execute('DELETE FROM group_ WHERE id = ? AND id_prof = ?', (id,user))
    db.commit()
    return redirect(url_for('userspace.schedule'))


@bp.route('/addSubject', methods=('POST','GET'))
@login_required
def addSubject():
    newSubject()
    return render_template('userspace/update.html')

