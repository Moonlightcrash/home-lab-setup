import subprocess
import time

import paramiko

# TODO make a CLI program into a utility (use click or argparse)
# TODO add information about the utility and its use to the readme
user: str = "moonlight"
password: str = "1337"
port: int = 22
hostnames: list = ["raspberry-node-1.local", "raspberry-node-2.local"]


def enable_root_auth(user, password, port, hostname):
    with paramiko.SSHClient() as ssh_client:
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh_client.connect(hostname=hostname, port=port,
                           username=user, password=password)

        stdin, stdout, stderr = ssh_client.exec_command("sudo passwd")
        stdin.write(f"{password}\n")
        stdin.flush()
        stdin.write(f"{password}\n")
        stdin.flush()
        print("\nPassword exchange!")

        ssh_client.exec_command("sudo sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' "
                                "/etc/ssh/sshd_config")
        ssh_client.exec_command("sudo service sshd restart")
        print("\nRoot user activate!")


def add_pub_key(password, port, hostname):
    pub = subprocess.check_output("cat ~/.ssh/id_rsa.pub", shell=True).decode("utf-8")
    time.sleep(1)
    with paramiko.SSHClient() as ssh_client:
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh_client.connect(hostname=hostname, port=port,
                           username="root", password=password)
        ssh_client.exec_command("echo \"" + pub + "\" > /root/.ssh/authorized_keys")


def main():
    for hostname in hostnames:
        enable_root_auth(user, password, port, hostname)
        print(f"\nRoot user is enabled for ssh login. "
              f"The password is identical to the password of the user {user}. "
              f"The public key has been added to the server - {hostname}")
        add_pub_key(password, port, hostname)
        print(f"Public key added to host: {hostname}")


if __name__ == '__main__':
    main()
