Summary: 	Window Maker dock applet resembling a miniature pinboard
Summary(pl):	dokowalna miniaturowa tablica na notatki dla WindowMakera 
Name:		wmpinboard 
Version: 	0.8.4
Release: 	1
Copyright: 	GPL
Group: 		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0: 	http://www.tu-ilmenau.de/~gomar/stuff/wmpinboard/%{name}-%{version}.tar.gz
URL: 		http://www.tu-ilmenau.de/~gomar/stuff/wmpinboard/
BuildPrereq:	xpm-devel
BuildPrereq:	XFree86-devel
BuildRoot: 	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6

%description
wmpinboard is a tiny, simple applet designed to be docked to Window
Maker's dock or workspace clip.  It resembles a miniaturized pinboard
which tiny, brightly colored notes can be "pinned" to.  Because the
pinboard is limited to a size of less than 64x64 pixels, the notes of
course can't be read in this view.  That's why each note can on demand
be viewed "full size", allowing for 8x5 (-1) characters to be displayed.

%description -l pl
wmpinboard jest niewielkim, prostym apletem zaprojektowanym w sposób
umo¿liwiaj±cy umieszczenie go w Doku lub Spinaczu WindowMakera. 
Przedstawia zminiaturyzowan± tablicê, do której mog± byæ "przypinane"
kolorowe karteczki z notatkami. Poniewa¿ rozmiar tablicy jest ograniczony
do wymiarów 64x64 pixeli, notatki nie mog± byæ oczywi¶cie w tym stanie 
widoczne. Dlatego te¿ ka¿da karteczka mo¿e byæ na ¿±danie rozwiniêta do 
"pe³nych wymiarów", pozwalaj±c w ten sposób wy¶wietliæ do 8x5 (-1) znaków.

%prep
%setup -q -n %{name}.app

%build
xmkmf
make CXXDEBUGFLAGS="$RPM_OPT_FLAGS" \
	CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT%{_prefix}
install wmpb-convert.pl $RPM_BUILD_ROOT%{_bindir}

gzip -9nf CREDITS ChangeLog README TODO ReleaseNotes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CREDITS,ChangeLog,README,TODO,ReleaseNotes}.gz

%attr(755,root,root) %{_bindir}/*

%changelog
* Thu May 20 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [0.8.4-1]
- based on spec maked by Jochem Wichers Hoeth <wiho@chem.uva.nl>,
- spec rewritten by me and Artur Frysiak <wiget@pld.org.pl>.
