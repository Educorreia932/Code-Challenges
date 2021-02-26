(defpackage #:challenge/solution
	(:use #:cl)
	(:export #:summation))
(in-package #:challenge/solution)

(defun summation (n) 
    (cond
        ((= n 1) 1)
        (T (+ n (summation (- n 1))))
    )
)
