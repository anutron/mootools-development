#!/bin/bash
if [ $# -lt 1 ]; then
  echo "Choose an option: (i)nstall, (d)ependency check, (r)un server on port 9876, (l)ive - run the server on port 80 (s)ync libraries"
  read option
else
  option=$1
fi
case $option in
    [i]* ) 
        curl -O -k https://raw.github.com/pypa/virtualenv/master/virtualenv.py;
        python virtualenv.py env;
        rm virtualenv.*;
        rm setuptools*;
        env/bin/easy_install crepo;
        cd lib;
        ../env/bin/crepo sync;
        cd mootools-runner;
        git submodule update --init;
        cd ../dev-app;
        ln -s ../../settings.py;
        cd ../depender/django;
        ../../../env/bin/python setup.py develop;
        cd ../../dev-app;
        ../../env/bin/python setup.py develop;;
    [d]* )
        cd lib/dev-app;
        ../../env/bin/python manage.py depender_check;;
    [r]* )
        cd lib/dev-app;
        ../../env/bin/python manage.py runserver_plus 0.0.0.0:9876;;
    [l]* )
        cd lib/dev-app;
        ../../env/bin/python manage.py runserver 0.0.0.0:80;;
    [s]* )
        cd lib;
        ../env/bin/crepo sync;;
    * ) echo "Please choose from i, d, r, l, or s.";;
esac
