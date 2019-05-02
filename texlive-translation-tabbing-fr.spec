# revision 24228
# category Package
# catalog-ctan /info/translations/Tabbing/fr
# catalog-date 2011-10-06 13:30:54 +0200
# catalog-license lppl1
# catalog-version undef
Name:		texlive-translation-tabbing-fr
Version:	20190228
Release:	1
Summary:	French translation of the documentation of Tabbing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/Tabbing/fr
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-tabbing-fr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-tabbing-fr.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111006-2
+ Revision: 757086
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111006-1
+ Revision: 719802
- texlive-translation-tabbing-fr
- texlive-translation-tabbing-fr
- texlive-translation-tabbing-fr

