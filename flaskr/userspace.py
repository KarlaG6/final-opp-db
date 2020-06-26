# # from functools import wraps
# import functools

# from flask import (
#     Blueprint, flash, g, redirect, render_template, request, url_for
# )
# from werkzeug.exceptions import abort

# from flaskr.auth import login_required
# from flaskr.db import get_db
# import abc
# from flask import copy_current_request_context
# bp = Blueprint('userspace', __name__)




# class Subject:
#     def __init__(self):
#         self.id = None
#         self.nameS = ''
#         self.professor = {}
#         self.roomType = ''
#         self.rooms = []
#         self.date = None
#         self.time = None
#         self.group = None

#     def setNameS(name):
#         self.nameS = name

#     def setId(i):
#         self.id = i

#     def addRoom(self, room):
#         self.rooms.append(room)

#     def setProfe(self, id):
#         self.professor.idP = id

#     def setTime(self, hora):
#         self.time = hora

#     def setDate(self, dia):
#         self.date = dia
#         setNameS(name) 
            

#     def delSubject(self):
#         pass


# class User(metaclass=abc.ABCMeta):
#     def __init__(self):
#         self.id = g.user['id']
#         self.name = g.user['username']
#         self.rol = g.user['rol_id']
#         self.user = {}

#     @abc.abstractmethod
#     def registrarse(self):
#         pass

#     def setId(self, id):
#         self.id = id

#     def getId(self):
#         return self.id

#     def setName(self, name):
#         self.name = name

#     def getName(self):
#         return self.name

#     def setRol(self, rol):
#         self.rol = rol

#     def getRol(self):
#         return self.rol

    

# class Professor( User):
#     def __init__(self):
#         User.__init__(self)

#     def registrarse(self):
#         return 'Soy metodo profesor'

# class Student( User):
#     def __init__(self):
#         User.__init__(self)

#     def registrarse(self):
#         return 'Estudiante'

# class Funcionary( User):
#     def __init__(self):
#         User.__init__(self)

#     def registrarse(self):
#         return 'Funcionario'

# class Tutor( User):
#     def __init__(self):
#         User.__init__(self)

#     def registrarse(self):
#         return 'Tutor'

# class Other( User):
#     def __init__(self):
#         User.__init__(self)

#     def registrarse(self):
#         return 'Other'

# # @bp.before_app_request
# # 
# # def whoami(user):
# #     return type(user).__name__
# # user = whoami(rolAssignedClass())

# def rolAssignedClass():
#     x = g.user['rol_id']
#     user = None
#     if x == 1:
#         user = Student()
#     elif x == 2:
#         user = Professor()
#     elif x == 3:
#         user = Funcionary()
#     elif x == 4:
#         user = Tutor()
#     else:
#         user = Other()
#     return user
# def whoami(user):
#     return type(user).__name__
# # user = whoami(rolAssignedClass())


# # falta que herede de la clase hija de usuario
# class Schedule(Subject):
#     def __init__(self):
#         self.subjects = []
#         self.schedules = []
#         self.owner = None

#     def getSbjcts(self):
#         return self.subjects

#     def getSchdls(self):
#         return self.schedules
    
#     def addSbjct(self):
#         db = get_db()
#         self.subjects = db.execute(
#             'SELECT id, name_s FROM subject_'
#         ).fetchall()
#         self.owner = g.user['id']
#         owner = self.owner
#         if request.method == 'POST':
#             subj = request.form['subject']
#             error = None
            
#             if not subj:
#                 error = 'Seleccione una asignatura.'
#             elif db.execute(
#                 'SELECT id_subj FROM schedule WHERE id_subj = ? AND id_user = ?', 
#                 (subj, owner)
#             ).fetchone() is not None:
#                 subject = get_subject(subj)
#                 error = 'La asignatura {} ya esta registrada.'.format(subject[0])
#                 # print(schedules)
#                 # mySchedule = Schedule()
#                 # for sch in schedules:
#                 #     mySchedule.addSubject(sch)
#             if error is None:
#                 db.execute(
#                     'INSERT INTO schedule (id_subj, id_user) VALUES(?, ?)', (subj, owner)
#                 )
#                 db.commit()
#             else:
#                 flash(error)
#         self.schedules = db.execute(
#             'SELECT s.name_s FROM subject_ s, schedule sch WHERE s.id = sch.id_subj AND sch.id_user = ?', 
#             (owner,)
#         ).fetchall()

        
#     def rmSubject(self, subject):
#         pass
#         # self.subjects.remove(subject.nameS)
        

