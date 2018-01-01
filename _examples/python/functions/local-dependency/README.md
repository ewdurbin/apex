The build hook can be used to install required libraries using pip. This is a refinement of the earlier example and includes an example of using a library that exists in a path relative to our function.

We can install these libraries in a subdirectory which become part of the zip files, and ensure they are added to the python path with a `.pth` file placed in the root of the zip.

The requirements are mentioned in the requirements.txt and the build hook is used to install the dependencies before the build

```
"hooks":{
    "build": "PYTHONDONTWRITEBYTECODE=1 python -m pip install -r requirements.txt -t .deps",
    "clean": "rm -rf .deps"
  }
```

Note, `PYTHONDONTWRITEBYTECODE` keeps us from needlessly writing `.pyc` and `__pycache__` files to the local disk.
