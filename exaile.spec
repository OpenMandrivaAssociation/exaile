%define firefox_lib %(pkg-config --variable=libdir firefox-gtkmozembed)

Summary:	A powerful GTK+ 2.x media player
Name:		exaile
Version:	0.2.13
Release:	%mkrel 6
Epoch:		1
Group:		Sound
License:	GPL+ and Artistic
URL:		http://www.exaile.org/
Source0:	http://www.exaile.org/files/%{name}_%{version}.tar.bz2
Patch0:		%{name}_0.2.13-support-xfburn.patch
# (tpg) https://bugs.launchpad.net/exaile/+bug/208351
Patch1:		exaile-save_files_panel_dir.patch
# (tpg) https://bugs.launchpad.net/exaile/+bug/207866
Patch2:		dbhit-etc.patch
Patch3:		%{name}_0.2.13-correct-ipod-mount-path.patch
# (tpg) https://bugs.launchpad.net/exaile/+bug/211325
Patch4:		exaile-collection_manual_rescan_fix.patch
# (tpg) https://bugs.launchpad.net/exaile/+bug/233894
Patch5:		list_performance.patch
# (tpg) https://bugs.launchpad.net/exaile/+bug/233899
Patch6:		tag_editor.patch
BuildRequires:	pygtk2.0-devel
BuildRequires:	python-devel
BuildRequires:	intltool
BuildRequires:	gettext-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	libmozilla-firefox-devel
Requires:	pygtk2.0
Requires:	python-sqlite2
Requires:	pygtk2.0-libglade
Requires:	gstreamer0.10-python
Requires:	gstreamer0.10-plugins-good
Requires:	gstreamer0.10-plugins-base 
Requires:	gstreamer0.10-plugins-ugly
Requires:	dbus-python
Requires:	mutagen python-elementtree
Requires:	gnome-python-gtkmozembed
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
%setup -q -n %{name}_%{version}
%patch0 -p1 -b .xfburn
%patch1 -p0
%patch2 -p0
%patch3 -p1
%patch4 -p0
%patch5 -p0
%patch6 -p0

# remove shebangs from all files as none should be executable scripts
sed -e '/^#!\//,1 d' -i plugins/*.py xl/plugins/*.py xl/*.py exaile.py
# (tpg) https://bugs.launchpad.net/exaile/+bug/145250
perl -pi -e "s/Exec=exaile/Exec=exaile --no-equalizer/g" %{name}.desktop

%build
export CFLAGS="%{optflags}"

%make

%install
rm -rf %{buildroot}
%makeinstall_std PREFIX=%{_prefix} LIBDIR=/%{_lib} FIREFOX=%{firefox_lib} DESTDIR=%{buildroot}

chmod 755 %{buildroot}%{_libdir}/exaile/mmkeys.so
chmod 755 %{buildroot}%{_libdir}/exaile/xl/burn.py
chmod 755 %{buildroot}%{_libdir}/exaile/xl/plugins/gui.py
chmod 755 %{buildroot}%{_libdir}/exaile/xl/cd_import.py

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

%files -f %{name}.lang
%defattr(-,root,root)
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_libdir}/%{name}/*
%{_mandir}/man1/*