#     def schedEmpty():
#         #  False if len(self.subjects) == 0 else True
#         pass


    
#     # def setGroups(self, subj):
#     #     db = get_db()
#     #     owner = self.owner
#     #     if request.method == 'POST':
#     #         subj = request.form['subject']
#     #         error = None
#     #         if not subj:
#     #             error = 'Seleccione una asignatura.'
#     #         elif db.execute(
#     #             'SELECT s.id_subj FROM schedule s, group_subject g WHERE s.id_subj = ? AND s.id_user = ? AND g.id_subj = ?', 
#     #             (subj, owner, subj,)
#     #         ).fetchone() is not None:
#     #             subject = get_subject(subj)
#     #             error = 'La asignatura {} ya esta registrada.'.format(subject[0])
#     #             # print(schedules)
#     #             # mySchedule = Schedule()
#     #             # for sch in schedules:
#     #             #     mySchedule.addSubject(sch)
#     #         if error is None:
#     #             db.execute(
#     #                 'INSERT INTO schedule (id_subj, id_user) VALUES(?, ?)', (subj, owner)
#     #             )
#     #             db.commit()
#     #         else:
#     #             flash(error)
        
#     #     self.setSchdls(owner)
        


# def get_subject(id):
#     db = get_db()
#     subject = db.execute(
#         'SELECT name_s FROM subject_  WHERE id = ?', 
#         (id,)
#     ).fetchone()
#     db.commit()
#     return subject 

# def newSubject():
#         db = get_db()
#         myUser = g.user['id']
        
#         if request.method == 'POST':
#             # subj = request.form['subject']
#             name = request.form['name_s']
#             error = None
            
#             if not name or name == '':
#                 error = 'Ingrese el nombre de la asignatura.'
#             elif db.execute(
#                 'SELECT name_s FROM subject_ WHERE name_s = ?', 
#                 (name,)
#             ).fetchone() is not None:
#                 error = 'La asignatura {} ya esta registrada.'.format(name)
                
#             if error is None:
#                 db.execute(
#                     'INSERT INTO subject_ (name_s) VALUES(?)',(name,)
#                 )
#                 db.commit()
#                 return redirect(url_for('userspace.schedule'))
#             else:
#                 flash(error)
#             id = db.execute(
#                 'SELECT id FROM subject_ WHERE name_s = ?', (name,)
#             ).fetchone()


# mySchedule = Schedule()

# def role_required(rol):
#     def decorator(function):
#         @wraps(function)
#         def wrapper():
#             res = None
#             if g.user['rol_id'] is not rol:

#                 res = 'Debes ser profesor para realizar esta accion'
#             else:
#                 res = 'Puedes realizar esta accion'
#             # este flash error es mejor mostrarlo en un prompt y redirect(url_for('userspace.schedule'))
#             flash(res)
            
#             return function()
#         return wrapper
#     return decorator

# def rol_req(rol):
#     def role_required(view):
#         @functools.wraps(view)
#         def wrapped_view(**kwargs):
#             rolname = get_db().execute(
#                 'SELECT name_rl FROM rol WHERE id = ?', (rol,)
#             ).fetchone()
#             if g.user['rol_id'] is not rol:
#                 flash('Debes ser {} para realizar esta accion'.format(rolname[0]))
#                 return redirect(url_for('userspace.schedule'))

#             return view(**kwargs)

#         return wrapped_view
#     return role_required

# @bp.before_request
# def getValueSubj( ):
#     db = get_db()
#     if request.method == 'POST':
#         subj = request.form['subject']
#         return subj
    

# @bp.route('/profile')
# def profile():
#     rolid = g.user['rol_id']
#     rol = get_db().execute(
#         'SELECT name_rl FROM rol WHERE id = ?',(rolid,)
#     ).fetchone()
#     return render_template('userspace/profile.html', rol=rol)
#     # return { 'rol': rol}


# @bp.route('/schedule', methods=('GET', 'POST'))
# @login_required
# def schedule():
#     mySchedule.addSbjct()
#     subjects = mySchedule.getSbjcts()
#     schedules = mySchedule.getSchdls()
#     return render_template('userspace/schedule.html', subjects=subjects, schedules=schedules)

# # Eliminar un grupo de una asignatura que corresponde a un profesor
# @bp.route('/<int:id>/delete', methods=('POST',))
# @login_required
# def delete(id):
#     get_subject(id)
#     db = get_db()
#     user = g.user['id']
#     db.execute('DELETE FROM group_subject WHERE id = ? AND id_prof = ?', (id,user))
#     db.commit()
#     return redirect(url_for('userspace.schedule'))


