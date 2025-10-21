Ansible Reverse proxy
=========

* Galaxy: [![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.reverse_proxy-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/reverse_proxy)
* Lint & requirements: ![Molecule](https://github.com/OsgiliathEnterprise/reverse_proxy/workflows/Molecule/badge.svg)
* Tests: [![Build Status](https://app.travis-ci.com/OsgiliathEnterprise/reverse_proxy.svg?branch=master)](https://travis-ci.com/OsgiliathEnterprise/reverse_proxy)
* Chat: [![Join the chat at https://gitter.im/OsgiliathEnterprise/platform](https://badges.gitter.im/OsgiliathEnterprise/platform.svg)](https://gitter.im/OsgiliathEnterprise/platform?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Installs Docker and configures a reverse proxy


```
firewalld_zones:
  - name: public # optional
    nics: # optional, will take all the network interfaces of the machine by default
      - eth0 # optional
    virtual_hosts:
      - name: idm.osgiliath.net # Virual host
        upstream: "idm.internal.osgiliath.net" # upstream server to proxy
        referer_suffix: "/ipa/ui" # referer header suffix
        proto: https # upstream proto
        container: False # proxy container or real VM/bare metal
        gen_certs: True # use letsencrypt to generate frontend certificate
        volumes:
          - "/etc/ipa:/etc/ipa:ro" # additional volumes to mount in proxy
        additional_nginx_headers:
          - "proxy_ssl_trusted_certificate /etc/ipa/ca.crt" # Additional nginx headers
        ports_binding:
          - "80:80" # mandatory for letsencrypt
          - "443:443"
      - name: idm.osgiliath.test
        ports_binding:
          - "80:80" # mandatory for letsencrypt
          - "443:443"
        gen_certs: yes # lets encrypt will take care of certificates
```

Requirements
------------

Like any other platform role, executing `tox -e pipdep` and `tox -e dependency` 

Role Variables
--------------

Take a look at the [molecule tests](./molecule/default/converge.yml) tests and the [default variables](./defaults/main.yml)

Dependencies
------------

[Ansible Container (docker)](https://github.com/OsgiliathEnterprise/ansible-containerization)

License
-------

[Apache-2](https://www.apache.org/licenses/LICENSE-2.0)

Author Information
------------------

* Twitter [@tcharl](https://twitter.com/Tcharl)
* Github [@tcharl](https://github.com/Tcharl)
* LinkedIn [Charlie Mordant](https://www.linkedin.com/in/charlie-mordant-51796a97/)
