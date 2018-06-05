# Author:zhang
# -*- coding:utf-8 -*-
import unittest
import os
import HTMLTestRunner
path = os.path.join(os.getcwd(), 'testbb')  # 当前路径且文件夹名为testbb
report_path=os.path.join(os.getcwd(),'report')



def all_case():
    discovery = unittest.defaultTestLoader.discover(start_dir=path, pattern="test*.py", top_level_dir=None)
    # for test_suit in discovery:
    #     for test_case in test_suit:
    #         testcase.addTests(test_case)
    #         testcase.addTests(discovery)
    print(discovery)
    return discovery


if __name__ == '__main__':
    report_abspath=os.path.join(report_path,'report.hmtl')
    fp = open(report_abspath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='My unit test',
            description='This demonstrates the report output by HTMLTestRunner.'
    )
    runner.run(all_case())
    fp.close()
