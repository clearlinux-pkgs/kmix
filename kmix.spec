#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kmix
Version  : 19.12.0
Release  : 13
URL      : https://download.kde.org/stable/release-service/19.12.0/src/kmix-19.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.0/src/kmix-19.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.0/src/kmix-19.12.0.tar.xz.sig
Summary  : KDE volume control program
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: kmix-bin = %{version}-%{release}
Requires: kmix-data = %{version}-%{release}
Requires: kmix-lib = %{version}-%{release}
Requires: kmix-license = %{version}-%{release}
Requires: kmix-locales = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(glib-2.0)
BuildRequires : extra-cmake-modules pkgconfig(libpulse)
BuildRequires : kglobalaccel-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libcanberra)
BuildRequires : plasma-framework-dev

%description
Contains localizations for the WhatsThis help for the soundcard controls.
This is not yet integrated into the KDE build / install.

%package bin
Summary: bin components for the kmix package.
Group: Binaries
Requires: kmix-data = %{version}-%{release}
Requires: kmix-license = %{version}-%{release}

%description bin
bin components for the kmix package.


%package data
Summary: data components for the kmix package.
Group: Data

%description data
data components for the kmix package.


%package doc
Summary: doc components for the kmix package.
Group: Documentation

%description doc
doc components for the kmix package.


%package lib
Summary: lib components for the kmix package.
Group: Libraries
Requires: kmix-data = %{version}-%{release}
Requires: kmix-license = %{version}-%{release}

%description lib
lib components for the kmix package.


%package license
Summary: license components for the kmix package.
Group: Default

%description license
license components for the kmix package.


%package locales
Summary: locales components for the kmix package.
Group: Default

%description locales
locales components for the kmix package.


