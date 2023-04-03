from application import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Worker(db.Model):
    id = db.Column(db.String(120), primary_key=True)
    salary = db.Column(db.Integer)  # salary
    worker_name = db.Column(db.String(80))  # name
    work_position = db.Column(db.String(80))  # role
    beginen_date = db.Column(db.String(80))  # onboarding date
    chif_id = db.Column(db.String(120))

    def get_chif_name(self):
        return 'chief name'

    def __str__(self):
        return f'{self.worker_name} ' \
               f'{self.beginen_date} ' \
               f'{self.work_position} ' \
               f'{self.salary} ' \
               f'{self.get_chif_name()}'


def position_maping():
    return {'Accounts': {
        'Assessor': {
            'Auditor': {
                'Bookkeeper': {
                    'Budget analyst': {
                        'Cash manager': ['Chief financial officer',
                                         'Controller',
                                         'Credit manager',
                                         'Tax specialist',
                                         'Treasurer'
                                         ]
                    }
                }
            }
        }
    }
    }


def get_workers_from_id(*args):
    return db.session.query(Worker).filter(Worker.id.in_(args)).all()


def get_workers_from_beginen_date(*args):
    return db.session.query(Worker).filter(Worker.beginen_date.in_(args)).all()


def get_workers_from_work_positiond(*args):
    return db.session.query(Worker).filter(
        Worker.work_position.in_(args),
    ).all()


def get_workers_from_salary(*args):
    return db.session.query(Worker).filter(Worker.salary.in_(args)).all()


def get_workers_from_chif_name(*args):
    return db.session.query(Worker).filter(Worker.chif_id.in_(args)).all()


def get_worker_from_name(*args):
    return db.session.query(Worker).filter(Worker.worker_name.in_(args)).all()


def get_chif_name_from_id(id):
    w: Worker = db.session.query(Worker).filter(Worker.id.in_(id)).all()
    c: Worker = db.session.query(Worker).filter(Worker.id.in_(w.chif_id)).all()
    return c.worker_name


def get_all_workers():
    workers = Worker.query.all()
    return workers
