%define _disable_ld_no_undefined 1

Name:		rawtherapee
Version:	4.0.9
Release:	%mkrel 1
Summary:	Raw image processing software
Group:		Graphics
License:	GPLv3 and MIT and IJG
URL:		http://www.rawtherapee.com/
Source0:	http://rawtherapee.googlecode.com/files/%{name}-%{version}.tar.xz
BuildRequires:	cmake >= 2.6
BuildRequires:	gtk2-devel >= 2.12
BuildRequires:	gtkmm2.4-devel
BuildRequires:	lcms2-devel
BuildRequires:	jpeg-devel
BuildRequires:	tiff-devel
BuildRequires:	png-devel
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(libiptcdata)
BuildRequires:	pkgconfig(expat)
BuildRequires:	mercurial
Requires:	hicolor-icon-theme

%description
Rawtherapee is a RAW image processing software. It gives full control over
many parameters to enhance the raw picture before finally exporting it
to some common image format.

%prep
%setup -q

# fix wrong line endings
%__sed -i "s|\r||g" AUTHORS.txt COMPILE.txt

# tell version
%__cat > rtgui/version.h << EOF
#ifndef _VERSION_
#define _VERSION_

#define VERSION "%{version}"
#define TAGDISTANCE 0
#define CACHEFOLDERNAME "RawTherapee${CACHE_NAME_SUFFIX}"
#endif
EOF

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

# These file are taken from the root already
%__rm -rf %{buildroot}%{_datadir}/doc/rawtherapee

%clean
%__rm -rf %{buildroot}

%files
%doc AUTHORS.txt LICENSE.txt COMPILE.txt
%{_bindir}/rawtherapee
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/rawtherapee.png


%changelog
* Mon Jun 04 2012 Alexander Khrukin <akhrukin@mandriva.org> 4.0.9-1mdv2012.0
+ Revision: 802347
- BR pkgconfig(expat)
- version update 4.0.9

* Fri Apr 27 2012 Andrey Bondrov <abondrov@mandriva.org> 4.0.8-1
+ Revision: 793934
- New version 4.0.8, drop useless patches and sources, convert Fedora spec to Mandriva style

* Wed Dec 07 2011 Alexander Khrukin <akhrukin@mandriva.org> 4.0.6-1
+ Revision: 738577
- version update 4.0.6

* Tue Oct 25 2011 Alexander Barakin <abarakin@mandriva.org> 4.0.4-1
+ Revision: 707133
- imported package rawtherapee

