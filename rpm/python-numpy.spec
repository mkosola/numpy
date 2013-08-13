Name:           python-numpy
Version:        1.7.1
Release:        1
Summary:        A fast multidimensional array facility for Python

Group:          Development/Languages
License:        BSD
URL:            http://numeric.scipy.org/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python-devel
BuildRequires:  python-setuptools

Provides:       numpy

%description
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type.

%package devel
Summary:        Development files for Numpy applications
Group:          Development/Languages
Requires:       %{name} = %{version}
Requires:       python-devel

%description devel
This package contains files for developing applications using Numpy.

%package f2py
Summary:        Fortran to py for numpy
Group:          Development/Libraries
Requires:       %{name} = %{version}
Requires:       python-devel
Provides:       f2py

%description f2py
This package includes a version of f2py that works properly with NumPy.

%prep
%setup -q -n %{name}-%{version}

%build
cd numpy
%{__python} setup.py build

%install
cd numpy
rm -rf %{buildroot}
%{__python} setup.py install --root %{buildroot}

# Remove tests
rm -rf %{buildroot}%{python_sitearch}/numpy/{core,distutils,f2py,fft,ma,matrixlib,oldnumeric,polynomial,random,testing}/tests

# Remove docs
rm -rf %{buildroot}%{python_sitearch}/numpy/doc

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc numpy/LICENSE.txt numpy/README.txt numpy/THANKS.txt
%doc numpy/DEV_README.txt numpy/COMPATIBILITY
%dir %{python_sitearch}/numpy
%{python_sitearch}/numpy/*.py*
%{python_sitearch}/numpy/core
%{python_sitearch}/numpy/distutils
%{python_sitearch}/numpy/fft
%{python_sitearch}/numpy/lib
%{python_sitearch}/numpy/linalg
%{python_sitearch}/numpy/ma
%{python_sitearch}/numpy/numarray
%{python_sitearch}/numpy/oldnumeric
%{python_sitearch}/numpy/random
%{python_sitearch}/numpy/testing
%{python_sitearch}/numpy/tests
%{python_sitearch}/numpy/compat
%{python_sitearch}/numpy/matrixlib
%{python_sitearch}/numpy/polynomial
%{python_sitearch}/numpy-*.egg-info
%exclude %{python_sitearch}/numpy/*/*/*.c
%exclude %{python_sitearch}/numpy/*/*.h
%exclude %{python_sitearch}/numpy/*/*/*.h
%exclude %{python_sitearch}/numpy/*/*/*/*.h
%exclude %{python_sitearch}/numpy/core/lib/libnpymath.a

%files devel
%defattr(-,root,root,-)
%{python_sitearch}/numpy/*/*/*.c
%{python_sitearch}/numpy/*/*.h
%{python_sitearch}/numpy/*/*/*.h
%{python_sitearch}/numpy/*/*/*/*.h
%{python_sitearch}/numpy/core/lib/libnpymath.a

%files f2py
%defattr(-,root,root,-)
%{_bindir}/f2py
%{python_sitearch}/numpy/f2py
%exclude %{python_sitearch}/numpy/f2py/*/*.h
%exclude %{python_sitearch}/numpy/f2py/*/*.c
