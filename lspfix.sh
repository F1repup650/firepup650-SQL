unzip pylsp.sh -d venv/lib/python3.8/site-packages
sed -i 6d .config/pip/pip.conf
pip install ujson docstring_to_markdown jedi
mv pylsp venv/bin