#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Inline
%define		pnam	Guile
Summary:	Inline::Guile - an Inline module for the GNU Guile Scheme interpreter
Summary(pl.UTF-8):	Inline::Guile - moduł Inline dla interpretera Scheme GNU Guile
Name:		perl-Inline-Guile
Version:	0.001
Release:	3
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2e1926f838cd44f244ab16ca7a655cb7
URL:		http://search.cpan.org/dist/Inline-Guile/
BuildRequires:	perl-Guile >= 0.001
BuildRequires:	perl-Inline >= 0.43
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Guile - Inline module for the GNU Guile Scheme interpreter. It
allows you to add blocks of Scheme code to your Perl scripts and
modules.

%description -l pl.UTF-8
Inline::Guile - moduł Inline do interpretera Scheme GNU Guile. Pozwala
na dodawanie bloków kodu Scheme do skryptów i modułów Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Inline/Guile.pm
%{_mandir}/man3/*
