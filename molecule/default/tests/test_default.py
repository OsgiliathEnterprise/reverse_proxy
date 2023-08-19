"""Role testing files using testinfra."""


def test_docker_is_installed(host):
    with host.sudo():
        command = """systemctl status docker.service | \
        grep -c 'active (running)'"""
        cmd = host.run(command)
    assert '1' in cmd.stdout


def test_nginx_proxy_is_installed(host):
    with host.sudo():
        command = """docker ps | \
        grep -c nginx-proxy"""
        cmd = host.run(command)
    assert '1' in cmd.stdout


def test_nginx_proxy_port_is_opened(host):
    with host.sudo():
        command = """docker ps | \
        grep -c '80/tcp'"""
        cmd = host.run(command)
    assert '1' in cmd.stdout


def test_socat_container_for_group_ip_is_present(host):
    with host.sudo():
        command = """
            docker container inspect groupip.osgiliath.test | \
            grep -c 'VIRTUAL_HOST=groupip.osgiliath.test'
        """
        cmd = host.run(command)
    assert '1' in cmd.stdout


def test_socat_container_for_external_vm_is_present(host):
    with host.sudo():
        command = """
            docker container inspect externalvm.osgiliath.net | \
            grep -c 'VIRTUAL_HOST=externalvm.osgiliath.net'
        """
        cmd = host.run(command)
    assert '1' in cmd.stdout


def test_additional_volume_is_mounted_in_nginx_proxy(host):
    with host.sudo():
        command = """
            docker container inspect nginx-proxy | \
            grep -c '\"Source\": \"/etc/ipa\"'
        """
        cmd = host.run(command)
    assert '1' in cmd.stdout


def test_nginx_proxy_vhost_files_are_present(host):
    with host.sudo():
        command = """
            ls /usr/share/dockerdata/nginx/vhost.d | \
            grep -c 'externalvm.osgiliath.net_location'
        """
        cmd = host.run(command)
    assert '1' in cmd.stdout


def test_nginx_proxy_vhost_files_contains_target(host):
    with host.sudo():
        command = """
            cd /usr/share/dockerdata/nginx/vhost.d
            cat externalvm.osgiliath.net_location \
            | grep -c 'idm.internal.osgiliath.net'
            """
        cmd = host.run(command)
    assert '3' in cmd.stdout


def test_docker_interface_is_configured_in_firewalld(host):
    command = """
        sudo firewall-cmd --list-all --zone=public | \
        grep -c 'docker0'
    """
    cmd = host.run(command)
    assert '1' in cmd.stdout
