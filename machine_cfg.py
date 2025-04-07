# This Python script contains all the machine dependent settings
# needed during the build process.

# Compilers to be used.

cc  = "cl.exe"
cxx = "cl.exe"
f77 = "ifx"

debug = False

link = "link.exe"
link_flags =  "-undefined dynamic_lookup -dynamic -stdlib=libc++ -o camfr/_camfr.so -stdlib=libc++"  #-dynamic -single_module -undefined dynamic_lookup"

if debug == True:
    link_flags += " /DEBUG"

# Compiler flags.
#
# Note: for the Fortran name definition you can define one of the following
#       preprocessor macros:
#
#           FORTRAN_SYMBOLS_WITHOUT_TRAILING_UNDERSCORES
#           FORTRAN_SYMBOLS_WITH_SINGLE_TRAILING_UNDERSCORE
#           FORTRAN_SYMBOLS_WITH_DOUBLE_TRAILING_UNDERSCORES

if debug == False:
    base_flags = "-DFORTRAN_SYMBOLS_WITH_SINGLE_TRAILING_UNDERSCORE -DNDEBUG \
                  /nologo /MD /GR /GX /W0"
    flags = base_flags + " /Ox"
else:
    base_flags = "-DFORTRAN_SYMBOLS_WITH_SINGLE_TRAILING_UNDERSCORE -DDEBUG \
                  /nologo /MD /GR /GX /W0 /Zi"
    flags = base_flags
    
flags_noopt = base_flags
fflags = flags

# Include directories.

include_dirs = ["C:/Users/emore/anaconda3/include",
                "C:/Users/emore/anaconda3/Lib/site-packages",
                "C:/vcpkg/packages/blitz_x64-windows/include/blitz",
                "C:/local/boost_1_87_0/boost"]

# Library directories.

library_dirs = ["C:/Users/emore/anaconda3/libs",
                "C:/vcpkg/packages/blitz_x64-windows/lib",
                "C:/vcpkg/packages/boost-python_x64-windows/lib",
                "C:/Program Files (x86)/Intel/oneAPI/compiler/2025.1/lib"]

# Library names.

libs = ["boost_python", "python25", "blitz", "fortran", "gcc", "g2c"]

# Command to strip library of excess symbols:

dllsuffix = ".pyd"
strip_command = "strip --strip-unneeded camfr/_camfr" + dllsuffix
strip_command = ""

# # all pil scripts and libs, something shorter once...?
# import os
# pilpath	    = "E:\\camfrcode/Pil1.1.6-py25/" 
# all_pil_files = os.listdir(pilpath)
# pillist     = []

# for n in all_pil_files: pillist.append(pilpath+ n)


# Extra files to copy into installation directory.
extra_files = [("doc", ["docs/camfr.pdf"])]
# extra_files = [(".",
#     ["e:\\lib/boost/boost_1_33_1/libs/python/build/bin-stage/boost_python.dll"]),
#     ("./.." , ["visualisation/pil.pth"]),
#     ("pil" , pillist )
#     ]
