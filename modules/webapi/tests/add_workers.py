import uuid
from asyncio import Queue
from datetime import datetime, timedelta
from random import randrange

from sqlalchemy import engine

from application import db

# from modules.webapi.models import Worker

sec_names = [
    "Page",
    "Larry",
    "Paige",
    "Satchel",
    "Paine",
    "Thomas",
    "Palahniuk",
    "Chuck",
    "Palgrave",
    "Francis Turner",
    "Palin",
    "Michael",
    "Palme",
    "Olof",
    "Parker",
    "Dorothy",
    "Parton",
    "Dolly",
    "Pascal",
    "Blaise",
    "Pasteur",
    "Louis",
    "Patañjali",
    "Pater",
    "Walter",
    "Paterson",
    "Isabel",
    "Patrick",
    "Saint",
    "Patton",
    "George S.",
    "Paul VI (Pope)",
    "Paul",
    "Ron",
    "Pauli",
    "Wolfgang",
    "Pauling",
    "Linus",
    "Payack",
    "Paul JJ",
    "Payne",
    "Max",
    "Peel",
    "John",
    "Peguy",
    "Charles",
    "Peirce",
    "Charles Sanders",
    "Penn",
    "William",
    "Percy",
    "Walker",
    "Peres",
    "Shimon",
    "Perger",
    "Andreas Paolo",
    "Pericles",
    "Perle",
    "Richard",
    "Perlis",
    "Alan",
    "Perry",
    "Michael D.",
    "Perry",
    "Oliver Hazard",
    "Pessoa",
    "Fernando",
    "Pet Shop Boys (Neil Tennant and Chris Lowe)",
    "Peter Kay",
    "Peter",
    "Dr. Laurence J.",
    "Petronius",
    "Gaius",
    "Petty",
    "Tom",
]
names = [
    "Nabokov",
    "Vladimir",
    "Nachman",
    "Rabbi",
    "of Bratzlav",
    "Nader",
    "Ralph",
    "Nagel",
    "Thomas",
    "Naidu",
    "Richard",
    "Nailatikau",
    "Adi Koila",
    "Nailatikau",
    "Ratu Epeli Qaraninamu",
    "Najimy",
    "Kathy",
    "Nash",
    "John Forbes",
    "Nash",
    "Thomas",
    "Navakasuasua",
    "Maciu",
    "Negroponte",
    "Nicholas",
    "Nelson",
    "Hailey Anne",
    "Nelson",
    "Horatio",
    "Nero (Emperor)",
    "Neruda",
    "Pablo",
    "Newhart",
    "Bob",
    "Newton",
    "Isaac",
    "Newton",
    "John",
    "Nicks",
    "Stevie",
    "Czar",
    "Nicholas II",
    "Nicoll",
    "James",
    "Niebuhr",
    "Reinhold",
    "Niemöller",
    "Martin",
    "Nietzsche",
    "Friedrich",
    "Nightingale",
    "Florence",
    "Nijinsky",
    "Vaslav",
    "Nin",
    "Anaïs Nin",
    "Ninio",
    "Jacques",
    "Niranjan",
    "Sangeeta",
    "Niven",
    "Larry",
    "Nixon",
    "Richard",
    "Noam",
    "Eli",
    "Norton",
    "Joshua Abraham",
    "Nostradamus",
    "Michel",
    "de Notredame",
    "Novalis",
    "Nugent",
    "Ted",
    "Nukem",
    "Duke",
    "Null",
    "Gary",
    "Nunally",
    "Patrick",
    "Nuwas",
    "Abu",
]
positions = [
    "Accounts",
    "Assessor",
    "Auditor",
    "Bookkeeper",
    "Budget analyst",
    "Cash manager",
    "Chief financial officer",
    "Controller",
    "Credit manager",
    "Tax specialist",
    "Treasurer",
]


def position_maping():
    pos = {
        "Accounts": {
            "Assessor": {
                "Auditor": {
                    "Bookkeeper": {
                        "Budget analyst": {
                            "Cash manager": [
                                "Chief financial officer",
                                "Controller",
                                "Credit manager",
                                "Tax specialist",
                                "Treasurer",
                            ]
                        }
                    }
                }
            }
        }
    }


def ger_chief_map():

    pass


queue = Queue(maxsize=50)


def gen_workers():
    from modules.webapi.models import Worker

    current_chief = uuid.uuid4()
    max_workers = 50

    for i in range(0, max_workers):
        if i // 10000 == 0:
            current_chief = str(uuid.uuid4())

        w = Worker(
            id=str(uuid.uuid4()),
            salary=randrange(100, 1200),
            worker_name=f"{names[randrange(len(names))]} {sec_names[randrange(len(sec_names))]}",
            work_position=f"{positions[randrange(len(positions))]}",
            chif_id=current_chief,
            beginen_date=f"{datetime.now() - timedelta(randrange(2000))}",
        )
        try:
            try:
                db.session.add(w)
            except Exception as r:
                print("ADD", r)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)

        finally:
            db.session.close()
            print("sesion closed")
