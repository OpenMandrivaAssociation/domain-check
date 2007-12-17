Summary:	DNS domain expiration checker
Name:		domain-check
Version:	1.3
Release:	%mkrel 1
License:	BSD-like
Group:		Monitoring
URL:		http://prefetch.net/code/domain-check.html
Source0:	http://prefetch.net/code/domain-check.bz2
Patch0:		domain-check-1.3-whois.diff
Requires:	whois
BuildArch:	noarch

%description
domain-check is a utility for checking DNS domain expiration dates. domain-check
queries WHOIS data in realtime, and can be integrated with cron to provide
e-mail notifications prior to a domain expiring.

%prep

%setup -q -c -T
bzcat %{SOURCE0} > %{name}
%patch0 -p0

%build

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/%{name}


