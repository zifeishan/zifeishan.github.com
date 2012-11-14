Libraries Included
----

* [Bootstrap](http://twitter.github.com/bootstrap/) - Apache License v2.0
* [jQuery](http://jquery.org/) - dual-licensed under the MIT License or the GPL
* a2ps - for pdf generation
* pdftk - for pdf generation
* pyyaml - for website generation
* pystache - for website generation
* pypdf - for pdf valdiation
* ratproxy - for form security validation
* libssl-dev - for ratproxy
* openssl - for ratproxy and NGINX
* curl - for NGINX

NGINX installation
----

1. Install PCRE: 
    - wget ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.31.tar.gz
    - tar xzvf pcre-8.31.tar.gz
    - cd pcre-8.31
    - ./configure, make, sudo make install
    
2. Install openssl

3. Install NGINX
    - default into: /usr/local/nginx

4. How to use:
    - Start: sudo nginx 
    - Restart: sudo kill -HUP `cat /usr/local/nginx/logs/nginx.pid` 
    - Test configuration: sudo nginx -t
    - Reload config: sudo nginx -s reload
    - Stop nginx: nginx -s stop

5. Run /usr/local/nginx/sbin/nginx: error while loading shared libraries: libpcre.so.1: cannot open shared object file: No such file or directory
    - Enter /lib, check: "ls libpcre*", my version is: libpcre.so.3.12.1.
    - Do the following link in /lib: sudo ln -s libpcre.so.3.12.1 libpcre.so.1

6. Edit /usr/local/nginx/conf/nginx.conf.

7. To support python scripts
    
    - Use FastCGI
    - Currently: use spawn-fcgi + flup. [Chinese guideline](http://blog.csdn.net/linvo/article/details/5870498)
        - But now it doesn't work.
    - Will try using [uwsgi](http://projects.unbit.it/uwsgi/).

    - Some tutorials on python CGI:
        - http://docs.python.org/library/cgi.html
        - http://wiki.python.org/moin/CgiScripts
        - http://forum.nginx.org/read.php?2,216514,216533
    
