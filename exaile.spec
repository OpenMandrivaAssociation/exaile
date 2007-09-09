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
URL:		http://www.exaile.org/
Group:		Sound
License:	GPL
BuildRequires:	pygtk2.0-devel
BuildRequires:	python-devel
BuildRequires:	intltool
BuildRequires:	perl(XML::Parser)
Requires:	pygtk2.0
Requires:	python-sqlite2
Requires:	pygtk2.0-libglade
Requires:	gstreamer0.10-python
Requires:	gstreamer0.10-plugins-good
Requires:	gstreamer0.10-plugins-base 
Requires:	gstreamer0.10-plugins-ugly
Requires:	dbus-python
Requires:	mutagen python-elementtree
#Requires:	gnome-python-gtkmozembed
%if %mdvver > 200700
Requires:	python-notify
Requires:	python-gpod
Requires:	python-CDDB
Requires:	python-sexy
Requires:	python-gamin
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

#Fix typo in the desktop file
sed -i 's/MimeType=M/M/' exaile.desktop 
# remove shebangs from all files as none should be executable scripts
sed -e '/^#!\//,1 d' -i plugins/*.py exaile.py

%build
export CFLAGS="%{optflags}"

# Mandrivaify the default settings
perl -pi -e "s#/media/ipod#/media/disk#g" ./xl/prefs.py ./xl/panels.py
# Patch the makefile for later pythons
PYTHON_VER=%{py_ver}	# Don't ask me why this hack is needed, but it is.
perl -pi -e "s#python2.4#python$PYTHON_VER#g" ./mmkeys/Makefile

%make

%install
rm -rf %{buildroot}
%makeinstall_std PREFIX=%{_prefix} LIBDIR=%{_libdir} DESTDIR=%{buildroot}

#%py_compile $RPM_BUILD_ROOT/usr/share/exaile

chmod 755 %{buildroot}%{_bindir}/exaile

chmod 755 %{buildroot}%{_libdir}/exaile/mmkeys.so

# Find the localization
%find_lang %{name}

%post
%{update_menus}
%{update_desktop_database}

%postun
%{update_menus}
%{clean_desktop_database}

%clean 
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc TODO
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_libdir}/%{name}/mmkeys.so
%{_mandir}/man1/*
