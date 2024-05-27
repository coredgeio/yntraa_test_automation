#
# import re
# import os
#
# def parse_pytest_output(output):
#     results = {
#         'passed': 0,
#         'failed': 0,
#         'skipped': 0,
#     }
#
#     passed = re.search(r"(\d+) passed", output)
#     if passed:
#         results['passed'] = int(passed.group(1))
#
#     failed = re.search(r"(\d+) failed", output)
#     if failed:
#         results['failed'] = int(failed.group(1))
#
#     skipped = re.search(r"(\d+) skipped", output)
#     if skipped:
#         results['skipped'] = int(skipped.group(1))
#
#     errors = re.search(r"(\d+) errors", output)
#     if errors:
#         results['errors'] = int(errors.group(1))
#
#     return results
# #
# # current_directory = os.path.dirname(os.path.abspath(__file__))
# # pytest_output_path = os.path.join(current_directory, "..", "..", "pytest_output.txt")
# pytest_output_path = "report.xml"
# with open(pytest_output_path, "r") as file:
#     pytest_output = file.read()
#
# results = parse_pytest_output(pytest_output)
# print(results)

#pytest --browser=chromium smoke_testing/sanity_for_different_function.py --junitxml=report.xml


import xml.etree.ElementTree as ET

def parse_pytest_output(xml_string):
    root = ET.fromstring(xml_string)

    results = {
        'passed': 0,
        'failed': 0,
        'skipped': 0,
        'errors': 0
    }

    for testcase in root.findall('.//testcase'):
        if testcase.find('failure') is not None:
            results['failed'] += 1
        elif testcase.find('error') is not None:
            results['errors'] += 1
        else:
            results['passed'] += 1

    return results

pytest_output_path = "report.xml"
with open(pytest_output_path, "r") as file:
    pytest_output = file.read()

results = parse_pytest_output(pytest_output)
print(results)
