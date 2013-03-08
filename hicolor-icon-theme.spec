Summary:	Basic requirement for icon themes
Name:		hicolor-icon-theme
Version:	0.12
Release:	9
License:	GPL
Group:		Graphical desktop/Other
URL:		http://icon-theme.freedesktop.org/wiki/HicolorTheme
Source0:	http://icon-theme.freedesktop.org/releases/%{name}-%{version}.tar.bz2
BuildArch:	noarch

%description
Contains the basic directories and files needed for icon theme support.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

touch %{buildroot}%{_datadir}/icons/hicolor/icon-theme.cache

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%triggerin -- %{_iconsdir}/hicolor/*/*/*
%update_icon_cache hicolor

%triggerpostun -- %{_iconsdir}/hicolor/*/*/*
%update_icon_cache hicolor

%files
%doc README
%dir %{_iconsdir}/hicolor
%{_iconsdir}/hicolor/*x*
%ghost %{_iconsdir}/hicolor/icon-theme.cache

%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.12-7mdv2011.0
+ Revision: 665413
- mass rebuild

  + Per Ã˜yvind Karlsen <peroyvind@mandriva.org>
    - avoid including same files twice (..and with different attributes)

* Sat Feb 26 2011 Funda Wang <fwang@mandriva.org> 0.12-6
+ Revision: 639957
- rebuild

* Sun Feb 13 2011 Funda Wang <fwang@mandriva.org> 0.12-5
+ Revision: 637526
- rebuild for fixed rpm-setup-mandriva

* Sun Feb 13 2011 Funda Wang <fwang@mandriva.org> 0.12-4
+ Revision: 637501
- fix file trigger

* Fri Feb 11 2011 Funda Wang <fwang@mandriva.org> 0.12-3
+ Revision: 637214
- update file list
- conver to old trigger to rpm5 standard trigger

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.12-2mdv2011.0
+ Revision: 605858
- rebuild

* Mon Jan 18 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.12-1mdv2010.1
+ Revision: 492990
- update to new version 0.12

* Sat Sep 26 2009 Frederik Himpe <fhimpe@mandriva.org> 0.11-1mdv2010.0
+ Revision: 449587
- update to new version 0.11

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.10-6mdv2010.0
+ Revision: 425147
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.10-5mdv2009.1
+ Revision: 351234
- rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 0.10-4mdv2009.0
+ Revision: 264654
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 10 2008 Pixel <pixel@mandriva.com> 0.10-3mdv2009.0
+ Revision: 217431
- add rpm filetrigger running gtk-update-icon-cache when rpm install/remove hicolor icons

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.10-2mdv2008.1
+ Revision: 150256
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Jun 17 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.10-1mdv2008.0
+ Revision: 40463
- correct url
- spec file clean


* Thu Dec 28 2006 Frederic Crozat <fcrozat@mandriva.com> 0.10-1mdv2007.0
+ Revision: 102365
- Release 0.10
  Remove patch0, no longer needed with latest gnome-icon-theme
- Import hicolor-icon-theme

* Sat Sep 02 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.9-1mdv2007.0
- rebuild for new clean_icon_cache macro

* Thu Aug 31 2006 Götz Waschk <waschk@mandriva.org> 0.9-4mdv2007.0
- fix uninstallation

* Mon Mar 06 2006 Frederic Crozat <fcrozat@mandriva.com> 0.9-3mdk
- Update patch0 with document stock icons (Mdk bug #21466)

* Fri Mar 03 2006 Frederic Crozat <fcrozat@mandriva.com> 0.9-2mdk
- Patch0: add missing generic stock icon (Mdk bug #21426)
- Update gtk icon cache on install/upgrade, if gtk-update-icon-cache is present

* Thu Mar 02 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.9-1mdk
- New release 0.9
- use mkrel

* Wed Apr 27 2005 Götz Waschk <waschk@mandriva.org> 0.8-1mdk
- New release 0.8

* Fri Feb 04 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7-1mdk
- New release 0.7

* Wed Feb 02 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.6-1mdk 
- Release 0.6

* Thu Apr 08 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.5-1mdk
- Release 0.5

* Tue Apr 06 2004 Frederic Crozat <fcrozat@mandrakesoft.com>  0.4-1mdk
- Initial Mandrakelinux package, based on Fedora package

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 04 2004 Alexander Larsson <alexl@redhat.com> 0.3-1
- update to 0.3

* Fri Jan 16 2004 Alexander Larsson <alexl@redhat.com> 0.2-1
- Initial build.

