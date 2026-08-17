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