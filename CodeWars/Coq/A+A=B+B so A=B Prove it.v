Require Import Arith.
Require Import Psatz.

From Coq Require Import omega.Omega.

Theorem invert : forall a b : nat, a + a = b + b -> a = b.

Proof. 
  lia.
Qed.