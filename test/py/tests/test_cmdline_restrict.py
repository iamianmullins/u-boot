# SPDX-License-Identifier: GPL-2.0

import pytest

@pytest.mark.buildconfigspec('cmdline_restrict')
@pytest.mark.parametrize('cmd', [
    'go',
    'booti',
    'bootz',
    'bootelf',
    'zboot',
    'pxe',
    'source',
    'spl',
    'saveenv',
    'editenv',
    'askenv',
])
def test_cmdline_restrict(ubman, cmd):
    """Test that commands disabled by CMDLINE_RESTRICT are not available."""

    with ubman.disable_check('unknown_command'):
        response = ubman.run_command(cmd)
    assert 'Unknown command' in response

@pytest.mark.buildconfigspec('cmdline_restrict')
def test_cmdline_restrict_env_import(ubman):
    """Test that 'env import' is unavailable with CMDLINE_RESTRICT."""

    response = ubman.run_command('env import')
    assert 'import' not in response
