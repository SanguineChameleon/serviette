# Some Quant Things

Here are some quantitative finance things I've learned, in no particular order.

This page is not remotely exhaustive of the field.

## Theory of Interest

### Accumulation Function

For $t \geq 0$, we define $a(t)$ as the **total accumulated value** of $1$ dollar after $t$ units of time.

The total accumulated value consists of:

- The **principal**: how much money you put in the bank (or invest) at the start.
- The **interest**: a bonus reward you get for putting your trust in the bank, because the bank people are nice.

Note that $a(t)$ is the total accumulated value for $1$ single dollar only. Hence, if we invest $X$ dollars at the start, we'll end up with $X \cdot a(t)$ dollars after $t$ units of time.

Unless otherwise specified, $t$ will be in years from now on.

### Simple Interest

The total interest is linearly proportional to how long you've invested for.

If $r$ is the **annual interest rate**, then if we invest $1$ dollar at the start, then we'll get $r$ bonus dollars for each year. Hence:

$$a(t) = 1 + r \cdot t$$

This is mainly for toy examples; your actual bank account probably doesn't do this.

### Compound Interest

What most people think of when we refer to "interest".

Again, letting $r$ be the annual interest rate, our total amount of money will be multiplied by $(1 + r)$ after each year. Intuitively, the accumulated interest at the end of one year becomes part of the principal for the next year. Conversely, for simple interest, interest is always calculated based on the original principal of $1$ dollar. Hence:

$$a(t) = (1 + r)^t$$

### Compounding Frequency

I go to a bank where $r = 10\%$. I put in $1$ dollar. I wait $1$ year. I return to the bank. I withdraw from my account. I now have $1.1$ dollars. Life is good.

But life is short. Waiting $1$ year is too long. So the bank offers to compound the interest over $2$ periods of $6$ months instead.

So now I put in $1$ dollar. I wait $6$ months this time. I return to the bank. How much money will be in my account now?

Well, $r = 10\%$, so let's just split that in half to get $5\%$. So I should have $1.05$ dollars.

After another $6$ months, how much money will I have? Remember that compound interest applies here, so I will have $1.05 \cdot 105\% = 1.1025$ dollars. An extra $0.0025$ dollars! Life is great.

In general, if interest is compounded $p$ times a year, we get:

$$a(t) = (1 + \frac{r}{p})^{p \cdot t}$$

So what do we call $r$ now? That would be the **nominal interest rate**, which is essentially what the bank advertises to you. In reality, your money is compounded $p$ times per year at a periodic rate of $\frac{r}{p}$. Don't worry, the bank isn't cheating you; you actually benefit from this.

To avoid confusing ourselves, let's use a superscript to indicate how many compounding periods $p$ are made annually, like so:

$$a(t) = (1 + \frac{r^{(p)}}{p})^{p \cdot t}$$

One last headache to consider: in the example above, we had $r^{(2)} = 10\%$, and we ended up with $1.1025$ dollars after $1$ year. This means we effectively have an interest rate of $10.25\%$. Unsurprisingly, this is called the **effective interest rate**, which we'll denote by $r_e$.

So to recap, $r^{(2)} = 10\%$ implies $r_e = 10.25\%$, and vice versa. If we have one, we can derive the other. $r^{(p)}$ is the **nominal interest rate**, $r_e$ is the **effective interest rate**. Different things.

Funny edge case: when $p = 1$, the effective interest rate is just the nominal interest rate as-is, so we can drop the superscript.

### Equivalent Interest Rates

Two nominal interest rates are **equivalent** if they have the same effective interest rate over a year, i.e.:

$$(1 + \frac{r^{(p)}}{p})^{p} = (1 + \frac{r^{(q)}}{q})^{q} $$

For nonzero effective interest rates, if $p < q$, then $r^{(p)} > r^{(q)}$. Proof by calculus; I am too lazy to show it here.

### Continuous Compounding

Surely you have seen this before. If you crank $p$ up to infinity, you get the famous identity:

