#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Email
%define		pnam	Thread
Summary:	Email::Thread - use JWZ's mail threading algorithm with Email::Simple objects
Summary(pl):	Email::Thread - u¿ycie algorytmu w±tkowania poczty JWZ na obiektach Email::Simple
Name:		perl-Email-Thread
Version:	0.68
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ccd44f6fffbe39b7e26be5d56d799181
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Mail-Thread
BuildRequires:	perl-Test-Pod >= 1.00
BuildRequires:	perl-Test-Simple >= 0.47
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Strictly speaking, this doesn't really need Email::Simple objects. It
just needs an object that responds to the same API. At the time of
writing the list of classes with the Email::Simple API comprises just
Email::Simple.

%description -l pl
Mówi±c dok³adnie, ten modu³ nawet nie wymaga obiektów Email::Simple.
Wymaga tylko obiektu odpowiadaj±cego na to samo API. Podczas pisania
listy klas przy u¿yciu Email::Simple, API obejmuje po prostu
Email::Simple.

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
%doc AUTHORS CREDITS Change* README
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