# @bp.route('/addSubject', methods=('POST','GET'))
# @login_required
# @rol_req(2)
# def addSubject():
#     newSubject()
#     return render_template('userspace/update.html')

from functools import wraps
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
from abc import ABC, abstractmethod

from flask_wtf import FlaskForm, Form
from wtforms import StringField
from wtforms.validators import DataRequired

bp = Blueprint('userspace', __name__)

# class Form1(Form):
#     name = StringField('name')
#     submit1 = SubmitField('submit')

# class Form2(Form):
#     name = StringField('name')
#     submit2 = SubmitField('submit')

class SubjectGroup:
    def __init__(self):
        self.subject = {'id': None, 'name': None}
        self.group = {'id': None, 'name': None}
        self.professor = {'id': None, 'name': None}
        self.roomType = ''
        self.rooms = []
        self.date = None
        self.time = None
        self.groups = None

    def setNameS(name):
        self.nameS = name

    def setId(i):
        self.id = i

    def addRoom(self, room):
        self.rooms.append(room)

    def setProfe(self, id, name):
        self.professor['id'] = id
        self.professor['name'] = name

    def getProfe(self):
        return self.professor

    def setTime(self, hora):
        self.time = hora

    def setDate(self, dia):
        self.date = dia
        setNameS(name) 
    
    def getSubject(self):
        return self.subject
    
    def setSubject(self, id, name):
        self.subject['id'] = id
        self.subject['name'] = name

    def getGroup(self):
        return self.group

    def setGroup(self, id, name):
        self.group['id'] = id
        self.group['name'] = name

    def delSubject(self):
        pass

class Schedule(SubjectGroup):
    def __init__(self):
        self.subjects = []
        self.schedules = []
        self.groups = []
        self.owner = None
        self.activeSubj = None
        super().__init__()

    def getSbjcts(self):
        return self.subjects

    def setSubjects(self):
        self.subjects = get_db().execute(
            'SELECT id, name_s FROM subject_'
        ).fetchall()

    def getSchdls(self):
        return self.schedules
    
    def setSchdl(self, owner):
        self.schedules = get_db().execute(
            'SELECT s.name_s FROM subject_ s, schedule sch WHERE s.id = sch.id_subj AND sch.id_user = ?', 
            (owner,)
        ).fetchall()

    def getOwner(self):
        return self.owner

    def setOwner(self):
        self.owner = g.user['id']

    def addSbjct(self):
        db = get_db()
        self.setSubjects()
        self.setOwner()
        subj = self.activeSubj
        owner = self.getOwner()
        if request.method == 'POST':
            group = request.form['group']
            error = None
            
            if not subj:
                error = 'Seleccione un grupo.'
            elif db.execute(
                'SELECT id_subj FROM schedule WHERE id_subj = ? AND id_user = ?', 
                (subj, owner)
            ).fetchone() is not None:
                subject = get_subject(subj)
                error = 'La asignatura con este grupo {} ya esta registrado.'.format(subject[0])
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
        self.setSchdl(owner)


    def getGroups(self):
        return self.groups


    def rmSubject(self, subject):
        pass
        # self.subjects.remove(subject.nameS)
        

    def schedEmpty():
        #  False if len(self.subjects) == 0 else True
        pass

    def selectedSubj(self):
        db = get_db()
        self.setSubjects()
        owner = self.getOwner()
        if request.method == 'POST' :
            subj = request.form['subject']
            error = None
            
            if not subj:
                error = 'Seleccione una asignatura.'
            if error is None:
                self.activeSubj = subj
                print (get_subject(subj)[0])
            else:
                flash(error)

    def getSelectedSubject(self):
        return self.activeSubj

    def setGroups(self):
        db = get_db()
        owner = self.owner
        subj = self.activeSubj
        if subj is not None:
            groups = db.execute(
                'SELECT id, name_g FROM group_subject  WHERE id_subj = ? ', 
                (subj)
            ).fetchall()
        else:
            groups = [{'id': 2, 'name_g': 'tumama'}]
        self.groups = groups

    
    def myfnc(self):
        if request.form['subject'] == 'Mostrar Grupos':
            print ('sed')
        else:
            print('fdg')


def initGroups():
    groups = get_db().execute(
        'SELECT * FROM group_subject WHERE id_subj = 1'
    ).fetchall()
    return groups

class User(ABC):
    def __init__(self):
        self.id = None
        self.name = ''
        self.rol = None
        # self.rolClass = None
        super().__init__()

    @abstractmethod
    def registrarse(self):
        return 'Soy User'

    def setId(self):
        self.id = g.user['id']

    def getId(self):
        return self.id

    def setName(self):
        self.name = g.user['username']

    def getName(self):
        return self.name

    def setRol(self):
        self.rol = g.user['rol_id']
        
    def getRol(self):
        return self.rol

