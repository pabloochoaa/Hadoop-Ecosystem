hadoop jar /home/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-files mapper.py,reducer.py \
-mapper mapper.py \
-reducer reducer.py \
-input /user/pao00050/wordcount/coffee.txt \
-output /user/pao00050/wordcount/results
