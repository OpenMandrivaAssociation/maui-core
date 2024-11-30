%define major 0

%define libname %mklibname MauiCore
%define devname %mklibname -d MauiCore

Name:		maui-core
Version:	0.6.6
Release:	3.20240611
Summary:	Core libraries to manage the DE to be shared between Maui Settings and Cask.
Url:		https://mauikit.org/
#Source0:	https://github.com/Nitrux/maui-core/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
# Use git to pull qt6 version
Source0:  maui-core-main.tar.gz
License:	LGPL-2.1-or-later, CC0 1.0, BSD-2-Clause
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(MauiKit4)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KDecoration2)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6WindowSystem)
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
%autosetup -p1 -n %{name}-main
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
