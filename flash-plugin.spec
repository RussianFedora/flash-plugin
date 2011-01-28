Summary:	Adobe Flash Player 10.2
Name: 		flash-plugin
Version: 	10.2.161.23
Release: 	2
Epoch:		5

Group: 		Applications/Internet
License: 	Commercial
URL: 		http://www.adobe.com
Source0:	flashplayer_square_p2_32bit_linux_092710.tar.gz
Source1:	flashplayer_square_p2_64bit_linux_092710.tar.gz

# https://bugzilla.redhat.com/show_bug.cgi?id=638477#c94
Source2:	memcpy-to-memmove.sh

BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Obsoletes:	swfdec-mozilla
Obsoletes:	flash-plugin-i386

Provides:	flash-plugin-meta

AutoReq:	on


%description
Adobe Flash (formerly Macromedia Flash) is a multimedia platform used to
add animation, video, and interactivity to Web pages. Flash is frequently
used for advertisements and games. More recently, it has been positioned
as a tool for "Rich Internet Applications" ("RIAs").


%prep
rm -rf %{buildroot}
%setup -q -c -T


%build


%install
mkdir -p %{buildroot}

%ifarch x86_64
pushd %{buildroot}
mkdir -p usr/lib64/flash-plugin
cd usr/lib64/flash-plugin
tar xzf %{SOURCE1}
# memcpy-to-memmove
%{SOURCE2} libflashplayer.so
popd
%else
pushd %{buildroot}
mkdir -p usr/lib/flash-plugin
cd usr/lib/flash-plugin
tar xzf %{SOURCE0}
popd
%endif

rm -rf %{buildroot}%{_datadir}/doc


mkdir -p %{buildroot}%{_libdir}/mozilla/plugins/
cd %{buildroot}%{_libdir}/mozilla/plugins/
ln -s ../../flash-plugin/libflashplayer.so


%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root)
%attr(0644,root,root) %{_libdir}/flash-plugin/*
%{_libdir}/mozilla/plugins/*.so


%changelog
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
