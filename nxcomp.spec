# NOTE
# - nxcomp is built in nx.spec in pld
#   https://github.com/pld-linux/nx/commit/5843d362d78ea5fc3689d34a391622b1d8a110e0

%define	_version_major	3.5.0
%define	_version_minor	2

Summary:	NX compression library
Summary(pl.UTF-8):	Biblioteka kompresji NX
Name:		nxcomp
Version:	%{_version_major}.%{_version_minor}
Release:	2
License:	GPL
Group:		X11/Libraries
Source0:	http://64.34.161.181/download/%{_version_major}/sources/%{name}-%{_version_major}-%{_version_minor}.tar.gz
# Source0-md5:	ad8c0f133122c6d07732ca69c8759410
Patch0:		%{name}-pic.patch
Patch1:		%{name}-FLAGS.patch
Patch2:		%{name}-libpng15.patch
URL:		http://www.nomachine.com/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NX compression library.

%description -l pl.UTF-8
Biblioteka kompresji NX.

%package devel
Summary:	Header files for nxcomp
Summary(pl.UTF-8):	Pliki nagłówkowe nxcomp
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for nxcomp.

%description devel -l pl.UTF-8
Pliki nagłówkowe nxcomp.

%package static
Summary:	Static nxcomp library
Summary(pl.UTF-8):	Statyczna biblioteka nxcomp
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static nxcomp library.

%description static -l pl.UTF-8
Statyczna biblioteka nxcomp.

%prep
%setup -q -n %{name}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

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
install NX*.h $RPM_BUILD_ROOT%{_includedir}
install MD5.h $RPM_BUILD_ROOT%{_includedir}

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
