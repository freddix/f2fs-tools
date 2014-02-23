Summary:	Tools for Flash-Friendly File System (F2FS)
Name:		f2fs-tools
Version:	1.3.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://git.kernel.org/cgit/linux/kernel/git/jaegeuk/f2fs-tools.git/snapshot/%{name}-%{version}.tar.gz
# Source0-md5:	fd5f9cbef72a58f3264f27d72a27b8ae
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for Flash-Friendly File System (F2FS).

%prep
%setup -q

%{__sed} -i 's|/sbin|%{_sbindir}|g' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
    --disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.{la,so}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %ghost %{_libdir}/libf2fs.so.0
%attr(755,root,root) %{_libdir}/libf2fs.so.*.*.*
%attr(755,root,root) %{_sbindir}/dump.f2fs
%attr(755,root,root) %{_sbindir}/f2fstat
%attr(755,root,root) %{_sbindir}/fibmap.f2fs
%attr(755,root,root) %{_sbindir}/fsck.f2fs
%attr(755,root,root) %{_sbindir}/mkfs.f2fs
%{_mandir}/man8/mkfs.f2fs.8*

