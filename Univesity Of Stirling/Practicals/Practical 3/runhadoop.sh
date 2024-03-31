hadoop jar /home/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-files mapper.py,combiner.py,reducer.py,excluded.txt \
-mapper mapper.py \
-combiner combiner.py \
-reducer reducer.py \
-input /user/tst/wordcount/coffee.txt \
-output /user/tst/wordcount/results