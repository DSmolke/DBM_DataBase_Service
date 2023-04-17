import pytest
import gdown
import subprocess
import time

from dbm_database_service.connectors import MySQLConnectionPoolBuilder


import logging
logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])

# TODO 1 Wymyśliłem sobie, że testy będą w pełni zautomatyzowane. Pierwszy fixture uruchamia docker compose z bazą,
#  aby testy połączeniowe były prostsze do zrealizowania dla rekrutera. Kolejne 3 fixture pobierają .envy z google
#  drive, też po to, żeby nie trzeba było się z nimi bawić. Czy jest to fajne rozwiązanie, czy jednak kicz i nie warto się w to bawić?


@pytest.fixture(autouse=True, scope='session')
def prepare_test_database():
    """ Fixture that creates mysql container using docker-compose  """
    cmd = 'docker-compose up -d'
    subprocess.getoutput(cmd)
    # TODO 2 Jeżeli TODO 1 na tak, to tutaj moje pytanie to, czy da się użyć tego loggera, aby wyświetlić ten komunikat
    logging.info("Creating database ...")
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
