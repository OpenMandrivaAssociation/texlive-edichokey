%global tl_name edichokey
%global tl_revision 56223

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.01y
Release:	%{tl_revision}.1
Summary:	Typeset dichotomous identification keys
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/edichokey
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/edichokey.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/edichokey.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a LaTeX package for typesetting dichotomous identification key
in indented style. It can be considered as an extended version of
package dichokey, as edichokey is more capable of dealing with complex
keys.

