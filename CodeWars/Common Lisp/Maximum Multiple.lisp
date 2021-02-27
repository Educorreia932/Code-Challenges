(defpackage #:challenge/solution
    (:use #:cl)
    (:export #:max-multiple))
(in-package #:challenge/solution)

(defun max-multiple (divisor bound)
    1

    (loop for i from 0 to bound
        if (= 0 (mod (- bound i) divisor))
        do (return (- bound i))
    )
)
