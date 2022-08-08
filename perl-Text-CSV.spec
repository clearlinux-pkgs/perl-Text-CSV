#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-CSV
Version  : 2.02
Release  : 28
URL      : https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/Text-CSV-2.02.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/Text-CSV-2.02.tar.gz
Summary  : 'comma-separated values manipulator (using XS or PurePerl)'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Text-CSV-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Text::CSV version 1.33
----------------------
Text::CSV provides facilities for the composition and decomposition of
comma-separated values.  An instance of the Text::CSV class can combine
fields into a CSV string and parse a CSV string into fields.

%package dev
Summary: dev components for the perl-Text-CSV package.
Group: Development
Provides: perl-Text-CSV-devel = %{version}-%{release}
Requires: perl-Text-CSV = %{version}-%{release}

%description dev
dev components for the perl-Text-CSV package.


%package perl
Summary: perl components for the perl-Text-CSV package.
Group: Default
Requires: perl-Text-CSV = %{version}-%{release}

%description perl
perl components for the perl-Text-CSV package.


%prep
%setup -q -n Text-CSV-2.02
cd %{_builddir}/Text-CSV-2.02

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::CSV.3
/usr/share/man/man3/Text::CSV_PP.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
