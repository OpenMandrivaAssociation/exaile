%define	name	exaile
%define	version 0.2.10
%define realver %version
%define rel	1
%define	release	%mkrel %rel

Name:		%{name}
Summary:	A powerful GTK+ 2.x media player
Version:	%{version} 
Release:	%{release} 
Source0:	%{name}_%{realver}.tar.bz2
Patch1:		color_depth.patch
URL:		http://www.exaile.org/
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
BuildRequires:	pygtk2.0-devel python-devel intltool
Requires:	pygtk2.0 python-sqlite2 gstreamer0.10-python pygtk2.0-libglade
Requires:	gstreamer0.10-plugins-good gstreamer0.10-plugins-base 
Requires:	gstreamer0.10-plugins-ugly
Requires:	dbus-python
Requires:	mutagen python-elementtree gnome-python-gtkmozembed
%if %mdvver > 200700
Requires:	python-notify
%endif

%description
Exaile is a media player aiming to be similar to KDE's AmaroK,
but for GTK+ 2.x. It incorporates many of the cool things from AmaroK
(and other media players).

Some of the features are:
- automatic fetching of album art
- handling of large libraries 
- lyrics fetching
- artist/album information via the wikipedia
- last.fm support
- optional iPod support (assuming you have python-gpod installed).
- builtin shoutcast directory browser
- tabbed playlists
- blacklisting of tracks
- downloading of guitar tabs from fretplay.com
- submitting played tracks on the iPod to last.fm

%prep
%setup -q -n %{name}_%realver
%patch1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} << EOF
?package(%name): needs="x11" \
        section="Multimedia/Sound" \
        title="Exaile" \
        longtitle="Listen to, browse, or edit your audio collection"\
        command="%{_bindir}/%{name}" \
        icon="%{name}.png" \
        xdg="true"
EOF
# Mandrivaify the desktop file
perl -pi -e "s#Categories=#Categories=X-MandrivaLinux-Multimedia-Sound;Sound;GNOME;#" ./exaile.desktop
# Mandrivaify the default settings
perl -pi -e "s#/media/ipod#/media/disk#g" ./xl/prefs.py ./xl/panels.py
# Patch the makefile for later pythons
PYTHON_VER=%py_ver	# Don't ask me why this hack is needed, but it is.
perl -pi -e "s#python2.4#python$PYTHON_VER#g" ./mmkeys/Makefile

make		DESTDIR=$RPM_BUILD_ROOT PREFIX=/usr/ LIBDIR=%_libdir
%makeinstall	DESTDIR=$RPM_BUILD_ROOT PREFIX=/usr/

%py_compile $RPM_BUILD_ROOT/usr/share/exaile

# Find the localization
%find_lang %{name}

%post
%update_desktop_database
%update_menus

%postun
%clean_desktop_database
%update_menus

%clean 
rm -rf $RPM_BUILD_ROOT 

%files -f %name.lang
%defattr(-,root,root)
%doc TODO
%_bindir/%name
%_datadir/%name/
%_datadir/applications/*
%_datadir/pixmaps/*
%_menudir/%name
%_libdir/exaile/mmkeys.so
%_datadir/man/man1/exaile.1.bz2
