
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  #enable root user
  config.vm.provision "shell", inline: <<-'SHELL'
    sed -i 's/^#* *\(PermitRootLogin\)\(.*\)$/\1 yes/' /etc/ssh/sshd_config
    sed -i 's/^#* *\(PasswordAuthentication\)\(.*\)$/\1 yes/' /etc/ssh/sshd_config
    systemctl restart sshd.service
    echo -e "vagrant\nvagrant" | (passwd vagrant)
    echo -e "1337\n1337" | (passwd root)
  SHELL

  config.vm.define "vm-node-1" do |vmn1|
      vmn1.vm.network  "public_network", ip: "10.10.11.52"
      vmn1.vm.hostname = "vm-node-1"
      vmn1.vm.provider "virtualbox" do |vb|
        vb.memory = 4096
        vb.cpus = 2
      end
  end


  config.vm.define "vm-node-2" do |vmn2|
      vmn2.vm.network  "public_network", ip: "10.10.11.53"
      vmn2.vm.hostname = "vm-node-2"
      vmn2.vm.provider "virtualbox" do |vb|
        vb.memory = 4096
        vb.cpus = 2
      end
  end


 #config.vm.define "db" do |db|
 #    db.vm.network "public_network", ip: "10.10.11.54"
 #    db.vm.hostname = "db"
 #    db.vm.provider "virtualbox" do |vb|
 #       vb.memory = 4096
 #       vb.cpus = 2
 #    end
 #end


end
