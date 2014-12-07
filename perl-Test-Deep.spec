%define modname	Test-Deep
%define modver 0.113

Summary:	Extremely flexible deep comparison
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Test/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
Buildrequires:	perl-devel
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Test::Tester)

%description
Test::Deep gives you very flexible ways to check that the result you got is the
result you were expecting. At it's simplest it compares two structures by going
through each level, ensuring that the values match, that arrays and hashes have
the same elements and that references are blessed into the correct class. It
also handles circular data structures without getting caught in an infinite
loop.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc  README TODO
%{perl_vendorlib}/Test/Deep
%{perl_vendorlib}/Test/Deep.pm
# %{perl_vendorlib}/Test/Deep.pod
%{_mandir}/man3/*
