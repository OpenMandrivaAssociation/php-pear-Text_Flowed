%define prj Text_Flowed

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          php-pear-Text_Flowed
Version:       0.0.2
Release:       5
Summary:       Horde Mime Library
License:       LGPL
Group:         Networking/Mail
Url:           https://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      horde-util
Requires:       php-pear
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde

%description
The Text_Flowed:: class provides common methods for manipulating text using
the encoding described in RFC 3676 ('flowed' text)

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Text
%dir %{peardir}/tests/Text_Flowed/tests
%{peardir}/Text/Flowed.php
%{peardir}/tests/Text_Flowed/tests/Flowed.phpt




%changelog
* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-3mdv2011.0
+ Revision: 564124
- Increased release for rebuild

* Wed Mar 17 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-2mdv2010.1
+ Revision: 523852
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear
  increased release version

* Mon Mar 08 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-1mdv2010.1
+ Revision: 515619
- removed BuildRequires: horder-framework
- import php-pear-Text_Flowed


