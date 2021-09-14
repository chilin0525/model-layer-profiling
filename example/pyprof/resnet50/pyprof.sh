nsys profile -f true -o net --export sqlite python3 pyprof_sample.py
python3 -m pyprof.parse net.sqlite > net.dict
python3 -m pyprof.prof --csv net.dict > pyprof
python3 pyprof_parser.py > pyprof_parsed