$$a(t) = \lim_{p \to \infty}(1 + \frac{r}{p})^{p \cdot t} = e^{r \cdot t} $$

I'm not really a fan of using the word "continuous", but it is what it is. We'll denote this continuously compounded rate by $r^{(\infty)}$.

### Force of Interest

I'm driving a car with an odometer. The odometer lets me know that I have driven a distance of $s(t)$ after $t$ units of time. So far so good, but I don't have a speedometer. What do?

Something something calculus, something something velocity $v(t)$ is the derivative of $s(t)$. If you know $s$, you can derive $v$. If you know $v$, you can derive $s$ ($+C$, lol).

Similarly, we can define the "velocity" at which we earn interest. This has a fancy name: the **force of interest**, denoted by $\delta(t)$.

As we'll see shortly, this is more general than anything we've seen so far. Under this framework, we can derive that continuous compounding has a constant "velocity": $\delta(t) = r^{(\infty)}$. That's cool and all, but not super realistic. Cars slow down and speed up all the time. Now we have the freedom to define a function $\delta$ as convoluted as we desire.

Okay, so first, how do we derive $\delta(t)$ from $a(t)$? We'll apply some basic limit-whacking. Consider a very small time step $h$. Since it's so small, we might as well assume we're using simple interest.

The raw amount of interest we earn between $t$ and $t + h$ is $a(t + h) - a(t)$. However, remember that interest rates are measured relative to how much we currently have. In all our earlier examples, we assumed we started out with $1$ dollar. But here, we actually have $a(t)$ dollars.

Putting this all together, and taking the limit as $h$ approaches $0$, we get:

$$\delta(t) = \lim_{h \to 0}\frac{a(t + h) - a(t)}{a(t) \cdot h} = \frac{a^\prime(t)}{a(t)}$$

So if we have $a$, we can derive $\delta$. Can we do it the other way around?

Sure. Let $u(x) = \ln(a(x))$. By the chain rule, we have:

$$u^{\prime}(x) = \frac{1}{a(x)} \cdot a^\prime(x) = \delta(x)$$

Then, by the fundamental theorem of calculus:

$$
\begin{align*}
\int_{0}^{t} \delta(x)\,dx
&= \int_{0}^{t} u^{\prime}(x)\,dx \\
&= u(t) - u(0) \\
&= \ln(a(t)) - \ln(a(0)) \\
&= \ln(a(t))
\end{align*}
$$

Thus,

$$
a(t) = \exp\left(\int_{0}^{t} \delta(x)\,dx\right)
$$

Nice. And this gives us a neat corollary. For any two points in time $s$ and $t$ ($0 \leq s \leq t$), if we put in $1$ dollar at time $s$, then the amount of money we'll have at time $t$ is:

$$
\begin{align*}
a(s, t) = \frac{a(t)}{a(s)}
& = \exp\left(\int_{0}^{t} \delta(x)\,dx - \int_{0}^{s} \delta(x)\,dx \right) \\
& = \exp\left(\int_{s}^{t} \delta(x)\,dx \right)
\end{align*}
$$

### Principle of Consistency

For $t_0 \leq t_1 \leq \ldots \leq t_n$,

$$
a(t_0, t_n) = a(t_0, t_1) \cdot a(t_1, t_2) \cdot \ldots \cdot a(t_{n - 1}, t_n)
$$

That's just how math works.

## Present Value and Time Value

### Present Value

Congrats! In $t$ units of time, you will receive $c$ dollars. But how much is that worth right now? Well, we know the total accumulated value of $1$ dollar after $t$ units of time is just $a(t)$. Sooo... $c$ dollars received in $t$ units of time is worth $\frac{c}{a(t)}$. Easy.

And just because we can, we might as well generalize. For a **cash flow**

$$ C = \{(c_1, t_1), (c_2, t_2), \ldots, (c_n, t_n)\} $$

the present value of said cash flow is:

$$ PV(C) = \sum_{i=1}^{n} \frac{c_i}{a(t_i)} $$

