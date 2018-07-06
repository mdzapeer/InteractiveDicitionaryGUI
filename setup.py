from cx_Freeze import setup, Executable

base = None


executables = [Executable("DictionaryApp1.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Interactive Dict",
    options = options,
    version = "1",
    description = 'dictionary',
    executables = executables
)
