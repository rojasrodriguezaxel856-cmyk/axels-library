import os

import pytest


TEST_DB = os.path.join(
    os.path.dirname(__file__),
    "test_biblioteca.db"
)

os.environ["DB_PATH"] = TEST_DB


@pytest.fixture(autouse=True)
def reset_test_db():
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

    import database

    database.init_db()
    yield

    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
