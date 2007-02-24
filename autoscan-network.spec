#	installed but not packaged:
#		/usr/lib/menu/AutoScan
%define		_subver	R1
Summary:	AutoScan - a utility for network exploration
Summary(pl.UTF-8):	AutoScan - narzędzie do odkrywania sieci
Name:		AutoScan
Version:	0.99
Release:	0.%{_subver}.1
License:	GPL
Group:		Networking
Source0:	http://autoscan.free.fr/Download/%{name}.%{version}_%{_subver}.tar.gz
# Source0-md5:	69aefe0da6ca19573e65245154296321
URL:		http://autoscan.free.fr/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libao-devel >= 0.8.5
BuildRequires:	libgtkhtml-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	net-snmp-devel >= 5.0
BuildRequires:	vte-devel >= 0.11.12
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	gnome-vfs2-devel >= 2.8.4
BuildRequires:	gnome-keyring-devel >= 0.4.2
BuildRequires:	libbonoboui-devel >= 2.8.1
BuildRequires:	pango-devel >= 1.8.1
BuildRequires:	libgnomeui-devel >= 2.8.1
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The objective of the program is to post the list of all equipment
connected to the network. A list of ports preset is scanned for each
equipment.

%description -l pl.UTF-8
Celem tego programu jest wskazanie wszystkich urządzeń podłączonych do
sieci. Dla każdego urządzenia przedstawiana jest lista otwartych
portów.

%prep
%setup -q -n %{name}-%{version}_%{_subver}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT{%{_datadir}/{apps,pixmaps,applications,sounds,icons}}

install bin/AutoScan_Network $RPM_BUILD_ROOT%{_bindir}
install bin/AutoScan_Agent $RPM_BUILD_ROOT%{_bindir}
cp -R usr/* $RPM_BUILD_ROOT/usr/
rm -f $RPM_BUILD_ROOT/usr/share/doc/AutoScan/copyright

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/%{name}
%{_datadir}/pixmaps/%{name}
%{_datadir}/sounds/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/%{name}.png
