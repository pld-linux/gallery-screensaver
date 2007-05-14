Summary:	Gallery Remote - Screensaver
Name:		gallery-screensaver
Version:	1.5.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gallery/gallery_screensaver_%{version}-b17_unix.zip
# Source0-md5:	167230d972196672009286dfd76c1667
URL:		http://codex.gallery2.org/Gallery_Remote:Screensaver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
Gallery Remote Screensaver

%prep
%setup -q -n gallery-unix

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
