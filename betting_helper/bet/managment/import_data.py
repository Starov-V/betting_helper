import csv
import sqlite3

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'The Zen of Python'
    def handle(self, *args, **options):
        connection = sqlite3.connect('betting_helper/db.sqlite3')
        cursor = connection.cursor()

        with open('betting_helper/data/teams.csv', 'r', encoding='utf-8') as fin:
            dr = csv.DictReader(fin)
            to_db = [(i['name'], i['id_on_api'], i['league']) for i in dr]
        insert_records = ("INSERT INTO bet_team"
                          "(name, id_on_api, league) VALUES (?, ?, ?);")
        cursor.executemany(insert_records, to_db)

        connection.commit()
        connection.close()


if __name__ == '__main__':
    command = Command()
    command.handle()