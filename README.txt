pytest directory/filename.py -v -s chromium --headed

pytest testcases/automated_cases/compute_suite/test_tejas_compute.py --junitxml=report.xml
pytest --browser=chromium testcases/automated_cases/compute_suite/test_vistaar_autoscale.py --junitxml=report.xml
pytest --browser=firefox testcases/automated_cases/compute_suite/test_vistaar_autoscale.py --junitxml=report.xml
pytest --browser=firefox testcases/automated_cases/compute_suite/test_tejas_compute.py --html=report01.html


Test Case Identifiers:
Include unique identifiers or references in the test case names.
This could be ticket numbers, user story IDs, or any other relevant identifiers.

