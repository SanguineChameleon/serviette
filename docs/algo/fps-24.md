# FPS 24 -- Unofficial Editorial

Here are my (somewhat questionable) solutions to all problems in AtCoder's FPS 24.

You can view the original statements [here](https://atcoder.jp/contests/fps-24). This page will skip over them for brevity.

## X -- Functional Square Root

Our main motivation comes from [this answer](https://math.stackexchange.com/a/950346) on Math Stack Exchange. Let

$$
G(x) = g_1x^1 + g_2x^2 + g_3x^3 + \ldots
$$

We will determine $g_1$, $g_2$, $g_3$, and so on, one coefficient at a time.

Initially, we know $g_1 = 1$. Suppose we want to find $g_k$ ($k \geq 2$). Define

$$
H(x) = g_1x^1 + g_2x^2 + g_3x^3 + \ldots + g_{k - 1}x^{k - 1}
$$

Let $H^{-1}(x)$ be the compositional inverse of $H(x)$, so $H(x) \circ H^{-1}(x) = x$.

Now, observe that:

$$
\begin{align*}
F(x) \circ H^{-1}(x)
&= (G(x) \circ G(x)) \circ H^{-1}(x) \\
&= G(x) \circ (G(x) \circ H^{-1}(x)) \\
&= G(x) \circ ((H(x) + g_kx^k + O(x^{k + 1})) \circ H^{-1}(x)) \\
&= G(x) \circ (H(x) \circ H^{-1}(x) + g_kx^k \circ H^{-1}(x) + O(x^{k + 1}) \circ H^{-1}(x)) \\
&= G(x) \circ (x + (g_kx^k + O(x^{k + 1}))+ O(x^{k + 1})) \\
&= G(x) \circ (x + g_kx^k + O(x^{k + 1})) \\
&= G(x) \circ (x + g_kx^k) + O(x^{k + 1}) \\
&= G(x + g_kx^k) + O(x^{k + 1}) \\
\end{align*}
$$

Therefore, since $g_1 = 1$:

$$
\begin{align*}
[x^k](F(x) \circ H^{-1}(x))
&= [x^k] G(x + g_kx^k) \\
&= 2g_k \\
\end{align*}
$$

Thus, to find $g_k$, we compute $H^{-1}(x)$ from $H(x)$, compose $F(x)$ with it, then find the coefficient of $x^k$ and divide by $2$.

Composition and inverse composition can be done in $O(N \log^2 N)$, so our solution is currently $O(N^2 \log^2 N)$, which is unfortunately not fast enough due to the massive constant factor.

Fret not, we still have one more trick up our sleeve. By the Lagrange--Bürmann formula:

$$
\begin{align*}
[x^k](F(H^{-1}(x)))
&= \frac{1}{k} [x^{k - 1}] F^\prime(x)\left(\frac{x}{H(x)}\right)^k \\
&= \frac{1}{k} [x^{k - 1}] F^\prime(x)\left(\frac{H(x)}{x}\right)^{-k} \\
&= \frac{1}{k} [x^{k - 1}] F^\prime(x)\exp\left(-k \log\left(\frac{H(x)}{x}\right) \right) \\
\end{align*}
$$

which is computable in $O(N \log N)$, so our final solution is $O(N^2 \log N)$ with good constants.
