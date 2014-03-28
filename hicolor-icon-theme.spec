Summary:	Basic requirement for icon themes
Name:		hicolor-icon-theme
Version:	0.13
Release:	2
License:	GPLv2
Group:		Graphical desktop/Other
Url:		http://icon-theme.freedesktop.org/wiki/HicolorTheme
Source0:	http://icon-theme.freedesktop.org/releases/hicolor-icon-theme-%{version}.tar.gz
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

%files
%doc README
%dir %{_iconsdir}/hicolor
%{_iconsdir}/hicolor/*x*
%ghost %{_iconsdir}/hicolor/icon-theme.cache

