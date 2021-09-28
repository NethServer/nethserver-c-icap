Summary: NethServer c-icap configuration
Name: nethserver-c-icap
Version: 1.1.1
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: c-icap
Requires: nethserver-base

BuildRequires: nethserver-devtools 

%description
NethServer c-icap configuration

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Tue Sep 28 2021 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.1-1
- c-icap not loading in arm - NethServer/dev#6573

* Thu Jul 07 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 1.1.0-1
- First NS7 release

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.2-1.ns6
- c-icap: disable access log - Enhancement #2288 [NethServer]
- Lib: synchronize service status prop and chkconfig - Feature #2067 [NethServer]

* Fri Jul 26 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1.ns6
- Change permissions and owner of c-icap.conf #1959
- Avoid zombie processes #1959

* Thu Jun 20 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1.ns6
- First release. Feature #1959


