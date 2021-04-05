cmake_minimum_required(VERSION 3.18)

cmake_policy(SET CMP0077 NEW)
cmake_policy(SET CMP0091 NEW)

# Allow to set up the options for
# the dependencies.
set(CMAKE_POLICY_DEFAULT_CMP0077 NEW)

# Allow to specify the MSVC runtime
# library for the dependencies.
set(CMAKE_POLICY_DEFAULT_CMP0091 NEW)

option(CXXP_ENABLE_EXE      "Enable executable"         ON)
option(CXXP_ENABLE_TESTING  "Enable testing"            OFF)
option(CXXP_ENABLE_COVERAGE "Enable coverage reporting" OFF)

set(CXXP_PROJECT    cxx-project)
set(CXXP_EXE        cxx-project)
set(CXXP_CONFIG     cxx-project-config)
set(CXXP_UNITTESTS  cxx-project-unittests)

project(
  ${CXXP_PROJECT}
    VERSION 0.0.1
    DESCRIPTION "C++ project template."
    LANGUAGES CXX
)

include(cmake/fetch-deps.cmake)

if(CXXP_ENABLE_EXE)
  include(cmake/config.cmake)

  add_executable(${CXXP_EXE})
  add_subdirectory(source)

  target_compile_features(${CXXP_EXE} PRIVATE cxx_std_20)

  if(MSVC)
    target_link_options(${CXXP_EXE} PRIVATE "/SUBSYSTEM:CONSOLE")
  endif()

  target_link_libraries(
    ${CXXP_EXE}
      ${CXXP_CONFIG} gtest
  )

  if(CXXP_ENABLE_TESTING OR CXXP_ENABLE_COVERAGE)
    enable_testing()

    add_test(
      NAME ${CXXP_UNITTESTS}
      COMMAND ${CXXP_EXE}
    )
  endif()
endif()

include(GNUInstallDirs)
