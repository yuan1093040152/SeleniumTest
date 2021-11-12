#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/8 16:54
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

from unittest import TestCase
from unittest.case import _Outcome

import time


class TestCase_(TestCase):
    # 是否开启失败重跑
    FAILURE_REPEAT_RUN_FLAG = True
    # 失败重跑尝试次数
    FAILURE_REPEAT_RUN_NUM = 2
    # 设置重跑时间间隔
    REPEAT_TIME_INTERVAL = 5
    # 新增全局通用名称
    name = u'analysis' + str(int(time.time()))

    def run(self, result=None):
        run_count = 1
        orig_result = result
        if result is None:
            result = self.defaultTestResult()
            startTestRun = getattr(result, 'startTestRun', None)
            if startTestRun is not None:
                startTestRun()

        result.startTest(self)

        testMethod = getattr(self, self._testMethodName)
        if (getattr(self.__class__, "__unittest_skip__", False) or
                getattr(testMethod, "__unittest_skip__", False)):
            # If the class or method was skipped.
            try:
                skip_why = (getattr(self.__class__, '__unittest_skip_why__', '')
                            or getattr(testMethod, '__unittest_skip_why__', ''))
                self._addSkip(result, self, skip_why)
            finally:
                result.stopTest(self)
            return
        expecting_failure_method = getattr(testMethod,
                                           "__unittest_expecting_failure__", False)
        expecting_failure_class = getattr(self,
                                          "__unittest_expecting_failure__", False)
        expecting_failure = expecting_failure_class or expecting_failure_method
        outcome = _Outcome(result)
        try:
            self._outcome = outcome
            while True:
                with outcome.testPartExecutor(self):
                    self.setUp()
                if outcome.success:
                    outcome.expecting_failure = expecting_failure
                    with outcome.testPartExecutor(self, isTest=True):
                        testMethod()
                    outcome.expecting_failure = False
                    with outcome.testPartExecutor(self):
                        self.tearDown()
                self.doCleanups()

                for test, reason in outcome.skipped:
                    self._addSkip(result, test, reason)
                self._feedErrorsToResult(result, outcome.errors)

                if outcome.success:  # 成功为True case 失败 为 false
                    if expecting_failure:
                        if outcome.expectedFailure:
                            self._addExpectedFailure(result, outcome.expectedFailure)
                        else:
                            self._addUnexpectedSuccess(result)
                    else:
                        result.addSuccess(self)
                # =======================重跑===================
                if not self.FAILURE_REPEAT_RUN_FLAG:
                    return result
                if run_count < self.FAILURE_REPEAT_RUN_NUM and outcome.success is False:
                    try:
                        result.current_failed = False  # 这次的测试结果有错误，把他设置为没有错误
                        outcome = _Outcome(result)  # 然后重新赋值
                    except Exception as e:
                        print(e)
                        pass
                    run_count += 1
                    time.sleep(self.REPEAT_TIME_INTERVAL)
                    continue
                # ==============================================
                return result

        finally:
            result.stopTest(self)
            if orig_result is None:
                stopTestRun = getattr(result, 'stopTestRun', None)
                if stopTestRun is not None:
                    stopTestRun()

            # explicitly break reference cycles:
            # outcome.errors -> frame -> outcome -> outcome.errors
            # outcome.expectedFailure -> frame -> outcome -> outcome.expectedFailure
            outcome.errors.clear()
            outcome.expectedFailure = None

            # clear the outcome, no more needed
            self._outcome = None
