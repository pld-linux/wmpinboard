%define name	wmpinboard
%define ver	0.5.5
%define rel	1

Summary: Window Maker dock applet resembling a miniature pinboard
Name: %name
Version: %ver
Release: %rel
Copyright: GPL
Group: X11/Utilities
Source: http://www.tu-ilmenau.de/~gomar/stuff/wmpinboard/wmpinboard-%{ver}.tar.gz
BuildRoot: /tmp/%{name}-root
URL: http://www.tu-ilmenau.de/~gomar/stuff/wmpinboard/
Docdir: /usr/doc
Packager: Jochem Wichers Hoeth <wiho@chem.uva.nl>

%description
wmpinboard is a tiny, simple applet designed to be docked to Window
Maker's dock or workspace clip.  It resembles a miniaturized pinboard
which tiny, brightly colored notes can be "pinned" to.  Because the
pinboard is limited to a size of less than 64x64 pixels, the notes of
course can't be read in this view.  That's why each note can on demand
be viewed "full size", allowing for 8x5 (-1) characters to be displayed.

%prep
%setup -n wmpinboard.app

%build
xmkmf
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT ; fi
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
install -s -m 755 -o 0 -g 0 wmpinboard $RPM_BUILD_ROOT/usr/X11R6/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/X11R6/bin/wmpinboard
%doc COPYING CREDITS ChangeLog FAQ INSTALL NOTES README TODO

%changelog
* Mon Jan 04 1999 Jochem Wichers Hoeth <wiho@chem.uva.nl>
- first build
