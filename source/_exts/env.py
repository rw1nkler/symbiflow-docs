import sys
import shutil
import subprocess

MAIN_SEPARATOR    = "==============================================================================="
SECTION_SEPARATOR = "-------------------------------------------------------------------------------"


# -- utilities ---------------------------------------------------------------

def _print_title(title):
    echo_cmd = "echo ' {}:'".format(title)
    subprocess.check_call(echo_cmd, shell=True, stdout=sys.stdout, stderr=sys.stderr)


def _print_section_separator(title=None):
    echo_cmd = "echo '{}'".format(SECTION_SEPARATOR)
    subprocess.check_call(echo_cmd, shell=True, stdout=sys.stdout, stderr=sys.stderr)
    if title is not None:
        _print_title(title)


def _print_main_separator(title=None):
    echo_cmd = "echo '{}'".format(MAIN_SEPARATOR)
    subprocess.check_call(echo_cmd, shell=True, stdout=sys.stdout, stderr=sys.stderr)
    if title is not None:
        _print_title(title)


def echo(cmd):
    echo_cmd = "echo '{}'".format(cmd)
    subprocess.check_call(echo_cmd, shell=True, stdout=sys.stdout, stderr=sys.stderr)


def run(cmd):
    echo("COMMAND: {}".format(cmd))
    subprocess.check_call(cmd, shell=True, stdout=sys.stdout, stderr=sys.stderr)

# -- print env ----------------------------------------------------------------


def print_conda():
    _print_main_separator("CONDA")
    if shutil.which("conda"):
        _print_section_separator()
        run("which conda")
        _print_section_separator()
        run("conda --version")
        _print_section_separator()
        run("conda info")
        _print_section_separator()
        run("conda list")
    else:
        echo("INFO: conda not found!")


def print_python3():
    _print_main_separator("PYTHON3")
    if shutil.which("python3"):
        _print_section_separator()
        run("which python3")
        _print_section_separator()
        run("python3 --version")
    else:
        echo("INFO: python3 not found!")


def print_python():
    _print_main_separator("PYTHON")
    if shutil.which("python"):
        _print_section_separator()
        run("which python")
        _print_section_separator()
        run("python --version")
    else:
        echo("INFO: python not found!")


def print_pip3():
    _print_main_separator("PIP3")
    if shutil.which("pip3"):
        _print_section_separator()
        run("which pip3")
        _print_section_separator()
        run("pip3 --version")
        _print_section_separator()
        run("pip3 list")
    else:
        echo("INFO: pip3 not found!")


def print_pip():
    _print_main_separator("PIP")
    if shutil.which("pip"):
        _print_section_separator()
        run("which pip")
        _print_section_separator()
        run("pip --version")
        _print_section_separator()
        run("pip list")
    else:
        echo("INFO: python not found!")


def setup(app):

    print_conda()
    print_python3()
    print_python()
    print_pip3()
    print_pip()

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
