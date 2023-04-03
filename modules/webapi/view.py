from flask import Blueprint, send_from_directory

from application import db

from modules.webapi.models import (Worker, get_chif_name_from_id,
                                   get_workers_from_id)

blue_print = Blueprint('blue_print', __name__)


@blue_print.route('style/<path:filename>')
def styles(filename):
    path = 'modules/webapi/html_template/'
    return send_from_directory(path, filename)


@blue_print.route('index')
def show_page():
    # rows: list[Worker] = get_all_workers()
    rows: list[Worker] = get_workers_from_id(
        "774a9334-c15a-42e1-9aa1-f8cf11505dfc",
        )
    rows_list = []
    with open('modules/webapi/html_template/index.html') as f:
        template_page: str = f.read()

    for worker in rows:
        with open('modules/webapi/html_template/row.html') as r:
            row_page: str = r.read()
        try:
            chief = get_chif_name_from_id(worker.chif_id)
        except Exception as e:
            chief = str(e)
        row_page = row_page.replace('{{#Count}', str(len(rows_list) + 1))
        row_page = row_page.replace('{{#Date_of_begin}', worker.beginen_date)
        row_page = row_page.replace('{{#Name}', str(worker.worker_name))
        row_page = row_page.replace('{{#Salary}', str(worker.salary))
        row_page = row_page.replace('{{#Chief}', str(chief))  #add getter for name chief # noqa
        row_page = row_page.replace('{{#Position}', str(worker.work_position))

        rows_list.append(row_page)
    return_rows = ''
    for i in rows_list:
        return_rows += i
    page = template_page.replace('{{#ROWS}', return_rows)

    return page


def health_database():
    try:
        print("--- CHECK ----")
        db.session.query("1").from_statement("SELECT 1").all()
        return True, 'It works'
    except Exception as e:
        return False, str(e)

# def health_check():
#     status = health_database()
#     logger.info("Check library", extra={"MESSAGE_ID": "OK"})
#     return status, f" API {'' if status else 'not '}initialized"
