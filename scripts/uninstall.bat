set PYCHARM_INSTALL_DIR=%~1
patch --reverse "%PYCHARM_INSTALL_DIR%\plugins\python-ce\helpers\pycharm\_jb_unittest_runner.py" _jb_unittest_runner.py.patch --batch --dry-run || exit /B
patch --reverse "%PYCHARM_INSTALL_DIR%\plugins\python-ce\helpers\pycharm\_jb_unittest_runner.py" _jb_unittest_runner.py.patch --batch
del "%PYCHARM_INSTALL_DIR%\plugins\python-ce\helpers\pycharm\_jb_django_test_runner.py" /Q
