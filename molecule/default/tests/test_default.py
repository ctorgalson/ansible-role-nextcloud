import os
import testinfra.utils.ansible_runner
import pytest
from distutils.version import LooseVersion

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name", [
    "dir",
    "env",
    "headers",
    "mime",
    "rewrite",
    "ssl",
])
def test_required_apache_modules(host, name):
    mods = host.run("apache2ctl -M")

    assert name in mods.stdout


@pytest.mark.parametrize("name", [
    "ctype",
    "dom",
    "gd",
    "iconv",
    "json",
    "libxml",
    "mbstring",
    "mysqli",
    "pdo_mysql",
    "posix",
    "xmlreader",
    "xmlwriter",
    "xml",
    "zip",
    "zlib",
])
def test_required_php_modules(host, name):
    mods = host.run("php -m")

    assert name in mods.stdout


def test_php_mcrypt_module(host):
    mods = host.run("php -m")
    version = host.run("php -v")

    if LooseVersion(version.stdout) < LooseVersion("7.2"):
        assert "mcrypt" in mods.stdout
    else:
        assert "mcrypt" not in mods.stdout


def test_mysql_user(host):
    mysqllogin = host.run("mysql -unextcloud -pnextcloud -e'quit' 2>/dev/null")

    assert mysqllogin.rc == 0
