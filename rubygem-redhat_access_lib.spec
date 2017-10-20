%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name redhat_access_lib

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.8
Release: 2%{?dist}
Summary: REST client library for accessing Red Hat support
Group: Development/Languages
License: GPLv2+
URL: https://github.com/redhataccess/redhat-support-lib-ruby
Source0: %{gem_name}-%{version}.gem


Requires: %{?scl_prefix_ruby}ruby(rubygems)

BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
REST client library for accessing Red Hat support


%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}


%setup -q -D -T -n  %{gem_name}-%{version}


%build
mkdir -p .%{gem_dir}

# Create our gem
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

# install our gem locally, to be moved into buildroot in %%install
%{?scl:scl enable %{scl} "}
gem install --local --no-wrappers --install-dir .%{gem_dir} --force --no-rdoc --no-ri %{gem_name}-%{version}.gem
%{?scl:"}


%install
mkdir -p %{buildroot}%{gem_dir}

cp -pa .%{gem_dir}/* %{buildroot}%{gem_dir}/


%files
%defattr(-,root,root,-)
%{gem_dir}


%changelog
* Fri Oct 20 2017 Lindani Phiri <lindani@redhat.com> - 1.0.8-2
- BZ 1449233 (topic filtering bug)

* Tue Jun 06 2017 Lindani Phiri <lindani@redhat.com> - 1.0.7-1
- BZ 1449233

* Wed Jan 04 2017 Lindani Phiri <lindani@redhat.com> - 1.0.6-1
- BZ 1403979

* Sat Sep 17 2016 Lindani Phiri <lindani@redhat.com> - 1.0.5-1
- BZ 1377025

* Thu Aug 18 2016 Lindani Phiri <lindani@redhat.com> - 1.0.4-1
- BZ 1362187

* Wed Aug 10 2016 Lindani Phiri <lindani@redhat.com> - 1.0.3-1
- BZ 1365590

* Tue May 31 2016 Lindani Phiri <lindani@redhat.com> - 1.0.2-1
- BZ 1340254

* Tue Feb 23 2016 Lindani Phiri <lindani@redhat.com> - 1.0.1-1
- Resolves 1306850

* Tue Feb 02 2016 Lindani Phiri <lindani@redhat.com> - 1.0.0-1
- Resolves 1297523
- Resolves 1293463

* Wed Nov 11 2015 Lindani Phiri <lindani@redhat.com> - 0.0.6-1
- Fix proxy Bug  BZ 1282576
- Set content type correctly for telemetry Proxy
- Resolves 1276677

* Fri Oct 2 2015 Lindani Phiri <lindani@redhat.com> - 0.0.5-1
- Add support for machine-id subsets queries for RHAI

* Mon Jul 13 2015 Lindani Phiri <lindani@redhat.com> - 0.0.4-2
- Remove unnecessary rubyabi dependency

* Mon Jul 13 2015 Lindani Phiri <lindani@redhat.com> - 0.0.4-1
- GA build for Access Insights
- Resolves : bz1193202

* Fri May 29 2015 Lindani Phiri <lindani@redhat.com> - 0.0.3-1
- Correct subset calls for telemetry system/status
- Resolves : bz1217726

* Tue May 19 2015 Lindani Phiri <lindani@redhat.com> - 0.0.2-2
- First tech preview  release of RHAI for QA testing
- Resolves : bz1217726

* Mon Apr 06 2015 Lindani Phiri <iphiri@redhat.com> - 0.0.2-1
- Beta build for HTB customers

* Wed Apr 30 2014 Rex White <rexwhite@redhat.com> - 0.0.1-1
- Resolves: bz1084590

* Thu Apr 3 2014 Rex White <rexwhite@redhat.com>
- Initial package
