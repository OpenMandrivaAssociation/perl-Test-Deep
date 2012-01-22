%define upstream_name	 Test-Deep
%define upstream_version 0.108

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	Extremely flexible deep comparison
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

Buildrequires:	perl-devel
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Test::Tester)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Test::Deep gives you very flexible ways to check that the result you got is the
result you were expecting. At it's simplest it compares two structures by going
through each level, ensuring that the values match, that arrays and hashes have
the same elements and that references are blessed into the correct class. It
also handles circular data structures without getting caught in an infinite
loop.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
