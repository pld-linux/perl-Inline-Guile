#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pnam	Guile
Summary:	Inline::Guile Perl module
Summary(cs):	Modul Inline::Guile pro Perl
Summary(da):	Perlmodul Inline::Guile
Summary(de):	Inline::Guile Perl Modul
Summary(es):	Módulo de Perl Inline::Guile
Summary(fr):	Module Perl Inline::Guile
Summary(it):	Modulo di Perl Inline::Guile
Summary(ja):	Inline::Guile Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Inline::Guile ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul Inline::Guile
Summary(pl):	Modu³ Perla Inline::Guile
Summary(pt):	Módulo de Perl Inline::Guile
Summary(pt_BR):	Módulo Perl Inline::Guile
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Inline::Guile
Summary(sv):	Inline::Guile Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Inline::Guile
Summary(zh_CN):	Inline::Guile Perl Ä£¿é
Name:		perl-Inline-Guile
Version:	0.001
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2e1926f838cd44f244ab16ca7a655cb7
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Guile >= 0.001
BuildRequires:	perl-Inline >= 0.43
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Guile - Inline module for the GNU Guile Scheme interpreter.
It allows you to add blocks of Scheme code to your Perl scripts and
modules.

%description -l pl
Inline::Guile - modu³ Inline do interpretera Scheme GNU Guile. Pozwala
na dodawanie bloków kodu Scheme do skryptów i modu³ów Perla.

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
