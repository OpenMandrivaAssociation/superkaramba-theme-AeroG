%define theme_name AeroG
%define aname aeroG

Summary:	Monitoring theme for superkaramba
Name:		superkaramba-theme-%{theme_name}
Version:	0.8
Release:	7
License:	GPL
Group:		Monitoring
Url:		http://kde-look.org/content/show.php?content=21407
Source0:	%{theme_name}.tar.bz2
Requires:	superkaramba
BuildArch:	noarch

%description
This is a superkaramba theme which is a desktop applet that displays
system information.

%files
%dir %{_datadir}/apps/superkaramba/themes/%{theme_name}
%{_datadir}/apps/superkaramba/themes/%{theme_name}/*

%post
if [ $1 = 1 ]; then
echo "THEME path=%{theme_name}/%{aname}-cpu.theme" >> %{_datadir}/apps/superkaramba/themes/default.theme
echo "THEME path=%{theme_name}/%{aname}-disktheme" >> %{_datadir}/apps/superkaramba/themes/default.theme
echo "THEME path=%{theme_name}/%{aname}-mail.theme" >> %{_datadir}/apps/superkaramba/themes/default.theme
echo "THEME path=%{theme_name}/%{aname}-ram.theme" >> %{_datadir}/apps/superkaramba/themes/default.theme
echo "THEME path=%{theme_name}/%{aname}-swap.theme" >> %{_datadir}/apps/superkaramba/themes/default.theme
fi

%postun
if [ $1 = 0 ]; then
grep -v "%{theme_name}" %{_datadir}/apps/superkaramba/themes/default.theme > %{_datadir}/apps/superkaramba/themes/default.theme
exit 0
fi

#----------------------------------------------------------------------------

%prep
%setup -q -n %{theme_name}

%build

%install
mkdir -p %{buildroot}%{_datadir}/apps/superkaramba/themes/%{theme_name}
cp -rf * %{buildroot}%{_datadir}/apps/superkaramba/themes/%{theme_name}

