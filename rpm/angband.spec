Name:    angband
Version: 4.2.3
Release: 1%{?dist}
Summary: Popular roguelike role playing game

License: Lots
URL:     https://rephial.org/
Source0: angband-4.2.3-patched.tar.gz
Source1: angband.desktop
Source2: angband.png
Patch0:  angband-4.2.3-0-freetype_bug.patch
Patch1:  angband-4.2.3-1-ncursesw6.patch
Patch2:  angband-4.2.3-2-fix_standalone.patch
Patch3:  angband-4.2.3-3-test_fix.patch

BuildRequires: autoconf automake
BuildRequires: ncurses-devel desktop-file-utils gcc python3-docutils
BuildRequires: SDL2-devel SDL2_image-devel SDL2_ttf-devel SDL2_mixer-devel

Requires: xorg-x11-fonts-misc SDL2 SDL2_image SDL2_ttf SDL2_mixer ncurses

%description
A roguelike game where you explore a very deep dungeon, kill monsters, try to
equip yourself with the best weapons and armor you can find, and finally face
Morgoth - "The Dark Enemy".

%prep
%setup -q
# Create a git repo within the expanded tarball.
git init
git config user.email "xxx"
git config user.name "xxx"
git add .
git commit -a -q -m "%{version} baseline."
# Apply all the patches on top.
git apply %{patches}

%build
./autogen.sh
%configure \
    --datadir=/usr/share \
    --enable-curses \
    --enable-x11 \
    --enable-sdl2 \
    --enable-sdl2-mixer
make %{?_smp_mflags}

%install
%make_install
install -d $RPM_BUILD_ROOT/%{_var}/games/%{name}

desktop-file-install \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
        %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6/
install -p -m 644 src/angband.man $RPM_BUILD_ROOT%{_mandir}/man6/angband.6


%files
%license docs/copying.rst
%doc docs/*.rst
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%dir %{_sysconfdir}/angband
%dir %{_sysconfdir}/angband/gamedata
%dir %{_sysconfdir}/angband/customize
%config(noreplace) %{_sysconfdir}/angband/gamedata/*
%config(noreplace) %{_sysconfdir}/angband/customize/*
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_mandir}/man6/angband.*
%{_datarootdir}/angband


%changelog
* Thu Nov 25 2021 Diego Herrera <dherrera@redhat.com> 4.2.3-1
- Testing

* Sun Aug 25 2019 Wart <wart at kobold dot org> 4.2.0-1
- Update to 4.2.0
- Fix group creation
- Fix desktop file
- Update license naming
- Add man page
- Remove restricted tileset

* Tue Aug 13 2019 Wart <wart at kobold dot org> 4.1.3-4
- Use recommended dynamic allocation for the group

* Sat Aug 10 2019 Wart <wart at kobold dot org> 4.1.3-3
- Minor spec file cleanup

* Wed Jul 24 2019 Wart <wart at kobold dot org> 4.1.3-2
- Enable shared scoreboard file

* Sun Jul 21 2019 Wart <wart at kobold dot org> 4.1.3-1
- Update to 4.1.3

* Sun Jul 21 2019 Wart <wart at kobold dot org> 3.0.6-5
- Updates to build for Fedora 30

* Wed Apr 4 2007 Wart <wart at kobold dot org> 3.0.6-4
- Add BR: to allow X11 support

* Tue Apr 3 2007 Wart <wart at kobold dot org> 3.0.6-3
- Add icon name to .desktop files
- Fix License tag
- Move game data to /var/games/angband
- Remove non-working -graphics desktop file

* Mon Apr 2 2007 Wart <wart at kobold dot org> 3.0.6-2
- Use custom group for setgid as added protection
- Install extra graphics files
- Add vendor to .desktop file installation

* Thu Mar 29 2007 Wart <wart at kobold dot org> 3.0.6-1
- Update to 3.0.6
- Updated spec to Fedora Extras standards (again)

* Sat Feb 25 2006 Wart <wart at kobold dot org> 3.0.3-5
- Update. spec to Fedora Extras standards
