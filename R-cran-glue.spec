%define		fversion	%(echo %{version} |tr r -)
%define		modulename	glue
Summary:	Interpreted string literals
Name:		R-cran-%{modulename}
Version:	1.8.0
Release:	1
License:	MIT
Group:		Applications/Math
Source0:	https://cran.r-project.org/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	283bba07f61d89e32f9895021bf5099c
URL:		https://cran.r-project.org/package=%{modulename}
BuildRequires:	R

Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interpreted string literals.

%prep
%setup -q -c

%build
R CMD build --no-build-vignettes %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
