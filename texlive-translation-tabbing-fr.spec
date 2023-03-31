Name:		texlive-translation-tabbing-fr
Version:	24228
Release:	2
Summary:	French translation of the documentation of Tabbing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/Tabbing/fr
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-tabbing-fr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-tabbing-fr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A translation to French (by the author) of the documentation of
the Tabbing package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/translation-tabbing-fr/f-Tabbing.dtx
%doc %{_texmfdistdir}/doc/latex/translation-tabbing-fr/f-Tabbing.pdf
%doc %{_texmfdistdir}/doc/latex/translation-tabbing-fr/ltxdoc.cfg

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
