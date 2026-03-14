# Uses 1 worker with 8 threads for concurrency, and disables Gunicorn's 
# internal timeout (0) to prevent 'Death Spiral' restarts on Cloud Run.
web: gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app