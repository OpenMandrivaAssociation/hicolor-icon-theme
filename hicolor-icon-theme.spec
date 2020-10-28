Summary:	Basic requirement for icon themes
Name:		hicolor-icon-theme
Version:	0.17
Release:	3
License:	GPLv2
Group:		Graphical desktop/Other
Url:		http://icon-theme.freedesktop.org/wiki/HicolorTheme
Source0:	https://icon-theme.freedesktop.org/releases/hicolor-icon-theme-%{version}.tar.xz
Patch0:		01_dont_scale_22x22_apps_icons_for_hicolor.patch
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

touch %{buildroot}%{_datadir}/icons/hicolor/icon-theme.cache

# automatic gtk icon cache update on rpm installs/removals
%transfiletriggerin -- %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
    gtk-update-icon-cache --force %{_datadir}/icons/hicolor &>/dev/null || :
fi

%transfiletriggerpostun -- %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
    gtk-update-icon-cache --force %{_datadir}/icons/hicolor &>/dev/null || :
fi

%files
%doc README
%dir %{_iconsdir}/hicolor
%{_iconsdir}/hicolor/*x*
%ghost %{_iconsdir}/hicolor/icon-theme.cache
