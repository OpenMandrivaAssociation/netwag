%define name netwag
%define version 5.4.0
%define release 1mdk

Summary: A graphic front-end to netwox
Summary(fr): Une interface graphique à netwox.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}-src.tar.bz2
Source1: %{name}-%{version}-doc_html.tar.bz2
Patch0: %name-5.4.0.genemake.patch.bz2
License: LGPL
Group: Networking/Other
Url: http://www.laurentconstantin.com/fr/netw/netwox/
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: netwox = %version
BuildRequires: tk
BuildRequires: netwox = %version
BuildRequires: tk
BuildArch: noarch

%description
Netwag provides:
  - find tools in netwox
  - running tools in a new window
  - keep track of command history
  - exchange data true the integrate clipboard
  - ect.

%description -l fr
Netwag permet de :
  - chercher parmi les outils de netwox
  - exécuter les outils dans une nouvelle fenêtre, ou une zone texte
  - garder un historique des commandes
  - échanger des données en utilisant les deux presse-papier intégrés
  - etc.

%prep
%setup -q -n %name-%version-src
%setup -q -D -T -a1 -n %name-%version-src
%patch0 -p1

perl -pi -e 's!^NETWIBDEF_INSTPREFIX=.*!NETWIBDEF_INSTPREFIX=/usr!' src/config.dat
perl -pi -e 's!^NETWOXDEF_INSTPREFIX=.*!NETWOXDEF_INSTPREFIX=/usr!' src/config.dat
# Hacking for lib64
perl -pi -e 's!^NETWIBDEF_INSTLIB=.*!NETWIBDEF_INSTLIB=%_libdir!' src/config.dat

perl -pi -e 's!^NETWIBDEF_SYSARCH=.*!NETWIBDEF_SYSARCH=%_arch!' src/config.dat

%build
cd src
./genemake
%make GCCOPT="$RPM_OPT_FLAGS -D_BSD_SOURCE -D__BSD_SOURCE -D__FAVOR_BSD -DHAVE_NET_ETHERNET_H"

%install
rm -rf $RPM_BUILD_ROOT
cd src
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc INSTALL.TXT README.TXT
%doc doc/*.txt
%doc %name-%version-doc_html/*
%_bindir/netwag*
%_mandir/man1/*
