%define		_subver	R0
Summary:	AutoScan - a utility for network exploration
Summary(pl):	AutoScan - narzêdzie do odkrywania sieci
Name:		AutoScan
Version:	beta_0.93
Release:	0.%{_subver}.1
License:	GPL
Group:		Networking
Source0:	http://autoscan.free.fr/%{name}-%{version}-%{_subver}.tar.gz
# Source0-md5:	e9532a7af284a37cd312e72cbfa35042
URL:		http://autoscan.free.fr/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libgtkhtml-devel
BuildRequires:	libsmbclient-devel
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The objective of the program is to post the list of all equipment
connected to the network. A list of ports preset is scanned for each
equipment.

%description -l pl
Celem tego programu jest wskazanie wszystkich urz±dzeñ pod³±czonych do
sieci. Dla ka¿dego urz±dzenia przedstawiana jest lista otwartych
portów.

%prep
%setup -q

%build
cd Sources/Autoscan
rm -rf autom4te.cache
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
cd src
%{__make}
cd ../../../

cd Sources/AutoScan_d
rm -rf autom4te.cache
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
cd src
%{__make}
cd ../../../

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/{apps,pixmaps}}

install Sources/Autoscan/src/autoscan $RPM_BUILD_ROOT%{_bindir}/AutoScan
install Sources/AutoScan_d/src/autoscan_d $RPM_BUILD_ROOT%{_bindir}
cp -R Data/apps/AutoScan $RPM_BUILD_ROOT%{_datadir}/apps
cp -R Data/pixmaps/AutoScan $RPM_BUILD_ROOT%{_datadir}/pixmaps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Data/doc/AutoScan
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/%{name}
%{_datadir}/pixmaps/%{name}
