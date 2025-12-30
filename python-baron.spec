%define module baron

Summary:	A Full Syntax Tree (FST) library for Python
Name:		python-%{module}
Version:	0.10.1
Release:	5
License:	LGPLv3+
Url:		https://github.com/PyCQA/baron
Group:		Development/Languages/Python
Source:		https://files.pythonhosted.org/packages/source/b/%{module}/%{module}-%{version}.tar.gz

BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(rply)
BuildRequires:	python3dist(setuptools)
# docs
#BuildRequires:	python3dist(ipython)
#BuildRequires:	python3dist(matplotlib)
#BuildRequires:	python3dist(sphinx)

BuildArch:	noarch

%description
Baron is a Full Syntax Tree (FST) library for Python. By opposition to an
AST which drops some syntax information in the process of its creation (like
empty lines, comments, formatting), a FST keeps everything and guarantees
the operation fst_to_code(code_to_fst(source_code)) == source_code.

#----------------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%install
%py_install

%files
%doc README.md
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-*.egg-info/
