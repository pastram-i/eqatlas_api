#TODO: Make this readme better

 - Docker build flags if needed (depending on deployment):
   - `--taget` ; build route in dockerfile
   - `--build-arg` ; environment variables
 - Docker run flags if needed (depending on deployment):
   - `-v` ; attach a volume
   - `-p` port forward
   - `-it` interactive
   - `--entrypoint=/bin.sh [name] -c [command]` shell'em

- To Run:
  - `uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload`