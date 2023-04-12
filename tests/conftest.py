import pytest
import gdown
import subprocess
import time

from dbm_database_service.connectors import MySQLConnectionPoolBuilder


import logging
logging.basicConfig(level=logging.INFO)
logging.StreamHandler()


@pytest.fixture(autouse=True, scope='session')
def prepare_test_database():
    cmd = 'docker-compose up -d'
    subprocess.getoutput(cmd)
    logging.info("Creating database ...")
    # Maximum time needed for docker-compose to build container etc.
    time.sleep(15)

@pytest.fixture(autouse=True, scope='session')
def download_dotenv_from_drive():
    url = 'https://drive.google.com/uc?id=1_CT3QaaurMCg1BBty2p0J6STy6RoIseX'
    output = '../.env'
    gdown.download(url, output, quiet=False)

@pytest.fixture(autouse=True, scope='session')
def download_dotenv_from_drive2():
    url = 'https://drive.google.com/uc?id=1_oxyqNn-HKMuMzDZir2d4Ff80e1nHJ_Y'
    output = '..//tests//test2.env'
    gdown.download(url, output, quiet=False)

@pytest.fixture(autouse=True, scope='session')
def download_dotenv_from_drive3():
    url = 'https://drive.google.com/uc?id=1_CT3QaaurMCg1BBty2p0J6STy6RoIseX'
    output = '..//tests//.env'
    gdown.download(url, output, quiet=False)

@pytest.fixture(scope='session')
def basic_builder():
    return MySQLConnectionPoolBuilder()
