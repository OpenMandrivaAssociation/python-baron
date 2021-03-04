%global pypi_name baron

Name:           python-%{pypi_name}
Version:        0.9
Release:        1
Summary:        IDE allow you to refactor code, Baron allows you to write refactoring code.
License:        LGPLv3
URL:            https://github.com/PyCQA/baron
Source:         https://files.pythonhosted.org/packages/a7/51/19d574b7ab82c1bb883d932150a285f9c5ffed87883fb1996894cb5d7e4a/baron-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

Requires: python3dist(rply)

Provides:	python-%{pypi_name} = %{EVRD}

%description
Baron is a Full Syntax Tree (FST) library for Python. 
By opposition to an AST which drops some syntax information in the process of its creation (like empty lines, comments, formatting), 
a FST keeps everything and guarantees the operation fst_to_code(code_to_fst(source_code)) == source_code.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -vrf *.egg-info
sed -i -e 's/\r//' README.md

%build
%py_build

%install
%py_install

%files -n python-%{pypi_name}
%{python_sitelib}/%{pypi_name}/
%{python_sitelib}/%{pypi_name}-*.egg-info/
#{python_sitelib}/__pycache__/*
