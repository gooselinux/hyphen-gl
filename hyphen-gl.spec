Name: hyphen-gl
Summary: Galician hyphenation rules
Version: 0.99
Release: 2.1%{?dist}
Source: http://extensions.services.openoffice.org/files/2004/0/hyph_gl.oxt
Group: Applications/Text
URL: https://forxa.mancomun.org/projects/hyphenation-gl
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv3
BuildArch: noarch
Requires: hyphen

%description
Galician hyphenation rules.

%prep
%setup -q -c -n hyphen-gl

%build
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_gl_ANY.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_gl_ES.dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LEME-gl_ANY.txt LICENCES-gl.txt LICENSES-en.txt  
%{_datadir}/hyphen/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.99-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 13 2009 Caolan McNamara <caolanm@redhat.com> - 0.99-1
- initial version
