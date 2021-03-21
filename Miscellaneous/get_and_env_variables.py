import os

# list all env variables

print(os.environ)

# read single env variable

print(os.environ.get("SOME_ENV"))

some_env = os.environ.get("SOME_ENV")

if some_env:
    os.environ.setdefault("SOME_ENV", "default")

# read and set default variable

os.environ.setdefault("SOME_ENV", "default")