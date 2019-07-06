#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Rserve
Version  : 1.7.3.1
Release  : 15
URL      : https://cran.r-project.org/src/contrib/Rserve_1.7-3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Rserve_1.7-3.1.tar.gz
Summary  : Binary R server
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: R-Rserve-lib = %{version}-%{release}
BuildRequires : buildreq-R
BuildRequires : openssl-dev

%description
This directory contains a sample C++ client for Rserve
You can compile this client without R. Just run "configure" in the
Rserve directory, a corresponding Makefile will be automatically
generated.
Win32: There is no configure for Windows, but there is a special
Makefile.win to build it - use "make -f Makefile.win" - it requires
MinGW (or compatible) and GNU make.

%package lib
Summary: lib components for the R-Rserve package.
Group: Libraries

%description lib
lib components for the R-Rserve package.


%prep
%setup -q -c -n Rserve

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555411554

%install
export SOURCE_DATE_EPOCH=1555411554
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rserve
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rserve
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rserve
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc Rserve || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Rserve/DESCRIPTION
/usr/lib64/R/library/Rserve/INDEX
/usr/lib64/R/library/Rserve/LICENSE
/usr/lib64/R/library/Rserve/Meta/Rd.rds
/usr/lib64/R/library/Rserve/Meta/features.rds
/usr/lib64/R/library/Rserve/Meta/hsearch.rds
/usr/lib64/R/library/Rserve/Meta/links.rds
/usr/lib64/R/library/Rserve/Meta/nsInfo.rds
/usr/lib64/R/library/Rserve/Meta/package.rds
/usr/lib64/R/library/Rserve/NAMESPACE
/usr/lib64/R/library/Rserve/NEWS
/usr/lib64/R/library/Rserve/R/Rserve
/usr/lib64/R/library/Rserve/R/Rserve.rdb
/usr/lib64/R/library/Rserve/R/Rserve.rdx
/usr/lib64/R/library/Rserve/help/AnIndex
/usr/lib64/R/library/Rserve/help/Rserve.rdb
/usr/lib64/R/library/Rserve/help/Rserve.rdx
/usr/lib64/R/library/Rserve/help/aliases.rds
/usr/lib64/R/library/Rserve/help/paths.rds
/usr/lib64/R/library/Rserve/html/00Index.html
/usr/lib64/R/library/Rserve/html/R.css
/usr/lib64/R/library/Rserve/java/REngine.jar
/usr/lib64/R/library/Rserve/java/Rserve.jar
/usr/lib64/R/library/Rserve/libs/Rserve
/usr/lib64/R/library/Rserve/libs/Rserve.dbg

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/Rserve/libs/Rserve.so
/usr/lib64/R/library/Rserve/libs/Rserve.so.avx2
/usr/lib64/R/library/Rserve/libs/Rserve.so.avx512
