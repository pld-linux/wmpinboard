Summary:	Window Maker dock applet resembling a miniature pinboard
Summary(pl.UTF-8):   Dokowalna miniaturowa tablica na notatki dla WindowMakera
Name:		wmpinboard
Version:	1.0
Release:	5
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.stud.tu-ilmenau.de/~gomar/stuff/wmpinboard/%{name}-%{version}.tar.bz2
# Source0-md5:	5a270397f7765b3416abae43d020a0c9
Source1:	%{name}.desktop
URL:		http://www.stud.tu-ilmenau.de/~gomar/stuff/wmpinboard/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmpinboard is a tiny, simple applet designed to be docked to Window
Maker's dock or workspace clip. It resembles a miniaturized pinboard
which tiny, brightly colored notes can be "pinned" to. Because the
pinboard is limited to a size of less than 64x64 pixels, the notes of
course can't be read in this view. That's why each note can on demand
be viewed "full size", allowing for 8x5 (-1) characters to be
displayed.

%description -l pl.UTF-8
wmpinboard jest niewielkim, prostym apletem zaprojektowanym w sposób
umożliwiający umieszczenie go w Doku lub Spinaczu WindowMakera.
Przedstawia zminiaturyzowaną tablicę, do której mogą być "przypinane"
kolorowe karteczki z notatkami. Ponieważ rozmiar tablicy jest
ograniczony do wymiarów 64x64 pikseli, notatki nie mogą być oczywiście
w tym stanie widoczne. Dlatego też każda karteczka może być na żądanie
rozwinięta do "pełnych wymiarów", pozwalając w ten sposób wyświetlić
do 8x5 (-1) znaków.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install wmpb-convert.pl	$RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1}	$RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog NEWS README TODO AUTHORS

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/wmpinboard.1*
%{_desktopdir}/docklets/wmpinboard.desktop
