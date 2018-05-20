## Role Name

This is the alpha version of a role designed to install Nextcloud 13 on a
LAMP server.

## Requirements

This role expects to be run on a LAMP server with Apache, Mysql, and PHP
pre-installed. If configured, the role will attempt to verify that
Nextcloud's PHP and Apache requirements are satisfied before proceeding
with the installation. See **Role Variables** below.

## Role Variables

| Variable Name | Default Value | Usage |
|---------------|---------------|-------|
| `nextcloud_min_ram` (vars) | `512` | Minimum amount of server RAM (in megabytes). |
| `nextcloud_min_apache_version` (vars) | `2.4` | Minmimum Apache version. |
| `nextcloud_min_php_version` (vars) | `7.1` | Minimum PHP version. Note: [Both php5.6 and php7.0 will reach EOL in 2018](http://php.net/supported-versions.php). |
| `nextcloud_trusted_domains` | `['localhost']` | Defines [`trusted_domains` in `config.php`](https://docs.nextcloud.com/server/13/admin_manual/installation/installation_wizard.html#trusted-domains-label). Should include at least the site's domain name. |
| `nextcloud_required_apache_modules` | `['rewrite']` | Defines the set of [required Apache modules](https://docs.nextcloud.com/server/13/admin_manual/installation/source_installation.html#additional-apache-configurations) that the role should install. |
| `nextcloud_recommended_apache_modules` | `['headers', 'env', 'dir', 'mime', 'ssl']` | Defines a set of [recommended Apache modules](https://docs.nextcloud.com/server/13/admin_manual/installation/source_installation.html#additional-apache-configurations) for the role to install. |
| `nextcloud_apache_user` | `www-data` | Defines the [webserver user that should own the Nextcloud directories](https://docs.nextcloud.com/server/13/admin_manual/installation/source_installation.html#installation-wizard). |
| `nextcloud_required_php_modules` | `['gd', 'json', 'mbstring', 'xml', 'zip']` | Defines the set of [required php modules](https://docs.nextcloud.com/server/13/admin_manual/installation/source_installation.html#prerequisites-for-manual-installation) that the role should install. |
| `nextcloud_recommended_php_modules` | `['curl', 'bz2', 'intl']` | Defines the set of [recommended php modules](https://docs.nextcloud.com/server/13/admin_manual/installation/source_installation.html#prerequisites-for-manual-installation) that the role should install. |
| `nextcloud_verify_requirements` | `true` | Determines whether the role will attempt to verify the server requirments. |
| `nextcloud_db_type` | `mysql` | The database server used. Currently only supports `mysql`. |
| `nextcloud_db_name` | `nextcloud` | The name for the Nextcloud database. The role will ensure this database's existence. |
| `nextcloud_db_user` | `nextcloud` | The user Nextcloud will use to connect to the database. The role will ensure this user's existence. |
| `nextcloud_db_host` | `-` | The database host for the Nextcloud database. Optional. |
| `nextcloud_db_port` | `-` | The database port for the Nextcloud database. Optional. |
| `nextcloud_db_table_prefix` | `-` | The database table prefix for the Nextcloud database. Optional. |
| `nextcloud_db_table_space` | `-` | The database table space for the Nextcloud database. Optional. |
| `nextcloud_db_pass` | `-` | The password for the Nextcloud database. Required. |
| `nextcloud_db_pass_encrypted` | `false` | Indicate whether the 'password' field is a `mysql_native_password` hash. |
| `nextcloud_configure_database` | `true` | Determines whether or not the role will attempt to ensure that the database and database user exists. If `true` requires that `nextcloud_db_root_user` and `nextcloud_db_root_password` are set. |
| `nextcloud_db_root_user` | `root` | The Mysql root username. Required if `nextcloud_configure_database` is set. |
| `nextcloud_db_root_pass` | `-` | The Mysql root password. Required if `nextcloud_configure_database` is set.|
| `nextcloud_git_force` | `false` | Whether or not to overwrite the Nextcloud codebase on subsequent playbook runs. |
| `nextcloud_git_repo` | `https://github.com/nextcloud/server.git` | The git repository to install Nextcloud from. Required. |
| `nextcloud_git_dest` | `-` | The directory to clone the Nextcloud codebase to. Required. |
| `nextcloud_git_update` | `false` | Whether or not to update Nextcloud codebase on subsequent playbook runs. |
| `nextcloud_git_repo_version` | `v13.0.0` | The version of Nextcloud to clone on the initial playbook run. |
| `nextcloud_admin_user` | `-` | The name of the Nextcloud admin user to create on the initial playbook run. |
| `nextcloud_admin_pass` | `-` | The name of the Nextcloud admin password to create on the initial playbook run. |
| `nextcloud_data_dir` | `{{ nextcloud_git_dest }}/data` | Where Nextcloud's data directory should reside. |
| `nextcloud_install_command` | `php occ maintenance:install --database "{{ nextcloud_db_type }}" --database-name "{{ nextcloud_db_name }}" --database-user "{{ nextcloud_db_user }}" --database-pass "{{ nextcloud_db_pass }}" --admin-user "{{ nextcloud_admin_user }}" --admin-pass "{{ nextcloud_admin_pass }}" --data-dir "{{ nextcloud_data_dir }}"` | The command used to install Nextcloud on the initial playbook run. |
| `nextcloud_config_commands` | `[]` | An array of nextcloud commands to run. Each one will execute on every playbook run. |

## Example Playbook

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      vars:
        nextcloud_db_name: "nextcloud_db"
        nextcloud_db_user: "nextcloud_user"
        nextcloud_db_pass: "lud2Orvyu)dy"
        nextcloud_db_root_password: "ot8OlbagMey&"
        nextcloud_git_destination: "/var/www/example.com/web"
        nextcloud_trusted_domains:
          - "localhost"
          - "example.com"
        nextcloud_config_commands:
          - "app:enable encryption"
          - "encryption:enable"
          - "encryption:encrypt-all"
          - "app:enable"
      roles:
         - ansible-role-nextcloud

## License

GPLv2

## Author Information

Christopher Torgalson
