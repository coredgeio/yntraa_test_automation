pytest directory/filename.py -v -s chromium --headed

EXECUTION command-

XML  --report
pytest testcases/automated_cases/compute_suite/test_tejas_compute.py --junitxml=report.xml
pytest --browser=chromium testcases/automated_cases/storage_suite/test_ananta_store.py --html=report01.html
pytest --browser=firefox testcases/automated_cases/compute_suite/test_vistaar_autoscale.py --junitxml=report.xml
pytest --browser=firefox testcases/automated_cases/compute_suite/test_tejas_compute.py --html=report01.html


Test Case Identifiers:
Include unique identifiers or references in the test case names.
This could be ticket numbers, user story IDs, or any other relevant identifiers.

