# TODO
# - saverbeans-api.jar should be external
# - need .o files from xscreensaver-4.24 to build
Summary:	Gallery Remote - Screensaver
Summary(pl.UTF-8):	Gallery Remote - wygaszacz ekranu
Name:		gallery-screensaver
Version:	1.5.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gallery/gallery_screensaver_%{version}-b17_unix.zip
# Source0-md5:	167230d972196672009286dfd76c1667
URL:		http://codex.gallery2.org/Gallery_Remote:Screensaver
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gallery Remote Screensaver.

%description -l pl.UTF-8
Wygaszacz ekranu Gallery Remote.

%prep
%setup -q -n gallery-unix

%build
export JAVA_HOME=%{java_home}
%{__make} Gallery-bin \
	cc="%{__cc}" \
	link="%{__cc}" \
	PLATFORM=Linux \
	XSCREENSAVER_HOME=../xscreensaver-4.24 \
	optflags="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_bindir},%{_datadir}/xscreensaver}
%{__make} install \
	SCREENSAVER_BIN=$RPM_BUILD_ROOT%{_bindir} \
	SCREENSAVER_CONF=$RPM_BUILD_ROOT%{_datadir}/xscreensaver

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Gallery
%attr(755,root,root) %{_bindir}/Gallery-bin
%attr(755,root,root) %{_bindir}/GalleryRemoteScreenSaver.jar
%attr(755,root,root) %{_bindir}/saverbeans-api.jar
%{_datadir}/xscreensaver/Gallery.xml
%{_datadir}/xscreensaver/GalleryEz.xml
