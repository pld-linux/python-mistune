#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Fast markdown parser in pure Python
Summary(pl.UTF-8):	Szybki parser markdown napisany w czystym Pythonie
Name:		python-mistune
Version:	0.8.4
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/mistune/
Source0:	https://files.pythonhosted.org/packages/source/m/mistune/mistune-%{version}.tar.gz
# Source0-md5:	fb6ab174ece938dea09f8b2adad771e4
URL:		https://github.com/lepture/mistune
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%{?with_tests:BuildRequires:	python-nose}
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%{?with_tests:BuildRequires:	python3-nose}
%endif
Requires:	python-modules >= 1:2.7
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

%description -n python3-mistune
The fastest markdown parser in pure Python with renderer features,
inspired by marked.

%description -n python3-mistune -l pl.UTF-8
Najszybszy parser markdown w czystym Pythonie z obsługą renderingu,
zainspirowany modułem marked.

%prep
%setup -q -n mistune-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
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
%doc CHANGES.rst LICENSE README.rst
%{py_sitescriptdir}/mistune.py[co]
%{py_sitescriptdir}/mistune-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-mistune
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py3_sitescriptdir}/mistune.py
%{py3_sitescriptdir}/__pycache__/mistune.cpython-*.py[co]
%{py3_sitescriptdir}/mistune-%{version}-py*.egg-info
%endif
