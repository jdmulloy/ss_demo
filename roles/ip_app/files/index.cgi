#!/usr/bin/env perl
use CGI;
#use CGI::Carp qw(fatalsToBrowser);
use Socket;

my $cgi = CGI->new;

print $cgi->header('text/plain');

my $ip_str = "$ENV{REMOTE_ADDR}";
my $ip = inet_aton($ip_str);
my $hostname = gethostbyaddr($ip, AF_INET);
my $timestamp = gmtime . " UTC";

print "IP: ${ip_str}\n";
print "Reverse DNS Hostname: ${hostname}\n";
print "Date: ${timestamp}\n";
