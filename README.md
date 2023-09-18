# home-lab-setup
![ansible-logo](https://upload.wikimedia.org/wikipedia/commons/0/05/Ansible_Logo.png)
## Description
Ansible scripts for configuring home servers taking into account the specifics of the Raspberry platform.
## Supported playbooks
* Upgrade os
* Install apps
* Install node exporter
## Instructions
### Configure environments
```ShellSession
python -m venv env
source env/bin/activate
pip instal -r requirements.txt
```
### Usage
```ShellSession
ansible-playbook <playbook>.yml -i inventories/home-lab/hosts
```
