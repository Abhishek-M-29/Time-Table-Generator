import random
import mysql.connector as sq

dbm = sq.connect(host='localhost', user='root', password='admin')
db = dbm.cursor()
dbm.autocommit = True


def generate(subjects, day_count, per_day):
    """
    Returns list of sub-list of randomly assigned periods
    """
    assert not day_count > 7, 'Maximum days = 7'
    subjects = [subject.strip() for subject in subjects]
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][:day_count]
    b_prim, b_exs = divmod((per_day - len(subjects)) * len(days), len(subjects))
    table = [random.sample(subjects, len(subjects)) for i in range(day_count)]

    pool = subjects * b_prim
    for i in range(b_exs):
        pool.append(subjects[i % len(subjects)])

    random.shuffle(pool)
    for row in table:
        for j in range(per_day - len(subjects)):
            sub = pool.pop()
            count = row.count(sub)

            i = 0
            while count >= 2:
                pool.append(sub)
                sub = pool[i % len(pool)]
                count = row.count(sub)
                i += 1
                if i > 100:
                    break
            row.insert(row.index(sub) + 1, sub)

    table = [[str(i + 1) for i in range(per_day)]] + table
    table = [[day] + row for day, row in zip(['D \\ P'] + days, table)]

    return table


def database(d_base='timetables'):
    """
    init for db,grades table if not exists
    Default section = 'A'
    """
    db.execute(f" select schema_name from information_schema.schemata where schema_name = '{d_base}' ")
    db_exists = True if db.fetchone() else False

    if not db_exists:
        db.execute(f'create database {d_base}')
    db.execute(f'use {d_base}')
    db.execute('show tables')

    if ('grades',) not in db.fetchall():
        db.execute(f'create table Grades(Class varchar(16),Sec varchar(32) DEFAULT "A",Subjects varchar(64))')


def class_add(classes, d_base='timetables'):
    """
    Updates Classes in Grade table
    input> {'Class 10': ['A,B,C','Math','CS'] , 'Class 12':['A,']}
    Sections = Mandatory , Subjects = Optional
    If Class already exists
    Recurring sects/subs will be added along with previous sects/subs
    """
    db.execute(f'use {d_base}')
    db.execute('select Class from Grades')
    class_in = db.fetchall()
    for k, v in classes.items():
        if len(v) < 2:
            v.append('')
        if (k,) not in class_in:
            db.execute(f'insert into Grades values("{k}","{v[0]}","{v[1]}")')
        else:  # If class already in table , add sections & subs
            db.execute(f'select sec,subjects from grades where class="{k}"')
            a, b = db.fetchone()
            db.execute(
                f'update grades set sec="{a},{v[0]}" ,subjects="{f"{b}," if b else b}{v[1]}"\
                 where class="{k}"')
    return bool(classes)


def class_del(grade, sec, d_base='timetables'):
    db.execute(f'use {d_base}')
    db.execute(f'select sec from grades where Class = "{grade}"')
    # print(db.fetchall())

    ext = db.fetchall()[0][0].replace(f'{sec}', '')
    ext = ext[1:] if ext.startswith(',') else ext

    db.execute(f'update grades set sec = "{ext}" where class = "{grade}"')
    db.execute(f'drop table {grade}_{sec}')

    db.execute(f'select sec from grades where Class = "{grade}"')

    if not db.fetchall()[0][0]:
        db.execute(f'delete from grades where Class ="{grade}"')


def store(p_day, days, d_base='timetables'):
    """
    Assigns timetable for each section in each class and stores in database
    """
    db.execute(f'use {d_base}')
    db.execute('show tables')
    tab_in = [i[0] for i in db.fetchall()]

    db.execute('select class ,sec , subjects from grades')
    for grade, sections, periods in db.fetchall():
        for section in sections.split(','):
            table = generate(periods.split(','), per_day=p_day, day_count=days)

            st = ','.join([f'A{i} varchar (64)' for i in range(len(table[0]))])
            # Field_name based on len
            if f'{grade.lower()}_{section.lower()}' not in tab_in:
                db.execute(f'create table {grade}_{section} ({st})')
                for row in table:
                    db.execute(f'insert into {grade}_{section} values({str(row)[1:-1]})')


if __name__ == '__main__':
    # for k in range(100):
    #     generate(['Math', 'Eng', 'Phy', 'Chem', 'CS'], day_count=random.randint(1, 7), per_day=random.randint(1, 20))
    #     print(k, 'done')
    '''database()
    class_add({'10': ['A,C', 'Math,CS, Eng,Soc'], '12': ['A,B', 'Math,Eng,Phy,Chem,CS'],
               '11': ['B', 'Math,Eng,Phy,Chem,CS']})
    store(8, 7)'''
    class_del('12', 'D')

