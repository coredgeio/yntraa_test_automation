import pytest
from plugins import TestRailPlugin
import logging

def pytest_addoption(parser):
    """ Add custom parameters to cmd line """
    logging.info("inside pytest add-option")
    parser.addoption('--ids', action='store', metavar='id1,id2,id3...', help='only run tests with the specified IDs')
    parser.addoption('--publish', action='store_true', default=True,
                     help='If set, create a new test run and publish results')

    parser.addoption('--include_all', action='store_true', default=False,
                     help='Used with --publish. If set, the test run will\
                     contain all test cases.')

    parser.addoption('--tr_name', action='store', metavar='<run name>',
                     help='Used with --publish to configure run name.')

    parser.addoption('--tr_id', action='store', metavar='run_id', help='If set, run tests in the test run and publish')


def pytest_configure(config):
    """ Configure marker
        Register plugin
    """
    logging.info("inside pytest configure")
    config.addinivalue_line('markers',
                            'testrail(id): mark test with the case id')
    if config.getoption('--publish') or config.getoption('--tr_id'):
        config.pluginmanager.register(
            TestRailPlugin(
                config.getoption('--tr_id'),
                config.getoption('--include_all'),
                config.getoption('--tr_name')))


def pytest_runtest_setup(item):
    """ This handle test case skipping when
        plugin is not available
    """
    logging.info("inside pytest runtest setup")
    logging.info('runtest setup called')
    ids = item.config.getoption('--ids')
    if not ids:
        return
    ids = set([int(x) for x in ids.split(',')])

    idmarker = item.get_closest_marker('testrail')
    logging.info("idmarker -> ")
    logging.info(idmarker.args[1])
    logging.info(idmarker)
    if idmarker is None:
        pytest.skip('skip')
    else:
        tid = idmarker.args[0]
        logging.info(tid)

        if tid not in ids:
            pytest.skip('skip')

