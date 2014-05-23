Summary:	Basic requirement for icon themes
Name:		hicolor-icon-theme
Version:	0.13
Release:	3
License:	GPLv2
Group:		Graphical desktop/Other
Url:		http://icon-theme.freedesktop.org/wiki/HicolorTheme
Source0:	http://icon-theme.freedesktop.org/releases/hicolor-icon-theme-%{version}.tar.gz
Patch0:		01_dont_scale_22x22_apps_icons_for_hicolor.patch
BuildArch:	noarch

%description
Contains the basic directories and files needed for icon theme support.

%prep
%setup -q
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std

touch %{buildroot}%{_datadir}/icons/hicolor/icon-theme.cache

# automatic gtk icon cache update on rpm installs/removals
# (see http://wiki.mandriva.com/en/Rpm_filetriggers)
install -d %{buildroot}%{_var}/lib/rpm/filetriggers
cat > %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-hicolor.filter << EOF
^./usr/share/icons/hicolor/
EOF
cat > %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-hicolor.script << EOF
#!/bin/sh
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  /usr/bin/gtk-update-icon-cache --force --quiet /usr/share/icons/hicolor
fi
EOF
chmod 755 %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-hicolor.script

%files
%doc README
%dir %{_iconsdir}/hicolor
%{_iconsdir}/hicolor/*x*
%ghost %{_iconsdir}/hicolor/icon-theme.cache
%{_var}/lib/rpm/filetriggers/gtk-icon-cache-hicolor.*

%changelog
* Wed Apr 23 2014 tpg (Tomasz Paweł Gajc) <tpgxyz@gmail.com> 0.13-3
+ Revision: 2f2b5ee
- add patch

* Wed Apr 23 2014 Tomasz Paweł Gajc <tpgxyz@gmail.com> 0.13-3
+ Revision: 43fbd58
- patch from mageia - do not scale 22x22 icons

* Wed Apr 23 2014 Tomasz Paweł Gajc <tpgxyz@gmail.com> 0.13-3
+ Revision: 97b9896
- use idea from Mageia for rebuilding icon cache

* Fri Mar 28 2014 Crispin Boylan <crisb@mandriva.org> 0.13-2
+ Revision: 3ab9906
- Remove trigger which makes package take ages to upgrade

* Tue Jan 28 2014 tpg (Tomasz Paweł Gajc) <tpgxyz@gmail.com> 0.13-1
+ Revision: 5fb49db
- new version 0.13

* Fri Dec 06 2013 Bernhard Rosenkraenzer <bero@bero.eu> 0.12-14
+ Revision: 6801f2b
- MassBuild#289: Increase release tag

* Fri Dec 06 2013 Bernhard Rosenkraenzer <bero@bero.eu> 0.12-13
+ Revision: a25f1ce
- MassBuild#289: Increase release tag

* Fri Dec 06 2013 Bernhard Rosenkraenzer <bero@bero.eu> 0.12-12
+ Revision: c72fe4a
- MassBuild#289: Increase release tag

* Fri Dec 06 2013 Bernhard Rosenkraenzer <bero@bero.eu> 0.12-11
+ Revision: 83ca206
- MassBuild#289: Increase release tag

* Thu Jul 18 2013 Tomasz Paweł Gajc <phenomenal@wp.pl> 0.12-10
+ Revision: 0ba0497
- bump release tag

* Fri May 10 2013 mdawkins (Matthew Dawkins) <mattydaw@gmail.com> 0.12-9
+ Revision: 311c474
- cleaned up spec

* Fri Mar 08 2013 Tomasz Paweł Gajc <tpg@mandriva.org> 0.12-9
+ Revision: 166bc4a
- rebuild

* Sat Dec 08 2012 alex <alex@localhost.localdomain> 0.12-8
+ Revision: 90de1ba
- merging with rosa2012.1 of project hicolor-icon-theme

* Wed May 04 2011 oden <oden@mandriva.org> 0.12-7
+ Revision: 233fa88
- - mass rebuild
- SILENT: svn-revision: 665413

* Sat Apr 09 2011 peroyvind <peroyvind@mandriva.org> 0.12-6
+ Revision: fd15b44
- avoid including same files twice (..and with different attributes)
- SILENT: svn-revision: 652150

* Sat Feb 26 2011 fwang <fwang@mandriva.org> 0.12-6
+ Revision: f38dc96
- rebuild
- SILENT: svn-revision: 639957

* Sun Feb 13 2011 fwang <fwang@mandriva.org> 0.12-5
+ Revision: a699589
- rebuild for fixed rpm-setup-mandriva
- SILENT: svn-revision: 637526

* Sun Feb 13 2011 fwang <fwang@mandriva.org> 0.12-4
+ Revision: cd30b2b
- fix file trigger
- SILENT: svn-revision: 637501

* Thu Feb 10 2011 fwang <fwang@mandriva.org> 0.12-3
+ Revision: 9052ab7
- update file list
- SILENT: svn-revision: 637214

* Thu Feb 10 2011 fwang <fwang@mandriva.org> 0.12-3
+ Revision: 684011a
- conver to old trigger to rpm5 standard trigger
- SILENT: svn-revision: 637213

* Fri Dec 03 2010 oden <oden@mandriva.org> 0.12-2
+ Revision: df37d90
- - rebuild
- SILENT: svn-revision: 605858

* Mon Jan 18 2010 goetz <goetz@mandriva.org> 0.12-1
+ Revision: f31c256
- update to new version 0.12
- SILENT: svn-revision: 492990

* Sat Sep 26 2009 fhimpe <fhimpe@mandriva.org> 0.11-1
+ Revision: 6870eca
- update to new version 0.11
- SILENT: svn-revision: 449587

* Wed Sep 02 2009 cfergeau <cfergeau@mandriva.org> 0.10-6
+ Revision: 22faabc
- rebuild
- SILENT: svn-revision: 425147

* Sat Mar 07 2009 aginies <aginies@mandriva.org> 0.10-5
+ Revision: fc5c9fa
- rebuild
- SILENT: svn-revision: 351234

* Wed Aug 06 2008 tv <tv@mandriva.org> 0.10-4
+ Revision: 7764aad
- rebuild early 2009.0 package (before pixel changes)
- SILENT: svn-revision: 264654

* Tue Jun 10 2008 pixel <pixel@mandriva.org> 0.10-3
+ Revision: 04a6ed1
- add rpm filetrigger running gtk-update-icon-cache when rpm install/remove hicolor icons
- SILENT: svn-revision: 217431

* Sat Jan 12 2008 tv <tv@mandriva.org> 0.10-2
+ Revision: 4071f16
- rebuild
- SILENT: svn-revision: 150256

* Wed Jan 02 2008 blino <blino@mandriva.org> 0.10-1
+ Revision: 1df4970
- restore BuildRoot
- SILENT: svn-revision: 140747


