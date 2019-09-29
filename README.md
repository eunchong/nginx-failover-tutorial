# nginx-failover-tutorial

This repository provides tutorial code for nginx failover(proxy_next_upstream) cases.
- https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_next_upstream
## proxy_next_upstream cases
- [x] **error**

    an error occurred while establishing a connection with the server, passing a request to it, or reading the response header;
- [x] **timeout**

    a timeout has occurred while establishing a connection with the server, passing a request to it, or reading the response header;
- [ ] **invalid_header**

    a server returned an empty or invalid response;
- [x] **http_5xx**

    a server returned a response with the code 5xx;
- [x] **http_4xx**

    a server returned a response with the code 4xx;
- [ ] **http_429**

    a server returned a response with the code 429 (1.11.13);

- [x] **non_idempotent**

    normally, requests with a non-idempotent method (POST, LOCK, PATCH) are not passed to the next server if a request has been sent to an upstream server (1.9.13); enabling this option explicitly allows retrying such requests;
    - (idempotent) https://tools.ietf.org/html/rfc7231#section-4.2.2

- [ ] **max_fails**
    
    sets the number of unsuccessful attempts to communicate with the server that should happen in the duration set by the fail_timeout parameter to consider the server unavailable for a duration also set by the fail_timeout parameter. By default, the number of unsuccessful attempts is set to 1. The zero value disables the accounting of attempts. What is considered an unsuccessful attempt is defined by the proxy_next_upstream, fastcgi_next_upstream, uwsgi_next_upstream, scgi_next_upstream, memcached_next_upstream, and grpc_next_upstream directives.

- [ ] **fail_timeout**

    sets the time during which the specified number of unsuccessful attempts to communicate with the server should happen to consider the server unavailable; and the period of time the server will be considered unavailable. By default, the parameter is set to 10 seconds.

