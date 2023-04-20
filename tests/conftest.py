import pytest
import gdown
import subprocess
import time
import logging

from dbm_database_service.connectors import MySQLConnectionPoolBuilder

logging.basicConfig(level=logging.INFO)

@pytest.fixture(autouse=True, scope='session')
def prepare_test_database():
    """ Fixture that creates mysql container using docker-compose  """
    logging.info('Creating and setting up database .....')
    cmd = 'docker-compose up -d'
    subprocess.getoutput(cmd)
    # Maximum time needed for docker-compose to build container etc.
    time.sleep(15)

@pytest.fixture(autouse=True, scope='session')
def download_dotenv_from_drive():
    """ Fixture that downloads .env file needed for tests """
    url = 'https://drive.google.com/uc?id=1_CT3QaaurMCg1BBty2p0J6STy6RoIseX'
    output = '../.env'
    gdown.download(url, output, quiet=False)

@pytest.fixture(autouse=True, scope='session')
def download_dotenv_from_drive2():
    """ Fixture that downloads test2.env file needed for tests """
    url = 'https://drive.google.com/uc?id=1_oxyqNn-HKMuMzDZir2d4Ff80e1nHJ_Y'
    output = '..//tests//test2.env'
    gdown.download(url, output, quiet=False)

@pytest.fixture(autouse=True, scope='session')
def download_dotenv_from_drive3():
    """ Fixture that downloads .env file needed for tests """
    url = 'https://drive.google.com/uc?id=1_CT3QaaurMCg1BBty2p0J6STy6RoIseX'
    output = '..//tests//.env'
    gdown.download(url, output, quiet=False)

@pytest.fixture(scope='session')
def basic_builder():
    return MySQLConnectionPoolBuilder()
