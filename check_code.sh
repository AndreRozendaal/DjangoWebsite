echo "### check config file django" 
python manage.py check --deploy

echo "### pylint"
pylint  --load-plugins=pylint_django --disable=missing-docstring,unused-import  */*.py

