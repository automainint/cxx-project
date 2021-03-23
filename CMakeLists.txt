cmake_minimum_required(VERSION 3.18)

option(CODE_COVERAGE "Enable coverage reporting" OFF)

set(PROJECT_NAME cxx-project)
set(EXE_NAME cxx-project)
set(CFG_COVERAGE config-coverage)

project(${PROJECT_NAME} CXX)

find_package(Threads REQUIRED)

add_library(${CFG_COVERAGE} INTERFACE)

if(CODE_COVERAGE AND CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
  target_compile_options(${CFG_COVERAGE} INTERFACE -O0 -g --coverage)
  target_link_options(${CFG_COVERAGE} INTERFACE --coverage)
endif()

add_library(Sockets INTERFACE)

if(WIN32)
  target_compile_definitions(Sockets INTERFACE _CONSOLE UNICODE _UNICODE)
  target_link_libraries(Sockets INTERFACE ws2_32)
endif()

add_executable(${EXE_NAME})

add_subdirectory(source)

set_property(TARGET ${EXE_NAME} PROPERTY CXX_STANDARD 20)

if(MSVC)
  target_link_options(${EXE_NAME} PRIVATE "/SUBSYSTEM:CONSOLE")
endif()

target_link_libraries(
  ${EXE_NAME}
    ${CFG_COVERAGE} Threads::Threads gtest benchmark
)

target_link_directories(
  ${EXE_NAME}
    PUBLIC lib
)

target_include_directories(
  ${EXE_NAME}
    PUBLIC include
)

enable_testing()

add_test(
  NAME unittests
  COMMAND ${EXE_NAME}
)
