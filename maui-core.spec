%define major 0

%define libname %mklibname MauiCore
%define devname %mklibname -d MauiCore

Name:		maui-core
Version:	0.6.0
Release:	1
Summary:	Core libraries to manage the DE to be shared between Maui Settings and Cask.
Url:		http://mauikit.org/
Source0:	https://github.com/Nitrux/maui-core/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
License:	LGPL-2.1-or-later, CC0 1.0, BSD-2-Clause
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(MauiKit)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KDecoration2)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:  cmake(KF5IdleTime)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  sound-theme-freedesktop

%description
Core libraries to manage the DE to be shared between Maui Settings and Cask

%package -n %{libname}
Summary:	Library files for maui-core
Group:		System/Libraries

%description -n %{libname}
Core libraries to manage the DE to be shared between Maui Settings and Cask

%package -n %{devname}
Summary:	Development files for maui-core
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for maui-core

%prep
%autosetup -p1 -n %{name}-%{version}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/libMauiCoreAudio.so.%{major}*
%{_libdir}/libMauiCoreNotifications.so.%{major}*
%{_libdir}/libMauiCorePower.so.%{major}*
%{_libdir}/qt5/qml/org/mauicore/audio/
%{_libdir}/qt5/qml/org/mauicore/notifications/
%{_libdir}/qt5/qml/org/mauicore/power/

%files -n %{devname}
%{_includedir}/Maui/Core/
%{_libdir}/cmake/MauiCore/
%{_libdir}/cmake/MauiCoreAudio/
%{_libdir}/cmake/MauiCoreNotifications/
%{_libdir}/cmake/MauiCorePower/
%{_libdir}/libMauiCoreAudio.so
%{_libdir}/libMauiCoreNotifications.so
%{_libdir}/libMauiCorePower.so
