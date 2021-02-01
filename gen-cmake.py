#!  /usr/bin/python
#   gen-cmake.py
#
#       Generate CMakeLists.txt files.
#
#   Copyright (c) 2021 Mitya Selivanov
#
#   This file is part of the Template Project.
#
#   Template Project is distributed in the hope that it will be
#   useful, but WITHOUT ANY WARRANTY; without even the implied
#   warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#   PURPOSE. See the MIT License for more details.

import os
import glob

def get_subdirs(folder):
  dirs = list()
  for f in glob.glob(os.path.join(folder, '*', '')):
    dirs.append(os.path.basename(os.path.normpath(f)))
  return dirs

def get_files(folder, ext):
  files = list()
  for f in glob.glob(os.path.join(folder, ext)):
    files.append(os.path.basename(f))
  return files

def check_subdirs(folder):
  for r, d, f in os.walk(folder):
    for file in f:
      return True
  return False

def print_list(s, offset):
  buf = ''
  char_count = offset
  for i in range(char_count):
    buf += ' '
  for f in s:
    char_count += len(f) + 1
    if char_count >= 64:
      char_count = 0
    if char_count == 0:
      buf += '\n'
      for i in range(offset - 1):
        buf += ' '
      char_count = offset - 1
    buf += ' ' + f    
  return buf

def print_sources(folder):
  buf = ''
  srcs = get_files(folder, '*.cpp')
  hdrs = get_files(folder, '*.h')
  if len(srcs) > 0 or len(hdrs) > 0:
    buf += 'target_sources(\n  ${EXE_NAME}'
    if len(srcs) > 0:
      buf += '\n    PRIVATE\n' + print_list(srcs, 6)
    if len(hdrs) > 0:
      buf += '\n    PUBLIC\n' + print_list(hdrs, 6)
    buf += '\n)\n'
  return buf

def print_subdirs(folder):
  buf = ''
  dirs = get_subdirs(folder)
  for f in dirs:
    if check_subdirs(os.path.join(folder, f)):
      buf += 'add_subdirectory(' + f + ')\n'
  return buf

def write_subdirs(folder):
  if check_subdirs(folder):
    out = open(os.path.join(folder, 'CMakeLists.txt'), 'w')
    out.write(print_sources(folder))
    out.write(print_subdirs(folder))
    out.close()

    for dir in get_subdirs(folder):
      write_subdirs(os.path.join(folder, dir))

def clean_subdirs(folder):
  for r, d, f in os.walk(folder):
    for file in f:
      if file == 'CMakeLists.txt':
        os.remove(os.path.join(r, file))

out = open('CMakeLists.txt', 'w')

out.write('cmake_minimum_required(VERSION 3.18)\n\n')

out.write('set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ../bin)\n')
out.write('set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE ../bin)\n\n')
out.write('set(PROJECT_NAME template-project)\n')
out.write('set(EXE_NAME template-project)\n\n')

out.write('project(${PROJECT_NAME} CXX)\n\n')

out.write('find_package(Threads REQUIRED)\n\n')

out.write('add_executable(${EXE_NAME})\n\n')

out.write('set_property(\n')
out.write('  TARGET ${EXE_NAME}\n')
out.write('  PROPERTY MSVC_RUNTIME_LIBRARY "MultiThreaded"\n')
out.write(')\n\n')

out.write('add_subdirectory(source)\n\n')

clean_subdirs('source')
write_subdirs('source')

out.write('target_link_libraries(\n  ${EXE_NAME}\n')

deps = list();
libs = open('libs.txt', 'r')
for line in libs:
  deps.extend(line.split())
libs.close()

out.write(print_list(deps, 4))
out.write('\n)\n\n')

out.write('target_link_directories(\n  ${EXE_NAME}\n')
out.write('    PUBLIC lib\n')
out.write(')\n\n')

out.write('target_include_directories(\n  ${EXE_NAME}\n')
out.write('    PUBLIC include\n')
out.write(')\n')