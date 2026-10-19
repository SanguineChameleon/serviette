# Basics of Probability Distributions

Statistics is pretty much all about probability distributions and how we use them to model real-world phenomena. So let's get right to it.

## Preamble

To prevent the inevitable headaches with infinities and measure spaces, there will be many abuses of notation throughout this article. Primarily, I'll be conflating $\sum$ and $\int$ a lot. They are, in some sense, "the same thing", and I'll only make the distinction when I see fit.

I don't want to be *too* formal, nor do I want to whack a bunch of formulas and call it a day. Ultimately, the goal is to develop an intuitive grasp of these concepts.

## Random Variables

A **random variable** is, unsurprisingly, a variable that is random. When you roll a die, its outcome $X$ is a random variable. In this case, $X$ is some integer from $1$ to $6$. We'll denote $S$ (or $S_X$ for disambiguation between multiple random variables) as the set of possible values that $X$ can take on. Here, for a die roll, $S = \{1, 2, 3, 4, 5, 6\}$.

A random variable is **discrete** if $S$ is finite or countably infinite (e.g., $S = \mathbb{Z}$). There are also continuous random variables, where we'll just assume $S$ is the union of some intervals of $\mathbb{R}$ for simplicity.

### Probability Mass Function

For a discrete random variable $X$, each outcome $x \in S$ has some probability $p(x)$ of occurring. For example, with fair dice, each number is equally likely to occur, so $p(x) = \frac{1}{6}$ for all $x \in S$. But maybe you have a loaded die which favors $6$'s, e.g., $p(6) = 1/2$, but $p(x) = 1/10$ for all other outcomes $x$.

$p$ is called the **probability mass function (PMF)** of $X$, and it satisfies two basic properties:

1. For any $x \in S$, $p(x) \geq 0$.
2. The sum of $p(x)$ over all $x \in S$ must equal $1$, i.e., $\displaystyle \sum_{x \in S} p(x) = 1$.

### Probability Density Function

The above definition is problematic for continuous random variables. Suppose you generate a random real number $X$ in the interval $(0, 10)$, so $S = (0, 10)$. What's the probability that $X = \pi$? Exactly? All infinitely many digits of it?

Well, it feels like it should be $0$, right? So $p(\pi) = 0$. But then we can say that for any real number, since they all have infinitely many digits. So $p(x) = 0$ for all $x \in S$, which means the probability of generating *anything* is $0$. Huh.

We can fix this issue by using integrals instead. So for continuous random variables:

1. For any $x \in S$, $p(x) \geq 0$.
2. $\displaystyle \int_{x \in S} p(x) \,dx = 1$.

Here, $p$ is called the **probability density function (PDF)** of $X$.

For a continuous random variable $X$, it doesn't really make sense to ask for the probability that $X$ equals *some* specific real number. Instead, we can ask for the probability that $X$ lies in some interval $(a, b)$, which, using integrals, is just $\displaystyle \int_{a}^{b} p(x) \, dx$.

### Probability Distribution

In either case, $p$ is some function that describes the **probability distribution** (i.e., randomness) of $X$. Most of the math in this article checks out regardless of whether $p$ is a PMF or PDF, so we'll just say $p$ is a **probability function** from now on. This isn't standard terminology, but you get the idea. Just mentally fill in "PMF" or "PDF" where appropriate.

## Expected Value

For random variables, we are interested in their averages. In the case of rolling fair dice, if we rolled, say, $1000$ dice, we'd expect around $1/6$-th of them to show $1$, $1/6$-th of them to show $2$, and so on. The average value of a single die is then the average of all these outcomes.

Building upon this, for a discrete random variable $X$, we can define the **expected value** of $X$, denoted as $\mathbb{E}[X]$ (or $\mu$, or $\mu_X$):

$$ \mathbb{E}[X] = \sum_{x \in S} x \cdot p(x) $$

Intuitively, this is a weighted average: how likely an outcome $x$ is (and thus how much it contributes to the expected value) is determined by $p(x)$. If we sampled $X$ independently enough times, we'd expect the mean of our samples to hover around $\mathbb{E}[X]$.

For continuous variables, we can do the same thing; just change the $\sum$ to $\int$.

### Law of the Unconscious Statistician

We can generalize the above formula. For a random variable $X$, we define $Y$ to be some function $f$ of $X$, so $Y = f(X)$. Here, $Y$ is a random variable whose value is solely determined by the value of $X$. Then,

$$ \mathbb{E}[Y] = \sum_{x \in S} f(x) \cdot p(x) $$

This makes sense, because the probability distribution of $Y$ is essentially based on that of $X$. Again, for continuous random variables, it'd be an integral.

### Linearity of Expectation

Given two random variables $X$ and $Y$, the expected value of their sum $\mathbb{E}[X + Y]$ is simply the sum of their expectations, $\mathbb{E}[X] + \mathbb{E}[Y]$. Here's a proof sketch:

!!! note "Proof Sketch"
    
    Let $T = (X, Y)$, a tuple consisting of the random variables $X$ and $Y$. $T$ is also a random variable, so let $p_T$ be its probability function. Then:

    $$
    \begin{align}
    \mathbb{E}[X + Y]
    &= \sum_{(x, y) \in S_T} (x + y) \cdot p_T((x, y)) \\
    &= \sum_{x \in S_X} \sum_{y \in S_Y} (x + y) \cdot p_T((x, y)) \\
    &= \sum_{x \in S_X} \sum_{y \in S_Y} x \cdot p_T((x, y)) + \sum_{x \in S_X} \sum_{y \in S_Y} y \cdot p_T((x, y)) \\
    &= \sum_{x \in S_X} x \cdot \sum_{y \in S_Y} p_T((x, y)) + \sum_{y \in S_Y} y \cdot \sum_{x \in S_X} p_T((x, y)) \\
    \end{align}
    $$

    We note that $\sum_{y \in S_Y} p_T((x, y))$ represents summing up over the probabilities that $X = x$, and $Y$ equals *anything* in $S_Y$. So this is just the probability that $X = x$, or $p_X(x)$. Analogously, $\sum_{x \in S_X} p_T((x, y)) = p_Y(y)$. Hence:

    $$
    \begin{align}
    \mathbb{E}[X + Y]
    &= \sum_{x \in S_X} x \cdot p_X(x) + \sum_{y \in S_Y} y \cdot p_Y(y) \\
    &= \mathbb{E}[X] + \mathbb{E}[Y] \\
    \end{align}
    $$

    and we are done.
