Name:		texlive-wordlike
Version:	15878
Release:	2
Summary:	Simulating word processor layout
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/wordlike
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wordlike.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wordlike.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wordlike.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/wordlike/wordlike.sty
%doc %{_texmfdistdir}/doc/latex/wordlike/README
%doc %{_texmfdistdir}/doc/latex/wordlike/wordlike.pdf
#- source
%doc %{_texmfdistdir}/source/latex/wordlike/wordlike.dtx
%doc %{_texmfdistdir}/source/latex/wordlike/wordlike.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
