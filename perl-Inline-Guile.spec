%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
%define	pnam	Guile
Summary:	Inline::Guile perl module
Summary(pl):	Modu³ perla Inline::Guile
Name:		perl-Inline-Guile
Version:	0.001
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Guile >= 0.001
BuildRequires:	perl-Inline >= 0.43
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Inline/Guile.pm
%{_mandir}/man3/*
