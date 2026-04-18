# Binary Lifting

Binary lifting is, at its core, just binary search. So let's begin there.

## Binary Search

There are many ways to formulate binary search, and they're pretty much all equivalent to each other. Here, we'll use the following framework:

!!! note "Framework"
    
    Let $P$ be some predicate defined over all integers $0 \leq i \leq n$, such that $P$ satisfies the following properties:

    1. $P(0)$ is false.
    2. $P(n)$ is true.
    3. For any $i$ where $0 \leq i < n$, if $P(i)$ is true, then so is $P(i + 1)$.


    Then, there exists exactly one value $x$ ($0 \leq x < n$) such that $P(x)$ is false, and $P(x + 1)$ is true. This is the "cut-off" point for $P$, and we're interested in finding it efficiently.

### Classic Method

To do classic binary search, keep track of two variables, $l$ and $r$. Initially, $l = 0$ and $r = n$. We'll maintain the following invariants:

1. $P(l)$ is false.
2. $P(r)$ is true.
3. The cut-off $x$ satisfies $l \leq x < r$.

We repeat the following until $r - l = 1$:

1. Choose any index $m$ such that $l < m < r$. Such an index must exist when $r - l > 1$.
2. If $P(m)$ is true, then set $r = m$. Otherwise, set $l = m$.

Once $r - l = 1$, we know the cut-off $x$ is equal to $l$.

This algorithm works regardless of what $m$ is chosen at each step $1$. But of course, ideally, we'd choose an $m$ somewhere in the middle, so we can roughly divide the search space in half:

```py linenums="1"
def binary_search(P, n):
    l = 0
    r = n
    while r - l > 1:
        m = (l + r) // 2
        if P(m):
            r = m
        else:
            l = m
    return l
```

However, we don't necessarily have to set $m = \lfloor \frac{l + r}{2} \rfloor$ at each iteration. As long as it still costs $O(\log n)$ iterations in total, we're good to go. This is the motivation for the Lifting Method.

### Lifting Method

Now, for each step, let $k$ be the largest integer such that $2^k < r - l$. Then set $m = l + 2^k$. The rest of the logic is unchanged:

```py linenums="1"
def binary_search(P, n):
    l = 0
    r = n
    while r - l > 1:
        k = (r - l - 1).bit_length() - 1
        m = l + (1 << k)
        if P(m):
            r = m
        else:
            l = m
    return l
```

We note that $2^k = m - l$ (by definition of $m$) and $2^k \geq r - m$ (proof by contradiction). Therefore, the $k$ computed in the next iteration must be strictly smaller than the current $k$.

Since $k$ is at most $O(\log n)$, and $k$ always decreases between iterations, this algorithm is $O(\log n)$.

Now, let's take this one step further. Instead of computing $k$ at each step, we just try all possible $k$ from $b = \lfloor \log_2(n - 1) \rfloor$ to $0$. If $m = l + 2^k$ happens to be greater than or equal to $r$, then no worries, we just skip that iteration.

```py linenums="1" hl_lines="7"
def binary_search(P, n):
    L = (n - 1).bit_length() - 1
    l = 0
    r = n
    for k in range(L, -1, -1):
        m = l + (1 << k)
        if m >= r:
            continue
        if P(m):
            r = m
        else:
            l = m
    return l
```

We can change the check at line $7$ to compare against $n$ instead of $r$. This does potentially mean our search space may unnecessarily grow to the right if $r < m < n$, but this isn't really an issue, since we're still bounded by $O(\log n)$ iterations, anyway.

```py linenums="1"
def binary_search(P, n):
    L = (n - 1).bit_length() - 1
    l = 0
    r = n
    for k in range(L, -1, -1):
        m = l + (1 << k)
        if m >= n:
            continue
        if P(m):
            r = m
        else:
            l = m
    return l
```

Actually, we don't even need ``r`` anymore:

