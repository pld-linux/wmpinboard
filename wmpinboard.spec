Summary: 	Window Maker dock applet resembling a miniature pinboard
Name:		wmpinboard 
Version: 	0.5.5
Release: 	1d
Copyright: 	GPL
Group: 		X11/Utilities
Group(pl):	X11/Narzêdzia
###### 		http://www.tu-ilmenau.de/~gomar/stuff/wmpinboard/
Source: 	%{name}-%{version}.tar.gz
BuildRoot: 	/tmp/%{name}-%{version}-root
URL: 		http://www.tu-ilmenau.de/~gomar/stuff/wmpinboard/

%description
wmpinboard is a tiny, simple applet designed to be docked to Window
Maker's dock or workspace clip.  It resembles a miniaturized pinboard
which tiny, brightly colored notes can be "pinned" to.  Because the
pinboard is limited to a size of less than 64x64 pixels, the notes of
course can't be read in this view.  That's why each note can on demand
be viewed "full size", allowing for 8x5 (-1) characters to be displayed.

%prep
%setup -q -n wmpinboard.app

%build
xmkmf
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT ; fi
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
install -s wmpinboard $RPM_BUILD_ROOT/usr/X11R6/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING CREDITS ChangeLog FAQ NOTES README TODO

%attr(711,root,root) /usr/X11R6/bin/wmpinboard

%changelog
* Mon Jan 04 1999 Jochem Wichers Hoeth <wiho@chem.uva.nl>
- first build
