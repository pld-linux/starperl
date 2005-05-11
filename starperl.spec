#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
%bcond_without	nbs	# don't build Starlink package (requires starlink-nbs)
#
%ifarch %{x8664} alpha ia64 ppc64 s390x sparc64
%undefine	with_nbs
%endif
%include	/usr/lib/rpm/macros.perl
Summary:	STARPERL - Starlink Perl modules
Summary(pl):	STARPERL - modu³y Perla z projektu Starlink
Name:		starperl
Version:	1.4.218
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.starlink.rl.ac.uk/pub/ussc/store/starperl/starperl.tar.Z
# Source0-md5:	33dda278be4474cf737be6a8b702a04a
Patch0:		%{name}-make.patch
Patch1:		%{name}-types.patch
URL:		http://www.starlink.rl.ac.uk/static_www/soft_further_STARPERL.html
# standalone NDF, GSD, Astro-SLA modules at:
#   http://www.jach.hawaii.edu/JACpublic/JCMT/software/perl/
#   ftp://ftp.jach.hawaii.edu/pub/jcmt/jcmt_sw/perl/
# ...but older.
BuildRequires:	gcc-g77
BuildRequires:	perl-ExtUtils-F77
BuildRequires:	perl-PDL
BuildRequires:	perl-Proc-Simple >= 1.13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	sed >= 4.0
BuildRequires:	starlink-gsd-devel
BuildRequires:	starlink-img-devel
%{?with_nbs:BuildRequires:	starlink-nbs-devel}
BuildRequires:	starlink-ndf-devel
BuildRequires:	starlink-sae-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		stardir		/usr/lib/star

%define		ver_Config	1.00
%define		ver_NDF		1.45
%define		ver_Starlink	1.14
%define		ver_GSD		1.13
%define		ver_SLA		0.96
%define		nConfig		Starlink-Config-%{ver_Config}
%define		nNDF		NDF-%{ver_NDF}
%define		nStarlink	Starlink-%{ver_Starlink}
%define		nGSD		GSD-%{ver_GSD}
%define		nSLA		Astro-SLA-%{ver_SLA}

%description
The StarPerl package is a selection of Perl modules that provide
access to Starlink infrastructure libraries. Currently, interfaces are
provided to the ADAM messaging system, the Starlink Noticeboard
system. Additional modules are provided to determine version numbers
of installed Starlink packages and to read NDF, HDS and GSD format
data files.

%description -l pl
Pakiet StarPerl to zbiór modu³ów Perla daj±cych dostêp do bibliotek z
infrastruktury Starlink. Aktualnie dostêpne s± interfejsy do systemu
komunikatów ADAM i systemu powiadamiania NBS. Do³±czone s± dodatkowe
modu³y do okre¶lania wersji zainstalowanych pakietów Starlinka oraz do
odczytu plików z danymi w formatach NDF, HDS i GSD.

%package -n perl-Starlink-Config
Summary:	Starlink::Config - retrieve local Starlink configuration
Summary(pl):	Starlink::Config - uzyskiwanie lokalnej konfiguracji Starlinka
Group:		Development/Languages/Perl
Version:	%{ver_Config}
Requires:	starlink-sae

%description -n perl-Starlink-Config
This package contains the location of the Starlink software on your
system. It is intended to simplify the building of Perl modules based
on Starlink libraries and allows for this information to be placed in
a single place rather than in every single Starlink module.

%description -n perl-Starlink-Config
Ten pakiet zawiera informacje o po³o¿eniu oprogramowania Starlink w
systemie. Ma za zadanie upro¶ciæ budowanie modu³ów Perla opartych na
bibliotekach Starlinka i pozwala na umieszczenie tych informacji w
jednym miejscu, zamiast w ka¿dym module Starlinka osobno.

%package -n perl-NDF
Summary:	NDFPERL - accessing Starlink N-dimensional data structures (NDFs) from Perl
Summary(pl):	NDFPERL - dostêp do wielowymiarowych struktur danych (Starlink NDF) z poziomu Perla
Version:	%{ver_NDF}
# "same as perl" (i.e. GPL or Artistic), but NDF is GPLed...
License:	GPL
Group:		Development/Languages/Perl

%description -n perl-NDF
This module gives access to the Starlink extensible N-dimensional data
format (NDF) and related error and message handling routines. Basic
hierarchical data structure (HDS) access routines are also supplied.

