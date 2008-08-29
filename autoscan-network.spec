Summary:	AutoScan - a utility for network exploration
Summary(pl.UTF-8):	AutoScan - narzędzie do odkrywania sieci
Name:		autoscan-network
Version:	1.12
Release:	0.1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://autoscan.fr/download/%{name}-%{version}.tar.gz
# Source0-md5:	59c94af105807738c379586447755e20
Patch0:		%{name}-install.patch
URL:		http://autoscan.free.fr/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-keyring-devel >= 0.4.2
BuildRequires:	gnome-vfs2-devel >= 2.8.4
BuildRequires:	libao-devel >= 0.8.5
BuildRequires:	libbonoboui-devel >= 2.8.1
BuildRequires:	libgnomeui-devel >= 2.8.1
BuildRequires:	libgtkhtml-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	net-snmp-devel >= 5.0
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pango-devel >= 1.8.1
BuildRequires:	vte-devel >= 0.11.12
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AutoScan Network is an application designed to explore and to manage
your network.

Some features:
- Automatic network discovery
- Entire subnets can be scanned simultaneously without human
  intervention
- Addition time-reality of the new machines put on the network
- Detection of the OS, brand and model known (possibility to add an
  unknown equipment in the database)
- Ability to save the network state
- A Samba share browser
- A Nessus client

%description -l pl.UTF-8
AutoScan Network to aplikacja przeznaczona do odkrywania i zarządzania
siecią.

Wybrane cechy:
- automatyczne odkrywanie sieci
- można skanować jednocześnie całe podsieci bez udziału człowieka
- dodawanie w czasie rzeczywistym nowych maszyn umieszczonych w sieci
- wykrywanie systemu operacyjnego, marki i modelu (z możliwością
  dodania nieznanego sprzętu do bazy)
- możliwość zapisu stanu sieci
- przeglądarka udziałów Samby
- klient Nessusa

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/%{name}
%{_datadir}/pixmaps/%{name}
%{_datadir}/sounds/%{name}
%{_desktopdir}/%{name}.desktop
%{_datadir}/icons/%{name}.png