%prep
%setup -q -n kmix-19.12.0
cd %{_builddir}/kmix-19.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576564580
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1576564580
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmix
cp %{_builddir}/kmix-19.12.0/COPYING %{buildroot}/usr/share/package-licenses/kmix/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/kmix-19.12.0/COPYING.DOC %{buildroot}/usr/share/package-licenses/kmix/fcbf818f92ef8679a88f3778b12b4c8b5810545b
cp %{_builddir}/kmix-19.12.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/kmix/ba8966e2473a9969bdcab3dc82274c817cfd98a1
cp %{_builddir}/kmix-19.12.0/cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/kmix/ff3ed70db4739b3c6747c7f624fe2bad70802987
pushd clr-build
%make_install
popd
%find_lang kmix

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kmix
/usr/bin/kmixctrl
/usr/bin/kmixremote

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kmix.desktop
/usr/share/dbus-1/interfaces/org.kde.kmix.control.xml
/usr/share/dbus-1/interfaces/org.kde.kmix.mixer.xml
/usr/share/dbus-1/interfaces/org.kde.kmix.mixset.xml
/usr/share/icons/hicolor/128x128/actions/kmix.png
/usr/share/icons/hicolor/16x16/actions/kmix.png
/usr/share/icons/hicolor/32x32/actions/kmix.png
/usr/share/icons/hicolor/48x48/actions/kmix.png
/usr/share/icons/hicolor/64x64/actions/kmix.png
/usr/share/kmix/pics/kmixdocked.png
/usr/share/kmix/pics/kmixdocked_error.png
/usr/share/kmix/pics/kmixdocked_mute.png
/usr/share/kmix/pics/mixer-ac97.png
/usr/share/kmix/pics/mixer-capture.png
/usr/share/kmix/pics/mixer-cd.png
/usr/share/kmix/pics/mixer-digital.png
/usr/share/kmix/pics/mixer-front.png
/usr/share/kmix/pics/mixer-headset.png
/usr/share/kmix/pics/mixer-lfe.png
/usr/share/kmix/pics/mixer-line.png
/usr/share/kmix/pics/mixer-master.png
/usr/share/kmix/pics/mixer-microphone.png
/usr/share/kmix/pics/mixer-midi.png
/usr/share/kmix/pics/mixer-pcm-default.png
/usr/share/kmix/pics/mixer-pcm.png
/usr/share/kmix/pics/mixer-surround.png
/usr/share/kmix/pics/mixer-video.png
/usr/share/kmix/pics/show-mixer.png
/usr/share/kmix/profiles/ALSA.TerraTec_DMX6Fire.1.default.xml
/usr/share/kmix/profiles/ALSA.capture.xml
/usr/share/kmix/profiles/ALSA.default.xml
/usr/share/kmix/profiles/ALSA.playback.xml
/usr/share/kmix/profiles/MPRIS2.default.xml
/usr/share/kmix/profiles/OSS.default.xml
/usr/share/kmix/profiles/PulseAudio.default.xml
/usr/share/kmix/profiles/SUNAudio.default.xml
/usr/share/knotifications5/kmix.notifyrc
/usr/share/kservices5/kmixctrl_restore.desktop
/usr/share/kservices5/plasma-dataengine-mixer.desktop
/usr/share/kxmlgui5/kmix/kmixui.rc
/usr/share/metainfo/org.kde.kmix.appdata.xml
/usr/share/plasma/services/mixer.operations
/usr/share/xdg/autostart/kmix_autostart.desktop
/usr/share/xdg/autostart/restore_kmix_volumes.desktop

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kmix/index.cache.bz2
/usr/share/doc/HTML/ca/kmix/index.docbook
/usr/share/doc/HTML/cs/kmix/index.cache.bz2
/usr/share/doc/HTML/cs/kmix/index.docbook
/usr/share/doc/HTML/de/kmix/index.cache.bz2
/usr/share/doc/HTML/de/kmix/index.docbook
/usr/share/doc/HTML/de/kmix/kmix-channels.png
/usr/share/doc/HTML/de/kmix/kmix-configure.png
/usr/share/doc/HTML/de/kmix/kmix-file.png
/usr/share/doc/HTML/de/kmix/kmix-master.png
/usr/share/doc/HTML/de/kmix/kmix-options.png
/usr/share/doc/HTML/de/kmix/kmix.png
/usr/share/doc/HTML/en/kmix/index.cache.bz2
/usr/share/doc/HTML/en/kmix/index.docbook
/usr/share/doc/HTML/en/kmix/kmix-configure-general.png
/usr/share/doc/HTML/en/kmix/kmix-configure-sound-menu.png
/usr/share/doc/HTML/en/kmix/kmix-configure-start.png
/usr/share/doc/HTML/en/kmix/kmix-file.png
/usr/share/doc/HTML/en/kmix/kmix-master.png
/usr/share/doc/HTML/en/kmix/kmix-options.png
/usr/share/doc/HTML/en/kmix/kmix.png
/usr/share/doc/HTML/es/kmix/index.cache.bz2
/usr/share/doc/HTML/es/kmix/index.docbook
/usr/share/doc/HTML/es/kmix/kmix-file.png
/usr/share/doc/HTML/es/kmix/kmix-master.png
/usr/share/doc/HTML/es/kmix/kmix-options.png
/usr/share/doc/HTML/es/kmix/kmix.png
/usr/share/doc/HTML/et/kmix/index.cache.bz2
/usr/share/doc/HTML/et/kmix/index.docbook
/usr/share/doc/HTML/fr/kmix/index.cache.bz2
/usr/share/doc/HTML/fr/kmix/index.docbook
/usr/share/doc/HTML/gl/kmix/index.cache.bz2
/usr/share/doc/HTML/gl/kmix/index.docbook
/usr/share/doc/HTML/id/kmix/index.cache.bz2
/usr/share/doc/HTML/id/kmix/index.docbook
/usr/share/doc/HTML/it/kmix/index.cache.bz2
/usr/share/doc/HTML/it/kmix/index.docbook
/usr/share/doc/HTML/it/kmix/kmix-channel-playback.png
/usr/share/doc/HTML/it/kmix/kmix-channel-record.png
/usr/share/doc/HTML/it/kmix/kmix-window.png
/usr/share/doc/HTML/lt/kmix/index.cache.bz2
/usr/share/doc/HTML/lt/kmix/index.docbook
/usr/share/doc/HTML/nl/kmix/index.cache.bz2
/usr/share/doc/HTML/nl/kmix/index.docbook
/usr/share/doc/HTML/pt/kmix/index.cache.bz2
/usr/share/doc/HTML/pt/kmix/index.docbook
/usr/share/doc/HTML/pt_BR/kmix/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kmix/index.docbook
/usr/share/doc/HTML/pt_BR/kmix/kmix-file.png
/usr/share/doc/HTML/pt_BR/kmix/kmix-master.png
/usr/share/doc/HTML/pt_BR/kmix/kmix-options.png
/usr/share/doc/HTML/pt_BR/kmix/kmix.png
/usr/share/doc/HTML/ru/kmix/index.cache.bz2
/usr/share/doc/HTML/ru/kmix/index.docbook
/usr/share/doc/HTML/sr/kmix/index.cache.bz2
/usr/share/doc/HTML/sr/kmix/index.docbook
/usr/share/doc/HTML/sv/kmix/index.cache.bz2
/usr/share/doc/HTML/sv/kmix/index.docbook
/usr/share/doc/HTML/sv/kmix/kmix-channel-switches.png
/usr/share/doc/HTML/sv/kmix/kmix-window.png
/usr/share/doc/HTML/uk/kmix/index.cache.bz2
/usr/share/doc/HTML/uk/kmix/index.docbook
/usr/share/doc/HTML/uk/kmix/kmix-configure-general.png
/usr/share/doc/HTML/uk/kmix/kmix-configure-sound-menu.png
/usr/share/doc/HTML/uk/kmix/kmix-configure-start.png
/usr/share/doc/HTML/uk/kmix/kmix-file.png
/usr/share/doc/HTML/uk/kmix/kmix-master.png
/usr/share/doc/HTML/uk/kmix/kmix-options.png
/usr/share/doc/HTML/uk/kmix/kmix.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkmixcore.so.5
/usr/lib64/libkmixcore.so.5.13.80
/usr/lib64/qt5/plugins/kf5/kded/kmixd.so
/usr/lib64/qt5/plugins/plasma/dataengine/plasma_engine_mixer.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmix/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/kmix/ba8966e2473a9969bdcab3dc82274c817cfd98a1
/usr/share/package-licenses/kmix/fcbf818f92ef8679a88f3778b12b4c8b5810545b
/usr/share/package-licenses/kmix/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files locales -f kmix.lang
%defattr(-,root,root,-)

