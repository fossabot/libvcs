# -*- coding: utf-8 -*-
"""Tests for libvcs svn repos."""
from __future__ import absolute_import, print_function, unicode_literals

import os

import pytest

from libvcs.shortcuts import create_repo_from_pip_url
from libvcs.util import run


@pytest.fixture
def svn_dummy_repo_dir(tmpdir_repoparent, scope='session'):
    """Create a git repo with 1 commit, used as a remote."""
    server_dirname = 'server_dir'
    server_dir = tmpdir_repoparent.join(server_dirname)

    run(['svnadmin', 'create', str(server_dir)])

    return str(server_dir)


def test_repo_svn(tmpdir, svn_dummy_repo_dir):
    repo_name = 'my_svn_project'

    svn_repo = create_repo_from_pip_url(**{
        'url': 'svn+file://' + svn_dummy_repo_dir,
        'parent_dir': str(tmpdir),
        'name': repo_name
    })

    svn_repo.obtain()
    svn_repo.update_repo()

    assert svn_repo.get_revision() == 0

    assert os.path.exists(str(tmpdir.join(repo_name)))
