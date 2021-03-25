#lang racket

(provide printer-error)

(define (printer-error s)
    (define l (string-length s))
    (define e (string-length (apply string-append (regexp-match* #rx"[n-z]+" s))))
    (format "~a/~a" e l)
)
