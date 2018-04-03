import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name", [
    "rewrite",
])
def test_apache_modules(host, name):
    mods = host.run("apache2ctl -M")

    assert name in mods.stdout
