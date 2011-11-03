# revision 24228
# category Package
# catalog-ctan /info/translations/Tabbing/fr
# catalog-date 2011-10-06 13:30:54 +0200
# catalog-license lppl1
# catalog-version undef
Name:		texlive-translation-tabbing-fr
Version:	20111006
Release:	1
Summary:	French translation of the documentation of Tabbing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/Tabbing/fr
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-tabbing-fr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-tabbing-fr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A translation to French (by the author) of the documentation of
the Tabbing package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/translation-tabbing-fr/f-Tabbing.dtx
%doc %{_texmfdistdir}/doc/latex/translation-tabbing-fr/f-Tabbing.pdf
%doc %{_texmfdistdir}/doc/latex/translation-tabbing-fr/ltxdoc.cfg
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}