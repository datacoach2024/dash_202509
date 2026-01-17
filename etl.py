import json
import logging
import time
import pandas as pd
from pathlib import Path
from sqlalchemy import text

from db import set_connection

SCHEMA = 'adv_works'
SOURCE = 'source/adventure_works.xlsx'

# важно сохранять порядок листов так как сначала идут таблицы без внешних ключей
SHEETS = ['Customers', 'Territory', 'ProductCategory', 
          'ProductSubCategory', 'Products', 'Sales']

with open('dicts/columns.json') as f:
    columns_dict = json.load(f)


def make_snake_case(camel_cased_word: str) -> str:
    snake_cased_word = ''
    for ix, sym in enumerate(camel_cased_word):
        if sym.isupper() and ix != 0:
            snake_cased_word += f"_{sym.lower()}"
        else:
            snake_cased_word += sym.lower().replace(' ', '')
    
    if snake_cased_word == 'group':
        snake_cased_word = 'continent'

    return snake_cased_word


def read_data(sheet_name: str) -> pd.DataFrame:
    print(f"reading data from {sheet_name}...")
    df = pd.read_excel(
        SOURCE, 
        sheet_name=sheet_name,
    ).dropna(thresh=3)

    df.rename(
        columns={col: make_snake_case(col) for col in df.columns}, 
        inplace=True
    )

    return df


def load_data(df: pd.DataFrame, table_name: str) -> None:
    print(f"{table_name}: {df.shape}")
    with set_connection() as pg:
        print(f"loading data to {table_name}...")
        df.to_sql(
            schema=SCHEMA,
            name=table_name,
            con=pg,
            index=False,
            if_exists='append'
        )


def create_schema() -> None:
    with set_connection() as pg:
        print(f"creating schema...")
        pg.execute(text(f"create schema if not exists {SCHEMA}"))
        pg.commit()


def create_table(table_name: str) -> None:
    ddl_file = f"ddl/{table_name}_ddl.sql"

    with open(ddl_file) as f:
        ddl_query = text(f.read().format(schema=SCHEMA))

    with set_connection() as pg:
        print(f"creating table {table_name}...")
        pg.execute(ddl_query)
        pg.commit()

    with set_connection() as pg:
        pg.execute(text(f"truncate table {SCHEMA}.{table_name} restart identity cascade"))
        pg.commit()


def pipeline() -> None:
    
    create_schema()

    for sheet_name in SHEETS:
        df = read_data(sheet_name)
        
        table_name = make_snake_case(sheet_name)
        usecols = columns_dict[table_name]

        create_table(table_name)
        load_data(df[usecols], table_name)