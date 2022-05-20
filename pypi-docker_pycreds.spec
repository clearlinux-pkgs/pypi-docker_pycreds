#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-docker_pycreds
Version  : 0.4.0
Release  : 26
URL      : https://files.pythonhosted.org/packages/c5/e6/d1f6c00b7221e2d7c4b470132c931325c8b22c51ca62417e300f5ce16009/docker-pycreds-0.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c5/e6/d1f6c00b7221e2d7c4b470132c931325c8b22c51ca62417e300f5ce16009/docker-pycreds-0.4.0.tar.gz
Summary  : Python bindings for the docker credentials store API
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-docker_pycreds-license = %{version}-%{release}
Requires: pypi-docker_pycreds-python = %{version}-%{release}
Requires: pypi-docker_pycreds-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(six)

%description
# docker-pycreds
[![CircleCI](https://circleci.com/gh/shin-/dockerpy-creds/tree/master.svg?style=svg)](https://circleci.com/gh/shin-/dockerpy-creds/tree/master)

%package license
Summary: license components for the pypi-docker_pycreds package.
Group: Default

%description license
license components for the pypi-docker_pycreds package.


%package python
Summary: python components for the pypi-docker_pycreds package.
Group: Default
Requires: pypi-docker_pycreds-python3 = %{version}-%{release}

%description python
python components for the pypi-docker_pycreds package.


%package python3
Summary: python3 components for the pypi-docker_pycreds package.
Group: Default
Requires: python3-core
Provides: pypi(docker_pycreds)
Requires: pypi(six)

%description python3
python3 components for the pypi-docker_pycreds package.


%prep
%setup -q -n docker-pycreds-0.4.0
cd %{_builddir}/docker-pycreds-0.4.0
pushd ..
cp -a docker-pycreds-0.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653058982
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-docker_pycreds
cp %{_builddir}/docker-pycreds-0.4.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-docker_pycreds/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-docker_pycreds/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
