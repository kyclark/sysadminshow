#!/usr/bin/env python3
"""tests for days.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './head.py'
sonnet = '../inputs/sonnet-29.txt'
bustle = '../inputs/the-bustle.txt'
gettysburg = '../inputs/gettysburg.txt'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    rv, out = getstatusoutput(f'{prg} -h')
    assert rv == 0
    assert out.lower().startswith('usage')
    assert False


# --------------------------------------------------
def test_bad_file():
    """Bad file"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_bad_num():
    """Bad num"""

    for bad in random.sample(range(-10, 1), 3):
        rv, out = getstatusoutput(f'{prg} -n {bad} {sonnet}')
        assert rv != 0
        assert re.search(f'--num "{bad}" must be > 0', out)


# --------------------------------------------------
def test_default():
    """Default --num"""

    print(f'{prg} {sonnet}')
    rv, out = getstatusoutput(f'{prg} {sonnet}')
    assert rv == 0
    assert len(out.splitlines()) == 10
    expected = f"""
Sonnet 29
William Shakespeare

When, in disgrace with fortune and men’s eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,
Wishing me like to one more rich in hope,
Featured like him, like him with friends possessed,
Desiring this man’s art and that man’s scope,
    """.strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_n():
    """Test values of -n"""

    for _ in range(10):
        file = random.choice([sonnet, gettysburg, bustle])
        num = random.randint(1, 10)
        rv, out = getstatusoutput(f'{prg} -n {num} {file}')
        assert rv == 0
        expected = ''.join(open(file).readlines()[:num])
        assert out.rstrip() == expected.rstrip()


# --------------------------------------------------
def test_multiple_files():
    """Test more than one file"""

    rv, out = getstatusoutput(f'{prg} -n 2 {sonnet} {gettysburg}')
    assert rv == 0
    expected = '\n'.join([
        '==> ../inputs/sonnet-29.txt <==',
        'Sonnet 29',
        'William Shakespeare',
        '',
        '==> ../inputs/gettysburg.txt <==',
        'Four score and seven years ago our fathers brought forth on this',
        'continent, a new nation, conceived in Liberty, and dedicated to the',
    ])

    assert out.rstrip() == expected

# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
