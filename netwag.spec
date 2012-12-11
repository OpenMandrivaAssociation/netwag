%define name netwag
%define version 5.39.0
%define release 1

Summary: A graphic front-end to netwox
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://downloads.sourceforge.net/project/ntwag/netwag/5.39/%{name}-%{version}-src.tgz
Source1: http://downloads.sourceforge.net/project/ntwag/netwag/5.39/%{name}-%{version}-doc_html.tgz
Patch0: netwag-5.35.0-prefix.patch
License: LGPL
Group: Networking/Other
Url: http://www.laurentconstantin.com/fr/netw/netwox/
Requires: netwox = %version
BuildRequires: tk
BuildRequires: netwox = %version
BuildRequires: xterm
BuildArch: noarch

%description
Netwag provides:
  - find tools in netwox
  - running tools in a new window
  - keep track of command history
  - exchange data true the integrate clipboard
  - ect.

%prep
%setup -q -n %name-%version-src
%setup -q -D -T -a1 -n %name-%version-src
%patch0 -p0

%build
cd src
./genemake
%make GCCOPT="$RPM_OPT_FLAGS -D_BSD_SOURCE -D__BSD_SOURCE -D__FAVOR_BSD -DHAVE_NET_ETHERNET_H"

%install
cd src
%makeinstall_std

%files
%doc INSTALL.TXT README.TXT
%doc doc/*.txt
%doc %name-%version-doc_html/*
%_bindir/netwag*
%_mandir/man1/*


%changelog
* Tue Jul 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 5.39.0-1
+ Revision: 808732
- rpmlint
- version update 5.39.0

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 5.35.0-4mdv2010.0
+ Revision: 430168
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 5.35.0-3mdv2009.0
+ Revision: 241093
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Jul 03 2007 Funda Wang <fwang@mandriva.org> 5.35.0-1mdv2008.0
+ Revision: 47502
- rediff patch0
- BR xterm
- New version
- Import netwag

