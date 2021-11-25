# Angband packaging for Fedora

Test project using Angband to learn how to package things for Fedora

## Prepare

This project uses Podman to containarize the work, mainly because I 
wanted to test many dependency packages and didn't want to leave 
them installed on my machine. Also it's a good chance to learn 
to use podman since I already know how to use Docker.

The angband repo is added as a submodule pointing to the latest stable 
version, so to prepare this project, run the following command.

```bash
git submodule update --init --recursive
```

## Standalone deploy

This is a test build to check what things are needed to safely build the current version of Angband.

Running the `standalone_deploy.sh` script does the following:

* Builds a base image on your local system using Podman with the required dependencies
* Runs the container, with the following permissions
  * Read access to angband source code
  * Write access to an ./out folder
    * Thx http://tutorialworks.com/podman-rootless-volumes/ for reference on howto
* Applies the patches in the patch folder
* Builds & installs in the ./out folder

The applied patches are the following:

* Add a TTF font as default for the SDL2 version.
  * Temporary workaround to https://github.com/angband/angband/issues/5079
* Upgrade the ncursesw5 requirement to ncursesw6 (Fedora specific).
* Fix so that the result can be moved from the compilation path.

To test, enter the `out` folder and runa

```bash
# X11
./src/angband -mx11

# Wayland
SDL_VIDEODRIVER=wayland ./src/angband -msdl2

# ncurses
./src/angband -mgcu
```