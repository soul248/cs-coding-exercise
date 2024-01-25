# !/bin/bash
docker build -t fake_sql_creator:latest .
docker run -v $(pwd):/script fake_sql_creator:latest