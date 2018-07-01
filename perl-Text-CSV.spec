#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-CSV
Version  : 1.95
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/Text-CSV-1.95.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/Text-CSV-1.95.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtext-csv-perl/libtext-csv-perl_1.95-1.debian.tar.xz
Summary  : 'comma-separated values manipulator (using XS or PurePerl)'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Text-CSV-man

%description
Text::CSV version 1.33
----------------------
Text::CSV provides facilities for the composition and decomposition of
comma-separated values.  An instance of the Text::CSV class can combine
fields into a CSV string and parse a CSV string into fields.

%package man
Summary: man components for the perl-Text-CSV package.
Group: Default

%description man
man components for the perl-Text-CSV package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n Text-CSV-1.95
mkdir -p %{_topdir}/BUILD/Text-CSV-1.95/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Text-CSV-1.95/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Text/CSV.pm
/usr/lib/perl5/site_perl/5.26.1/Text/CSV_PP.pm

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Text::CSV.3
/usr/share/man/man3/Text::CSV_PP.3
