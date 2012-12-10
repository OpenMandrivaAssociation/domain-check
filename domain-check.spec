Summary:	DNS domain expiration checker
Name:		domain-check
Version:	1.3
Release:	%mkrel 5
License:	BSD-like
Group:		Monitoring
URL:		http://prefetch.net/code/domain-check.html
Source0:	http://prefetch.net/code/domain-check.bz2
Patch0:		domain-check-1.3-whois.diff
Requires:	whois
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
domain-check is a utility for checking DNS domain expiration dates. domain-
check queries WHOIS data in realtime, and can be integrated with cron to
provide e-mail notifications prior to a domain expiring.

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




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3-5mdv2011.0
+ Revision: 617872
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.3-4mdv2010.0
+ Revision: 428327
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.3-3mdv2009.0
+ Revision: 244455
- rebuild
- fix description-line-too-long

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.3-1mdv2008.1
+ Revision: 136373
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3-1mdv2007.0
+ Revision: 101692
- Import domain-check

* Wed Aug 23 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3-1mdv2007.0
- initial Mandriva package

