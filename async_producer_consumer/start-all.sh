./run-redis.sh && celery worker -A server.celery --loglevel=info && python3 server.py
