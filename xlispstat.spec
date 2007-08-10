%define name xlispstat
%define version 3.52.18
%define release %mkrel 16

# yves 3.52.18-9mdk -- gb hack for openoffice
# Find a free display (resources generation requires X) and sets XDISPLAY
%define init_display XDISPLAY=$(i=0; while [ -f /tmp/.X$i-lock ]; do i=$(($i+1)); done; echo $i)
# The virtual X server PID
%define kill_display kill $(cat /tmp/.X$XDISPLAY-lock)

Summary:	An implementation of the Lisp language with statistics extensions
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD-like
Group:		Sciences/Mathematics
BuildRequires:	XFree86-devel XFree86-Xvfb
Source:		ftp://ftp.stat.umn.edu/pub/xlispstat/3-52/xlispstat-3-52-18.tar.bz2
URL:		http://lib.stat.cmu.edu/xlispstat
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
The xlispstat package contains XLISP-PLUS, an implementation of the Lisp
programming language for the X Window System.  XLISP-PLUS also includes
extensions for performing advanced statistical computations.

Install the xlispstat package if you need a version of the Lisp
programming language for X with statistics extensions.

%prep
%setup -q -n xlispstat-3-52-18

%build
%configure --prefix=%{_prefix}

# Launch a virtual framebuffer X server on a free display
%{init_display}
/usr/bin/Xvfb :$XDISPLAY >& /dev/null &
DISPLAY=:$XDISPLAY make UCFLAGS="$RPM_OPT_FLAGS -DX11WINDOWS"
%{kill_display}

%install
rm -rf $RPM_BUILD_DIR
%makeinstall

%clean
rm -rf $RPM_BUILD_DIR

%files
%defattr(-,root,root)
%doc README RELEASE doc
%{_bindir}/xlispstat
/usr/lib/xlispstat