# def rolAssignedClass():
#     pass
#     # x = rol
#     # if x == 1:
#     #     user = Student()
#     # elif x == 2:
#     #     user = Professor()
#     # elif x == 3:
#     #     user = Funcionary()
#     # elif x == 4:
#     #     user = Tutor()
#     # else:
#     #     user = Other()
#     # g.rolClass = user


class Professor( User):
    def __init__(self):
        super().__init__()

    def registrarse(self):
        super().registrarse()
        return 'Soy Profesor'

    def setId(self):
        super().setId()

    def getId(self):
        super().getId()

    def setName(self):
        super().setName()

    def getName(self):
        super().getName()

    def setRol(self):
        super().setRol()

    def getRol(self):
        super().getRol()

    
class Student( User):
    def __init__(self):
        super().__init__()

    def registrarse(self):
        return 'Estudiante'
    
    def setId(self):
        super().setId()

    def getId(self):
        super().getId()

    def setName(self):
        super().setName()

    def getName(self):
        super().getName()

    def setRol(self):
        super().setRol()

    def getRol(self):
        super().getRol()

class Funcionary( User):
    def __init__(self):
        super().__init__()

    def registrarse(self):
        return 'Funcionario'

    def setId(self):
        super().setId()

    def getId(self):
        super().getId()

    def setName(self):
        super().setName()

    def getName(self):
        super().getName()

    def setRol(self):
        super().setRol()

    def getRol(self):
        super().getRol()

class Tutor( User):
    def __init__(self):
        super().__init__()

    def registrarse(self):
        super().registrarse()
        return 'Tutor'

    def setId(self):
        super().setId()

    def getId(self):
        super().getId()

    def setName(self):
        super().setName()

    def getName(self):
        super().getName()

    def setRol(self):
        super().setRol()

    def getRol(self):
        super().getRol()

class Other( User):
    def __init__(self):
        super().__init__()

    def registrarse(self):
        return 'Other'

    def setId(self):
        super().setId()

    def getId(self):
        super().getId()

    def setName(self):
        super().setName()

    def getName(self):
        super().getName()

    def setRol(self):
        super().setRol()

    def getRol(self):
        super().getRol()


# @bp.context_processor
# def inject_group():
#     return dict(user=g.user)   
       

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
    myUser = g.user['id']
    
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

def rol_req(rol):
    def role_required(view):
        @functools.wraps(view)
        def wrapped_view(**kwargs):
            rolname = get_db().execute(
                'SELECT name_rl FROM rol WHERE id = ?', (rol,)
            ).fetchone()
            if g.user['rol_id'] is not rol:
                flash('Debes ser {} para realizar esta accion'.format(rolname[0]))
                return redirect(url_for('userspace.schedule'))

            return view(**kwargs)

        return wrapped_view
    return role_required

@bp.context_processor
def inject_group():
    grupo = 'mi grupo'
    return dict(grupo = grupo)

@bp.route('/profile')
def profile():
    rolid = g.user['rol_id']
    rol = get_db().execute(
        'SELECT name_rl FROM rol WHERE id = ?',(rolid,)
    ).fetchone()
    # print( user.registrarse())
    # print( type(user).__name__)
    return render_template('userspace/profile.html', rol=rol)
    # return {'rol': rol}

@bp.route('/addMySubject', methods=('GET', 'POST'))
@login_required
def addMySubject():
    mySchedule.setGroups()
    subject = mySchedule.getSelectedSubject()
    groups = mySchedule.getGroups()
    mySchedule.addSbjct()
    mySchedule.setSchdl(g.user['id'])
    schedules = mySchedule.getSchdls()
    return render_template('userspace/addSubject.html', subject=subject, groups=groups, schedules=schedules)
    


@bp.route('/schedule', methods=('GET', 'POST'))
@login_required
def schedule():
    mySchedule.selectedSubj()
    # mySchedule.setGroups()
    subjects = mySchedule.getSbjcts()
    schedules = mySchedule.getSchdls()
    if request.method == 'POST':
         return redirect(url_for('userspace.addMySubject'))
    return render_template('userspace/schedule.html', subjects=subjects, schedules=schedules)
    # return { 'subjects': mySchedule.getSbjcts(), 'schedules': mySchedule.getSchdls(), 'groups': initGroups()}
    ##corregirlo, es una fachada, 0 programatico##

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
@rol_req(2)
def addSubject():
    newSubject()
    return render_template('userspace/update.html')