%global rtlastrev changeset:1583:1a1fe5838576
%global rtlasttag Latest-tag:4.0.4,CSet:1583:1a1fe5838576

Name:		rawtherapee
Version:	4.0.4
Release:	%mkrel 1
Summary:	Raw image processing software

Group:		Editors 
License:	GPLv3 and MIT and IJG
URL:		http://www.rawtherapee.com/
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	rawtherapee-icons-3.0.1.tar

BuildRequires:	cmake >= 2.6
BuildRequires:	lcms2-devel
BuildRequires:	gtk2-devel >= 2.12
BuildRequires:	gtkmm2.4-devel
BuildRequires:	lcms-devel  libjpeg-devel libtiff-devel
BuildRequires:	libpng-devel libiptcdata-devel desktop-file-utils
Patch0:		libpng1_5_rawthe.patch	
Requires:	hicolor-icon-theme


%description
Rawtherapee is a RAW image processing software. It gives full control over
many parameters to enhance the raw picture before finally exporting it
to some common image format.


%prep
%setup -q
%patch0 -p1

# fix wrong line endings
sed -i "s|\r||g" AUTHORS.txt COMPILE.txt

# Do not move LICENSE.txt and AUTHORS.txt in bindir
sed -i "s|install (FILES AUTHOR.*$||" CMakeLists.txt

# Do not install useless rtstart:
sed -i "s|install (PROGRAMS rtstart|\#install (PROGRAMS rtstart|" CMakeLists.txt

# Tell version
cat > rtgui/version.h << EOF
#ifndef _VERSION_
#define _VERSION_

#define VERSION "%{rtlastrev} %{rtlasttag}"
#define TAGDISTANCE %{rtdist}
#define CACHEFOLDERNAME "RawTherapee${CACHE_NAME_SUFFIX}"
#endif
EOF

cat > AboutThisBuild.txt << EOF
See package informations
EOF

%build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=None -DAUTOMATED_BUILD_SYSTEM:BOOL=ON -DLIBDIR=%{_libdir}  -DBINDIR=%{_bindir} .
make VERBOSE=1 %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT 

desktop-file-install --dir $RPM_BUILD_ROOT/%{_datadir}/applications/ %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/16x16/apps/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/



# These file are taken from the root already
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/rawtherapee

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor
fi 
%{_bindir}/update-desktop-database %{_datadir}/applications || :

/sbin/ldconfig

%postun
%{_bindir}/update-desktop-database %{_datadir}/applications
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor
fi || :

/sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS.txt LICENSE.txt COMPILE.txt
%{_bindir}/rawtherapee
#% {_libdir}/*.so
#% {_datadir}/doc/rawtherapee/AUTHORS.txt
#% {_datadir}/doc/rawtherapee/COMPILE.txt
#% {_datadir}/doc/rawtherapee/LICENSE.txt
%{_datadir}/rawtherapee/images
%{_datadir}/rawtherapee/options
%{_datadir}/rawtherapee/profiles
%{_datadir}/rawtherapee/sounds
%{_datadir}/rawtherapee/languages
%{_datadir}/rawtherapee/themes
%{_datadir}/rawtherapee/iccprofiles
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/rawtherapee.png
