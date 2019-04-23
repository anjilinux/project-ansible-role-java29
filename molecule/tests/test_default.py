import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_etc_profile_d_java_sh(host):
    f = host.file('/etc/profile.d/java-openjdk.sh')
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains('JAVA_HOME')


def test_opt_java(host):
    f = host.file('/opt/java/bin/java')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
