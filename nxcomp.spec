%define	_version_major	1.4.0
%define	_version_minor	31
%define	_release	1

Summary:	NX compression library
Summary(pl):	Biblioteka kompresji NX
Name:		nxcomp
Version:	%{_version_major}
Release:	%{_version_minor}.%{_release}
License:	GPL
Group:		X11/Libraries
Source0:	http://www.nomachine.com/download/nxsources/%{_version_major}/%{name}-%{_version_major}-%{_version_minor}.tar.gz
# Source0-md5:	c2eb354e141e9f0e81f4cd1673b2a3ae
URL:		http://www.nomachine.com/
BuildRequires:	XFree86-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NX compression library.

%description -l pl
Biblioteka kompresji NX.

%package devel
Summary:	Header files for nxcomp
Summary(pl):	Pliki nag³ówkowe nxcomp
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for nxcomp.

%description devel -l pl
Pliki nag³ówkowe nxcomp.

%package static
Summary:	Static nxcomp library
Summary(pl):	Statyczna biblioteka nxcomp
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static nxcomp library.

%description static -l pl
Statyczna biblioteka nxcomp.

%prep
%setup -q -n %{name}
sed -i 's/CXXFLAGS="-O3"/CXXFLAGS="%{rpmcflags}"/' configure.in
sed -i 's/CPPFLAGS="-O3"/CPPFLAGS="%{rpmcflags}"/' configure.in

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

#%{__make} install \
#	DESTDIR=$RPM_BUILD_ROOT

cp -a lib*.so* $RPM_BUILD_ROOT%{_libdir}
install lib*.a $RPM_BUILD_ROOT%{_libdir}
install NX.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
