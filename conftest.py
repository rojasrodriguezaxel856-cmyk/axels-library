import os


TEST_DB = os.path.join(
    os.path.dirname(__file__),
    "test_biblioteca.db"
)

os.environ["DB_PATH"] = TEST_DB
