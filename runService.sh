#! /bin/sh
echo 'start'
python /home/jenkins/workspace/melvin0119-1@2/MyServer.py 8091 &
echo 'end'

echo 'part2'
python MyTest.py