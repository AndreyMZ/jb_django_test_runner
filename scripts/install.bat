set PYCHARM_INSTALL_DIR=%~1
patch --forward "%PYCHARM_INSTALL_DIR%\plugins\python-ce\helpers\pycharm\_jb_unittest_runner.py" _jb_unittest_runner.py.patch --batch --dry-run || exit /B
patch --forward "%PYCHARM_INSTALL_DIR%\plugins\python-ce\helpers\pycharm\_jb_unittest_runner.py" _jb_unittest_runner.py.patch --batch --backup
copy _jb_django_test_runner.py "%PYCHARM_INSTALL_DIR%\plugins\python-ce\helpers\pycharm\_jb_django_test_runner.py" /Y
