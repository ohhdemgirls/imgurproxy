#!/usr/bin/env perl

no warnings; 
use strict; 
use CGI::Carp qw(fatalsToBrowser); # don't just give Error 500 messages
use CGI;
use LWP; # that which grabs the imgur image

my $cachedir = "/set/cache/dir/";

my $q = CGI->new();
my $user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"; # useragent passed to imgur
my $img = $ENV{'QUERY_STRING'}; # get the imgur information

if (-e "$cachedir/$img") { # cached
	chomp(my $mime = qx!file -i $cachedir/$img!); #use `file` to get the mimetype
	$mime =~ s/^.*?: //; #process
	$mime =~ s/;.*//; #process more
	$| = 1; # stdout hot
	print "Content-type: $mime\n\n"; #output magic
	use File::Copy;
	copy "$cachedir/$img", \*STDOUT;
	
} else {

my @header = ('Referer'=>'https://imgur.com/', 'User-Agent'=>$user_agent);

# virtual browser
my $browser = LWP::UserAgent->new();

# read the imgur data
my $response = $browser->get('http://i.imgur.com/' . $img, @header);

# post the imgur data from whatever server this is currently residing on
# and don't have to figure out what type of image it is!
print "Content-type: " . $response->header("Content-Type") . "\n\n";

# image data stuck in this object
print $response->content;

#the caching
open my $fh, ">", "$cachedir/$img" or die "$!";
print $fh $response->content;
close $fh;
}

