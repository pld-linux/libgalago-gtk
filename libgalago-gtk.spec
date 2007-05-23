Summary:	Galago GTK library
Summary(pl.UTF-8):	Biblioteka Galago dla GTK
Name:		libgalago-gtk
Version:	0.5.0
Release:	1
License:	LGPL v2.1+
Group:		Applications/System
Source0:	http://www.galago-project.org/files/releases/source/libgalago-gtk/%{name}-%{version}.tar.bz2
# Source0-md5:	20e809869ec764efb2259ee0d0dee263
URL:		http://www.galago-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.1
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	dbus-glib >= 0.71
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgalago is a part of Galago Project (D-BUS-based desktop presence
framework).

%description -l pl.UTF-8
libgalago jest częścią Projektu Galago (bazowany na D-BUSie szkielet
stanu obecności).

%package devel
Summary:	libgalago-gtk header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgalago-gtk
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel >= 0.71

%description devel
Header files for libgalago-based programs development.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia programów opartych o libgalago.

%package static
Summary:	Static libgalago-gtk library
Summary(pl.UTF-8):	Statyczna biblioteka libgalago-gtk
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgalago-gtk library.

%description static -l pl.UTF-8
Statyczna biblioteka libgalago-gtk.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__gettextize}
%{__automake}

%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/autopackage

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_pixmapsdir}/galago

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
