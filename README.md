<h1>Perl Imgur.com Caching Proxy</h1>

<h2>Setup & Use...</h2>

Stick `index.cgi` in a directory with +ExecCGI<br>
Make a directory to save the cached images to and set it in the `my $cachedir` variable. <br>

To view and cache an image, browse to `https://{your.host}/cgidirectory/index.cgi?{id}.{ext}` <br>

Example: https://i.imgur.com/aaa8x.gif --> `https://your.host/cgi-bin/index.cgi?aaa8x.gif`

<h2>Todo...</h2>

* Set ignore on placeholder image for removed images and return error rather than caching it. <br>
  Example: `aaaa2.jpg --> removed.png` and `md5sum` is `d835884373f4d6c8f24742ceabe74946`

* Add nesting to cache directory structure.
