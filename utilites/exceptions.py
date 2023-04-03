

class RequestError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        super(RequestError, self).__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class FieldRequired(RequestError):
    status_code = 405


class DBObjectError(Exception):

    def __init__(self, message) -> None:
        super(DBObjectError, self).__init__()
        self.message = message
        from modules.webapi.models import Worker
        self.c_worker = Worker(id=str(None),
                               salary=-1,
                               worker_name=str(message),
                               work_position=str(None),
                               chif_id=str(None),
                               beginen_date=str(None))


class Notauthorized(RequestError):
    status_code = 403
