#
# Conditional build:
%bcond_without	java		# Java extensions
%bcond_without	static_libs	# static libraries
#

%{?with_java:%{?use_default_jdk}}

Summary:	Static cluster configuration database
Summary(pl.UTF-8):	Statyczna baza danych konfiguracji klastra
Name:		genders
Version:	1.27.3
%define	gittag	%(echo %{version} | tr . -)
Release:	4
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/chaos/genders/releases
Source0:	https://github.com/chaos/genders/archive/genders-%{gittag}/%{name}-%{gittag}.tar.gz
# Source0-md5:	c86a3bc3a0b2c7e5b79c525de50e2f3b
Patch0:		%{name}-make.patch
URL:		https://github.com/chaos/genders
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
%{?with_java:%buildrequires_jdk}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-tools-pod
BuildRequires:	python-devel
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.021
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Genders is a static cluster configuration database used for cluster
configuration management. It is used by a variety of tools and scripts
for management of large clusters. The genders database is typically
replicated on every node of the cluster. It describes the layout and
configuration of the cluster so that tools and scripts can sense the
variations of cluster nodes. By abstracting this information into a
plain text file, it becomes possible to change the configuration of a
cluster by modifying only one file.

%description -l pl.UTF-8
Genders to statyczna baza danych konfiguracji klastra, służąca do
zarządzania klastrem. Jest wykorzystywana przez różne narzędzia i
skrypty do zarządzania dużymi klastrami. Baza danych genders jest
zwykle replikowana na każdym węźle klastra. Opisuje układ i
konfigurację klastra, aby narzędzia i skrypty miały informacje o
właściwościach węzłów klastra. Poprzez wyciągnięcie tych informacji do
zwykłego pliku tekstowego, można zmieniać konfigurację klastra
modyfikując tylko jeden plik.

%package devel
Summary:	Header file for genders library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki genders
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for genders library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki genders.

%package static
Summary:	Static genders library
Summary(pl.UTF-8):	Statyczna biblioteka genders
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static genders library.

%description static -l pl.UTF-8
Statyczna biblioteka genders.

%package c++
Summary:	C++ library for genders database
Summary(pl.UTF-8):	Biblioteka C++ do bazy danych genders
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
C++ library for genders database.

%description c++ -l pl.UTF-8
Biblioteka C++ do bazy danych genders.

%package c++-devel
Summary:	Header file for gendersplusplus library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki gendersplusplus
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
Header file for gendersplusplus library.

%description c++-devel -l pl.UTF-8
Plik nagłówkowy biblioteki gendersplusplus.

%package c++-static
Summary:	Static gendersplusplus library
Summary(pl.UTF-8):	Statyczna biblioteka gendersplusplus
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
Static gendersplusplus library.

%description c++-static -l pl.UTF-8
Statyczna biblioteka gendersplusplus.

%package compat
Summary:	Compatibility library for earlier releases of genders
Summary(pl.UTF-8):	Biblioteka dla zgodności ze starszymi wydaniami genders
Group:		Libraries
Requires:	perl-genders = %{version}-%{release}

%description compat
Genders API that is compatible with earlier releases of genders.

%description compat -l pl.UTF-8
API Genders zgodne ze starszymi wydaniami pakietu.

%package -n java-genders
Summary:	Java interface to genders library
Summary(pl.UTF-8):	Interfejs Javy do biblioteki genders
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}

%description -n java-genders
Java interface to genders library.

%description -n java-genders -l pl.UTF-8
Interfejs Javy do biblioteki genders.

%package -n java-genders-javadoc
Summary:	Javadoc documentation for Java interface to genders library
Summary(pl.UTF-8):	Dokumentacja Javadoc Interfejsu Javy do biblioteki genders
Group:		Documentation

%description -n java-genders-javadoc
Javadoc documentation for Java interface to genders library.

%description -n java-genders-javadoc -l pl.UTF-8
Dokumentacja Javadoc Interfejsu Javy do biblioteki genders.

%package -n perl-genders
Summary:	Perl interface to genders library
Summary(pl.UTF-8):	Interfejs Perla do biblioteki genders
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description -n perl-genders
Perl interface to genders library.

%description -n perl-genders -l pl.UTF-8
Interfejs Perla do biblioteki genders.

%package -n python-genders
Summary:	Python interface to genders library
Summary(pl.UTF-8):	Interfejs Pythona do biblioteki genders
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-genders
Python interface to genders library.

%description -n python-genders -l pl.UTF-8
Interfejs Pythona do biblioteki genders.

%prep
%setup -q -n %{name}-%{name}-%{gittag}
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%{?with_java:CPPFLAGS="%{rpmcppflags} -I%{java_home}/include -I%{java_home}/include/linux"}
%configure \
	 PYTHON="%{__python}" \
%if %{with java}
	 ac_cv_path_JAR="%{java_home}/bin/jar" \
	 ac_cv_path_JAVA="%{java_home}/bin/java" \
	 ac_cv_path_JAVAC="%{java_home}/bin/javac" \
	 ac_cv_path_JAVADOC="%{java_home}/bin/javadoc" \
	 ac_cv_path_JAVAH="%{java_home}/bin/javah" \
%endif
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	--with-extension-destdir=$RPM_BUILD_ROOT \
	%{!?with_java:--without-java-extensions} \
	--with-perl-vendor-arch

# -j1 due to racy flex/yacc invocation
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

# no external dependencies
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgenders*.la
%if %{with java}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libGendersjni.la \
	%{?with_static_libs:$RPM_BUILD_ROOT%{_libdir}/libGendersjni.a}
%endif

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%post	-n java-genders -p /sbin/ldconfig
%postun	-n java-genders -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog DISCLAIMER DISCLAIMER.UC NEWS README TODO TUTORIAL
%attr(755,root,root) %{_bindir}/nodeattr
%attr(755,root,root) %{_libdir}/libgenders.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgenders.so.0
%{_mandir}/man1/nodeattr.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgenders.so
%{_includedir}/genders.h
%{_mandir}/man3/genders*.3*
%{_mandir}/man3/libgenders.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgenders.a
%endif

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgendersplusplus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgendersplusplus.so.2

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgendersplusplus.so
%{_includedir}/gendersplusplus.hpp

%if %{with static_libs}
%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libgendersplusplus.a
%endif

%files compat
%defattr(644,root,root,755)
%dir %{_prefix}/lib/genders
%attr(755,root,root) %{_prefix}/lib/genders/gendlib.pl
%attr(755,root,root) %{_prefix}/lib/genders/hostlist.pl
%{_mandir}/man3/gendlib.3*

%if %{with java}
%files -n java-genders
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGendersjni.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libGendersjni.so.0
%attr(755,root,root) %{_libdir}/libGendersjni.so
%{_javadir}/Genders.jar

%files -n java-genders-javadoc
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-1.27-javadoc
%endif

%files -n perl-genders
%defattr(644,root,root,755)
%{perl_vendorarch}/Genders.pm
%{perl_vendorarch}/Libgenders.pm
%dir %{perl_vendorarch}/auto/Libgenders
%attr(755,root,root) %{perl_vendorarch}/auto/Libgenders/Libgenders.so
%{_mandir}/man3/Genders.3pm*
%{_mandir}/man3/Libgenders.3pm*

%files -n python-genders
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/libgenders.so
%{py_sitedir}/genders.py[co]
%{py_sitedir}/libgenders-*.egg-info
