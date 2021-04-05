#!/usr/bin/python3

import os, shutil

build_to = "build"
config = "Release"
msvc_runtime = "MultiThreaded"

os.chdir('..')

os.system(
    'cmake' +
    ' -D CMAKE_INSTALL_PREFIX=_tmp' +
    ' -D CMAKE_INSTALL_LIBDIR=../lib' +
    ' -D CMAKE_INSTALL_INCLUDEDIR=../include' +
    ' -D CMAKE_BUILD_TYPE=' + config +
    ' -D CMAKE_MSVC_RUNTIME_LIBRARY=' + msvc_runtime +
    ' -D CXXP_ENABLE_EXE=OFF' +
    ' -B ' + build_to + 
    ' -S .')

os.system(
    'cmake '
    ' --build ' + build_to +
    ' --config ' + config)

os.system(
    'cmake' +
    ' --install ' + build_to +
    ' --config ' + config)

if os.path.exists('_tmp'):
    shutil.rmtree('_tmp')

os.chdir('tools')
