%define debug_package %{nil}
%global __requires_exclude	%{?__requires_exclude:%__requires_exclude|}typelib\\(GtkosxApplication

Summary:	A powerful GTK+ 2.x media player
Name:		exaile
Version:	4.1.3
Release:	1
Group:		Sound
License:	GPLv3
URL:		http://www.exaile.org/
Source0:	https://github.com/exaile/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gir-repository
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(python)
BuildRequires:	intltool
BuildRequires:	gettext
BuildRequires:	help2man
BuildRequires:	gobject-introspection
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	python3dist(sphinx)

Requires:	gstreamer1.0-plugins-good
Requires:	gstreamer1.0-plugins-base 
Requires:	gstreamer1.0-plugins-ugly
Requires:	gstreamer1.0-plugins-bad
Requires:	gstreamer1.0-cdio
Requires:	python3dist(beautifulsoup4)
Requires:	python3dist(pycairo)
Requires:	python-gi
Requires:	python3dist(dbus-python)
Requires:	python3dist(feedparser)
Requires:	python-gobject3
Requires:	python-gstreamer1.0
#Requires:	python3-musicbrainzngs
Requires:	python3dist(mutagen)
Requires:	python3dist(pylast)
Requires: python3dist(bsddb3)
Requires:	typelib(GstBase)
Requires:	typelib(Gtk) = 3.0
Requires:	typelib(Keybinder)
Requires:	typelib(Rsvg)
Requires:	udisks2
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

%build

%make locale

%install

# Exaile launcher works with LIBINSTALLDIR which is a relative path from %%{_prefix}.
%makeinstall_std PREFIX=%{_prefix} LIBINSTALLDIR=%{_datadir} DESTDIR=%{buildroot}


# Find the localization
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%config(noreplace) %{_sysconfdir}/xdg/%{name}/
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/exaile.appdata.xml
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/dbus-1/services/org.%{name}.Exaile.service

%changelog
* Sat Jul 30 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.3.2.2-1mdv2012.0
+ Revision: 692419
- update to new version 0.3.2.2

* Sat Mar 12 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.3.2.1-1
+ Revision: 644019
- update to new version 0.3.2.1

* Sat Jul 10 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.3.2.0-1mdv2011.0
+ Revision: 550138
- update to new version 0.3.2.0

* Mon Apr 19 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.3.1.1-1mdv2010.1
+ Revision: 536787
- update to new vewrsion 0.3.1.1

* Tue Apr 06 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.3.1.0-1mdv2010.1
+ Revision: 532335
- update to new version 0.3.1.0

* Sat Feb 20 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.3.1-0.b.2mdv2010.1
+ Revision: 508831
- update exailemusictracker plugin to new version 0.1.2

* Wed Feb 17 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.3.1-0.b.1mdv2010.1
+ Revision: 507304
- update to new version 0.3.1-beta

* Thu Dec 31 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.3.0.2-2mdv2010.1
+ Revision: 484455
- add exailemusictracker plugin

* Wed Nov 25 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.3.0.2-1mdv2010.1
+ Revision: 470128
- update to new version 0.3.0.2

* Sun Oct 11 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.3.0.1-2mdv2010.0
+ Revision: 456687
- add requires for gstreamer0.10-cdio and gstreamer0.10-moodbar

* Sun Sep 20 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.3.0.1-1mdv2010.0
+ Revision: 445385
- update to new version 0.3.0.1

* Sun Aug 30 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.3.0-1mdv2010.0
+ Revision: 422364
- fix installation directory
- update to new version 0.3.0
- drop all patches
- spec file clean

* Mon Jun 08 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.3.0-0.a2.4mdv2010.0
+ Revision: 383805
- Patch2: fix support for pyinotify

* Sun Jun 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.3.0-0.a2.3mdv2010.0
+ Revision: 383756
- add requires on python-pyinotify

* Sat Jun 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.3.0-0.a2.2mdv2010.0
+ Revision: 383272
- move files to share dir

* Sat Jun 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.3.0-0.a2.1mdv2010.0
+ Revision: 383231
- package is noarch now
- drop requires on mozilla related stuff
- Patch1: install all plugins
- update to new prerelease 0.3.0a2

* Thu Jan 29 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.3.0-0.a1.1mdv2009.1
+ Revision: 335289
- disable all patches
- update to new version 0.3.0a1

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 1:0.2.14-2mdv2009.1
+ Revision: 320328
- rebuild for new python

* Sat Oct 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.2.14-1mdv2009.1
+ Revision: 292533
- update to new version 0.2.14 (bugfix release)
- drop merged patches 1,2,4 and 5

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1:0.2.13-8mdv2009.0
+ Revision: 266737
- rebuild early 2009.0 package (before pixel changes)

* Wed Aug 06 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.2.13-7mdv2009.0
+ Revision: 264549
- Patch7: fix makefile
- pass correct MOZILLA_FIVE_HOME variable, it is extracted from /etc/gre.d/*.conf

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Jun 03 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.2.13-6mdv2009.0
+ Revision: 214570
- Patch4: fix manual collection rescan
- Patch5: improve performance
- Patch6: fix tag editor

* Thu May 01 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.2.13-5mdv2009.0
+ Revision: 199878
- Patch3: fix ipod mount path
- remove shebangs for files
- fix license
- spec file clean

* Thu May 01 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.2.13-4mdv2009.0
+ Revision: 199868
- Patch1: save last directory on files tab
- Patch2: do not hit collection database so often

* Sun Apr 20 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.2.13-3mdv2009.0
+ Revision: 195965
- rebuild for new firefox

* Fri Apr 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.2.13-2mdv2009.0
+ Revision: 195658
- Patch0: add support for xfburn

* Sat Apr 12 2008 Funda Wang <fwang@mandriva.org> 1:0.2.13-1mdv2009.0
+ Revision: 192630
- fix tarball dir

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - new version
    - br gettext-devel

* Fri Mar 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.2.12-1mdv2008.1
+ Revision: 190809
- new version (upstream has messed up the versioning, epoch is needed)
- handle nicely firefox version

* Wed Feb 20 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.12b-1mdv2008.1
+ Revision: 173382
- no docs
- drop patch 1, fixed upstream
- drop patch 0, fixed upstream
- new version

* Wed Jan 23 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.11.1-3mdv2008.1
+ Revision: 156931
- speed up(about two times) music library loading with patch 0
- hopefully fix bug #36608 by adding patch 1
- gstreamer sound volume is broken, especially with apps which are using its equalizer, thus makes exaile sound volume lower. running exaile with --no-equalizer solves this.Anyways added it to the *.desktop file

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.11.1-2mdv2008.1
+ Revision: 117657
- rebuild for new firefox

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 0.2.11.1-1mdv2008.1
+ Revision: 109290
- fix tarball dir

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - new version (correct tarball with no entire bzr branch, source is now ~800 KB ;)

* Mon Nov 05 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.11-3mdv2008.1
+ Revision: 106136
- rebuild against new mozilla-firefox-2.0.0.9

* Fri Oct 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.11-2mdv2008.1
+ Revision: 100488
- rebuild against ff 2.0.0.8
- new license policy

* Thu Oct 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.11-1mdv2008.1
+ Revision: 99846
- final release

* Thu Oct 11 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.11-0.b.1mdv2008.1
+ Revision: 97214
- update to latest beta release
- do not hardcode icon extension in desktop file
- mark executable some files
- set path to firefox
- fix file list
- spec file clean

* Sun Sep 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.10-3mdv2008.0
+ Revision: 92415
- readd requires on gnome-python-gtkmozembed
- correct url for source0

  + Emmanuel Andry <eandry@mandriva.org>
    - add P0 to fix bug #33970

* Sun Sep 09 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.10-1mdv2008.0
+ Revision: 83475
- drop old menu style
  add requires on python-CDDb,python-sexy,python-gamin
  remove requires on gnome-python-gtkmozembed
  compile with optflags
  use macros
  spec file clean

  + Jérôme Soyer <saispo@mandriva.org>
    - Fix Requires
      New release 0.2.10

  + Thierry Vignaud <tv@mandriva.org>
    - replace %%_datadir/man by %%_mandir!
    - fix man pages

  + Eskild Hustvedt <eskild@mandriva.org>
    - Added buildrequire on intltool
    - Added patch1: fixes crash-on-startup when not running in 24bit colour depth
    - New version 0.2.10
    - Dropped patch0: merged upstream

  + Adam Williamson <awilliamson@mandriva.org>
    - requires pygtk2.0-libglade (thanks siimo)

* Fri Apr 27 2007 Eskild Hustvedt <eskild@mandriva.org> 0.2.9-2mdv2008.0
+ Revision: 18508
- Patch0: Expand ~ in the file browser
- /media/disk is now the default mount point for removable drives

* Tue Apr 17 2007 Eskild Hustvedt <eskild@mandriva.org> 0.2.9-1mdv2007.1
+ Revision: 13638
- New version 0.2.9


* Wed Feb 28 2007 Adam Williamson <awilliamson@mandriva.com> 0.2.8-2mdv2007.0
+ Revision: 127326
- Depend on pygtk2, not python-gtk

* Thu Jan 25 2007 Eskild Hustvedt <eskild@mandriva.org> 0.2.8-1mdv2007.1
+ Revision: 113532
- Compiled all python modules
- Requires python-notify on %%mdvver > 200700
- New version 0.2.8

* Sun Dec 17 2006 Eskild Hustvedt <eskild@mandriva.org> 0.2.7b2-1mdv2007.1
+ Revision: 98322
- New version 0.2.7b2 (fixes a bug that caused the Open Media menu item to fail)

* Wed Dec 13 2006 Eskild Hustvedt <eskild@mandriva.org> 0.2.7b-1mdv2007.1
+ Revision: 96506
- New version 0.2.7b
- Now does conditional patching of the mmkeys makefile to work with the newer python version
- Added BuildRequires on python-devel
- New version 0.2.6
- New version 0.2.4
- Import exaile

  + plouf <plouf>
    - Fix requires

* Wed Sep 06 2006 Eskild Hustvedt <eskild@mandriva.org> 0.2.r-1mdv2007.0
- New version 0.2

* Sun Sep 03 2006 David Walluck <walluck@mandriva.org> 0.2.b5-2mdv2007.0
- Requires: dbus-python

* Sat Aug 19 2006 Eskild Hustvedt <eskild@mandriva.org> 0.2.b5-1mdv2007.0
- New release 0.2b5

* Fri Aug 04 2006 Götz Waschk <waschk@mandriva.org> 0.2.b4-2mdv2007.0
- fix deps

* Tue Jun 27 2006 Eskild Hustvedt <eskild@mandriva.org> 0.2.b4
- Initial Mandriva Linux package

