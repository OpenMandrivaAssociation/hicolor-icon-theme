Summary:	Basic requirement for icon themes

Name:		hicolor-icon-theme
Version:	0.17
Release:	1
License:	GPLv2
Group:		Graphical desktop/Other
Url:		http://icon-theme.freedesktop.org/wiki/HicolorTheme
Source0:	https://icon-theme.freedesktop.org/releases/hicolor-icon-theme-%{version}.tar.xz
Patch0:		01_dont_scale_22x22_apps_icons_for_hicolor.patch
BuildArch:	noarch

%description
Contains the basic directories and files needed for icon theme support.

%prep
%setup -q
%apply_patches

%build
%configure
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

