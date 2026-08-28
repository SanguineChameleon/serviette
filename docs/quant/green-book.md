# Green Book Speedrun Any%

This page is my attempt at getting through all the problems in *A Practical Guide to Quantitative Financial Interviews*, otherwise known as the **Green Book**, by Xinfeng Zhou.

I'll assume you already have a copy. If not, you can find one at your nearest local quant event.

Timer begins now.

## Chapter 1 -- General Principles

Meh, who cares. I say just ~~YOLO~~ be yourself during the interview. It's worked for me so far at least. You'll be fine.

## Chapter 2 -- Brain Teasers

### Screwy pirates

This is the classic [pirate game](https://en.wikipedia.org/wiki/Pirate_game) problem, which is so mainstream, it even has a [TED-Ed video](https://www.youtube.com/watch?v=Mc6VA7Q1vXQ) on it. The interested reader can try out a much harder version of this problem, [Project Euler #950](https://projecteuler.net/problem=950).

### Tiger and sheep

!!! Statement

    $100$ tigers and $1$ sheep are put on a magic island that only has grass. Tigers
    can eat grass, but they would rather eat sheep. Assume that:

    - Each time, only $1$ tiger can
    eat $1$ sheep, and that tiger itself will become a sheep after it eats the sheep.
    - All tigers are smart and perfectly rational and they want to survive.

    Will the sheep be eaten?

Observe that at any point, there will always be exactly $1$ sheep on the island.

If there were $1$ tiger on the island, then it should eat the sheep. If there were $2$ tigers, $X$ and $Y$, then neither would want to eat the sheep. If $X$ ate the sheep, then $Y$ would eat $X$, and vice versa. For $3$ tigers, the sheep will be eaten. The first tiger that gets to it will leave the other $2$ in a stalemate as before.

You get the idea by now. $100$ is even, so the sheep will not be eaten.

### River crossing

This is the [bridge and torch problem](https://en.wikipedia.org/wiki/Bridge_and_torch_problem), and naturally it also has a [TED-Ed video](https://www.youtube.com/watch?v=7yDmGnA8Hw0). You can check out a much harder version, [Bridging the Gap](https://codeforces.com/gym/105255/problem/J) from the 2023 ICPC World Finals. I haven't solved it.

### Birthday problem

!!! note "Statement"

    Andy and Benny know that Cindy's birthday is one of the following dates:

    ```
    Mar 4, Mar 5, Mar 8, Jun 4, Jun 7, Sep 1, Sep 5, Dec 1, Dec 2, Dec 8
    ```

    Cindy tells Andy the month of her birthday, and tells Benny the day of her birthday.

    Andy says: "I don't know Cindy's birthday; Benny doesn't know it either."

    After hearing Andy, Benny replies: "I didn't know Cindy's birthday at first, but now I know."

    Andy smiles and says: "Now I know it too!"

    So when is Cindy's birthday?

This is a variant of the wonderful [Cheryl's Birthday](https://en.wikipedia.org/wiki/Cheryl%27s_Birthday). The dates are different, so let's go through it together.

First, how can Andy confidently claim that Benny doesn't know Cindy's birthday? He must know that Benny wasn't given a day that could've uniquely identified Cindy's birthday. 

If Cindy's birthday were ``Jun 7``, Benny would immediately know which date it was, as none of the other dates are on the 7th. So if Andy was given ``Jun``, he wouldn't be able to make that claim. Thus, we can eliminate ``Jun`` from our list of dates:

```
Mar 4, Mar 5, Mar 8, Sep 1, Sep 5, Dec 1, Dec 2, Dec 8
```

Similarly, because of ``Dec 2``, we can eliminate ``Dec`` from our list of dates as well:

```
Sep 1, Sep 5, Mar 4, Mar 5, Mar 8
```

Now we move on to Benny. He now knows Cindy's birthday, so his given day must uniquely identify it from the remaining dates. This means it's not ``Sep 5`` or ``Mar 5``; both are on the 5th:

```
Sep 1, Mar 4, Mar 8
```

Andy, having gone through the same logic, now also knows Cindy's birthday. So it couldn't be ``Mar``, since there are two dates left.

Therefore, Cindy's birthday is ``Sep 1``.

### Card game

!!! Statement

    A casino offers a card game involving a standard deck of $52$ cards. You turn over a pair of cards each time:

    - If both are black, they go to the dealer's pile.
    - If both are red, they go to your pile.
    - If one is black and one is red, they are discarded.

    The process is repeated until you have gone through all $52$ cards.

    If you have strictly more cards in your pile, you win $100$ dollars. Otherwise, you get nothing.

    How much would you be willing to pay for this game?

Sigh. Okay. You got me. I spent way longer on this than I should have.

Let:

- $X$ be the number of pairs where both cards are black;
- $Y$ be the number of pairs where both cards are red;
- $Z$ be the number of pairs where one card is red and one card is black.

Since there are exactly $26$ black cards and $26$ red cards, we have:

$$
\begin{align*}
2X + Z = 26 \\
2Y + Z = 26
\end{align*}
$$

Thus, $X = Y$, which means... wait, you'll always tie. So you'll actually *never* win this game.

Don't make a fool of yourself. Pay exactly $0$ dollars for this game.

### Burning ropes

Obligatory [Wikipedia article](https://en.wikipedia.org/wiki/Rope-burning_puzzle) and [TED-Ed video](https://www.youtube.com/watch?v=9uZ-jeZS8d0).

### Defective ball

Obligatory [Wikipedia article](https://en.wikipedia.org/wiki/Balance_puzzle) and [TED-Ed video](https://www.youtube.com/watch?v=tE2dZLDJSjA). But FYI, I don't think I could've derived this on the spot. Then again, if you're using classic puzzles like this as a legitimate hiring procedure, you're doing it wrong.

### Trailing zeros

!!! Statement
    How many trailing zeros are there in $100$ factorial?

See [Legendre's formula](https://en.wikipedia.org/wiki/Legendre%27s_formula).

### Horse race

!!! Statement

    There are $25$ horses, each of which runs at a constant speed. All horses' speeds are unique.

    Each race can have at most $5$ horses. What is the minimum number of races needed to identify the $3$ fastest horses?

This has apparently become folklore; there's not even a Wikipedia article for this one.

Split the $25$ horses into $5$ groups of $5$ horses, $A$, $B$, $C$, $D$, and $E$. Let $A_1 > A_2 > A_3 > A_4 > A_5$ be the horses from race $A$ in order ($A_1$ is fastest, $A_5$ is slowest), and do the same for the other $4$ races.

Then we race $A_1$, $B_1$, $C_1$, $D_1$ and $E_1$. Without loss of generality (and for the sake of convenience), suppose $A_1 > B_1 > C_1 > D_1 > E_1$.

Now we can eliminate all horses that have (directly or indirectly) lost to at least $3$ horses, since they could never be in the top $3$. This already reduces our candidates all the way down to $6$ horses: $A_1$, $A_2$, $A_3$, $B_1$, $B_2$, and $C_1$.

Obviously $A_1$ is the fastest horse, so all we need to do is race the remaining $5$ horses to determine the second and third fastest horses.

$7$ races in total. It's pretty clear you can't do better than that.

### Infinite sequence

!!! Statement

    Solve for $x$ if $x^{x^{x^{...}}} = 2$.

Haha, real funny. Just replace the infinite power tower with itself, so $x^2 = 2$, which means $x = \sqrt{2}$. Note that $x = -\sqrt{2}$ doesn't work because I said so. Mathematicians would kill you over this, by the way.

### Box packing

!!! Statement

    Can you pack $53$ bricks of dimension $1 \times 1 \times 4$ into a $6 \times 6 \times 6$ box?

The book's solution implicitly assumes the bricks are axis-aligned. If you don't do this, you will waste many hours of your life and ruin your entire day. Not... speaking from experience.

Anyway:

```
..x...
...x..
x...x.
.x...x
..x...
...x..

...x..
..x...
.x...x
x...x.
...x..
..x...

x...x.
.x...x
...x..
..x...
x...x.
.x...x

.x...x
x...x.
..x...
...x..
.x...x
x...x.

..x...
...x..
x...x.
.x...x
..x...
...x..

...x..
..x...
.x...x
x...x.
...x..
..x...
```

Each brick occupies exactly $1$ marked `x`. But there are only $52$ of them, so $53$ is impossible.

I'm totally fine. Yeah.  

### Calendar cubes

!!! Statement

    You have two cubes. Place a single digit on each of the faces so that you can arrange the numbers `01`, `02`, ..., `31` using the two cubes. You can switch the order of the cubes if needed.

Try taking the problem statement at face value and you will quickly run into a logical contradiction: there just aren't enough faces on each die. The key "observation" is that you can rotate a $6$ to get a $9$. So $\{0, 1, 2, 5, 7, 8\}$ and $\{0, 1, 2, 3, 4, 9\}$ is one such valid numbering.

I like it, despite the cheap trick.

### Door to offer

!!! Statement

    You are facing two doors. One leads to your job offer and the other leads to the exit. In front
    of each door is a guard. One guard always lies and the other always tells the truth.
    You can only ask one guard one yes/no question. 

    What should you ask to get the job offer?

This is a variant of [Knights and Knaves](https://en.wikipedia.org/wiki/Knights_and_Knaves). The usual setting has one door leading to heaven and one door leading to hell, though being unemployed is arguably hell in this job market.

### Message delivery

!!! Statement

    Andy wants to communicate with his boyfriend Benny via a messenger service. Andy's documents are sent in a box, but unfortunately, the messenger service isn't secure: anything inside an unlocked box will inevitably get lost during delivery, including any locks placed inside one.

    Andy and Benny each have exactly one high-security lock-and-key pair: Andy owns pair $A$ and Benny owns pair $B$. Lock $A$ can only be opened with key $A$, and lock $B$ can only be opened with key $B$.

    How can Andy securely send his documents to Benny?

Lovers and their weird schemes.

Andy places his documents inside the box and locks it with his lock $A$. The box is delivered to Benny, who then locks it again with his lock $B$. The box is delivered back to Andy, who unlocks his lock $A$ with his key $A$. The box is delivered one last time to Benny, who can now open it with his key $B$.

Why they couldn't just meet in person, I have no idea.

### Last ball

!!! Statement

    A bag has $20$ blue balls and $14$ red balls. Each time, you randomly take out $2$ balls (each ball has an equal probability of being taken).

    You do not put the $2$ balls back. Instead:

    - If both balls have the same color, you add a blue ball to the bag;
    - If they have different colors, you add a red ball to the bag.

    You repeat this process until exactly $1$ ball remains.

    What color is the last ball? What if the bag has $20$ blue balls and $13$ red balls instead?

It's always parity this, parity that, eh?

For $20$ blue balls and $14$ red balls, observe that the number of red balls is always even, no matter what you do. Therefore, at the end, the last ball must be blue. Similarly, for $20$ blue balls and $13$ red balls, the last ball must be red.

### Light switches

!!! Statement

    There is $1$ light bulb inside a room and $4$ switches outside. All switches are currently off and exactly $1$ switch controls the light bulb. You may turn any number of switches on or off any number of times you want.

    How many times do you need to go
    into the room to determine which switch controls the light bulb? 

The canonical version that I know of involves $3$ switches controlling $3$ light bulbs, but this is no different.

Of course you can do it in $2$ visits, but of course the interviewer won't be impressed. Here's how to do it in $1$:

1. Turn the first light switch on and wait a few minutes.
2. Turn the first light switch off, turn the second light switch on, and wait a few minutes.
3. Turn the second light switch off, *immediately* turn on the third light switch, and run inside.

Now, observe the state of the light bulb inside the room. If it's on, then obviously it's the third light switch. Otherwise, touch the light bulb. If it's very hot and your hands burn (ow oof owie), it's the second light switch. If it's just slightly warm, it's the first light switch. Lastly, if it's cold, it must be the fourth light switch.

**Update**: Okay, so the book's intended solution is to treat on/off and hot/cold as $2$ separate things you can check for, which is how you obtain $4$ separate states. I don't think I could physically bring myself to touch a light bulb that's on, so I'm good, thanks. This problem has a lot of unstated assumptions, anyway.

### Quant salary

!!! Statement

    $8$ quants from different banks are getting together for drinks. They are all interested
    in knowing the average salary of the group. Nevertheless, being cautious and humble
    individuals, everyone prefers not to disclose his or her own salary to the group. Can you
    come up with a strategy for the quants to calculate the average salary without knowing
    other people's salaries?

Narrowly avoided throwing up upon reading the statement. Anyway, I've heard of this [before](https://puzzling.stackexchange.com/questions/11829/find-average-age-without-revealing-your-age).

The first guy, we'll call him Andy, punches in a random number, $X$, on his calculator. He then adds his salary to $X$ and passes the calculator to the next person. Each subsequent person adds their own salary to the running total, which has been obfuscated by $X$. The last person returns the calculator back to Andy, who can subtract $X$ and divide by $8$ to get the average salary.

If you want to be extra secure, each person can offset the running total by their own random number and cancel them out later, but $1$ should be sufficient.

### Coin piles

!!! Statement

    You are blindfolded. There are $1000$ coins on the floor. $980$ of the coins are tails up and the other $20$ coins have heads up. Can you separate the coins into two piles to guarantee both piles have equal number of coins that are heads up? You cannot determine a coin's side just by touching it, but you are allowed to turn over any number of coins.

Obligatory [TED-Ed video](https://www.youtube.com/watch?v=pnSw8g3DPHw).

### Mislabeled bags

!!! Statement

    You are given three bags of fruits. One has apples in it, one has oranges in it, and one
    has a mix of apples and oranges in it. Each bag has a label on it (apple, orange or mixed). Unfortunately, your manager tells you that **all** bags are mislabeled.

    Find the correct label of each bag by taking out the minimum number of fruits. You can take out any number of fruits from each bag.

I legitimately remember solving this when I was 10. Does that mean I only need to be smarter than a 10-year-old to pass a quant interview? That's somewhat reassuring.

Take out $1$ fruit from the bag labeled as mixed. If it's an apple, we know this is the all-apples bag, and if it's an orange, we know this is the all-oranges bag. Knowing the correct identity of one bag is enough for us to identify the remaining bags as well.

### Wise men

!!! Statement

    A sultan has captured $50$ wise men. There is a glass inside the room, which is currently bottom-side-up.

    Each minute, he calls one of the wise men into the room. Then, they can either turn the glass over or do nothing. The wise men will be called randomly.
    
    At any point, one of the wise men can claim that all wise men have been inside the room at least once. If his claim is correct, everyone goes free. But if not, everyone dies.

    The wise men are allowed to communicate only once before they are imprisoned in separate rooms. Design a strategy that lets the wise men go free.

Label the wise men $M_1, M_2, \ldots, M_{50}$. We'll elect $M_1$ to be the leader.

For $i > 1$, when $M_i$ is called into the room:

- If the glass is bottom-side-down, he does nothing.
- If the glass is bottom-side-up and he has *not* turned the glass over, he turns it over.
- If the glass is bottom-side-up and he has previously turned the glass over, he does nothing.

When $M_1$ is called into the room:

- If the glass is bottom-side-up, he does nothing.
- If the glass is bottom-side-down, he turns it over.

Eventually, $M_1$ will turn the glass over $49$ times. At that point, he can make the claim, and everyone will go free.

### Clock pieces

!!! Statement

    A clock with numbers $1$ to $12$ fell off the wall and broke into three pieces. The sums of the numbers on each piece are equal. What are the numbers on each piece? Assume the pieces don't have weird shapes.

Uhhh...

$$1 + 2 + \ldots + 12 = \frac{12 \cdot 13}{2} = 78$$

So each piece has sum $26$. A little trial and error gives us the following pieces: $\{11, 12, 1, 2\}$, $\{5, 6, 7, 8\}$, and $\{3, 4, 9, 10\}$. Yeah, they're not consecutive, but if you actually draw it out, the shapes are quite reasonable.

### Missing integers

!!! Statement

    Suppose we have $98$ distinct integers from $1$ to $100$. What is a good way to find the $2$ missing integers?

Use a hash table.

So, when can I get started?

### Counterfeit coins I

!!! Statement

    There are $10$ bags with $100$ identical coins in each bag. In all but $1$ of the bags, each coin weighs $10$ grams. All the coins in the counterfeit bag weigh either $9$ or $11$ grams.

    You have an exact digital scale. Find the counterfeit bag in only $1$ weighing.

Take $1$ coin from the first bag, $2$ coins from the second bag, $3$ coins from the third bag, and so on. Pretending these are all real coins, we can determine their total weight. Take the absolute difference between this and the scale's actual reading to determine which bag is counterfeit.

### Glass balls

!!! Statement
    
    You are holding $2$ glass balls in a $100$-floor building. When an (unbroken) ball is thrown out of the window, if the floor number is less than $X$, the ball won't break. Otherwise, it will.

    Determine $X$ while minimizing the number of drops needed in the worst case.

Let $n$ be the minimum number of drops needed in the worst case. Define:

$$
\begin{align*}
a_0 &= 0 \\
a_1 &= n \\
a_2 &= n + (n - 1) \\
&\ldots \\
a_n &= n + (n - 1) + \ldots + 1 \\
\end{align*}
$$

We drop the first glass ball at floor $a_1$, then floor $a_2$, and so on, until it breaks.

Let $a_i$ be the first floor where the glass ball breaks. Since it survived floor $a_{i - 1}$, we can now use the second glass ball to sequentially check all floors from $a_{i - 1} + 1$ to $a_i - 1$, inclusive. The way we set these numbers up ensures that at most $n$ drops are needed, no matter which $i$ it is.

All we need to do now is to find an $n$ that *guarantees* we cover all floors. In other words, just find the smallest $n$ such that $a_n \geq 100$. So $n = 14$ is sufficient and optimal.

Note that the above strategy works as-is when there are exactly $105$ floors. For the original problem, if you need to drop the glass ball from a nonexistent floor, just stand on a very high ladder on the top of the building and drop the ball from there instead. Or, you know, just cap it at $100$ floors. That works too.

### Matching socks

I've set a harder version of this problem on [Codeforces](https://codeforces.com/problemset/problem/2096/B) before.

### Handshakes

!!! Statement

    You are invited to a welcome party with $25$ other team members. Each person shakes hands with some (or none) of the other people at the party.

    Can you say with certainty that there are at
    least $2$ people present who shook hands with exactly the same number of people?

Essentially, given a simple graph with $26$ nodes, can we guarantee that there exist $2$ nodes with the same degree?

Yep. Suppose each node had a unique degree between $0$ and $25$ inclusive. There are $26$ nodes in total, so each number from $0$ to $25$ is used exactly once. But the sum of these is $325$, which is odd. This contradicts the handshake lemma (heh).

**Update**: Upon paraphrasing the original statement, I accidentally omitted the fact that everyone already shook hands with *you*, which trivializes the problem even further. Meh, this version is cooler anyway.

### Have we met before?

!!! Statement

    Show that, if there are $6$ people at a party, then either at least $3$ people met each other before the party, or at least $3$ people were strangers before the party. 

Oops, it's [Ramsey's theorem](https://en.wikipedia.org/wiki/Ramsey's_theorem). $R(3, 3) = 6$. Suck it.

### Ants on a square

!!! Statement

    There are $51$ ants on a square with side length of $1$. If you have a glass with a radius of $\frac{1}{7}$, can you always put your glass at some position on the square that encompasses at least $3$ ants?

Divide the square into a $5 \times 5$ grid of cells. Each ant belongs to exactly one such cell (if there's an ant on the border, you can gently nudge it). By the pigeonhole principle, there exists a cell with $3$ ants. By Pythagoras, a circle of radius $\frac{1}{7}$ can just about encompass the entire cell, so we are done.

### Counterfeit coins II

!!! Statement

    There are $5$ bags with $100$ coins in each bag. A coin can weigh $9$ grams, $10$ grams or $11$ grams. Each bag contains coins of equal weight, but you do not know which type of coins a bag contains.

    You have an exact digital scale. How many
    times do you need to use the scale to determine which type of coin each bag contains?

Same idea as before; only $1$ weighing needed.

Take $1$ coin from the first bag, $3$ coins from the second bag, $9$ coins from the third bag, $27$ coins from the fourth bag, and $81$ coins from the fifth bag. Pretend that all the coins weigh $9$ grams and determine what their total weight would be. Then, just interpret the difference between this and the actual reading as a ternary number.

### Prisoner problem

Obligatory [TED-Ed video](https://www.youtube.com/watch?v=N5vJSNXPEwA).

### Division by 9

!!! Statement
    Given an arbitrary integer, come up with a rule to decide whether it is divisible by 9 and prove it.

...What??? I learned this when I was 8???

### Chameleon colors

!!! Statement

    A remote island has $13$ red
    chameleons, $15$ green chameleons and $17$ blue chameleons. Each time $2$ chameleons
    with different colors meet, they change their colors to the remaining one. For example,
    if a green chameleon meets a red chameleon, they both change their color to blue. Is it
    ever possible for all chameleons to become the same color?

Observe that at any point, one color's count is $0$ modulo $3$, another is $1$ modulo $3$, and the remaining one is $2$ modulo $3$. There are $45$ chameleons in total; it is impossible to achieve the desired counts of $45$, $0$, and $0$.

### Coin split problem

!!! Statement

    You have a pile of $1000$ coins. Initially, your total score is $0$.

    In one operation, you choose a pile with at least $2$ coins and split it into two piles. If there are $x$ coins in the first pile and $y$ coins in the second pile, your total score increases by $x \cdot y$.
    
    Repeat the process until each coin is in a separate pile. What is the maximum total score you can obtain?

The original statement kind of spoils the fun, so I've added a slight layer of obfuscation.

In fact, no matter what you do, your total score is always the same.

For each operation where you split a pile into two piles of sizes $x$ and $y$, you can really think of $x \cdot y$ as representing the number of pairs of coins where one coin is taken from each pile.

Then, for each pair of coins, say $C_1$ and $C_2$, consider the first (and only) time they get separated. That pair will contribute exactly once to the overall total score. But this is true for any pair, so the answer is simply the number of pairs of coins in total, which is $499\,500$.

### Chocolate bar problem

!!! Statement

    A chocolate bar consists of $48$ pieces arranged in a grid of $6$ rows and $8$ columns. In one operation, you choose one rectangle and break it into two smaller rectangles. You may only break a rectangle along the grid lines.

    What is the minimum number of operations required to break the chocolate bar into $48$ separate pieces?

Again, no matter what you do, you will always need the same number of operations.

This one is even more straightforward: each operation increases the total number of rectangles by exactly $1$, so exactly $47$ operations are required.

### Race track

!!! Statement

    You are on a one-way circular race track. There are several gas cans placed at different positions on the track; the total amount of gas in these cans is enough for your car to travel exactly one complete lap.

    Your car's gas tank is initially empty; assume it has unlimited capacity. You can start your car at any position on the track, and you can pick up gas cans along the way to fill up the tank.

    Is it always possible to choose a starting
    point on the track so that your car can travel one complete lap?

Let's do a trial run first. Fill your car's tank with a lap's worth of gas and begin your journey from an arbitrary position, picking up gas cans along the way as you go. We'll keep track of how much gas is left in the tank throughout the lap.

After the trial run is complete and everything is reset, find the position where you had the least amount of gas left, and begin the real journey there. You can be sure that you won't run out of gas.

### Irrational number

!!! Statement

    Prove that $\sqrt{2}$ is irrational.

I know Hippasus did over 2000 years ago and, well, let's just say it didn't really work out for him. Pass.

### Rainbow hats

!!! Statement

    $7$ prisoners have the chance to be set free tomorrow. The executioner will put a
    hat on each prisoner's head. Each hat is in one of the $7$ colors of the rainbow; the hat colors are assigned at the executioner's discretion. Each prisoner can
    see the hat colors of the other $6$ prisoners, but not his own. They cannot communicate with others in any form.

    Each prisoner writes down what he thinks his own hat color is. If at least $1$ prisoner correctly guesses the color of his hat, they will all be set free. Otherwise, they will all be executed.

    Can the prisoners come up with a strategy that guarantees freedom?

Yes. Label the colors from $0$ to $6$, and the prisoners from $0$ to $6$.

Prisoner $i$ assumes the sum of all the prisoners' hat colors (including his own) is $i$ modulo $7$, and writes down what his hat color would have to be for that assumption to be true. Exactly one of the prisoners' assumptions will actually be true, so ggwp.

## Chapter 3 -- Calculus and Linear Algebra

Oh thank goodness, we're done with the brain teasers.

### Limits and Derivatives

!!! Exercise

    What is the derivative of $y = \ln(x)^{\ln(x)}$?

Let $w = \ln(x)$ and $z = \ln(y) = w \cdot \ln(w)$, so $y = e^z$. Then:

$$
\begin{align*}
\frac{dy}{dx}
&= \frac{dy}{dz} \cdot \frac{dz}{dw} \cdot \frac{dw}{dx} \\
&= e^z \cdot (\ln(w) + 1) \cdot \frac{1}{x} \\
&= \ln(x)^{\ln(x)} \cdot (\ln(\ln(x)) + 1) \cdot \frac{1}{x} \\
&= \boxed{\frac{\ln(x)^{\ln(x)} \cdot \ln(\ln(x)) + \ln(x)^{\ln(x)}}{x}} \\
\end{align*}
$$

!!! Exercise

    Without calculating the numerical results, which is larger, $e^\pi$ or $\pi^e$?

I remember seeing this on TikTok; apparently you're supposed to do this in your head. Insane.

Note that $\ln(x)$ is increasing for $x > 0$, so it suffices to compare their logarithms instead:

$$
\begin{align*}
e^\pi &\lessgtr \pi^e \\
\iff \ln(e^\pi) &\lessgtr \ln(\pi^e) \\
\iff \pi \cdot \ln(e) &\lessgtr e \cdot \ln(\pi) \\
\iff \frac{\pi}{\ln{\pi}} &\lessgtr \frac{e}{\ln{e}}
\end{align*}
$$

Let $g(x) = \frac{x}{\ln(x)}$. We wish to compare $g(\pi)$ and $g(e)$.

Let's try computing $g^\prime(x)$ first and see what we get:

$$
\begin{align*}
g^\prime(x) &= \frac{\ln(x) - 1}{\ln(x)^2}
\end{align*}
$$

Thus, $g^\prime(x) > 0$ for $x > e$, so $g(x)$ is increasing for $x > e$. Therefore, $g(\pi) > g(e)$, which means $\boxed{e^{\pi} > \pi^{e}}$.

!!! Exercise

    What is the limit of $\frac{e^x}{x^2}$ as $x \to \infty$?

Just whack L'Hôpital:

$$
\begin{align*}
\lim_{x \to \infty} \frac{e^x}{x^2} &= \lim_{x \to \infty}\frac{e^x}{2x} \\
&= \lim_{x \to \infty}\frac{e^x}{2} \\
&= \boxed{\infty}
\end{align*}
$$

!!! Exercise

    What is the limit of $x^2 \ln(x)$ as $x \to 0^+$?

Express $x^2 \ln(x)$ as $\frac{\ln(x)}{x^{-2}}$ and whack L'Hôpital again:

$$
\begin{align*}
\lim_{x \to 0^+} \frac{\ln(x)}{x^{-2}} &= \lim_{x \to 0^+}\frac{1}{-2x^{-2}} \\
&= \lim_{x \to 0^+}-\frac{1}{2}x^2 \\
&= \boxed{0}
\end{align*}
$$

### Integrals

!!! Exercise

    What is the integral of $\ln(x)$?

Whack integration by parts. Let $u = x$, $v = \ln(x)$. Then:

$$
\begin{align*}
\int \ln(x)\,dx &= \int 1 \cdot \ln(x)\,dx \\
&= \int \frac{du}{dx} \cdot v\,dx \\
&= u \cdot v - \int \frac{dv}{dx} \cdot u\,dx \\
&= x \cdot \ln(x) - \int 1\,dx \\
&= \boxed{x \cdot \ln(x) - x + C}\\
\end{align*}
$$

!!! Exercise

    What is the integral of $\sec(x)$ from $x = 0$ to $x = \frac{\pi}{6}$?

I genuinely had a stroke solving this.

We'll use integration by substitution. Let $u = \sin(x)$. Then:

$$
\begin{align*}
\int \sec(x)\,dx &= \int \frac{\cos(x)}{\cos^2(x)}\, dx \\
&= \int \frac{1}{1 - \sin^2(x)} \cdot \cos(x) \, dx \\
&= \int \frac{1}{1 - u^2} \cdot \frac{du}{dx} \, dx \\
&= \int \frac{1}{1 - u^2} \, du \\
&= \frac{1}{2} \cdot \int \left(\frac{1}{1 - u} + \frac{1}{1 + u}\right) \, du \\
&= \frac{1}{2}(\ln(1 + u) - \ln(1 - u)) + C \\
&= \frac{1}{2}(\ln(1 + \sin(x)) - \ln(1 - \sin(x))) + C \\
\end{align*}
$$

Therefore:

$$
\begin{align*}
\int_0^{\frac{\pi}{6}} \sec(x)\,dx &= \frac{1}{2}\left(\ln\left(1 + \frac{1}{2}\right) - \ln\left(1 - \frac{1}{2}\right)\right) - \frac{1}{2}(\ln(1 + 0) - \ln(1 - 0)) \\
&= \boxed{\frac{\ln(3)}{2}}
\end{align*}
$$

I don't wanna talk about it.

!!! Exercise

    Two infinitely long cylinders, each with radius $1$, are perpendicular to each other and intersect at their centers. What is the volume of the intersection?

Literally NO ONE ASKED--

Label the cylinders $C_1$ and $C_2$ and let them intersect at the origin, $(0, 0, 0)$. Also let $C_1$ be parallel to the $x$-axis and $C_2$ be parallel to the $y$-axis.

Thus, the equations for $C_1$ and $C_2$ are:

$$
\begin{align*}
C_1&:\, y^2 + z^2 \leq 1 \\
C_2&:\, x^2 + z^2 \leq 1
\end{align*}
$$

Consider the two-dimensional slice of their intersection at some specific $z$ level. The corresponding $x$ and $y$ coordinates must satisfy:

$$
\begin{align*}
-\sqrt{1 - z^2} \leq x \leq \sqrt{1 - z^2} \\
-\sqrt{1 - z^2} \leq y \leq \sqrt{1 - z^2}
\end{align*}
$$

So the area of this slice is exactly $4(1 - z^2)$.

Integrating from $z = -1$ to $z = 1$ gives us:

$$
\begin{align*}
\int_{-1}^{1} 4(1 - z^2)\, dz &= \left[4z - \frac{4}{3}z^3\right]_{-1}^{1} \\
&= \frac{8}{3} - \left(-\frac{8}{3}\right) \\
&= \boxed{\frac{16}{3}}
\end{align*}
$$