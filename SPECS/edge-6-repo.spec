Name:           edge-release
Version:        6
Release:        2%{?dist} 
Summary:        Edge Packages for Enterprise Linux repository configuration

Group:          System Environment/Base
License:        GPLv2

# This is a Edge maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.
URL:            https://github.com/gboddin/el6-lamp-stack 
Source0:        https://repo.siwhine.net/EDGE-REPO-KEY.pub
Source1:        https://repo.siwhine.net/el/el6.repo
Source2:        https://www.gnu.org/licenses/gpl.txt

BuildArch:     noarch
Requires:      redhat-release >=  l
BuildRoot:      %{_tmppath}/%{name}-%{version}%{version}

%description
This package contains the Edge Packages for Enterprise Linux (Edge) repository
GPG key as well as configuration for yum.

%prep
%setup  -c -T

%build


%install
rm -rf %{buildroot} 

#GPG Key
install -Dpm 644 %{SOURCE0} \
    %{buildroot}%{_sysconfdir}/pki/rpm-gpg/EDGE-REPO-KEY

# yum
install -dm 755 %{buildroot}%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE1}  \
    %{buildroot}%{_sysconfdir}/yum.repos.d/edge.repo

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root,-)
%doc gpl.txt 
%config(noreplace) %{_sysconfdir}/etc/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg/*

%changelog
* Wed Oct 19 2016 Gregory Boddin <gregory@siwhine.net> - 6-2
- Created package for easy install on RHELs

* Mon Aug 22 2016 Gregory Boddin <gregory@siwhine.net> - 6-1
- Created package for easy install on RHELs
 
* Mon Dec 16 2013 Dennis Gilmore <dennis@ausil.us> - 6-0.1
- initial epel 6 build. 

