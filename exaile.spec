%define debug_package %{nil}

Summary:	A powerful GTK+ 2.x media player
Name:		exaile
Version:	0.3.2.2
Release:	%mkrel 1
Epoch:		1
Group:		Sound
License:	GPLv3
URL:		http://www.exaile.org/
Source0:	http://www.exaile.org/files/%{name}-%{version}.tar.bz2
# (tpg) somehow a musictracker plugin for pidgin doesnt work... http://code.google.com/p/pidgin-musictracker/issues/detail?id=164
# let's use native plugin for exaile
# http://sourceforge.net/projects/exailemusictrac/
Source1:	http://downloads.sourceforge.net/project/exailemusictrac/%{name}musictracker-0.1.2.tar.bz2
BuildRequires:	pygtk2.0-devel
BuildRequires:	python-gobject-devel
BuildRequires:	python-devel
BuildRequires:	intltool
BuildRequires:	gettext-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	help2man
Requires:	pygtk2.0
Requires:	python-sqlite2
Requires:	pygtk2.0-libglade
Requires:	gstreamer0.10-python
Requires:	gstreamer0.10-plugins-good
Requires:	gstreamer0.10-plugins-base
Requires:	gstreamer0.10-plugins-ugly
Requires:	gstreamer0.10-cdio
Requires:	gstreamer0.10-moodbar
Requires:	dbus-python
Requires:	mutagen
Requires:	python-elementtree
Requires:	python-notify
Requires:	python-gpod
Requires:	python-CDDB
Requires:	python-sexy
Requires:	python-gamin
Requires:	python-pyinotify
BuildArch:	noarch
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
%setup -qn %{name}-%{version}
# (tpg) unpack the plugin
tar xf %{SOURCE1} -C plugins/

%build
export CFLAGS="%{optflags}"
%make

%install
rm -rf %{buildroot}
%makeinstall_std PREFIX=%{_prefix} LIBINSTALLDIR=/share DESTDIR=%{buildroot}

# Find the localization
%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%endif

%if %mdkversion < 200900
%postun
%{update_menus}
%{clean_desktop_database}
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{_sysconfdir}/xdg/exaile
%{_sysconfdir}/xdg/exaile/settings.ini
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/man1/%{name}.*
