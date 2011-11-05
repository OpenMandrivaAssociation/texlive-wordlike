# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/wordlike
# catalog-date 2009-06-03 09:03:24 +0200
# catalog-license lppl
# catalog-version 1.2b
Name:		texlive-wordlike
Version:	1.2b
Release:	1
Summary:	Simulating word processor layout
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/wordlike
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wordlike.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wordlike.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wordlike.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package simulates typical word processor layout: narrow
page margins, Times, Helvetica and Courier fonts, \LARGE or
\Large headings, and \sloppy typesetting. The package aims at
making life easier for users who are discontent with LaTeX's
standard layout settings because they need a layout that
resembles the usual "wordlike" output. The design of the
package draws on several discussions in the de.comp.text.tex
and comp.text.tex newsgroups that are referred to in the
manual.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/wordlike/wordlike.sty
%doc %{_texmfdistdir}/doc/latex/wordlike/README
%doc %{_texmfdistdir}/doc/latex/wordlike/wordlike.pdf
#- source
%doc %{_texmfdistdir}/source/latex/wordlike/wordlike.dtx
%doc %{_texmfdistdir}/source/latex/wordlike/wordlike.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
