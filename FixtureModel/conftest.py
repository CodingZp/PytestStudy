# import pytest
#
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     print(f"\nstart {rep.when}")
#     if rep.when == "call":
#         # 使用 item（即 request.node）来保存结果
#         item.test_outcome = rep.outcome
#
#
# @pytest.fixture(scope='class')
# def sub_my_fixture(request):
#     print("\nSetting up sub_fixture...")
#     yield
#
#     if hasattr(request.node, "test_outcome"):
#         if request.node.test_outcome == "failed":
#             print("\nTest failed, skipping sub teardown!")
#             return
#
#     print("\nTest passed, executing sub teardown...")
#
# conftest.py 或 test_module.py
import pytest


@pytest.fixture(scope="session")
def session_fixture():
    print("\n[session] setup")
    yield "session_data"
    print("[session] teardown")


@pytest.fixture(scope="module")
def module_fixture():
    print("\n[module] setup")
    yield "module_data"
    print("[module] teardown")


@pytest.fixture(scope="class")
def class_fixture():
    print("\n[class] setup")
    yield "class_data"
    print("[class] teardown")


@pytest.fixture(scope="function")
def function_fixture():
    print("\n[function] setup")
    yield "function_data"
    print("[function] teardown")
