#global	debug_package %%{nil}
%global	__requires_exclude ^typelib\\(GtkosxApplication\\)(.*)|^typelib\\(WebKit2\\) = 4.0

Summary:	A powerful GTK+ media player
Name:	exaile
Version:	4.2.0
Release:	1
License:	GPLv3+
Group:	Sound
Url:		https://www.exaile.org/
Source0:	https://github.com/exaile/exaile/archive/v%{version}/%{name}-%{version}.tar.gz
# Avoid a bazilion of rpmlint errors
Patch0:	exaile-4.1.4-disable-bytecompiling.patch
#Patch1:	exaile-4.1.4-avoid-appdatacli-validation-errors.patch
BuildRequires:	make
BuildRequires:	gettext
BuildRequires:	gir-repository
BuildRequires:	gobject-introspection
BuildRequires:	help2man
BuildRequires:	intltool
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(sphinx)
BuildRequires:	python3dist(sphinx-rtd-theme)
Requires:	gstreamer1.0-plugins-good
Requires:	gstreamer1.0-plugins-base 
Requires:	gstreamer1.0-plugins-ugly
Requires:	gstreamer1.0-plugins-bad
Requires:	gstreamer1.0-cdio
Requires:	python-gi
Requires:	python-gobject3
Requires:	python-gstreamer1.0
Requires:	python3dist(beautifulsoup4)
Requires:	python3dist(bsddb3)
Requires:	python3dist(dbus-python)
Requires:	python3dist(feedparser)
#Requires:	python3-musicbrainzngs
Requires:	python3dist(mutagen)
Requires:	python3dist(pycairo)
Requires:	python3dist(pylast)
Requires:	typelib(GstBase)
Requires:	typelib(Gtk) = 3.0
Requires:	typelib(Keybinder)
Requires:	typelib(Rsvg)
Requires:	udisks2
BuildArch:	noarch

%description
Exaile is a media player aiming to be similar to KDE's AmaroK, but for GTK+.
It incorporates many of the cool things from AmaroK (and other media players).
Some of the features are:
- automatic fetching of album art;
- handling of large libraries;
- lyrics fetching;
- artist/album information via the wikipedia;
- last.fm support;
- optional iPod support (assuming you have python-gpod installed);
- builtin shoutcast directory browser;
- tabbed playlists;
- blacklisting of tracks;
- downloading of guitar tabs from fretplay.com;
- submitting played tracks on the iPod to last.fm.

%files -f %{name}.lang
%license COPYING
%doc README.md
%config(noreplace) %{_sysconfdir}/xdg/%{name}/
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/dbus-1/services/org.%{name}.Exaile.service
%{_datadir}/metainfo/org.%{name}.%{name}.appdata.xml
%{_iconsdir}/hicolor/*x*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%make_build all


%install
# Exaile launcher works with LIBINSTALLDIR which is a relative path from %%{_prefix}.
%make_install PREFIX=%{_prefix} LIBINSTALLDIR=%{_datadir} DESTDIR=%{buildroot}

%find_lang %{name}

