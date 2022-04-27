#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Fast markdown parser in pure Python
Summary(pl.UTF-8):	Szybki parser markdown napisany w czystym Pythonie
Name:		python-mistune
Version:	2.0.2
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/mistune/
Source0:	https://files.pythonhosted.org/packages/source/m/mistune/mistune-%{version}.tar.gz
# Source0-md5:	cde384cabc49477549ef78f946670e7d
URL:		https://github.com/lepture/mistune
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%{?with_tests:BuildRequires:	python-pytest}
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%{?with_tests:BuildRequires:	python3-pytest}
%endif
Requires:	python-modules >= 1:2.7
# no compatible versions so far
Conflicts:	python-docwriter
Conflicts:	python-m2r
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The fastest markdown parser in pure Python with renderer features,
inspired by marked.

%description -l pl.UTF-8
Najszybszy parser markdown w czystym Pythonie z obsługą renderingu,
zainspirowany modułem marked.

%package -n python3-mistune
Summary:	Fast markdown parser in pure Python
Summary(pl.UTF-8):	Szybki parser markdown napisany w czystym Pythonie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5
# no compatible versions so far
Conflicts:	python3-docwriter
Conflicts:	python3-m2r

%description -n python3-mistune
The fastest markdown parser in pure Python with renderer features,
inspired by marked.

%description -n python3-mistune -l pl.UTF-8
Najszybszy parser markdown w czystym Pythonie z obsługą renderingu,
zainspirowany modułem marked.

%prep
%setup -q -n mistune-%{version}

# stub for setuptools
cat >setup.py <<EOF
from setuptools import setup

setup()
EOF

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/mistune
%{py_sitescriptdir}/mistune-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-mistune
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/mistune
%{py3_sitescriptdir}/mistune-%{version}-py*.egg-info
%endif
