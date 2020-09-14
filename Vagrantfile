# -*- mode: ruby -*-
# vi: set ft=ruby :

REPO_NAME = "RaibeartRepos"
SERVER_IP = "10.0.0.10"
CLIENT_IP = "10.0.0.11"

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"

  config.vm.define "server" do |server|
    server.vm.hostname = "server"
    server.vm.network "private_network", ip: SERVER_IP
    server.vm.provision "ansible" do |ansible|
      ansible.playbook = "server/site.yml"
      ansible.extra_vars = {
        "REPO_NAME" => REPO_NAME
      }
    end
  end

  config.vm.define "client" do |client|
    client.vm.hostname = "clinet"
    client.vm.network "private_network", ip: CLIENT_IP
    client.vm.provision "ansible" do |ansible|
      ansible.playbook = "client/site.yml"
      ansible.extra_vars = {
        "REPO_NAME" => REPO_NAME,
        "REPO_SERVER" => SERVER_IP
      }
    end
  end
end
