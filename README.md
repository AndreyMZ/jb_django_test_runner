# Run/debug Django unittests from the context menu in PyCharm Community Edition

This is for PyCharm **Community** Edition which does not have any Django integration. PyCharm **Professional** Edition supports [Django Test](https://www.jetbrains.com/help/pycharm/run-debug-configuration-django-test.html) out of the box.

## Supported PyCharm versions

Tested on:
- 2019.3.2

Not supported:
- ≤ 2019.2.3

## Instruction

1. Adjusting PyCharm internals:

    1.  Try to run test from the context menu. You will see somethin like:
    
            Testing started at 16:15 ...
            C:\Programs\Python38\python.exe "C:\Program Files (x86)\JetBrains\PyCharm Community Edition 2019.3.2\plugins\python-ce\helpers\pycharm\_jb_unittest_runner.py" --target example.tests.test_foo.FooTestCase.test_bar
            
        Note the path to `_jb_unittest_runner.py`.

    2.  Apply patch [`_jb_unittest_runner.py.patch`](_jb_unittest_runner.py.patch) to `YOUR_PYCHARM_INSTALL_DIR/plugins/python-ce/helpers/pycharm/_jb_unittest_runner.py`
    
    3.  Copy [`_jb_django_test_runner.py`](_jb_django_test_runner.py) to `YOUR_PYCHARM_INSTALL_DIR/plugins/python-ce/helpers/pycharm/_jb_django_test_runner.py`.
    
2. Edit the run/debug configuration template:

    1. Go to the menu *Run* > *Edit Configurations...*
    2. Go to *Templates* > *Python tests* > *Unittests*
    3. Set the *Working directory* to the root path of your project (where `manage.py` file is located)
    4. In the *Environment variables* add a new one with *name* `DJANGO_TEST_MODE_GAINARIE` and any *value*

3. Remove all previously added run/debug configurations that inherit this template.
    
    When modifying a Template configuration, all previously added configurations that inherit it won't be updated, so they have to be manually removed. They will be automatically readded when tests run from the context menu.

## References

- <https://stackoverflow.com/questions/42989471/run-debug-a-django-applications-unittests-from-the-mouse-right-click-context>
- <https://pypi.org/project/teamcity-messages/#django>
