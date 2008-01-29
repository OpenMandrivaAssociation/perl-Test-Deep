%define module	Test-Deep
%define name	perl-%{module}
%define version	0.100
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Extremely flexible deep comparison
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(Test::Tester)
BuildRequires:	perl(Test::NoWarnings)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Test::Deep gives you very flexible ways to check that the result you got is the
result you were expecting. At it's simplest it compares two structures by going
through each level, ensuring that the values match, that arrays and hashes have
the same elements and that references are blessed into the correct class. It
also handles circular data structures without getting caught in an infinite
loop.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README TODO
%{_mandir}/*/*
%{perl_vendorlib}/Test/Deep
%{perl_vendorlib}/Test/Deep.pm
%{perl_vendorlib}/Test/Deep.pod


