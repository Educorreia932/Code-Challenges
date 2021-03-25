#lang racket

(provide product-fib)

(define (fibonacci n)
    (if (< n 2) 
        n 
        (+ (fibonacci (- n 1)) (fibonacci (- n 2)))
    )
)

(define (product-fib-aux n prod)
    (define fib1 (fibonacci n))
    (define fib2 (fibonacci (+ n 1)))
    (define product (* fib1 fib2))

    (if (= product prod) 
        (list fib1 fib2 #t)
        (if (> product prod) 
            (list fib1 fib2 #f)
            (product-fib-aux (+ n 1) prod)
        )
    )
)

(define (product-fib prod)
    (product-fib-aux 0 prod)
)
