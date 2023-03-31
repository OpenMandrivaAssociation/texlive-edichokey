Name:		texlive-edichokey
Version:	56223
Release:	2
Summary:	Typeset dichotomous identification keys
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/edichokey
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/edichokey.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/edichokey.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a LaTeX package for typesetting dichotomous
identification key in indented style. It can be considered as
an extended version of package dichokey, as edichokey is more
capable of dealing with complex keys.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/edichokey
%doc %{_texmfdistdir}/doc/latex/edichokey

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
