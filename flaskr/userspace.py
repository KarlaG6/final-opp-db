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
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
import abc

bp = Blueprint('userspace', __name__)



 

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
        self.id = g.user['id']

    def getId(self):
        return self.id

    def setName(self, name):
        self.name = g.user['username']

    def getName(self):
        return self.name

    def setRol(self):
        self.rol = g.user['rol_id']

    def getRol(self):
        return self.rol

        

class Professor( User):
    def __init__(self):
        User.__init__(self)

    def registrarse(self):
        return 'Soy metodo profesor'

class Student( User):
    def __init__(self):
        User.__init__(self)

    def registrarse(self):
        return 'Estudiante'

class Funcionary( User):
    def __init__(self):
        User.__init__(self)

    def registrarse(self):
        return 'Funcionario'

class Tutor( User):
    def __init__(self):
        User.__init__(self)

    def registrarse(self):
        return 'Tutor'

class Other( User):
    def __init__(self):
        User.__init__(self)

    def registrarse(self):
        return 'Other'

def rolAssignedClass():
    x = g.user['rol_id']
    user = None
    if x == 1:
        user = Student()
    elif x == 2:
        user = Professor()
    elif x == 3:
        user = Funcionary()
    elif x == 4:
        user = Tutor()
    else:
        user = Other()
    return user

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

@bp.route('/profile')
def profile():
    rolid = g.user['rol_id']
    rol = get_db().execute(
        'SELECT name_rl FROM rol WHERE id = ?',(rolid,)
    ).fetchone()
    user = rolAssignedClass()
    # print( user.registrarse())
    # print( type(user).__name__)
    return render_template('userspace/profile.html', rol=rol)


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
@rol_req(2)
def addSubject():
    newSubject()
    return render_template('userspace/update.html')