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

%description
Core libraries to manage the DE to be shared between Maui Settings and Cask

%prep
%autosetup -p1 -n %{name}-%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files 
