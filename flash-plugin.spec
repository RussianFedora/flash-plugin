Summary:    Adobe Flash Player 11
Name:       flash-plugin
Version:    11.2.202.491
Release:    1%{?dist}
Epoch:      7

Group:      Applications/Internet
License:    Proprietary
URL:        http://www.adobe.com
Source0:    http://fpdownload.macromedia.com/get/flashplayer/pdc/%{version}/install_flash_player_11_linux.i386.tar.gz
Source1:    http://fpdownload.macromedia.com/get/flashplayer/pdc/%{version}/install_flash_player_11_linux.x86_64.tar.gz

Provides:   flash-plugin-meta
AutoReq:    on


%description
Adobe Flash (formerly Macromedia Flash) is a multimedia platform used to
add animation, video, and interactivity to Web pages. Flash is frequently
used for advertisements and games. More recently, it has been positioned
as a tool for "Rich Internet Applications" ("RIAs").

%package kde
Summary:    KDE workspace files
Group:      Applications/Internet
Requires:   %{name} = %{epoch}:%{version}


%description kde
Adobe Flash files to work with KDE


%prep
%setup -q -c -T 


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

pushd %{buildroot}

mkdir -p %{buildroot}%{_libdir}/mozilla/plugins/
%ifarch x86_64
tar xzf %{SOURCE1}
%else
tar xzf %{SOURCE0}
%endif
mv libflashplayer.so %{buildroot}%{_libdir}/mozilla/plugins/

rm -f %{buildroot}/readme.txt

%ifarch x86_64
rm -rf %{buildroot}/usr/lib/kde4/
%endif

rm -rf %{buildroot}/LGPL


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database %{_datadir}/applications &> /dev/null ||:


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
update-desktop-database %{_datadir}/applications &> /dev/null ||:


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root, -)
%{_bindir}/flash-player-properties
%attr(0755,root,root) %{_libdir}/mozilla/plugins/*.so
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/flash-player-properties.png
%{_datadir}/pixmaps/flash-player-properties.png

%files kde
%defattr(-, root, root, -)
%{_libdir}/kde4/kcm_adobe_flash_player.so
%{_datadir}/kde4/services/kcm_adobe_flash_player.desktop


%changelog
* Thu Jul 16 2015 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.491-1.R
- update to 11.2.202.491

* Thu Jul  9 2015 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.481-1.R
- update to 11.2.202.481

* Thu Jun 25 2015 Vasiliy N. Glazov <vascom2@gmail.com> 7:11.2.202.468-1.R
- update to 11.2.202.468

* Sun Jun 14 2015 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.466-1.R
- update to 11.2.202.466

* Wed May 13 2015 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.460-1.R
- update to 11.2.202.460

* Sun Mar 15 2015 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.451-1.R
- update to 11.2.202.451

* Fri Jan 30 2015 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.440-1.R
- update to 11.2.202.440

* Wed Jan 14 2015 Vasiliy N. Glazov <vascom2@gmail.com> 7:11.2.202.429-1.R
- update to 11.2.202.429

* Fri Dec 12 2014 Vasiliy N. Glazov <vascom2@gmail.com> 7:11.2.202.425-1.R
- update to 11.2.202.425

* Thu Nov 27 2014 Vasiliy N. Glazov <vascom2@gmail.com> 7:11.2.202.418-1.R
- update to 11.2.202.418
- correct bogus dates in changelog

* Sat Aug  2 2014 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.400-1.R
- update to 11.2.202.400

* Wed Apr 30 2014 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.356-1.R
- update to 11.2.202.356

* Mon Mar 17 2014 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.346-3.R
- and in kde package too

* Mon Mar 17 2014 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.346-2.R
- pack only files

* Mon Mar 17 2014 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.346-1.R
- update to 11.2.202.310

* Mon Sep 30 2013 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.310-1.R
- update to 11.2.202.310

* Mon Jul 22 2013 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.297-1.R
- update to 11.2.202.297

* Fri Apr 12 2013 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.280-1.R
- update to 11.2.202.280

* Thu Feb 28 2013 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.273-1.R
- update to 11.2.202.273

* Mon Oct 15 2012 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.243-1.R
- update to 11.2.202.243

* Fri Aug 24 2012 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.238-1.R
- update to 11.2.202.238

* Thu Jun 14 2012 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.236-1.R
- update to 11.2.202.236

* Mon May 14 2012 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.235-1.R
- update to 11.2.202.235

* Thu Apr 26 2012 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.1.102.63-2.R
- back to old flash.

* Mon Apr  2 2012 Arkady L. Shane <ashejn@russianfedora.ru> 6:11.2.202.228-1.R
- update to 11.2.202.228. Last?

* Wed Mar  7 2012 Arkady L. Shane <ashejn@russianfedora.ru> 6:11.1.102.63-1.R
- update to 11.1.102.63

* Fri Feb 17 2012 Arkady L. Shane <ashejn@russianfedora.ru> 6:11.1.102.62-1.R
- update to 11.1.102.62

* Mon Nov 14 2011 Arkady L. Shane <ashejn@russianfedora.ru> 6:11.1.102.55-1.R
- update to 11.1.102.55

* Tue Oct 04 2011 Vasiliy N. Glazov <vascom2@gmail.com> 6:11.0.1.152-1.R
- update to 11.0.1.152

* Fri Sep 09 2011 Vasiliy N. Glazov <vascom2@gmail.com> 6:11.0.r1.129-1.R
- update to 11.0.r1.129

* Thu Jul 14 2011 Arkady L. Shane <ashejn@yandex-team.ru> 6:11.0.1.60-3.R
- fix R in kde

* Thu Jul 14 2011 Arkady L. Shane <ashejn@yandex-team.ru> 6:11.0.1.60-2.R
- create separate package for KDE

* Thu Jul 14 2011 Arkady L. Shane <ashejn@yandex-team.ru> 6:11.0.1.60-1
- update to 11.0.1.60

* Thu Nov 18 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 10.2.161.23-2
- apply https://bugzilla.redhat.com/show_bug.cgi?id=638477#c94 hack

* Wed Sep 29 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 10.2.161.23-1
- update to preview 2 10.2.161.23

* Mon Sep 20 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 10.2.161.22-1
- update to preview 1 10.2.161.22

* Mon Aug  3 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.32.18-1
- update to 10.0.32.18

* Fri Feb 27 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.22.87-1
- update to 10.0.22.87

* Mon Dec 22 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.15.3-2
- drop x86_64 compatibility

* Fri Dec 19 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.15.3-1
- update to 10.0.15.3

* Mon Nov 17 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.12.36-2
- remove depends on libflashsupport

* Wed Oct 15 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.12.36-1
- update to 10.0.12.36

* Thu May 22 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 9.0.124.0-1
- try to do everything for x86_64