FYI, this is called **discounting**.

### Time Value

What if we don't care about the present, but some other time $t^\prime$ instead? Well, we know how much $C$ is worth at present, so we just multiply by $a(t^\prime)$ to get:

$$ {TV}_{t^\prime}(C) = PV(C) \cdot a(t^\prime) $$

Note that $PV(C)$ is really just $TV_0(C)$. In general, for $0 \leq t \leq t^{\prime}$, we have:

$$ 
\begin{align*}
TV_{t^\prime}(C)
& = \frac{TV_{t}(C)}{a(t)} \cdot a(t^\prime) \\
& = \frac{a(t^\prime)}{a(t)} \cdot TV_{t}(C) \\
& = a(t, t^\prime) \cdot TV_{t}(C)
\end{align*}
$$

Nice.

### Principle of Equivalence

Two cash flows $C_1$ and $C_2$ in the same environment (i.e., same accumulation function $a$) are equivalent if $TV_t(C_1) = TV_t(C_2)$ for *some* time $t \geq 0$. When this holds, $TV_t(C_1) = TV_t(C_2)$ is actually true for *all* times $t \geq 0$.

This is fairly intuitive, but I think it's a neat property.

### Deferred Cash Flow

Sike, I lied. You'll actually receive your cash flow $C$ after a $k$-year delay, which we'll denote as $C_{(k)}$. What is its present value now?

For an *annual effective interest rate* of $r$:

$$ PV(C_{(k)}) = \frac{PV(C)}{(1 + r)^k} $$

Don't get the numerator and denominator the wrong way round. If your cash flow is *deferred* by $k$ years, then it should be worth less at present, due to the compounded interest of those extra $k$ years. Well, assuming your cash flow is positive anyway.

## Internal Rate of Return

For reasons unknown, I find myself in an alien kingdom. There are plenty of banks here, which means plenty of opportunities to get my money's worth. Excellent.

I go to one such bank. I ask them what their annual effective interest rate is. They have no idea what I'm talking about, because they don't speak English.

I take out some units of their local currency from my pocket. Luckily, they seem to get the memo this time, and they show me a big table of cash payments:

$$ C = \{(c_1, t_1), (c_2, t_2), \ldots, (c_n, t_n)\} $$

"So, uh, what's your interest rate then?" I ask. They still have no idea what I'm talking about, because they still don't speak English.

Well, if they refuse to be accommodating to foreigners, I guess I'll have to take matters into my own hands.

For an annual effective interest rate of $r$, the present value of $C$ is:

$$ PV(C) = \sum_{i=1}^{n} \frac{c_i}{(1 + r)^{t_i}} $$

Since this is a bank after all, I expect that $PV(C)$ should equal the amount of money I offered them. We'll denote this initial payment as $(c_0, 0)$. Here, $c_0$ should be negative, since I'm giving the bank my money. All other $c_i$ should be positive, since the bank is giving *me* money.

Thus, we wish to solve for the following **equation of value**:

$$ c_0 + \sum_{i=1}^{n} \frac{c_i}{(1 + r)^{t_i}} = 0 $$

Under these constraints ($c_0 < 0$, $c_i > 0$ and $t_i > 0$ for $i \geq 1$), it can be shown that this equation has a *unique* root $r > -1$, which we'll call the **internal rate of return** (IRR).

That's cool and all, but who cares? It's not like the bank is actually paying me on a regular basis. Their payment times $t_i$ are all over the place.

Well, if this alien bank had an IRR of $10\%$, and some other alien bank had an IRR of $50\%$, then it's (probably) worth going to the other bank instead. Of course, there's more nuance to this. If getting that $50\%$ IRR required me to pay way more money upfront, or the bank was ethically questionable and at risk of shutting down, then maybe I should think twice about it.

But anyway, IRR gives us an imperfect but much more intuitive grasp than just staring at a pile of cash payments. This applies to many other things, such as companies making financial decisions about the profitability of projects, not just rude alien banks.