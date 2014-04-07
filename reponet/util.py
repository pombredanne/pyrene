import os
import sys
import subprocess
import contextlib


@contextlib.contextmanager
def set_env(key, value):
    exists = key in os.environ
    original_value = os.environ.get(key, '')
    os.environ[key] = value
    yield
    os.environ[key] = original_value
    if not exists:
        del os.environ[key]


def pip_install(*args):
    '''
    Run pip install ...

    Explicitly ignores user's config.
    '''
    pip_cmd = os.path.join(os.path.dirname(sys.executable), 'pip')
    with set_env('PIP_CONFIG_FILE', os.devnull):
        cmd = [pip_cmd, 'install'] + list(args)
        print(' '.join(cmd))
        subprocess.call(cmd)


def write_file(path, content):
    try:
        os.makedirs(os.path.dirname(path))
    except OSError:
        pass
    with open(path, 'wb') as file:
        file.write(content)