```py linenums="1"
def binary_search(P, n):
    L = (n - 1).bit_length() - 1
    l = 0
    for k in range(L, -1, -1):
        m = l + (1 << k)
        if m >= n:
            continue
        if P(m):
            continue
        else:
            l = m
    return l
```

Finally, let's do some clean-up and rename ``l`` to ``x``:

```py linenums="1"
def binary_search(P, n):
    L = (n - 1).bit_length() - 1
    x = 0
    for k in range(L, -1, -1):
        t = 1 << k
        if x + t < n and not P(x + t):
            x += t
    return x
```

This is **binary lifting**. Intuitively, we are building (or "lifting") the result $x$ one bit at a time, starting from the MSB and working towards the LSB.

## Focus Problem

Now let's try solving [CSES - Visible Buildings Queries](https://cses.fi/problemset/task/3304).

!!! note "Statement"

    There are $n$ buildings with heights $h[0], h[1], \ldots, h[n-1]$.

    Process $q$ queries. In each query, you are given two integers $a$ and $b$ ($0 \leq a \leq b \leq n-1$). 

    You are standing in front of building $c_1 = a$. The next building you see is the smallest index $c_2 > c_1$ such that $h[c_2] > h[c_1]$. The next building you see after that is the smallest index $c_3 > c_2$ such that $h[c_3] > h[c_2]$, and so on.

    Only indices up to $b$ will be considered; the rest are ignored. In total, how many buildings can you see?

Let's ignore the constraint on $b$ for now, and focus on finding where the next visible building would be. For a given index $i$, let $J(i)$ be the smallest index $j$ such that $h[j] > h[i]$, or $n$ if there's no such index. We'll also define $J(n) = n$; this will make things easier later on.

$J(0), J(1), \ldots, J(n)$ can be computed in total $O(n)$ time using a monotonic stack. It is not the focus of this article, so here I'll just provide a dummy $O(n^2)$ implementation:

```py linenums="1"
J = [None] * (n + 1)
for i in range(n):
    for j in range(i + 1, n):
        if h[j] > h[i]:
            J[i] = j
            break
    else:
        J[i] = n
J[n] = n
return J
```

To answer a query $(a, b)$, just start from $a$, and keep setting $a = J(a)$ until $a > b$:

```py linenums="1"
def query(a, b):
    res = 0
    while a <= b:
        res += 1
        a = J[a]
    return res
```

This is very slow. Surely we can do better.

### Iterated Jumping

We'll take inspiration from iterated functions.

Let $J^m$ be the $m$-th iterate of $J$. In other words, $J^m(i)$ is the result of repeatedly setting $i = J(i)$ a total of $m$ times in a row:

```py linenums="1"
def J_iterate(m, i):
    for _ in range(m):
        i = J[i]
    return i
```

We'll pretend that we can somehow compute this efficiently for now.

Let's then return to using binary search. We define $P(m)$ to be true if $J^m(a) > b$, and false otherwise. Let the cut-off point for $P$ be $x$. Then, by definition, $J^x(a) \leq b$ and $J^{x+1}(a) > b$, so after seeing the first $x$ buildings in front of $a$, the next one will exceed the boundary $b$. The answer to our query is thus $x + 1$.

```py linenums="1"
def query(a, b):
    
    def P(m):
        return J_iterate(m, a) > b

    L = (n - 1).bit_length() - 1
    x = 0
    for k in range(L, -1, -1):
        t = 1 << k
        if x + t < n and not P(x + t):
            x += t
    return x + 1
```

Replace $P(m)$ with its definition and we get:

```py linenums="1" hl_lines="6"
def query(a, b):
    L = (n - 1).bit_length() - 1
    x = 0
    for k in range(L, -1, -1):
        t = 1 << k
        if x + t < n and J_iterate(x + t, a) <= b:
            x += t
    return x + 1
```

Next, we observe that, by function composition, $J^{x + t}(a) = J^t(J^x(a))$:

