import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, inspect, func

def test():
    engine = create_engine("postgresql://postgres:{PASSWORD_HERE}@localhost:5432/crowdfunding_db")

    result = engine.execute(text('SELECT * FROM campain LIMIT 5')).fetchall()
    result_dicts = [dict(row) for row in result]

    print(result_dicts[0])

def get_tabel(tabel):
    engine = create_engine("postgresql://postgres:fartface92@localhost:5432/crowdfunding_db")
    query = f'SELECT * FROM {tabel}'
    result = engine.execute(text(query)).fetchall()
    result_dicts = [dict(row) for row in result]
    return result_dicts

def get_col(tabel, col):
    engine = create_engine("postgresql://postgres:fartface92@localhost:5432/crowdfunding_db")
    query = f'SELECT {col} FROM {tabel}'
    result = engine.execute(text(query)).fetchall()
    result_dicts = [dict(row) for row in result]
    return result_dicts

def get_match(tabel, col, data):
    engine = create_engine("postgresql://postgres:fartface92@localhost:5432/crowdfunding_db")
    query = f'SELECT * FROM {tabel} WHERE {col} = {data}'
    result = engine.execute(text(query)).fetchall()
    result_dicts = [dict(row) for row in result]
    return result_dicts
