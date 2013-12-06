Summary:	Basic requirement for icon themes
Name:		hicolor-icon-theme
Version:	0.12
Release:	13
License:	GPLv2
Group:		Graphical desktop/Other
Url:		http://icon-theme.freedesktop.org/wiki/HicolorTheme
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