```py linenums="1" hl_lines="6"
def query(a, b):
    L = (n - 1).bit_length() - 1
    x = 0
    for k in range(L, -1, -1):
        t = 1 << k
        if x + t < n and J_iterate(t, J_iterate(x, a)) <= b:
            x += t
    return x + 1
```

Let's do some refactoring. Whenever we increment $x$ by $t$, we'll also set $a = J^t(a)$:

```py linenums="1"
def query(a, b):
    L = (n - 1).bit_length() - 1
    x = 0
    for k in range(L, -1, -1):
        t = 1 << k
        c = J_iterate(t, a)
        if x + t < n and c <= b:
            x += t
            a = c
    return x + 1
```

Intuitively, we're trying each power of $2$ in decreasing order: $2^L, 2^{L - 1}, \dots, 2^0$. At each iteration, we try to "jump" forwards by $2^k$. If we haven't exceeded $b$, then good, keep going! Otherwise, we know we've jumped too far, so we must skip over this power of $2$.

Again, this is the essence of binary lifting. We are determining how far we can jump forward, one bit at a time, from the MSB to the LSB.

### Jump Table

Now, we just need to optimize our ``J_iterate``.

This is luckily straightforward. Note that in all invocations of ``J_iterate`` during the query, the $m$ argument is, by design, always a power of $2$.

So, simply use the fact that $J^{m}(i) = J^{\frac{m}{2}}(J^{\frac{m}{2}}(i))$ for all even $m > 1$:

```py linenums="1"
@cache
def J_iterate(m, i):
    if m == 1:
        return J[i]
    else:
        return J_iterate(m // 2, J_iterate(m // 2, i))
```

Okay, but let's not abuse Python's magical ``@cache`` and instead pre-compute and store the values of ``J_iterate`` in a table. Here, $\text{table}[k][i] = J^{2^k}(i)$:

```py linenums="1"
K = (n - 1).bit_length() - 1
table = [[None] * (n + 1) for _ in range(K + 1)]
table[0] = J
for k in range(1, K + 1):
    for i in range(n + 1):
        table[k][i] = table[k - 1][table[k - 1][i]]
```

Finally, our query now looks like this:

```py
def query(a, b):
    x = 0
    for k in range(K, -1, -1):
        t = 1 << k
        c = table[k][a]
        if x + t < n and c <= b:
            x += t
            a = c
    return x + 1
```

Pre-computation is $O(n \log n)$, and each query costs $O(\log n)$. We are done!

## Appendix

### Arbitrary Jumping

It's worth noting that, after building the table, we can efficiently compute $J^{m}(i)$ for any value of $m$, not just for powers of $2$. Just use the binary representation of $m$ and apply function composition. This is $O(\log m)$ per query, and can be useful for other problems, e.g., querying the $m$-th ancestor of a node $u$ in a rooted tree.

### Full Code

Here's the full code, which gets Accepted on CSES.

??? success "Full Code"
    ```py
    import io, os
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    n, q = map(int, input().split())
    h = list(map(int, input().split()))

    J = [None] * (n + 1)
    stack = []
    for i in range(n - 1, -1, -1):
        while len(stack) > 0 and h[stack[-1]] <= h[i]:
            stack.pop(-1)
        if len(stack) == 0:
            J[i] = n
        else:
            J[i] = stack[-1]
        stack.append(i)
    J[n] = n

    K = max(0, (n - 1).bit_length() - 1)
    table = [[None] * (n + 1) for _ in range(K + 1)]
    table[0] = J
    for k in range(1, K + 1):
        for i in range(n + 1):
            table[k][i] = table[k - 1][table[k - 1][i]]

    def query(a, b):
        x = 0
        for k in range(K, -1, -1):
            t = 1 << k
            c = table[k][a]
            if x + t < n and c <= b:
                x += t
                a = c
        return x + 1

    for _ in range(q):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        print(query(a, b))
    ```
