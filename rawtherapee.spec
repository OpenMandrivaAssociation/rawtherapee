#global optflags %{optflags} -latomic

%global optflags %{optflags} -O3

Name:		rawtherapee
Version:	5.6
Release:	1
Summary:	Raw image processing software
Group:		Graphics
License:	GPLv3 and MIT and IJG
URL:		http://www.rawtherapee.com/
Source0:	http://rawtherapee.com/shared/source/%{name}-%{version}.tar.xz

BuildRequires:	cmake >= 2.6
BuildRequires:	pkgconfig(expat) >= 2.0
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(fftw3f)
BuildRequires:	pkgconfig(gio-2.0) >= 2.16
BuildRequires:	pkgconfig(giomm-2.4) >= 2.12
BuildRequires:	pkgconfig(glib-2.0) >= 2.16
BuildRequires:	pkgconfig(glibmm-2.4) >= 2.16
BuildRequires:	pkgconfig(gobject-2.0) >= 2.16
BuildRequires:	pkgconfig(gthread-2.0) >= 2.16
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.12
BuildRequires:	pkgconfig(gtkmm-3.0)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(lensfun)
BuildRequires:	pkgconfig(libcanberra-gtk)
BuildRequires:	pkgconfig(libiptcdata)
BuildRequires:	pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:	bzip2-devel
BuildRequires:	mercurial
BuildRequires:	jpeg-devel
BuildRequires:	tiff-devel
BuildRequires:	png-devel
BuildRequires:	libgomp-devel
BuildRequires:  libatomic-devel
Requires:	hicolor-icon-theme

%description
Rawtherapee is a RAW image processing software. It gives full control over
many parameters to enhance the raw picture before finally exporting it
to some common image format.

%prep
%setup -q -n %{name}-%{version}
%apply_patches

%build
# Force GCC due to clang crash at build
#export CC=gcc
#export CXX=g++
%cmake -DBUILD_SHARED_LIBS=OFF
%make_build

%install
%make_install -C build

# These file are taken from the root already
rm -rf %{buildroot}%{_datadir}/doc/rawtherapee

%files
%doc AUTHORS.txt LICENSE.txt RELEASE_NOTES.txt
%{_bindir}/rawtherapee
# %{_bindir}/camconst.json
%{_bindir}/rawtherapee-cli
%{_datadir}/rawtherapee
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/com.rawtherapee.RawTherapee.appdata.xml
%{_iconsdir}/hicolor/*/apps/rawtherapee.png
%{_mandir}/man1/%{name}.1*
