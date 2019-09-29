# nginx-failover-tutorial

This repository provides tutorial code for nginx failover(proxy_next_upstream) cases.

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
