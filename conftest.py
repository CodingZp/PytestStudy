import pytest


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#
#     if rep.when == "call":
#         item.test_outcome = rep.outcome


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # 将测试结果存储在 item 中，供 fixture 访问
    if report.when == "call":  # 仅存储测试主体的结果
        item.rep_call = report


@pytest.fixture(scope='class')
def my_fixture(request):
    # setup 逻辑
    print("\nSetting up fixture...")

    yield  # 测试用例执行在此处暂停

    # teardown 逻辑
    if hasattr(request.node, "test_outcome") and request.node.test_outcome == "failed":
        print("\nTest failed, skipping teardown!")
    else:
        print("\nTest passed, executing teardown...")
