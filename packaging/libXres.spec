
Name:       libXres
Summary:    X.Org X11 libXres runtime library
Version:    1.0.5
Release:    0
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.gz
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(resourceproto)

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
Description: %{summary}


%package devel
Summary:    X.Org X11 libXres development package
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   xorg-x11-filesystem

%description devel
Description: %{summary}


%prep
%setup -q -n %{name}-%{version}


%build

%reconfigure \
	LDFLAGS="-Wl,--hash-style=both -Wl,--as-needed"

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig



%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libXRes.so.1
%{_libdir}/libXRes.so.1.0.0


%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/X11
%dir %{_includedir}/X11/extensions
%{_includedir}/X11/extensions/XRes.h
%{_libdir}/libXRes.so
%{_libdir}/pkgconfig/xres.pc
#%dir %{_mandir}/man3x
%{_mandir}/man3/*.3*

