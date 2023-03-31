Summary:	Basic requirement for icon themes
Name:		hicolor-icon-theme
Version:	0.17
Release:	5
License:	GPLv2
Group:		Graphical desktop/Other
Url:		https://www.freedesktop.org/wiki/Software/icon-theme/
Source0:	https://icon-theme.freedesktop.org/releases/%{name}-%{version}.tar.xz
Patch0:		01_dont_scale_22x22_apps_icons_for_hicolor.patch
# upstream patch to include directories for @2 scaled icons
Patch1:		https://gitlab.freedesktop.org/xdg/default-icon-theme/-/commit/b3f1207.patch
Requires:	gtk-update-icon-cache
BuildArch:	noarch

%description
Contains the basic directories and files needed for icon theme support.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

touch %{buildroot}%{_iconsdir}/hicolor/icon-theme.cache

# automatic gtk icon cache update on rpm installs/removals
%transfiletriggerin -- %{_iconsdir}/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
    gtk-update-icon-cache --force %{_iconsdir}/hicolor &>/dev/null || :
fi

%transfiletriggerpostun -- %{_iconsdir}/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
    gtk-update-icon-cache --force %{_iconsdir}/hicolor &>/dev/null || :
fi

%files
%license COPYING
%doc README
%dir %{_iconsdir}/hicolor
%{_iconsdir}/hicolor/16x16/
%{_iconsdir}/hicolor/16x16@2/
%{_iconsdir}/hicolor/22x22/
%{_iconsdir}/hicolor/22x22@2/
%{_iconsdir}/hicolor/24x24/
%{_iconsdir}/hicolor/24x24@2/
%{_iconsdir}/hicolor/32x32/
%{_iconsdir}/hicolor/32x32@2/
%{_iconsdir}/hicolor/36x36/
%{_iconsdir}/hicolor/36x36@2/
%{_iconsdir}/hicolor/48x48/
%{_iconsdir}/hicolor/48x48@2/
%{_iconsdir}/hicolor/64x64/
%{_iconsdir}/hicolor/64x64@2/
%{_iconsdir}/hicolor/72x72/
%{_iconsdir}/hicolor/72x72@2/
%{_iconsdir}/hicolor/96x96/
%{_iconsdir}/hicolor/96x96@2/
%{_iconsdir}/hicolor/128x128/
%{_iconsdir}/hicolor/128x128@2/
%{_iconsdir}/hicolor/192x192/
%{_iconsdir}/hicolor/192x192@2/
%{_iconsdir}/hicolor/256x256/
%{_iconsdir}/hicolor/256x256@2/
%{_iconsdir}/hicolor/512x512/
%{_iconsdir}/hicolor/512x512@2/
%{_iconsdir}/hicolor/scalable/
%{_iconsdir}/hicolor/symbolic/
%{_iconsdir}/hicolor/index.theme
%ghost %{_iconsdir}/hicolor/icon-theme.cache
