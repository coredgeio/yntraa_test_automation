import re
import os

def parse_pytest_output(output):
    results = {
        'passed': 0,
        'failed': 0,
        'skipped': 0,
    }

    passed = re.search(r"(\d+) passed", output)
    if passed:
        results['passed'] = int(passed.group(1))

    failed = re.search(r"(\d+) failed", output)
    if failed:
        results['failed'] = int(failed.group(1))

    skipped = re.search(r"(\d+) skipped", output)
    if skipped:
        results['skipped'] = int(skipped.group(1))

    errors = re.search(r"(\d+) errors", output)
    if errors:
        results['errors'] = int(errors.group(1))

    return results
#
# current_directory = os.path.dirname(os.path.abspath(__file__))
# pytest_output_path = os.path.join(current_directory, "..", "..", "pytest_output.txt")
pytest_output_path = "pytest_output.txt"
with open(pytest_output_path, "r") as file:
    pytest_output = file.read()

results = parse_pytest_output(pytest_output)
print(results)