%description -n perl-NDF -l pl
Ten modu³ daje dostêp do rozszerzalnego formutu wielowymiarowych
danych (Starlink NDF) oraz zwi±zanych z nim funkcji obs³ugi b³êdów i
komunikatów. Za³±czone s± tak¿e funkcje do dostêpu do podstawowych
hierarchicznych struktur danych (HDS).

%package -n perl-Starlink
Summary:	Starlink Perl modules - interface to Starlink libraries
Summary(pl):	Modu³y Perla Starlink - interfejs do bibliotek Starlink
Group:		Development/Languages/Perl
Version:	%{ver_Starlink}
Requires:	perl-NDF = %{ver_NDF}-%{release}
Requires:	perl-Starlink-Config = %{ver_Config}-%{release}

%description -n perl-Starlink
The StarPerl package is a selection of Perl modules that provide
access to Starlink infrastructure libraries. Currently, interfaces are
provided to the ADAM messaging system, the Starlink Noticeboard
system.

%description -n perl-Starlink -l pl
Pakiet StarPerl to zbiór modu³ów Perla daj±cych dostêp do bibliotek z
infrastruktury Starlink. Aktualnie dostêpne s± interfejsy do systemu
komunikatów ADAM i systemu powiadamiania NBS.

%package -n perl-GSD
Summary:	GSD Perl module - read access to JMCT GSD data
Summary(pl):	Modu³ Perla GSD - umo¿liwiaj±cy odczyt danych GSD z JMCT
Group:		Development/Languages/Perl
Version:	%{ver_GSD}

%description -n perl-GSD
The James Clerk Maxwell Telescope (JCMT), Mauna Kea, Hawaii uses an
in-house format for storing spectral line and UKT14 continuum data.
This format is called the Global Section Data format (GSD). This
module gives read only access to JCMT data.

%description -n perl-GSD -l pl
Teleskop JCMT (James Clerk Maxwell Telescope) w Mauna Kea na Hawajach
u¿ywa w³asnego formatu do zapisu linii widm i danych continuum UKT14.
Ten format jest nazywany GSD (Global Section Data - dane sekcji
globalnej). Ten modu³ daje dostêp tylko do odczytu do danych JCMT.

%package -n perl-Astro-SLA
Summary:	Astro::SLA - Perl interface to SLAlib positional astronomy library
Summary(pl):	Astro::SLA - perlowy interfejs do biblioteki astronomii pozycyjnej SLAlib
Group:		Development/Languages/Perl
Version:	%{ver_SLA}

%description -n perl-Astro-SLA
This modules provides a Perl interface to either the C or Fortran
versions of the SLALIB astrometry library written by Pat Wallace.

%description -n perl-Astro-SLA -l pl
Ten modu³ udostêpnia perlowy interfejs do wersji C lub fortranowej
biblioteki astronometrycznej SLALIB napisanej przez Pata Wallace'a.

%prep
%setup -q -c

tar xf %{nConfig}.tar
tar xf %{nNDF}.tar
tar xf %{nStarlink}.tar
tar xf %{nGSD}.tar
tar xf %{nSLA}.tar

%patch0 -p1
%patch1 -p1

%build
R=`pwd`

cd %{nConfig}
STARLINK=%{stardir} \
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

cd ../%{nNDF}
PATH="$PATH:%{stardir}/bin" \
%{__perl} -I"${R}/%{nConfig}/blib/lib" Makefile.PL \
	INSTALLDIRS=vendor \
	OPTIMIZE="%{rpmcflags}"
%{__make}
%{?with_tests:%{__make} test}

%if %{with nbs}
cd ../%{nStarlink}
PATH="$PATH:%{stardir}/bin" \
%{__perl} -I"${R}/%{nConfig}/blib/lib" Makefile.PL \
	INSTALLDIRS=vendor \
	OPTIMIZE="%{rpmcflags}"
%{__make}
%if %{with tests}
PATH="$PATH:%{stardir}/bin" \
%{__make} test \
	PERL5LIB="${R}/%{nConfig}/blib/lib:${R}/%{nNDF}/blib/lib:${R}/%{nNDF}/blib/arch"
%endif
%endif

cd ../%{nGSD}
PATH="$PATH:%{stardir}/bin" \
%{__perl} -I"${R}/%{nConfig}/blib/lib" Makefile.PL \
	INSTALLDIRS=vendor \
	OPTIMIZE="%{rpmcflags}"
