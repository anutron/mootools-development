#!/bin/bash
if [ $# -lt 1 ]; then
  echo "Choose an option: (i)nstall, (d)ependency check, (r)un server on port 9876, (s)ync libraries"
  read option
else
  option=$1
fi
case $option in
    [i]* ) 
        cd lib
        crepo sync
        cd mootools-runner;
        git submodule update --init;
        cd test-runner;
        ln -s ../../runner_settings.py ./settings.py;
        virtualenv env;
        cd ../depender/django;
        ../../test-runner/env/bin/python setup.py develop;
        cd ../../test-runner;
        env/bin/python setup.py develop;;
    [d]* )
        cd lib/test-runner;
        env/bin/python manage.py depender_check;;
    [r]* )
        cd lib/test-runner;
        env/bin/python manage.py runserver_plus 0.0.0.0:9876;;
    [s]* )
        cd lib;
        crepo sync;;
    * ) echo "Please choose from i, d, r, or s.";;
esac
