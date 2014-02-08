%define upstream_name	 Test-Deep
%define upstream_version 0.108

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    7

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.108.0-5mdv2012.0
+ Revision: 765676
- rebuilt for perl-5.14.2

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.108.0-4
+ Revision: 764922
- rebuild

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.108.0-3
+ Revision: 764187
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.108.0-2
+ Revision: 667323
- mass rebuild

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.108.0-1mdv2011.0
+ Revision: 596036
- update to new version 0.108

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.106.0-2mdv2011.0
+ Revision: 426593
- rebuild

  + Jérôme Quelin <jquelin@mandriva.org>
    - update to 0.106
    - update to 0.106

* Fri Mar 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.104-1mdv2009.1
+ Revision: 349682
- update to new version 0.104

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.103-2mdv2009.0
+ Revision: 268731
- rebuild early 2009.0 package (before pixel changes)

* Wed Jun 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.103-1mdv2009.0
+ Revision: 215041
- update to new version 0.103

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.102-1mdv2009.0
+ Revision: 213630
- update to new version 0.102

* Sat May 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.101-1mdv2009.0
+ Revision: 208376
- update to new version 0.101

* Tue Jan 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.100-1mdv2008.1
+ Revision: 159905
- update to new version 0.100

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.099-1mdv2008.1
+ Revision: 104577
- update to new version 0.099

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.098-1mdv2008.1
+ Revision: 97567
- update to new version 0.098

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.097-1mdv2008.0
+ Revision: 63964
- update to new version 0.097


* Wed Dec 13 2006 Olivier Thauvin <nanardon@mandriva.org> 0.096-1mdv2007.0
+ Revision: 96134
- 0.096
- Import perl-Test-Deep

* Fri Apr 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.095-1mdk
- new version

* Fri Apr 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.094-1mdk
- new version  
- spec cleanup
- rpmbuildupdate aware
- better buildrequires syntax

* Fri Dec 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.093-1mdk
- 0.093

* Sat Oct 29 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.092-1mdk
- 0.092

* Wed Oct 12 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.089-1mdk
- Initial MDV release

