# Catppuccin Grub RPM
RPM build of the great theme produced by https://github.com/catppuccin/grub.

Installing the RPM puts the theme in `/usr/share/grub/themes/`. Available RPMs:

- `catppuccin-grub` (All the flavors!)
- `catppuccin-grub-frappe`
- `catppuccin-grub-latte`
- `catppuccin-grub-macchiato`
- `catppuccin-grub-mocha`

# Build
Install the RPM build tools for your distro:
- `rpm-build`
- `rpmdevtools`

Now issue the build command:

    make rpm

# Usage
After installing an RPM, start using the theme:
1. Tell Grub to use the theme

    ```bash
    sudo bash -c 'echo GRUB_THEME=\"/usr/share/grub/themes/catppuccin-$FLAVOR-grub-theme/theme.txt\" >> /etc/default/grub'
    ```
2. Update Grub

       sudo grub-mkconfig -o /boot/grub/grub.cfg

3. Enjoy Catppuccin Grub :)
