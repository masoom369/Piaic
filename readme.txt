docker build -t lesson_1 .
docker run -it lesson_1 /bin/bash
docker build -t lesson_2 .
docker run -d -p 8888:8888 lesson_2