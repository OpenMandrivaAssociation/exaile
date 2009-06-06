%define debug_package %{nil}

%define prel a2

Summary:	A powerful GTK+ 2.x media player
Name:		exaile
Version:	0.3.0
Release:	%mkrel -c %prel 1
Epoch:		1
Group:		Sound
License:	GPLv3
URL:		http://www.exaile.org/
Source0:	http://www.exaile.org/files/%{name}_%{version}%prel.tar.bz2
Patch0:		%{name}_0.2.13-support-xfburn.patch
Patch1:		exaile_0.3.0a2-install_all_plugins.patch
# (tpg) https://bugs.launchpad.net/exaile/+bug/207866
Patch3:		%{name}_0.2.13-correct-ipod-mount-path.patch
# (tpg) https://bugs.launchpad.net/exaile/+bug/233899
Patch6:		tag_editor.patch
Patch7:		%{name}-0.2.13-makefile.patch
BuildRequires:	pygtk2.0-devel
BuildRequires:	python-devel
BuildRequires:	intltool
BuildRequires:	gettext-devel
BuildRequires:	perl(XML::Parser)
#BuildRequires:	gnome-python-gtkmozembed
Requires:	pygtk2.0
Requires:	python-sqlite2
Requires:	pygtk2.0-libglade
Requires:	gstreamer0.10-python
Requires:	gstreamer0.10-plugins-good
Requires:	gstreamer0.10-plugins-base
Requires:	gstreamer0.10-plugins-ugly
Requires:	dbus-python
Requires:	mutagen
Requires:	python-elementtree
#Requires:	gnome-python-gtkmozembed
Requires:	python-notify
Requires:	python-gpod
Requires:	python-CDDB
Requires:	python-sexy
Requires:	python-gamin
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
%setup -qn %{name}_%{version}%prel
%patch1 -p1
#%patch0 -p1 -b .xfburn
#%patch3 -p1
#%patch6 -p0
#%patch7 -p0

# remove shebangs from all files as none should be executable scripts
#sed -e '/^#!\//,1 d' -i plugins/*.py xl/plugins/*.py xl/*.py exaile.py

# (tpg) https://bugs.launchpad.net/exaile/+bug/145250
#perl -pi -e "s/Exec=exaile/Exec=exaile --no-equalizer/g" %{name}.desktop

%build
export CFLAGS="%{optflags}"

#ifarch x86_64
#define gre_conf %{_sysconfdir}/gre.d/1.9-64.system.conf
#else
#define gre_conf %{_sysconfdir}/gre.d/1.9.system.conf
#endif

%make

%install
rm -rf %{buildroot}
%makeinstall_std PREFIX=%{_prefix} LIBDIR=/%{_lib} DESTDIR=%{buildroot}
#GRE_CONF_PATH=%{gre_conf} PREFIX=%{_prefix} LIBDIR=/%{_lib} DESTDIR=%{buildroot}

#chmod 755 %{buildroot}%{_libdir}/exaile/mmkeys.so
#chmod 755 %{buildroot}%{_libdir}/exaile/xl/burn.py
#chmod 755 %{buildroot}%{_libdir}/exaile/xl/plugins/gui.py
#chmod 755 %{buildroot}%{_libdir}/exaile/xl/cd_import.py

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
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_libdir}/%{name}/*
#%{_mandir}/man1/*
