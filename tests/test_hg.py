# -*- coding: utf-8 -*-
"""Tests for libvcs hg repos."""
from __future__ import absolute_import, print_function, unicode_literals

import os

import pytest

from libvcs import exc
from libvcs.shortcuts import create_repo_from_pip_url
from libvcs.util import run, which

try:
    which('hg')
except exc.LibVCSException:
    pytestmark = pytest.mark.skip(reason="hg is not available")


@pytest.fixture
def hg_dummy_repo_dir(tmpdir_repoparent, scope='session'):
    """Create a git repo with 1 commit, used as a remote."""
    name = 'dummyrepo'
    repo_path = str(tmpdir_repoparent.join(name))

    run(['hg', 'init', name], cwd=str(tmpdir_repoparent))

    testfile_filename = 'testfile.test'

    run(['touch', testfile_filename],
        cwd=repo_path)
    run(['hg', 'add', testfile_filename],
        cwd=repo_path)
    run(['hg', 'commit', '-m', 'test file for %s' % name],
        cwd=repo_path)

    return repo_path


def test_repo_mercurial(tmpdir, tmpdir_repoparent, hg_dummy_repo_dir):
    repo_name = 'my_mercurial_project'

    mercurial_repo = create_repo_from_pip_url(**{
        'pip_url': 'hg+file://' + hg_dummy_repo_dir,
        'repo_dir': str(tmpdir_repoparent.join(repo_name)),
    })

    run(['hg', 'init', mercurial_repo.name],
        cwd=str(tmpdir))

    mercurial_repo.obtain()
    mercurial_repo.update_repo()

    test_repo_revision = run(
        ['hg', 'parents', '--template={rev}'],
        cwd=str(tmpdir_repoparent.join(repo_name)),
    )

    assert mercurial_repo.get_revision() == test_repo_revision
    assert os.path.exists(str(tmpdir.join(repo_name)))
