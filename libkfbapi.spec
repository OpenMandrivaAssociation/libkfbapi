Summary:	Library to access various Facebook services via their public API
Name:		libkfbapi
Version:	1.0
Release:	8
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/extragear/libs/%{name}
Source0:	http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	xsltproc
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	pkgconfig(QJson)

%description
Library to access various Facebook services via their public API.

#----------------------------------------------------------------------------

%package i18n
Summary:	Translations for libkfbapi
Group:		System/Internationalization
BuildArch:	noarch

%description i18n
Translations for libkfbapi.

%files i18n -f %{name}.lang

#----------------------------------------------------------------------------

%define major 1
%define libname %mklibname kfbapi %{major}

%package -n %{libname}
Summary:	Runtime library for libkfbapi
Group:		System/Libraries
Requires:	%{name}-i18n

%description -n %{libname}
Library to access various Facebook services via their public API.

%files -n %{libname}
%{_kde_libdir}/libkfbapi.so.%{major}*

#----------------------------------------------------------------------------

%define devname %mklibname -d kfbapi

%package -n %{devname}
Summary:	Development files for libkfbapi
Group:		Development/KDE and Qt
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for libkfbapi.

%files -n %{devname}
%{_kde_libdir}/libkfbapi.so
%{_kde_includedir}/*
%{_kde_libdir}/pkgconfig/*.pc
%{_kde_libdir}/cmake/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name}
