# import os
# from collections import OrderedDict
#
# import pytest
#
# test_results = OrderedDict()
#
# def get_current_test():
#     """Just a helper function to extract the current test"""
#     print(os.environ.get('PYTEST_CURRENT_TEST'))
#     full_name = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]
#     test_file = full_name.split("::")[0].split('/')[-1].split('.py')[0]
#     test_name = full_name.split("::")[1]
#     return full_name, test_file, test_name
#
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """The actual wrapper that gets pytcalled before and after every test"""
#     print(call)
#     global test_results
#     outcome = yield
#     rep = outcome.get_result()
#
#     # only check the result of the test
#     if rep.when == "call":
#         full_name, test_file, test_name = get_current_test()
#         test_name_msg = f"{test_name}_msg"
#         if rep.failed:
#             test_results[test_name] = "Failure"
#             # return the last error msg either by pytest.fail or from any exception raised
#             test_results[test_name_msg] = f"{call.excinfo.typename} - {call.excinfo.value}"
#         else:
#             test_results[test_name] = "Success"
#             test_results[test_name_msg] = ''
#
# def pytest_unconfigure(config):
#     """Called when pytest is about to end. Can be used to print the result dict or
#     to pipe the data into a file"""
#     print(test_results)