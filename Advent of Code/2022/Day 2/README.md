# Day 2

The year is 1999, Matrix has just been released, and so has [C99](https://wikipedia.org/wiki/C99), one of the revisions of the **C** programming language, and it's going to be language used for this day.

Buckle up, because this is going to get overly complicated very soon.

![](https://media.tenor.com/MNsyvrBKTHIAAAAC/matric-matrix.gif)

## Solution

Rock, paper and scissors are represented by different letters, so I mapped them into this chart:

```mermaid
graph TD;
    R(fa:fa-hand-back-fist A/X)
    P(fa:fa-hand-paper B/Y)
    S(fa:fa-hand-scissors C/Z)

    R-->S;
    P-->R;
    S-->P;
```

Now, let $x \in \{A, B, C\}$  be the the opponent's play and $y \in \{X, Y, Z\}$  our play. These correspond to the first and second columns of the input, respectively.

Since in [ASCII](https://en.wikipedia.org/wiki/ASCII), the characters have different values, let's offset let them, so that both plays have the same value (since they are both representing the same shape, *e.g.* $A \equiv X \equiv Rock$).

To do so, we subtract the decimal ASCII value of the shape with the lowest value: $A \rightarrow 65; X \rightarrow 88$.

$y = y - 65$

$x = x - 88$

This produces the following mapping:

$$
\begin{cases}
    {A, X} \gets 0 \\
    {B, Y} \gets 1 \\
    {C, Z} \gets 2
\end{cases}
$$

After this, instead of:

```
A Y
B X
C Z
```

We have:

```
0 1
1 0
2 2
```

Now, we have to calculate the score for each round, $R$. The score is composed of two elements, the score for the selected shape, $S$, and the outcome of the round, $O$.

### Shape score

$$
S = 
\begin{cases}
    0, \text{Defeat} \\
    3, \text{Draw} \\
    6, \text{Victory} 
\end{cases}
$$

Let $\delta = x - y$.

Now, interpreting this value as the outcome of the round, $S'$.

$$
\delta = S' = 
\begin{cases}
    -1, \text{Defeat} \\
    0, \text{Draw} \\
    1, \text{Victory} 
\end{cases}
$$

However, for **Rock (A)** *vs* **Scissors (Z)**:

$$
\begin{aligned}
S' &= A - Z \\
   &= 0 - 2 \\
   &= -2
\end{aligned}
$$

$-2$ should not be of the possible values of $S'$. Instead, the intended correct value is $1$ (a victory for rock).

This is because the value $0$ of $A$ should actually be $3$ to comply with the scheme of the chart, *i. e* every winning shape's value, $W$ is the losing shape's value, $L$, plus one $W = L + 1$.

However, due to the cyclic nature of the game, $3$ becomes $0$, as every value is in modulus $3$: $3 \equiv 0 \mod 3$.

For **Scissors (Z)** *vs* **Rock (A)** we would have $2$ instead.

To get around this, we need to make sure $S' \in \{-1, 0, 1\}$.

A simple solution would be to get the $S' \mod 3$, however for $\delta = -1$:

$$
\begin{aligned}
    S' &= -1 \mod 3 \\
       &= 2 \\ 
       &\neq -1
\end{aligned}
$$

So, even though this solution works for this case, I wanted a more general approach that would assure consistency without any specific conditions.

That solution is offsetting the values until they meet the interval $[-1, 1]$.

```
...
-2 -> 1
-1 -> -1
0 -> 0
1 -> 1
2 -> -1
...
```

$$
S' = -3 \Bigl\lfloor\dfrac{\delta \pm 1}{3}\Bigr\rfloor + \delta
$$

Finally, to map $S'$ to $S$:

$$
S = 3 (S' + 1)
$$

### Outcome score

$$
S = 
\begin{cases}
    1, \text{Rock} \\
    2, \text{Paper} \\
    3, \text{Scissors} 
\end{cases}
$$

$O = y + 1$

### Round score

After obtaining both scores, we get:

$$\therefore R = S + O$$