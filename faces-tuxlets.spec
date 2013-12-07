Summary:	Tuxlets face icons by Arvi Pingus
Name:		faces-tuxlets
Version:	1.1
Release:	2
License:	Artistic
URL:		https://abf.rosalinux.ru/moondrake/faces-tuxlets
Group:		System/Configuration/Other	
Source0:	%{name}-%{version}.tar.xz
BuildArch:	noarch

%description
Tuxlets face icons theme provided by Arvi Pingus.

%prep
%setup -q

%build

%install
%makeinstall_std

%files
%{_datadir}/mdk/faces/01-tuxlets
