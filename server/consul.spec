Summary:	Consul
Name:		consul
Version:	1.7.0
Release:	1
License:	Mozilla Public License, version 2.0
URL:		https://github.com/hashicorp/consul
Group:		Sistem/Server
BuildArch:	x86_64

%description
Consul from Server Raibeart

%prep
curl -o %{name}-%{version}.zip https://releases.hashicorp.com/consul/%{version}/consul_%{version}_linux_amd64.zip

%build
unzip %{name}-%{version}.zip

%install
mkdir -p %{buildroot}/usr/bin
mv consul %{buildroot}/usr/bin/consul

%files
%defattr(755, root, root)
/usr/bin/consul
