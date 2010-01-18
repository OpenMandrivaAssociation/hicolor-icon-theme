Summary:	Basic requirement for icon themes
Name:		hicolor-icon-theme
Version:	0.12
Release:	%mkrel 1
License:	GPL
Group:		Graphical desktop/Other
URL:		http://icon-theme.freedesktop.org/wiki/HicolorTheme
Source0:	http://icon-theme.freedesktop.org/releases/%{name}-%{version}.tar.bz2
BuildArch:	noarch
Conflicts:	kdelibs-common <= 30000000:3.2.1-1mdk
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Contains the basic directories and files needed for icon theme support.

%prep
%setup -q

%build

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std
touch %buildroot%{_datadir}/icons/hicolor/icon-theme.cache

# automatic gtk icon cache update on rpm installs/removals
# (see http://wiki.mandriva.com/en/Rpm_filetriggers)
install -d %buildroot%{_var}/lib/rpm/filetriggers
cat > %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-hicolor.filter << EOF
^./usr/share/icons/hicolor/
EOF
cat > %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-hicolor.script << EOF
#!/bin/sh
if [ -x /usr/bin/gtk-update-icon-cache ]; then 
  /usr/bin/gtk-update-icon-cache --force --quiet /usr/share/icons/hicolor
fi
EOF
chmod 755 %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-hicolor.script

%clean
rm -rf %{buildroot}

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%files
%defattr(-,root,root,-)
%doc README
%dir %{_datadir}/icons/hicolor
%{_datadir}/icons/hicolor/index.theme
%{_datadir}/icons/hicolor/*/
%ghost %{_datadir}/icons/hicolor/icon-theme.cache
%{_var}/lib/rpm/filetriggers/gtk-icon-cache-hicolor.*
