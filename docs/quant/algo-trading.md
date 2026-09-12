# Algorithmic Trading 101

This page was adapted and translated from my dad's notes. Thanks Dad!

## Financial jargon

Let's try speeding through some much-needed context.

### Assets

An **asset** is basically any resource owned by something or someone. Walk into any bakery and you'll see a ton of its assets: the ovens, the furniture, the ingredients, etc. Even the brownies that you buy and eat can be considered assets.

Assets are divided into two main classes: **tangible assets** and **intangible assets**, which should hopefully be self-explanatory. Here, we focus mainly on one specific type of intangible asset, and that is **financial assets**.

### Investments

Companies need money (allegedly). Investors have money (allegedly). Naturally, investors can give companies money. However, this is not merely a charity: the investor expects to make a profit for putting their trust in the company.

For example, if Andy and Benny need funding for their bakery, maybe they can call up their friend Cindy and ask her for $\$1000$. Then, maybe at the end of the year, they promise to pay her back $\$1500$ using part of their revenue. Cindy is the **investor** and she has made an **investment**.

Now, there are a few issues worth considering. First of all, Andy and Benny have been good friends with Cindy for years, so they keep in close contact with her. But what about companies that don't already have those connections? Surely they can't just go to the local bar and look for investors there. Second of all, Andy and Benny are nice boys, so of course they'll hold up their end of the deal. But we can't say the same for all companies. What if they successfully scam their investors and run away with all the money?

Thus, we'd like an easy way for investors to put their trust in companies without having to physically meet, while (reasonably) ensuring that companies don't just pull a fast one on them. That's why they invented the...

### Exchange

An **exchange** is a centralized place where people can trade... stuff.

There is obviously more nuance to this, but the really important mental model you need to have for now is that, yes, there are a *lot* of flavors of exchange, and yes, there are a *lot* of exchanges with different flavors, each operating under its own rules.

Just like with farmers' markets, there are many exchanges in the world, and you can buy and sell things from them. That's why exchanges are a type of... **market**. Yeah.

The specific flavor of exchange we'll be dealing with throughout is the **stock exchange**. Each stock exchange only makes up one part of the entire **stock market** ecosystem.

## Market participants

Who actually participates in the ~~casino~~ stock market, anyway?

This list is not exhaustive, and the actual line between these categories isn't really that clear-cut.

### Retail investors

Individuals who are willing to gamble away their life savings. Yes, you too can be a retail investor!

### Institutional investors

Organizations that gamble a *lot* more than the average Joe. These include **pension funds**, **mutual funds**, and **hedge funds**. Essentially, they all work under the same idea: give us *your* money, and we'll invest it for you. You can think of them as banks with a gambling addiction.

### Traders

Buy sell buy buy sell buy sell buy sell sell. Profit. They can either be retail or institutional.

### Market makers

Very roughly (and using brownies as a placeholder), market makers sell brownies to those who want to buy brownies, but they also buy brownies from those who want to sell brownies. They provide **liquidity** in the market: thanks to them, you can more easily convert brownies into dollars. Usually, market makers make a profit too.

### Brokers

Unlike a casino, a retail investor can't just walk into a trading floor and demand brownies. Instead, they'll do it via a third party, known as a **broker**, who executes the trades on their behalf, or at least routes the trades to someone else. Brokers can make money by charging retail investors a little bit extra for their transactions, or through arrangements with market makers.

### Dealers

Firms that YOLO with their own money. They can larp as market makers, but aren't required to do so. Market makers generally have obligations under the stock exchange's regulations to, you know, make markets or whatever.

## Asset classes

What can you gamble in the stock market, anyway? Again, this list is not exhaustive.

### Stocks

**Stocks** are also known as **equities**. The primary unit of stocks is **shares**.

Andy and Benny give Cindy $500$ slips of paper (shares) with their signatures in exchange for investing $\$1000$ in their bakery. Thus, Cindy paid $\$2$ for each share.

On the way home, Cindy meets up with Darcy, so she decides to sell Darcy $200$ of her existing shares. She can sell them at the same price, undercharge, overcharge... it doesn't really matter, but you get the idea. Darcy can then sell her shares to someone else, and so on. Sooner or later, the whole neighborhood is buying and selling shares.

For a **private company**, its shares are not publicly available for trade: they simply handle things privately with their investors. But a **public company** is where the fun begins: you can buy and sell your shares to your heart's content.

Now, there are various legal implications of owning a share. As a **shareholder**, you technically own a (very small) part of the company itself. The more shares you own, the more ownership you have over the company proportionally. Depending on the type of shares, shareholders can vote on company decisions, receive a portion of the profit earned by the company (a **dividend**), get access to certain company information like annual financial reports, and so on. We don't really need to care about all that jazz; we're just here to gamble, of course.

### Exchange-traded funds

Commonly abbreviated as **ETFs**.

ETFs are sort of like private funds in that you give them money and they invest in stuff. But unlike private funds, you usually don't have to pay a decent chunk of money upfront. The way you invest in an ETF is simply by purchasing its shares. Share price goes up as the ETF's investments increase in value. Naturally, ETF shares are publicly available for trade.

In theory, an ETF can YOLO-gamble like your average private fund, but most ETFs are **index funds**. Index funds don't do anything daring; they just follow a **stock index**. If the stock index says this company has a weight of $7\%$, then the ETF will invest $7\%$ of its funding into said company. Of course, there are many different stock indexes which are maintained by many different organizations and stock experts.

### Options

Suppose you own $1000$ shares of company $X$, priced at $\$200$ each. While you have high hopes that the share price will eventually rise to $\$250$, you're also worried that company $X$ is going through a rough patch right now and suspect that the share price may drop to as low as $\$150$. What can you do?

That's where **options** come in. For example, you can buy a **put option** which gives you the *option* (ha) to sell $100$ of your shares at a price of $\$190$ sometime in the near future (based on the option's terms and conditions). Conversely, there are also **call options**.

If the share price doesn't actually drop in the first place, then hey, crisis averted, and you only incur the cost of buying the put option. If the share price *does* drop to $\$150$, then you can choose to exercise the put option and sell $100$ of your shares at a higher price of $\$190$ instead, which is at least better than nothing, right?

Alternatively, you can choose to sell the put option itself. It'd be quite valuable right now for other people who own a lot of company $X$'s shares. The ability to buy and sell options really does open up a whole new world of 5D chess in the stock exchange. 

Unlike shares, which are initially issued by companies, in theory, anyone in the market can offer (**write**) an option, and anyone in the market can buy (**hold**) that option. Lastly, and this is somewhat obvious, but for options that are publicly available for trade, they're generally standardized by the stock exchange's regulations. You can't just make up a put option to sell a bajillion shares at a ludicrously high price, for example.