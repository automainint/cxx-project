# cxx-project

[![linux][linux-badge]][linux-link]
[![codecov][codecov-badge]][codecov-link]

C++ project template.

##  How to build
CMake is required to build the project.

### With provided build script
- Execute `build.py`.

```shell
python3 build.py
```

Done!

### With CMake
```shell
cmake -D CMAKE_BUILD_TYPE=Release -B build -S .
cmake --build build --config Release
```  

### By hand
- Use `tools/build-deps.py` to build the dependencies.

```shell
cd tools
python3 build-deps.py
cd ..
```

Add `source` to the project and build manually. Required headers will be in `include` folder, libraries will be in `lib` folder.

[linux-badge]:    https://github.com/automainint/cxx-project/workflows/linux/badge.svg
[linux-link]:     https://github.com/automainint/cxx-project/actions?query=workflow%3Alinux
[codecov-badge]:  https://codecov.io/gh/automainint/cxx-project/branch/feature-codecov/graph/badge.svg
[codecov-link]:   https://codecov.io/gh/automainint/cxx-project
