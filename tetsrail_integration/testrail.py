
from tetsrail_integration.api_client import APIClient
import logging
from tetsrail_integration.const import (
    USER,
    PWD,
    URL,
    PROJECT_ID, CASE_TYPE_TO_ID)


class TestRailAgent():
    def __init__(self):
        logging.info("inside testrail agent constr")
        self.client = APIClient(URL)
        self.client.user = USER
        self.client.password = PWD

    def get_case(self, tid):
        logging.info("inside get_case")
        """ get test case by id
        """
        return self.client.send_get('get_case/%d' % int(tid))

    def get_run(self, rid):
        logging.info("inside get_run")
        """ get a test run by its id
        """
        return self.client.send_get('get_run/%d' % int(rid))

    def add_run(self, name, description='', milestone=None, assignedTo=None,
                include_all=False, case_ids=None):
        logging.info("inside add_run")
        """ add test run based on parameters
            milestone: int
            assignedTo: int
            case_ids: list
        """
        if not case_ids:
            case_ids = []

        data = {
            'name': name,
            'description': description,
            'milestone_id': milestone,
            'assignedto_id': assignedTo,
            'include_all': include_all,
            'case_ids': case_ids
        }
        resp =  self.client.send_post('add_run/%d' % PROJECT_ID, data)
        logging.info("add run resp -> ")
        logging.info(resp)
        return resp


    def get_tests(self, rid):
        logging.info("inside get_tests")
        """ get tests in a test run
        """
        return self.client.send_get('get_tests/%d' % int(rid))

    def get_case_types(self):
        logging.info("inside get_case_types")
        """ get available case type mapping
        """
        return self.client.send_get('get_case_types')

    def get_cases_by_type(self, test_type):
        logging.info("inside get_cases_by_type")
        """ get all cases for a certain type
        """
        assert test_type in CASE_TYPE_TO_ID
        return self.client.send_get('get_cases/%d&type_id=%d' %
                                    (PROJECT_ID, CASE_TYPE_TO_ID[test_type]))

    def add_results(self, rid, results):
        logging.info("inside add_results")
        return self.client.send_post('add_results/%d' % rid, results)

    # def delete_test_run(self,tr_id):
    #
    #     logging.info("inside delete_test_run")
    #
    #     return self.client.send_post(f'delete_run/{tr_id}',{})


if __name__ == '__main__':
    """ test TestRailAgent
    """
    agent = TestRailAgent()