%{__make}
%{?with_tests:%{__make} test}

cd ../%{nSLA}
PATH="$PATH:%{stardir}/bin" \
%{__perl} -I"${R}/%{nConfig}/blib/lib" Makefile.PL \
	INSTALLDIRS=vendor \
	OPTIMIZE="%{rpmcflags}"
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install -C %{nConfig} \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install -C %{nNDF} \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with nbs}
%{__make} install -C %{nStarlink} \
	DESTDIR=$RPM_BUILD_ROOT

mv -f %{nStarlink}/ADAM/ChangeLog %{nStarlink}/ChangeLog.ADAM
mv -f %{nStarlink}/AMS/Core/ChangeLog %{nStarlink}/ChangeLog.AMS-Core
mv -f %{nStarlink}/AMS/Init/ChangeLog %{nStarlink}/ChangeLog.AMS-Init
mv -f %{nStarlink}/AMS/Task/ChangeLog %{nStarlink}/ChangeLog.AMS-Task
mv -f %{nStarlink}/NBS/ChangeLog %{nStarlink}/ChangeLog.NBS
%endif

%{__make} install -C %{nGSD} \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install -C %{nSLA} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files -n perl-Starlink-Config
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/Starlink
%{perl_vendorlib}/Starlink/Config.pm
%{_mandir}/man3/Starlink::Config.3*

%files -n perl-NDF
%defattr(644,root,root,755)
%doc NDF-%{ver_NDF}/{ChangeLog,README}
%{perl_vendorarch}/NDF.pm
%dir %{perl_vendorarch}/auto/NDF
%{perl_vendorarch}/auto/NDF/autosplit.ix
%{perl_vendorarch}/auto/NDF/NDF.bs
%attr(755,root,root) %{perl_vendorarch}/auto/NDF/NDF.so
%{_mandir}/man3/NDF.3*

%if %{with nbs}
%files -n perl-Starlink
%defattr(644,root,root,755)
%doc %{nStarlink}/{starperl.news,ChangeLog*}
%attr(755,root,root) %{_bindir}/starversion
%attr(755,root,root) %{_bindir}/MessageRelay.pl
%dir %{perl_vendorarch}/Starlink
%{perl_vendorarch}/Starlink/AMS
%{perl_vendorarch}/Starlink/*.pm
%dir %{perl_vendorarch}/auto/Starlink
%dir %{perl_vendorarch}/auto/Starlink/ADAM
%{perl_vendorarch}/auto/Starlink/ADAM/ADAM.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Starlink/ADAM/ADAM.so
%dir %{perl_vendorarch}/auto/Starlink/EMS
%{perl_vendorarch}/auto/Starlink/EMS/EMS.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Starlink/EMS/EMS.so
%dir %{perl_vendorarch}/auto/Starlink/NBS
%{perl_vendorarch}/auto/Starlink/NBS/autosplit.ix
%{perl_vendorarch}/auto/Starlink/NBS/NBS.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Starlink/NBS/NBS.so
%{_mandir}/man1/starversion.1*
%{_mandir}/man3/Starlink::[!C]*.3*
%endif

%files -n perl-GSD
%defattr(644,root,root,755)
%doc %{nGSD}/{ChangeLog,README}
%attr(755,root,root) %{_bindir}/gsdprint
%{perl_vendorarch}/GSD.pm
%dir %{perl_vendorarch}/GSD
%{perl_vendorarch}/GSD/PDL.pm
%{perl_vendorarch}/PDL/IO/GSD.pm
%dir %{perl_vendorarch}/auto/GSD
%{perl_vendorarch}/auto/GSD/GSD.bs
%attr(755,root,root) %{perl_vendorarch}/auto/GSD/GSD.so
%{_mandir}/man1/gsdprint.1*
%{_mandir}/man3/GSD*.3*
%{_mandir}/man3/PDL::IO::GSD.3*

%files -n perl-Astro-SLA
%defattr(644,root,root,755)
%doc %{nSLA}/{ChangeLog,README}
%attr(755,root,root) %{_bindir}/stime
%{perl_vendorarch}/Astro/SLA.pm
%dir %{perl_vendorarch}/auto/Astro/SLA
%{perl_vendorarch}/auto/Astro/SLA/SLA.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Astro/SLA/SLA.so
%{_mandir}/man1/stime.1*
%{_mandir}/man3/Astro::SLA.3*
