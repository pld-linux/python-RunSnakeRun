%define 	module	RunSnakeRun
Summary:	GUI Viewer for Python profiling runs
Summary(pl.UTF-8):	Interfejs graficzny do wyników profilowania programów Pythonowych
Name:		python-%{module}
Version:	2.0.4
Release:	1
License:	BSD
Group:		Development/Languages/Python
#               http://pypi.python.org/packages/source/R/RunSnakeRun/RunSnakeRun-2.0.2a1.tar.gz
Source0:	http://pypi.python.org/packages/source/R/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	3220b5b89994baee70b1c24d7e42a306
URL:		http://www.vrplumber.com/programming/runsnakerun/
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-distribute
Requires:	python-SquareMap >= 1.0.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
simple program, it doesn't provide all the bells-and-whistles of a
program like KCacheGrind, it's intended to allow for profiling your
Python programs, and just your Python programs

%description -l pl.UTF-8
Prosty program pozwalający zobaczyć wyniki profiliwoania programów w
Pythonie.

%prep
%setup -q -n %{module}-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# %doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/runsnake
%attr(755,root,root) %{_bindir}/runsnakemem
%dir %{py_sitescriptdir}/runsnakerun
%{py_sitescriptdir}/runsnakerun/*.py[co]
%{py_sitescriptdir}/%{module}*.egg-info
