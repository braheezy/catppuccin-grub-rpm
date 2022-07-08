%global debug_package %{nil}
%global url https://github.com/catppuccin/grub
%global SUMMARY Catppuccin GRUB2 gfxmenu pop theme, based on and inspired by Vimix and Dracula grub themes

Name:           %{_name}
Version:        %{_version}
Release:        %{_release}%{?dist}
Summary:        %{SUMMARY}

License:        MIT
URL:            %{url}
Source0:        %{url}/archive/refs/heads/main.zip
BuildArch:      noarch

%description
Catppuccinize your GRUB theme.

%package frappe
Summary:        %{SUMMARY}
%description frappe
Catppuccin Frappe GRUB theme

%package latte
Summary:        %{SUMMARY}
%description latte
Catppuccin Latte GRUB theme

%package macchiato
Summary:        %{SUMMARY}
%description macchiato
Catppuccin Macchiato GRUB theme

%package mocha
Summary:        %{SUMMARY}
%description mocha
Catppuccin Mocha GRUB theme

%prep
%setup -q -n grub-main

%build
# no build required

%install
INSTALL_DIR=%{buildroot}%{_datadir}/grub/themes/

install --mode 755 --directory $INSTALL_DIR
# Install each flavor
cp -r src/catppuccin-frappe-grub-theme/    $INSTALL_DIR
cp -r src/catppuccin-latte-grub-theme/     $INSTALL_DIR
cp -r src/catppuccin-macchiato-grub-theme/ $INSTALL_DIR
cp -r src/catppuccin-mocha-grub-theme/     $INSTALL_DIR

%files
/usr/share/grub/themes/catppuccin-*-grub-theme

%files frappe
/usr/share/grub/themes/catppuccin-frappe-grub-theme

%files latte
/usr/share/grub/themes/catppuccin-latte-grub-theme

%files macchiato
/usr/share/grub/themes/catppuccin-macchiato-grub-theme

%files mocha
/usr/share/grub/themes/catppuccin-mocha-grub-theme

%changelog
* Sun Jul 3 2022 braheezy <https://github.com/mbraha/>
- Initial specfile
