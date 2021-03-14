from selenium import webdriver
import pytest
from sqlalchemy import create_engine
from sqlalchemy import insert, delete
from sqlalchemy import table, column
from helpers.general_helpers import generate_string


@pytest.fixture()
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture()
def create_group():
    name = generate_string(8)
    engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/postgres')
    auth_group_table = table("auth_group",
                             column("id"),
                             column("name")
                             )
    stmt = (
        insert(auth_group_table).values(name=name)
    )
    engine.execute(stmt)
    yield name
    stmt = (
        delete(auth_group_table).where(auth_group_table.c.name == name)
    )
    engine.execute(stmt)
