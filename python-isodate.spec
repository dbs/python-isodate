%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

Name:           python-isodate
Version:        0.4.6
Release:        2%{?dist}
Summary:        An ISO 8601 date/time/duration parser and formater
Group:          Development/Languages
License:        BSD
URL:            http://pypi.python.org/pypi/isodate
Source0:        http://pypi.python.org/packages/source/i/isodate/isodate-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
%if 0%{?fedora} >= 11 || 0%{?rhel} >= 6
BuildRequires:  python-setuptools-devel
%else
BuildRequires:  python-setuptools
%endif
%if 0%{?with_python3}
BuildRequires:  python3-devel
%endif # if with_python3

%description
This module implements ISO 8601 date, time and duration parsing. The
implementation follows ISO8601:2004 standard, and implements only date/time
representations mentioned in the standard. If something is not mentioned there,
then it is treated as non existent, and not as an allowed option.

For instance, ISO8601:2004 never mentions 2 digit years. So, it is not intended
by this module to support 2 digit years. (while it may still be valid as ISO
date, because it is not explicitly forbidden.) Another example is, when no time
zone information is given for a time, then it should be interpreted as local
time, and not UTC.

As this module maps ISO 8601 dates/times to standard Python data types, like
date, time, datetime and timedelta, it is not possible to convert all possible
ISO 8601 dates/times. For instance, dates before 0001-01-01 are not allowed by
the Python date and datetime classes. Additionally fractional seconds are
limited to microseconds. That means if the parser finds for instance
nanoseconds it will round it to microseconds.


%prep
%setup -qn isodate-%{version}


%build
%if 0%{?fedora} >= 11 || 0%{?rhel} >= 6
%{__python} setup.py build
%else
CFLAGS="%{optflags}" %{__python} -c 'import setuptools; execfile("setup.py")' build
%endif


%install
rm -rf %{buildroot}
%if 0%{?fedora} >= 11 || 0%{?rhel} >= 6
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%else
%{__python} -c 'import setuptools; execfile("setup.py")' install --skip-build --root %{buildroot}
%endif


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README.txt TODO.txt
%{python_sitelib}/isodate
%{python_sitelib}/isodate*.egg-info


%changelog
* Mon Jan 23 2012 James Laska <jlaska@redhat.com> - 0.4.6-1
- Update to 0.4.6

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 28 2011 James Laska <jlaska@redhat.com> - 0.4.4-1
- Initial package build
