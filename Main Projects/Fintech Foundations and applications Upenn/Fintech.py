import os
#indexes for course specializations, topics, segments
course_data = {
    1: {
        'name': 'Fintech: Foundations, Payments, Regulations',
        'topics': {
            1: {
                'name': 'Overview of Fintech',
                'segments': [
                    'Introduction in Fintech',
                    'Robo-Advising',
                    'Market Size',
                    'Attitudes towards Financial apps',
                    'Global Market',
                ]
            },
            2: {
                'name': 'Key Considerations in Fintech',
                'segments': [
                    'Millennials Attitude',
                    'Risk',
                    'Millennials Social Impact',
                    'Trust',
                    'Choice architecture',
                ]
            },
            3: {
                'name': 'Payments',
                'segments': [
                    'History',
                    'Payment Methods: Trends',
                    'Two-sided Payment market',
                    'Complex payment process',
                    'Merchant Cost burden',
                ]
            },
            4: {
                'name': 'Regulation',
                'segments': [
                    '2008 Financial Crisis: Regulation',
                    'US vs International: Regulation',
                    'Great Recession',
                    'Regulation Innovation Tradeoff',
                    'Issues with regulating Fintech',
                    'US Fintech Regulation',
                    'Global Fintech Regulation'
                ]
            }
        }
    },
    2: {
        'name': 'Cryptocurrency & Blockchain: Intro to Digital Currencies',
        'topics': {
            1: {
                'name': 'Introduction to Cryptocurrency',
                'segments': [
                    'Introduction',
                    'Bitcoin transactions',
                    'Why Crypto?',
                ]
            },
            2: {
                'name': 'Rules & Structure of Bitcoin',
                'segments': [
                    'Digital Signature',
                    'Tamper Proof Ledger',
                    'Distributed Consensus',
                    'Proof of Work',
                    'Mining & Currency Supply',
                    'Challenges',
                ]
            },
            3: {
                'name': 'Cryptocurrency Asset Class',
                'segments': [
                    'Introduction',
                    'Risk and Return',
                    'Portfolio theory',
                    'Asset Allocation of Crypto',
                ]
            },
            4: {
                'name': 'Blockchain Ecosystem',
                'segments': [
                    'Blockchain Ecosystem',
                    'Crypto Finance',
                    'Crypto Fintech',
                    'Business uses',
                    'Gaming uses',
                    'Investing uses',
                    'Government & Regulation',
                ]
            }
        }
    },
    3: {
        'name': 'Lending, Crowdfunding, Modern Investing',
        'topics': {
            1: {
                'name': 'Robo-Advising',
                'segments': [
                    'Overview',
                    'Portfolio Theory',
                    'Mean Variance Optimization',
                    'ETF, Mutual Funds, Target Date Funds',
                    'Customization',
                ]
            },
            2: {
                'name': 'Crowdfunding',
                'segments': [
                    'Introduction',
                    'Raising Capital',
                    'Jobs Act',
                    'Cost of Crowdfunding',
                    'Learning from the crowd',
                    'Impact investing',
                ]
            },
            3: {
                'name': 'Marketplace Lending',
                'segments': [
                    'Introduction',
                    'Consumer Credit Landscape',
                    'Evolution of P2P Landscape',
                    'Student Loan Debt',
                    'Lending: Small business',
                ]
            },
            4: {
                'name': 'New Frontier of Fintech (Examples)',
                'segments': [
                    'Square',
                    'Commonbond',
                ]
            }
        }
    },
    4: {
        'name': 'AI, InsurTech, Real Estate Tech',
        'topics': {
            1: {
                'name': 'Artificial Intelligence',
                'segments': [
                    'Background',
                    'AI Applications',
                    'Use Cases in Fintech',
                    'Future of AI: Robo-Advising',
                    'Machine Learning',
                ]
            },
            2: {
                'name': 'InsurTech',
                'segments': [
                    'AI & ML in Insurtech',
                    'Redefining Insurance Industry',
                    'Classifications of IT Companies',
                    'Investment & Market Size',
                    'Fintech Financial Inclusion',
                ]
            },
            3: {
                'name': 'Real Estate Tech',
                'segments': [
                    'Industry Background',
                    'Definition of ReTech',
                    'Residential: ReTech Startup + Trends + Examples',
                    'Commercial: ReTech + Examples',
                    'Data',
                ]
            },
            4: {
                'name': 'Case Studies',
                'segments': [
                    'Vanguard',
                ]
            }
        }
    }
}


# ANSI escape codes for bold and reset
bold = "\033[1m"
reset = "\033[0m"

# course material 
material_storage = {
    "1-1-1": f"""{bold}What is Fintech?{reset}

{bold}Businesses that leverage technology to:{reset}
- Create new & better financial services
- For Consumers and Businesses
- Personal financial management, insurance, payment, asset management, products

{bold}Includes:{reset}
- ABCDs
- Deep and thin learning
- Automated CRM (customer relationship management)
- Robo-Advising
- Insurtech
- Payments
- Cash management
- Lending

{bold}Main Goals:{reset}
- Reduce transaction/service cost
- Reaching market segments typically impractical or uneconomic
- Economies of scale
- Improve customer experience
- Segment marketplace
""",

    "1-1-2": f"""{bold}Current Definition:{reset}
- Financial Advisor Firm uses Algorithm to automate customer allocation 

{bold}Provides:{reset}
- Automated Capture of Client information (goals, risk tolerance)
- Recommend portfolio allocation
- Rebalancing & Tax loss harvesting
- Automated Reporting

{bold}Future:{reset}
- No such thing as “pure” robo-advisors
- Has client service representative & expanding models
- Economically viable to clients with less assets
""",

    "1-1-3": f"""{bold}Market Size:{reset}

KPMG Fintech Report
- Highly Aggressive Funding ($2 Trillion Overhang Venture)
- Sub-Category: Digital Payments & Remittance (largest $4T)
- 2019 $119b funding

Robo-Advisors Companies: 
Betterment
WealthFront
Vanguard (150b AUM - 2020)
""",

    "1-1-4": f"""{bold}% of Actions done on a Mobile Phone:{reset}
- Paid bill using phone: 65%
- Purchased items remotely: 42%
- Paid for a physical item in-store: 33%
- Sent money to others within the US: 25%

{bold}In 12-Month Period:{reset}
Most Respondents Felt Comfortable Digitally:
- Interacting
- Allocating
- Sending Money
""",

    "1-1-5": f"""{bold}Top 10 Fintech Deals:{reset}
- 40% largest only in the US
- Largest deal: $17 billion based in the US
- Chinese company: $14 billion
- Worldpay (UK): $12.9 billion
- Nets (Denmark): $5.5 billion

{bold}Not just Venture Capital, Private Equity as well.{reset}

{bold}KPMG Reports:{reset}

{bold}China:{reset}
- $18.2 billion funding in China Fintech 2018
- Increase in activity with money flowing in
- Deal counts cyclical

{bold}UK:{reset}
- Larger than China at $20.7 billion
- Positive upward trend
- Cyclical funding

{bold}Europe:{reset}
- Combination of China & UK at $34.2 billion
""",

    "1-2-1": f"""{bold}Importance of Millennials:{reset}
- {bold}Wealth Inheritance:{reset} Fast adoption of technology, disruptive in industries.
- {bold}Demographic:{reset} 25% of the US population (83 million), 40% globally (2015), diverse, expressive, optimistic.
- {bold}Attitudes to Financial Advice:{reset} Optimistic about the future, 50% expect no Social Security payout, 2/3 express ESG values through investment.

{bold}Money-wise:{reset}
- 68% confident in handling family’s money.
- 80% own smartphones.
- 54% started a business plan, 27% are self-employed.

{bold}However:{reset}
- Low trust in others in volatile markets.
- Optimistic about financial futures despite less wealth comparatively.

{bold}Why Fintech Holds Promise for Millennials:{reset}
- Adoption of technology is increasing.
- Younger Millennials are the greatest adopters of digital payments/banking.
- Older Millennials are adopting less but increasing.
""",

    "1-2-2": f"""
{bold}From 1998-2015:{reset}
- Younger people became less risk-averse compared to older

{bold}Depression Baby Affect:{reset}
Behavioral Characteristics of those who lived through the Great Depression:
- Less Risk Tolerant
- Save more
- Introvert

{bold}Investor Market Experience Impacts:{reset}
Risk Aversion, capacity, risk-taking

Investors with low historical returns:
- Take less financial risk
- Less likely to invest in stock
- Invest less money
- Longer-lasting effects - Early-life bad experience

{bold}Old vs Young Effect:{reset}
Past returns low - Future participation low
Past returns high - Future participation high
- Not all about the Great Depression, but about market experiences

{bold}% Willing to Take Substantial Risk:{reset}
1998 Data: 
- 16% - 65 and older 
- 35% - 50-64
- 39% - 35-49
- 52% - <35
""",

    "1-2-3": f"""{bold}General Shift in Social Attitudes:{reset}
- Desire to make a difference in the world
- Impact Investment strategies gaining importance
- Consideration of social impacts (88% invest in social impact)
- 2013 WEF survey: 36% believe "{bold}improving society should be a top priority for businesses{reset}"

{bold}Top 2 Primary Purposes of Business:{reset}
1. {bold}Produce Profits{reset}
2. {bold}Improve Society{reset}

{bold}ESG Pursuits Increase along FinTech:{reset}
- $12 trillion in "{bold}non-financial capacity{reset}" across ESG criteria
""",

    "1-2-4": f"""{bold}Trust in Tech Algorithms vs Humans:{reset}

Companies emphasize trust in tech algorithms.

{bold}Levels of trust{reset} :
1. Technical Competence
2. Ethical Conduct & Character
3. Empathic Skills & Maturity

{bold}Building trust with advisory systems:{reset}
- Clear product explanations
- Staying updated with trends
- Responsive to client needs

Complexity scenarios:
- High complexity: Authenticity > technicality.
- Low complexity: Latest financial techniques most important.

{bold}Trust in Algorithms vs Humans:{reset}
- People prefer humans.
- Trust decreases when algorithms are perceived at work.
- Algorithms Mistake > Human Mistake.

Studies show:
- Trust depends on observing a statistical model.
- Fintech context: Algorithm Aversion observed.

{bold}Conclusion:{reset}
- Human+Machine yields the best result for trust in algorithms.
""",

    "1-2-5": f"""{bold}Complexity & Choice Limitations:{reset}

{bold}1. Information Overload:{reset}
  - Skews risk perceptions.
  - Slow decision-making
  - dissatisfaction with outcomes.

{bold}2. Time horizon factors{reset}
  - Long-term success > short-term gains.
  - Single long-term decision > Multiple short-term decisions

{bold}3. Choice Overload :{reset}
- Analysis Paralysis 
- Evidence from 401k (2% participation decline every 10 options)

{bold}4. Advisor answers{reset}
- Advisors are rated based on:
  1. Providing correct and simple answers
  2. Admitting ignorance
  3. Clear communication 
- "I don't know" > unclear & made-up response
""",

    "1-3-1": f"""{bold}Bartering Era (8000 years ago):{reset}
- Shells, livestock, salt, rare products, coconut beans.
- Inefficient with no standard of value.

{bold}Metals/Coins Era (3500 years ago):{reset}
- Silver, Gold (Not coins, just pieces cut and weighed).
- Fluctuation of metal value.
- Burden to weigh and carry.

{bold}Paper Money Era:{reset}
- 13th century (Marco Polo Europe) to 19th century (Commonplace Europe).
- 1000 years ago (Chinese first paper money).
- Issues of theft and forgery.

{bold}Credit Card Era (1950):{reset}
- Large fees are an issue.
- Credit card oligopoly (few companies control).
""",

    "1-3-2": f"""{bold}1990s Trends:{reset}
- 90% non-cash transactions were cheques.
- Check usage declined; credit and debit card usage rose.

{bold}Post-Great Recession Trends:{reset}
- Debit card usage increased; 69% believe debit cards are safe.
- 2013 report: 120 million credit card accounts lost.

{bold}Cash Usage:{reset}
- Largest payment method in 2018 but decreasing.
- Typically lower-income individuals.

{bold}Debit Cards:{reset}
- Mostly low to middle-income individuals.

{bold}Credit Cards:{reset}
- Predominantly used by higher-income individuals.
- Visa, Mastercard, and American Express with 90% market share.

{bold}UnionPay (China):{reset}
- Established in China, nw operates in 150 countries.
- All Chinese cards are UnionPay branded.

{bold}Payment Trends in the USA:{reset}
- 67% Debit; 33% Credit card usage.
- High-income: attracted to credit card rewards.
- Low-income: limited trust / access to credit.
""",

    "1-3-3": f"""{bold}Intermediary:{reset}
- facilitates transactions between merchants and customers.

{bold}Card Networks Dynamics:{reset}
- Cardholders may face fees but receive rewards.
- Merchants charged high processing fees.
- Elevated costs on one side may not indicate market failure.

{bold}Setting Two-Sided Markets:{reset}
- Complicated, platform valueless without participation.
- Examples: 
    1. Grab (Cheaper cab rates = Low salary (trade-off))
    2. Nightclubs (ladies night loss-leader).

{bold}Benefits and Costs:{reset}
- Benefits: ease of payment, rewards, credit lines, cashless transactions.
- Costs: Merchant & cardholder fees (1-3% for merchants), fraud 
""",

    "1-3-4": f"""{bold}Credit Card Transaction Process:{reset}

{bold}Terminology:{reset}
- Credit Card Network (CCN): e.g., Mastercard, Visa, Chase
- Acquirer: Institution maintaining the merchant's account
- Issuing Bank: Institution maintaining the customer's card

{bold}Transaction Process:{reset}
1. {bold}Authorization:{reset}
- Cardholder requests payment authorization through Merchant, Acquirer, CCN, to Issuing Bank.

2. {bold}Authentication:{reset} 
- Issuing Bank verifies information, sends approval code to the Merchant.

3. {bold}Clearing & Settlement:{reset} 
- CCN sends transaction batch to Issuing Bank, which credits the merchant minus the "discount rate."
""",

    "1-3-5": f"""{bold}Fees in Credit Card Transactions:{reset}

{bold}Merchant Fees:{reset}
- Pay fees to Acquiring Bank (Merchant bank).
- Fees go to Issuing Bank (interchange fee) and CCN (processing fee).

{bold}Debit vs. Credit:{reset}
- Debit incurs lower fees compared to Credit.

{bold}Issues & Solutions:{reset}
- Some merchants avoid certain cards and set minimum transactions.
- Fintech solutions use e-payments to lower swipe fees and eliminate card minimums.

{bold}Examples:{reset}
- Starbucks: Gift cards for mobile wallets to reduce fees.
- Venmo: mobile app for P2P and C2B transactions, no fees.
- PayStand: cloud-based billing for B2B payments to reduce fees.

{bold}Industry Perspective:{reset}
- PayStand CEO advocates for a move to a cashless society
- Decentralized networks to avoid penalizing merchants with fees.
""",

    "1-4-1": f"""{bold}Regulation of Credit and Debit Cards{reset}

- {bold}Fairness:{reset} Disallowing unfair practices like over-limit spending and hiking interest rates on existing balances.
- {bold}Transparency:{reset} Mandating transparent disclosure of fees and rates.
- {bold}Systemic Risk:{reset} Implementing appropriate consumer credit practices to reduce overall risk.

{bold}Leading up to the Financial Crisis:{reset}
- Overdraft fees became a significant revenue stream for banks.
- Originally handled on a case-by-case basis, later changed to encourage overdraft facilities.
- Banks manipulated transactions chronologically to maximize fees.

{bold}Overdraft Practices During the Crisis:{reset}
- Automatic opt-ins for overdraft protection.
- Exploitative practices disproportionately affected lower-income and less financially savvy consumers.

{bold}Changes After the Crisis:{reset}
- Manual opt-in for overdraft protection.
- Substantial decrease in overdraft revenue.
- Introduction of the ability to "rewind" overdrafts within 24 hours if covered.

{bold}Current Concerns:{reset}
- Enforcement of new rules questioned.
- Financial institutions still target lower-income customers.
- Some customers prefer overdrafting despite rules.
""",

    "1-4-2": f"""{bold}USA{reset}:

{bold}Credit Card Accountability Responsibility Disclosure (CARD) Act (2009):{reset}
- Improved price transparency on credit for consumers.
- Reduced or eliminated late fees.
- Limited unwarned interest rate hikes.

{bold}Durbin Amendment (2010):{reset}
- Capped debit card interchange fees by merchants.
- Led to a decrease in debit rewards and an increase in credit rewards.
- Encouraged credit instruments with a focus on fee-driven profits.

{bold}Australia:{reset}

    {bold}2018 Banking Measures Act{reset}
    - Legislated responsible lending based on the ability to repay debts.
    - Provided options to cancel cards or reduce limits online.
    - Imposed limits on unsolicited credit offers and interest rate changes without notice.

{bold}UK (2011 - Electronic Money Regulation):{reset}
- Limited card networks' ability to generate interchange fee revenue.
- Set interchange fees at 0.2-0.3%, significantly lower than the 2-3% in the US.

{bold}China:{reset}
- Implemented measures to reduce fraud, including a cap on payments by QR codes.
- Increased the reserve fund ratio for e-payment platforms.
- At the forefront of financial technology, gradually replacing cash.

These regulatory measures aim to:
-enhance transparency
-protect consumers
-promote responsible lending and financial innovation.
""",

    "1-4-3":f"""Post-Recession Financial Impact and Regulation:

{bold}Losses:{reset}
- 8 million Americans lost their jobs.
- 2.5 million businesses shuttered.
- 40.1% decline in median real net worth.
- 4.3% decline in real GDP.

{bold}Financial Regulation Measures:{reset}
1. {bold}Dodd-Frank Wall Street Reform and Consumer Protection Act:{reset}
   - Regulated the financial sector.
   - Focused on consumer protection.

2. {bold}Consumer Financial Protection Bureau (CFPB):{reset}
   - Regulates institutions from the consumer's perspective.
   - Passes rules to best serve customers.
   - Aims to eliminate unfair, deceptive, and abusive practices.

3. {bold}Capital Reserve Requirements:{reset}
   - Implemented to securitize lending to others.

4. {bold}Stress-testing:{reset}
   - Tailors capital requirements to new risks.

5. {bold}Expanded Regulation of Shadow Banking System:{reset}
   - Heightened regulation towards big banks resulted in their withdrawal from small-business lending markets.
   - Consequence: Traditional small banking activities are now performed by less regulated non-bank sectors, e.g., peer-to-peer lending.

Post-recession, these regulations were introduced to stabilize the financial sector, protect consumers, and address the risks associated with lending and shadow banking.
""",

    "1-4-4": f"""Regulation and Innovation Tradeoffs:

{bold}At Best:{reset}
- Regulation ensures consumer safety and reduces market/societal risk.
- Innovation thrives as companies create new products in a safe and responsible way.

{bold}At Worst:{reset}
- hinder innovation through bureaucratic hurdles.
- Benefit incumbent companies: transfer risk from more regulated to less regulated sectors.
- Fast-paced innovation may fail to address security and cybercrime risks.

{bold}Tradeoff Respondent Survey:{reset}
- Concerns about regulation have risen since 1990.
- Overly burdensome regulation 
- Distrust in government to police markets.

{bold}Regulation's Impact:{reset}
- hHlp consumers and protect against risks in various markets.
- May harmfully serve customers by making certain markets less competitive and providing advantages to incumbents.

{bold}Occupation State License:{reset}
- From 1950 to 2015, percentage of occupations requiring a license increased from 5% to 25%.
- Over-regulation of licensing can:
        - make it more expensive for consumers
        - increase inequality
        - create barriers to entry for career options.
    """,

    "1-4-5": f"""Fintech Challenges:

{bold}1. Data Breaches / Cybercrime:{reset}
- US Cybercrime resulted in a $1.4 billion loss in 2017.
- Equifax data breach exposed 143 million people.
- Legislation giving Federal Trade Commission supervisory power over credit-reporting agencies.

{bold}2. Bitcoin - Anonymity:{reset}
- Bitcoin used for nefarious activity, like the Silk Road.
- FBI seized 26,000 bitcoins and shut down the Silk Road.

{bold}3. Unanticipated "Weird" Problems:{reset}
- Crypto investors locked out of $190 million after the exchange founder died.
- Crypto's decentralized ledger became inaccessible.
- P2P lending sold loans "without fees" but deceived customers by collecting hidden fees.

{bold}Challenges with Regulating Fintech:{reset}
- Rapidly evolving technologies
- Unclear regulatory jurisdiction.
- Lack of global coordination in regulation.
- Risks in countries outside US jurisdiction may harm US consumers.
- Question of the best regulator for specific fintech services.
- Information flow concerns

{bold}Goal:{reset}
- Establish a structure for information to flow freely.
- Discourage regulation shopping.""",

    "1-4-6": f"""OCC vs States:

{bold}OCC Charter for Fintechs (2018):{reset}
- OCC, under the Department of Treasury, starts accepting applications for Special Bank Charters.
- Special Charters allow Fintechs to operate nationally.

{bold}Eligibility Criteria:{reset}
- Fintechs must avoid taking deposits to qualify (to avoid traditional bank regulations).
- Specifically designed for P2P lending platforms.

{bold}State Regulator Reaction (2017 Lawsuit - CSBS vs OCC):{reset}
- CSBS filed a lawsuit against OCC, claiming it lacked authority to authorize non-depository Fintech companies.
- Turf wars between state and federal regulators, especially in imposing standards and unique risks.

{bold}Challenges and Lack of Consensus:{reset}
- No single regulatory framework for new payment and crypto technologies.
- Federal Banking Security Act and Treasury regulations come into play.
- State licenses add complexity.
- Lack of consensus on P2P platforms operating across states.
- Differential regulatory standards across states, creating challenges for new providers.""",

    "1-4-7": f"""{bold}Regulatory Sandbox:{reset}
- A controlled environment framework for small-scale testing of innovations by private firms.
- Allows testing without the burden of established frameworks in mature industries.

{bold}Global Initiatives:{reset}
- Euro-US-HK collaboration for a global Fintech sandbox to foster new industries and firms.
- Aim to improve and provide financial services globally.

{bold}Australia (ASIC):{reset}
- Companies decide which license and regulation apply.
- Protects consumers and investors when dealing with Fintechs.
- 12-month regulatory sandbox for new financial firms to test products and services without a license.

{bold}UK (FCA):{reset}
- Working on a global sandbox for Fintechs with cross-border ambitions.
- Focus on creating a well-defined space and duration with appropriate safeguards for consequences.

{bold}Singapore (MAS):{reset}
- Monetary Authority of SG allows institutions and Fintechs to experiment with product and service innovation.
- Provides a well-defined space and duration with appropriate safeguards.

{bold}China:{reset}
- Loose regulatory oversight over Fintech, effectively making the entire country a sandbox.
- Ministry's role includes providing ratings on blockchain products.
- Beijing has banned ICOs and blocked websites with crypto trading services.""",

    "2-1-1":  f"""
- {bold}Quotes on Crypto:{reset}
  - "A fraud, worse than tulip bulbs." - Jamie Dimon, JP Morgan CEO
  - "Probably rat poison." - Warren Buffet
  - "Crypto, mother of all scams, blockchain overhyped technology." - Roubini

- {bold}What is Crypto?{reset}
  - Is it the future of money?
  - Not an actual coin
  - Unit of Exchange
""",

    "2-1-2": f"""
- {bold}Transacting in Bitcoin:{reset}
  - **Wallet (private key, 256 number) (generated using cryptography)**
    - Private key can generate a unique address (public)

- **Ways to Transact:**
  - **Third-Party Software (Coinbase):**
    - Provides a wallet & access to a Bitcoin exchange
    - Choose between wallet/exchange
  - **Buy with Cash using Bitcoin ATM:**
    - Hard copy of private key, can transfer to digital

- {bold}Uses of Bitcoin:{reset}
  - Purchase goods & services
  - Trade back to dollars
  - Use as a currency (not a stock, treasury bill)
""",

    "2-1-3": f"""
- {bold}Bitcoin Allows:{reset}
  - Online Transactions
  - Any transaction where a credit card is used
  - Decentralization

- {bold}Why Bitcoin > Credit Card:{reset}
  - High Fees
  - Abuse of Monopoly Power (Franchise Value)
  - Companies May Tamper with Ledger

- {bold}Philosophical Reasons:{reset}
  - Libertarian
  - Lack of Trust in Government

  {bold}Fiat Money Instability (2 Issues){reset}
    1. Inflation
      - Inflation = Erode in Value
      - Investors Must Hold Cash for Transactions (Fiat)
      - Government Prints Money (Inflation > Value Drops) (Tax)
      > With Crypto, Residents Not Trapped by Seigniorage

    2. Unstable Currency
      - Weimar Republic 1921-1923
      - Venezuela 2016-Present
""",

    "2-2-1": f"""
- {bold}Issue with Property Rights (Traditional Transactions):{reset}
  - Transferring between banks expensive (fees)
  > Crypto must create its own property rights while maintaining anonymity

- {bold}Bitcoin's Answer:{reset}
  - Dispenses with the notion of human presence
  - You are your own signature
  - Private Component (Private Key) + Public Component (Address)

- {bold}Digital Signature:{reset}
  - Random Private Key
  - Protocol attaching private key to electronic message 
  - Protocol to verify signature without revealing private key

- {bold}Importance of Digital Signature:{reset}
  - No one can forge the signature
  - Creation of the signature is random
  - Signature to message is encrypted 

- {bold}Human Signature Randomness vs. Digital Randomness:{reset}
  1. Human Signature Randomness
    - No two humans are alike
    - Not the same every day
  2. Digital Randomness
    - Random-number generator on computer = pseudo-random numbers (Not perfectly random)
""",

    "2-2-2": f"""
- {bold}Satoshi Tampering Detection:{reset}
  - Make Ledger Recursive
  - Alongside each entry - put “Digest” - Shorthand to previous entry
  - Shorthand: Algorithm of using the initial of each word

- {bold}Example:{reset}
  - Maria creates a single Mariacoin
  - Maria sells Mariacoin to Sophie <MCSM>
  - Sophie sells the Mariacoin to Geoff <MSMS<mcsm>>
  - <SSMG <msms<mcsm>>>

- {bold}Tampering Detection by Bob:{reset}
  - If Bob tampers:
    - MSMS will not be initials of Bob (MSMB)
    - Bob must tamper with all 4 digests (but not that simple as)

- {bold}Digest Creation using Cryptography:{reset}
  - All random (not just initials)
  - Virtually impossible to change names
  -SHA-256 (Crypto Hash function)
""",

     "2-2-3": f"""
    {bold}Bitcoin Consensus Protocol:{reset}

1. {bold}Network Structure:{reset}
   - Bitcoin operates on a decentralized network with thousands of interconnected nodes

2. {bold}Consensus Goal:{reset}
   - The primary objective is to establish a protocol that ensures nodes agree on the state of the ledger

3. {bold}Distributed Consensus Protocol:{reset}
   - Involves nodes with varying values, aiming for agreement even in the presence of potentially malicious nodes

4. {bold}Blockchain Application:{reset}
   - Assumes an honest start and integrates new transactions into blocks to maintain ledger consistency

5. {bold}Bitcoin Protocol Strategy:{reset}
   - Achieves consensus through randomness, preventing issues like double spending and denial of service attacks

6. {bold}User Benefits:{reset}
   - Users wait for confirmations by honest nodes, ensuring the security of their transactions

7. {bold}Double Spend Prevention:{reset}
   - Nodes follow a policy, including messages and choosing the longest fork to prevent inconsistencies

8. {bold}Security Measures:{reset}
   - Confirmations extend over time, forming a long-term consensus for enhanced security

9. {bold}Handling Orphaned Forks:{reset}
   - Orphaned forks may be revisited, but the policy favors the longest fork to maintain consensus
""",

    "2-2-4": f"""
- {bold}Proof of Work Concept 1: Block Reward{reset}

1. Random Node Proposal:
   - A random node is chosen to propose a block, rewarded with bitcoins

2. Keeping Blocks Honest:
   - Nodes receive rewards only if future nodes accept their block
   - Malicious actions are deterred by the inclusion of hash pointers, ensuring acceptance

3. Self-fulfilling Equilibrium:
   - Nodes act honestly due to the expectation that others will do the same
   - Incentives drive honest behavior, creating a balanced and secure network
""",

    "2-2-5": f"""
{bold}Bitcoin Mining{reset}

1. {bold}Resource-Intensive Activity:{reset}
   - Nodes engage in resource-intensive mining to discover new coins

2. {bold}Hash Puzzle and Block Proposal:{reset}
   - Nodes compete to propose the next block by solving a cryptographic hash puzzle
   - Computing power determines the speed of solving the puzzle

3. {bold}PoW and Randomness:{reset}
   - The unpredictable nature of solving puzzles prevents nodes from being predicted
   - Randomness is a key element in the Proof of Work (PoW) system

4. {bold}Currency Creation:{reset}
   - Block rewards are the only way bitcoins are mined
   - Rewards are limited and halved every 210,000 blocks (4 years)
   - Bitcoin supply starts limited and gradually increases

5. {bold}Inflation and Transaction Fees:{reset}
   - Bitcoin can be inflated, but not manipulated by a central bank
   - Transaction fees become more significant as a potential source of mining income
   - Nodes proposing transactions ensure a balance in Bitcoin values and receive fees
""",

    "2-2-6": f"""
- {bold}PoW Challenge 1: The 51% Attack{reset}

1. {bold}Centralization Risk:{reset}
   - Possibility of a node gaining majority CPU power and centralizing the system
   - Improbable due to limited profitability and the need to maintain trade in Bitcoin

2. {bold}Improbability Factors:{reset}
   - Limited profitability and the necessity to avoid countermeasures
   - Historical instances like the 2014 mining pool incident

- {bold}PoW Challenge 2: Resource Intensity{reset}

1. {bold}Electricity Consumption:{reset}
   - Mining's electricity usage is a fraction of global banking
   - Addresses concerns of wastefulness by enabling Bitcoin trading

2. {bold}Green Critique:{reset}
   - The energy-intensive process is not wasteful, as it facilitates Bitcoin trading
   - Bitcoin, as a zero-sum game, contributes to society's net benefit

- {bold}PoW Challenge 3: Can Network Scale?{reset}

1. {bold}Scalability Dilemma:{reset}
   - Blocks limited in size, creating only one every 10 minutes
   - The trilemma: Blockchain systems can only have 2 of 3 - decentralization, scalability, security
   """,

    "2-3-1": f"""
- {bold}View 1: Traditional Finance - Theory Perspective{reset}

1. {bold}Capital Asset Pricing Model (CAPM):{reset}
   - Suggests holding risky securities based on market-weighted values
   - CAPM aligns well with index funds
   - Crypto evaluation by CAPM: discourages holding due to lack of intrinsic value in cash and currency

2. {bold}Gordon Growth Model (GGM):{reset}
   - Valuation benchmark for companies based on cash flow
   - Crypto cannot be valued by GGM as it relies on dividends, which currency lacks

- {bold}View 2: Traditional Finance - Data Perspective{reset}

1. {bold}Constructing Returns in Crypto:{reset}
   - Analyzing empirical properties of returns in Crypto
   - Treating returns similarly to traditional investments raises questions about desirability

{bold}Theoretical vs. Empirical Views:{reset}
   - {bold}Theoretical Perspective (View 1):{reset} Evaluating whether something is overlooked
   - {bold}Empirical Perspective (View 2):{reset} Focusing on limitations related to available data

3. {bold}Is there a 3rd view?{reset}
   - Exploring potential alternative perspectives in Crypto evaluation
""",

    "2-3-2": f"""
- {bold}Data-Driven Approach to Determine Dollar-Crypto Exchange Rate{reset}

1. {bold}Active Addresses:{reset}
   - Currency stabilized post-2018 crypto crash
   - Prices correlate with active addresses

2. {bold}Returns:{reset}
   - Daily growth rates (sample):
     - Bitcoin: 0.254%
     - Ether: 0.584%
     - Ripple: 0.514%
   - Cryptocurrency returns show positive skewness with significant outliers

3. {bold}Volatility:{reset}
   - Measures risk
   - Daily volatility is high, but returns are more concentrated than volatility
   - Outliers exist

4. {bold}Survivor Bias:{reset}
   - Analysis limited to top Cryptos
   - Many Cryptos have failed

- {bold}Summary:{reset}
  - Crypto prices appear stabilized.
  - Active addresses and prices are positively correlated
  - Ripple exhibits negative median returns
  - Most days result in losses, but high positive outliers impact overall returns
  - Survivor bias influences return analysis
""",

"2-3-3": f"""
- {bold}Assumptions to Portfolio Theory:{reset}
  - Investors prefer more to less
  - Investors are risk-averse
  - Returns are normally distributed

- {bold}Trade-offs in Portfolio Theory:{reset}
  - Diagram illustrating the trade-offs between mean and standard deviation
  - Balancing profit and risk
  - Risky assets depicted in a sideways U shape (risky asset frontier)
  - Clever combination of risky assets results in the efficient frontier (top part of the frontier)

- {bold}The Tangency Portfolio:{reset}
  - Introduction of a new riskless asset (Treasury Bill)
  - Tangency portfolio with a better mean and the same standard deviation
  - Tangency portfolio line with the highest possible slope, known as the Sharpe Ratio

- {bold}Capital Allocation Line:{reset}
  - Line from the risk-free rate to the tangency portfolio
  - Represents the highest Sharpe ratio achievable

- {bold}Mutual Fund Theorem:{reset}
  - Division of the portfolio allocation problem into two steps
    1. Determine the Tangency Portfolio: Optimal combination of risky assets or mutual funds
    2. Determine position on the Capital Allocation Line: Adjust risk by adding risk-free assets
  
- {bold}Consequence of Mutual Fund Theorem (Good):{reset}
  - Bill Sharpe's insight: If everyone holds the same portfolio, the market portfolio (weighted average) becomes the best possible portfolio
  - No need for statistical analysis to find the tangency; simply observe market weights from crowds

- {bold}CAPM (Capital Asset Pricing Model):{reset}
  - Market portfolio holding assets according to weights
  - Efficient and represents the highest Sharpe ratio possible
""",

   "2-3-4": f"""
- {bold}Asset Allocation with Crypto:{reset}
  - Theoretical perspective: Crypto lacks intrinsic value and dividends, seemingly not part of an optimal portfolio
  - Empirical findings: High average returns, high standard deviation, and positively skewed returns

- {bold}Sharpe Ratio and CAPM:{reset}
  - Sharpe Ratio adjusts the risk of an asset (risk-return tradeoff)
  - CAPM calculates expected return based on market risk and risk-free rate
  - Beta measures how an asset moves with the market
  - Introduction of another measure: {bold}Alpha{reset}, representing abnormal returns

- {bold}Crypto Metrics (2019):{reset}
  - Daily alphas for Bitcoin, Ether, and Ripple
  - Considering metrics: Alpha more suitable for Crypto, as it has low covariance with the market

- {bold}Portfolio Considerations:{reset}
  - High Sharpe Ratio portfolio combined with high alpha asset expands the investment opportunity set
  - Including Crypto and SNP500 may result in a higher Sharpe Ratio

- {bold}Caveats and Considerations:{reset}
  - Survivor bias, transaction costs, and mismeasurements due to a short sample
  - Importance of covariance in assessing risk and return
  - Beta on Crypto: 0.5, suggesting potential value as a hedge
  - Simple model of Bitcoin pricing using the Gordon Growth Model
  
- {bold}Pricing and Covariance:{reset}
  - Two offsetting effects: Greater economic activity increases demand for currency, while technological innovation impacts the crypto market
  - Positive covariance and high beta are desirable for Crypto's role as a hedge
  - Considerations for when Crypto becomes a medium of exchange or store of value

- {bold}Summary:{reset}
  - Crypto's role as an asset in a diversified portfolio depends on various metrics, including alpha, Sharpe Ratio, and covariance with the market
""",

    "2-4-1": f"""
- {bold}Blockchain Layers:{reset}
  - The blockchain is organized into layers, application layer on top
  - Decentralized structure fosters a competitive ecosystem

- {bold}Mining and Validation:{reset}
  - Mining involves validating transactions and recording them through Proof of Work (PoW) or Proof of Stake (PoS)

  {bold}Proof of Stake (PoS):{reset}
  - Implemented to address speed issues in mining.

1.{bold}Mechanism of PoS:{reset}
  - Amount held in a specific currency determines the portion that can be mined by the holder.
  - Example: Holding 3% of Gcoin allows mining 3% of blocks.

2.{bold}Assumption in PoS:{reset}
  - Assumes individuals with stake will act in the best interest of the blockchain network.
  - Motivated to avoid devaluing their holdings.

- {bold}Interoperability and Development:{reset}
  - Interoperability standards allow different blockchains to work together
  - Two types: Cross Chain Messaging and Cross Chain Atomic Swaps
  - Development areas include scalability, forks, efficiency improvements, and smart contracts

- {bold}Security Measures:{reset}
  - Security relies on cryptographic fingerprints and consensus protocols
  - Security audits are conducted by specialized companies
  - Legal and audit compliance are integral to blockchain use
  - Privacy is ensured through distributed data privacy platforms

- {bold}Sovereignty and Communications:{reset}
  - Users have control over their internet data for enhanced security
""",

    "2-4-2": f"""
1. {bold}Crypto Payments:{reset}
  - Manages ownership and transfership of crypto in real-time, non-cash payments
  - Decentralized to avoid a single point of failure
  - Eliminates the need for third parties and delays in transactions

2. {bold}Crypto Privacy:{reset}
  - Obscures the identity of the sender
  - Uses ring signatures, allowing digital signatures from any group member
  - Transactions are not linked to real identities

3. {bold}Crypto Wallets:{reset}
  - "Soft" wallets are software programs storing public and private keys
  - Interact with the blockchain to send and receive funds
  - Can support single or multiple currencies

4. {bold}Crypto Exchanges:{reset}
  - Online trading platforms where crypto is exchanged with fiat
  - Similar to traditional stock exchanges
  - Emphasizes security and liquidity

5. {bold}Stable Coins:{reset}
  - Designed for price stability, often pegged to a stable asset like the US dollar, a basket of currencies, or an index
  - Aims to avoid price volatility

6. {bold}Hardware Wallets and Storage:{reset}
  - Physical devices that store private keys in a protected area
  - Similar to paper wallets but more resistant to computer viruses
  - Reduces the risk of large-scale vulnerabilities

7. {bold}Blockchain Merchants:{reset}
  - Merchants, including physical retailers, accepting crypto or Bitcoin as payment
""",

    "2-4-3": f"""
- {bold}Trading Platforms:{reset}
  - Online platforms facilitate buying and selling of cryptocurrencies
  - Diverse features and user interfaces
  - Varied security measures across platforms

- {bold}Insurance in Crypto:{reset}
  - Challenges due to limited customer information compared to traditional insurance
  - Actuarial analysis is difficult
  - Focus on scrutinizing security and storage procedures
  - Coverage types vary, may include payment theft but not hacking

- {bold}Lending Against Digital Assets:{reset}
  - Allows users to lend against their digital assets as collateral
  - Loan-to-value ratio is crucial (e.g., $20k collateral for a $10k loan)

- {bold}Investment Funds:{reset}
  - Cryptocurrency investment funds operate in the trading space
  - Investment strategies may involve only crypto or a mix with other assets
""",

    "2-4-4": f"""
- {bold}Value Exchange:{reset}
{bold}1. Content Monetization:{reset}
  - Challenges with high costs and tied-up rights
  > Blockchain facilitates transparent content trading, funding ideas, and sharing rights on a distributed ledger
  
{bold}2. Marketplaces{reset}
  - Enabling secure exchange of goods, services, and jobs
  > Blockchain allows the transfer of reputation between buyers and sellers, addressing trust challenges

{bold}3. Energy:{reset}
  - Blockchain supports decentralized energy data exchange and smart grid management
  - Enhances transparency and forecasting in smart grid systems

- {bold}Shared Data:{reset}
  
{bold}1. Internet of Things (IoT):{reset} 
    -Blockchain secures and optimizes IoT applications, transforming device communication

{bold}2. Supply Chain/Logistics:{reset} 
    -Blockchain ensures transparency, security, and efficiency across complex supply chains

- {bold}Attributions for Collaboration:{reset}
  - Blockchain in collaborative spaces (e.g., music) generates immutable titles, registers assets, and certifies authorizations
  
-{bold}Reputation systems{reset}
  - Blockchain address counterparty risk and reward accurate information

- {bold}Healthcare Information:{reset}
  - Blockchain disrupts fragmented healthcare data, allowing individuals to own and control personal information
  - Patients choose access permissions and can sell data for drug trials

- {bold}Authenticity and Validation of Data:{reset}
  - {bold}Real Estate:{reset} Blockchain secures integrity, creates an audit trail, and provides proof of events for titles
  - {bold}Ticketing:{reset} Blockchain facilitates secure ticket ownership transfer, issuance, and validation, preventing fraud

- {bold}Diversified Financial Space:{reset}

{bold}1. Legal:{reset}
- Smart contracts leverage blockchain, reducing the need for written contracts and lawyer involvement

{bold}2. Accounting:{reset} 
- Blockchain introduces a new type of continuous and secure accounting ledger

{bold}3. Middle & Back Office Functions:{reset} 
- Blockchain impacts various financial services, including risk management, administration, support, and payment services
""",

    "2-4-5": f"""
- {bold}Gaming & Esports:{reset}
  - Creation of digital assets, including virtual characters, profiles, items, and resources on the blockchain
  - New monetization strategies for digital assets usable across multiple games

- {bold}Gambling & Prediction Markets:{reset}
  - Blockchain allows anyone to join a casino, share funding, and profit from casino activities
  - Prediction markets use oracles on the blockchain to predict outcomes of events

- {bold}Virtual Reality:{reset}
  - Blockchain powers an economy of tradable digital assets, including holographic avatars
  """,


    "2-4-6": f"""- {bold}Blockchain Stakeholders:{reset}
  - {bold}Investors:{reset} Pour resources into the blockchain community
  - {bold}Government & Regulation:{reset} Establish rules around blockchain technology
  - {bold}Media & Advocates:{reset} Serve as sources of information and influence

- {bold}Types of Investment:{reset}
  - {bold}ICO (Initial Coin Offering):{reset} Fundraising mechanism for new projects, selling crypto coins to investors
  - {bold}Venture Capitalists:{reset} Actively invest in blockchain companies, supporting and growing new businesses
  - {bold}Corporate Investors:{reset} Traditional companies investing in blockchain, with over $1 billion invested since 2012

- {bold}Private & Public Blockchains:{reset}
  - {bold}Private:{reset} Restricted to few companies
  - {bold}Public:{reset} Open to everyone

- {bold}Consortia:{reset}
  - Fall between private and public blockchains
  - Bring organizations into a distributed database, combining the security of private with the network effects of public
  """,

  "2-4-7": f"""
1. {bold}Securities & Exchange Commission (SEC):{reset}
  - Securities Act of 1933: reduce risk to investors by ensuring adequate information.
  - Blockchain space: Issuing reports on token issues/sales
  - Howie test to determine if something is a security, establishing the SEC Cyber Unit.

2. {bold}Commodity Futures Trading Commission (CFTC):{reset}
  - Established a regulatory environment for investors and market participants.
  - In 2014, declared crypto as a commodity, overseeing its activities.
  - Took action against unregistered futures exchanges 
  - Promotes responsible regulation to foster innovation.

3. {bold}FinCEN & TFI (Financial Crime Enforcement Network & Office of Terrorism & Financial Intelligence):{reset}
  - Enforces the Bank Secrecy Act (BSA), making virtual currency exchanges and administrators subject to BSA regulations.
  - Businesses must register with FinCEN.

4. {bold}IRS (Internal Revenue Service):{reset}
  - Collects and manages revenue in the U.S.
  - Sets principles for virtual currency transactions, treating them as property and subject to tax principles.

5. {bold}States:{reset}
  - State governments recognize the transformative power of blockchain, launching initiatives and implementing specific laws.

  
{bold}Non-U.S Regulators:{reset}
  - In the process of building rules and regulations.

- {bold}European Union:{reset}
  - Implemented Data Protection Guidance (GDPR).

- {bold}International Standard Setting Bodies:{reset}

{bold}1. Financial Stability Board:{reset} Consists of G20 countries, monitoring crypto markets.
{bold}2. Bank for International Settlements:{reset} Published a chapter on risks in crypto.
""",

    "3-1-1": f"""
{bold}Introduction:{reset}
- Robot giving advice, handling logistics for account aggregation, and presenting financials.

{bold}Adding Value:{reset}
- Aims to help users achieve financial goals with optimal portfolio recommendations.

{bold}Focus:{reset}
- Delivers high-impact, cost-effective investment advice.

{bold}Historical Context:{reset}
- Traditional financial advice often limited to the affluent.
- Reliance on social security and pension plans had drawbacks.

{bold}Downsides of Traditional Approaches:{reset}
- Employers' liability for maintaining pension assets.
- Examples of insolvency risks: Detroit, GM, Chrysler, Puerto Rico.

{bold}Era of Personal Responsibility:{reset}
- Emergence of 401(k) plans, encouraging DIY retirement savings.
- Contributions from pre-tax income became standard.

{bold}Goal of Robo-Advisors:{reset}
- Streamline investment, intelligent retirement saving, and propose effective plans.
- Provide insights into potential outcomes.
""",

    "3-1-2": f"""
{bold}Axioms of Economics:{reset}

1. {bold}Preference for More Money:{reset}
   - Individuals generally prefer having more money than less.
   - Wealthier individuals experience a decrease in the marginal utility of the next dollar.

2. {bold}Risk Aversion:{reset}
   - Example: Choosing $1,000 with certainty over a 50% chance of $2,000.
   - Demonstrates the principle of risk aversion.

3. {bold}Certainty Equivalent:{reset}
   - Represents the amount below $1,000 (e.g., $970) where an individual wouldn't take a gamble.
   - Decision-making influenced by risk aversion.
   - Robo-advising apps leverage information on risk aversion to guide investment choices.
""",

    "3-1-3": f"""
{bold}Easy Way:{reset}
Take the value-weighted market index (S&P 500) as the efficient portfolio.

{bold}Economic Reasons for this Approach:{reset}
- Combination of efficient portfolios is also efficient.
- If borrowable at the risk-free rate, it's optimal to hold risky assets in the same weights (lever up/down).

{bold}Index vs Individual Assets:{reset}
- Index is often more cost-effective compared to individual assets.

{bold}Hard Way:{reset}
- Guess inputs (expected return, variance, covariance of assets) and calculate the efficient portfolio.
- Expected returns are hard to guess, co-movements are easier to estimate.
- Consider transaction costs, and the challenge of private information (Akerlof's "market for lemons").

{bold}Hybrid Approach:{reset}
- Find the efficient portfolio of indices, industries, countries, and asset classes (not limited to stocks or metals).
- Diversification benefits and savings on transaction costs.
""",

    "3-1-4": f"""
{bold}ETFs:{reset}
- Trades on the open market.
- Money goes to the share seller, does not affect the fund.
- Market transaction costs.
- Can be traded anytime when the market is open.
- Minimum 1 share (excluding fractionals).
- Easy access from any brokerage account.

{bold}Mutual Funds (Active Management):{reset}
- Investment program funded by shareholders.
- Professionally managed with diversified holdings.
- Typically pay 1-2% for the fund manager.
- One trading time a day.
- Money goes into the fund, making it a "trade."
- Accessible from limited platforms.
- Minimum investment amount required.

{bold}Index Funds (S&P 500):{reset}
- Offers cheaper fees.
- Does not charge for stock picking.

{bold}Target Date Funds (Lifecycle Investing):{reset}
- Robo-advisors customize portfolios based on the investor's position in the lifecycle.
- Investment pattern shifts over time, more risk for younger investors ; more bonds for older investors.

{bold}Target Date Funds (Popular for Retirement):{reset}
- Investors choose  fund based on their expected retirement year.
- Rebalances investments over time, risk shifts lower over time
- Not targeting a specific end balance.
""",

    "3-1-5": f"""
{bold}Robo-Advisor Customization:{reset}
- Takes investor's risk tolerance into account
- Considers closer-time financial goals (house)
- Analyzes existing assets and evaluates current mortgage rates.
- Provides suggestions on mortgages and student loans

{bold}Information Available to Robo-Advisors:{reset}
- Gathers data on the time and place of usage.
- Identifies events triggering app usage.
- Tracks the location of external parties when interacting with investment suggestions.

{bold}Social Impact Preferences:{reset}
- Select preferred ethical guidelines.
- Options to avoid or support certain industries.
- Considers specific behaviors, helping users align investments with personal values.
""",

    "3-2-1": f"""
{bold}Promises & Challenges of Crowdfunding:{reset}
- Possibility of financial loss, contributing to a negative experience.
- Overcoming Challenges:
  - Traditional method of businesses connecting with investors.
  - JOBS Act 2012 introduced financial innovation, promoting crowdfunding.
  - Consideration of the cost of funding in crowdfunding models.
  - Harnessing the wisdom of crowds for collective decision-making.
  - Recognition of non-financial motives driving crowdfunding participation.
""",

    "3-2-2": f"""
{bold}IPO Process:{reset}
1. {bold}Engage an underwriter through a "bake-off," where banks pitch to invest{reset}
 - Prioritize underwriters with experience in capital markets.

2. {bold}File a registration statement with the Securities & Exchange Commission (SEC){reset}
 - This process is tightly regulated, and companies receive comments.

3. {bold}Submit the registration statement, often referred to as the S1.{reset}
 - Choose the price range and the number of shares to be offered.

4. {bold}Conduct a roadshow, pitching to institutional investors. {reset}
 - Engage in book building
 - Creating a book of interested investors and determining the number of shares at a specific price.{reset}

5. {bold}Set the final price and place the shares in the market.{reset}

On average:
IPOs experience an 18% increase from the offer price to the next day
""",

    "3-2-3": f"""
{bold}Title I: Emerging Growth Companies{reset}
- Facilitates an easier IPO for companies with revenue under a billion dollars
- Allows companies wanting to go public to identify obstacles and relax disclosure rules
- Testing waters before a public offering is permitted under the JOBS Act

Under the JOBS Act:
- Submit a Draft Registration Statement to the SEC Confidentially
- The public does not see it
- Receive SEC feedback and then decide

Initially limited to Emerging Growth Companies, now not limited under Trump

Comparison: Lyft (public) vs Uber (private)
Uber can fail privately

Failing privately under Title I:
- Requires 2 years of audited financials (not 3)
- Less disclosure
- Exempt from Say on Pay (disclosing pay to top personnel)
- Exempt from the auditor reporting financials
- Expensive to get an auditor, acting as a deterrent to small firms going public

{bold}Title II: Private Company Financing{reset}
- Regulation D allows private companies to raise money without going public
- Funding can be obtained from friends, friends of friends, and connections
- General solicitation is not allowed; money cannot be brought in by advertising

The Catch:
- Investing in Title 2 is only for Accredited Investors (Rich)
- Net worth of $1 million (excluding residence)
- $200,000 annual income for the last 2 years

Title II Portals verify the wealth of potential investors, alleviating concerns for entrepreneurs. Crowdfunding is restricted to the wealthy

{bold}Title III: Crowdfunding for Anybody{reset}
- Accessible crowdfunding for everyone with limits on investments and company raises
- Entrepreneurs are limited to raising $1 million in 12 months

For Entrepreneurs:
- Raising <100k requires company officer sign-off on disclosures
- Raising 100-500k is reviewed by a public accountant (not audit expensive)
- Raising 500k-1m is first-time reviewed and second-time audited

For Investors, restrictions depend on income:
- <100k annual (2k/year or 5% income)
- >100k annual (10% income, up to 100k)
- Total investment given in a 12-month period
- Wait a year before selling

{bold}Title IV: Mini IPO{reset}
- Regulation A+ allows selling directly to retail investors on a best-efforts basis
- Underwriters build conduits to both retail public and institutional investors

Normally in an IPO, the underwriter buys shares from the issuer and then places shares with the public
""",

    "3-2-4": f"""
{bold}1. Cost to Raise Money{reset}
- Professional time (lawyer, accountant): 100 hours at $500/hour = $50,000
- Professional fees for the internet portal: Median 5%, up to 7% (e.g., Wefunder)
- Minimum 10% in costs (5% professional costs + 5% portal fees) excluding campaign costs (video, advertising, personal time)

{bold}2. Cost to Investors{reset}
- Example: If an investor makes $100k/year (allowed to invest 10%, $10k)
- Spread $10k across 5 offerings ($2k each)

{bold}3. Investor Opportunity Costs{reset}
- If earning $50/hour, spending 8 hours on research incurs an opportunity cost of $400

{bold}Expected Return for Investors{reset}
- To make the investment worthwhile, the expected return must be at least $800
- Profit expectations must be realistic, especially if the chance of investing is lower than 50%

{bold}4. Due Diligence{reset}
- Alternative: Don't waste time researching and rely on what you already know

{bold}5. Concerns as an Investor in Crowdfunding{reset}
- Was crowdfunding a last resort? Consider the company's relationships with family, friends, and venture capital.
  
{bold}Why Crowdfunding May Not Be a Last Resort{reset}
- Proof of concept: Crowdfunding before approaching venture capital to demonstrate potential demand.
- To convince venture capitalists that crowdfunding shareholders are also potential customers.
""",

    "3-2-5": f"""
{bold}Learning from Others{reset}
- Learn the value of an investment based on demand.
- Setting a Minimum Raise: If the minimum is unmet, investors' money is refunded. If met, the investment proceeds only if others also invest.

{bold}Wisdom of the Crowd{reset}
- Each individual investor brings different knowledge.
- Potential issue: Everyone may have the same information.

{bold}Judicial Analogy{reset}
- Risk of Free Riding: Group decisions may be influenced, leading to dismissal of individual thoughts.
- Example: 1 believes not guilty, 11 believe guilty, and 1 follows the majority due to "wisdom of the crowd."

{bold}Free Riding in Finance{reset}
- Concerns: How to ensure others aren't free riding?
""",

    "3-2-6": f"""
{bold}Impact Investing{reset}

- Not all about profit, societal impact too.
- Combines financial returns with social impact
- Buying shares of ill-impact companies to influence decisions.

{bold}Foster Startups with Social Missions{reset}
- Aims to help companies achieve self-sustaining financials.

{bold}WeFunder{reset}
- Stresses that investing is more than profits and should contribute to making the world a better place.

{bold}B Corp{reset}
- Asks whether the company is approved by B Lab, a private outfit that vets and approves B Corps.
- Companies with high scores are designated as B Corps.

{bold}Benefit Corp{reset}
- Legal designation registered under state law.
- Companies commit to a special social impact goal, mapping out the goal and measurement.
- Designates a corporate director to oversee the societal purpose, reflecting a strong legal commitment to social benefits.
""",

    "3-3-1": f"""
{bold}Peer-to-Peer Lending (P2P){reset} - Past

- Originally known as P2P lending.
- Platforms eliminated the middleman, matching lenders directly with borrowers.
- Initially involved retail investors.

{bold}Evolution of P2P Lending{reset}

- Platforms now take on the majority of the work, making credit-granting decisions.
- Funding primarily comes from large investors, including hedge funds.
- Shifted away from relying on retail investors.
""",

    "3-3-2": f"""
{bold}Liabilities in Consumer Credit{reset}

- Types include mortgage, car loans (debt for assets), student loans (debt for human capital), credit card debt, etc.

{bold}Household Debt Components{reset}

- Mainly composed of mortgage.
- Other components include credit card debt, student loans, home equity lines, and car loans.
- Student loans show a linear increase, while home equity is decreasing.

{bold}Fintech Opportunities{reset}

- Fintech presents opportunities to disrupt various consumer credit segments.
- Major mortgage lenders, such as Quicken, have been impacted, and fintech companies are focusing on car loans.

{bold}Credit Card Debt{reset}

- Often results in borrowing at high interest rates with no collateral.
- Strategies to lower interest rates include moving the balance to a new card or taking out a home-equity line of credit.

{bold}Student Loan Debt{reset}

- Good when borrowing to build human capital.
- Can become problematic if income doesn't align with loan obligations.
- Linear increase in student loans attributed to graduates struggling to repay.

{bold}Income Driven Repayment{reset}

- Sets a maximum of 10% of income toward loans.
- Unpaid interest is added to the principal balance, leading to a continuous increase.
- Debt may be discharged after 20 years.
""",

    "3-3-3": f"""
{bold}Evolution of Peer-to-Peer Lending{reset}

{bold}Origins{reset}:
- Platforms like Lending Club & Prosper Marketplace match borrowers and lenders.

{bold}Present Landscape{reset}:
1. 95% of lending is by institutional investors.
2. Platforms facilitate loans, relying on big data and machine learning.
3. Traditional credit scores like FICO have diminished in influence.
4. Platforms reevaluate prime-ness, considering an invisible "prime" borrower.
5. Subprime risks range from A to G.
6. Credit rationing occurs as borrowers are aware of their risk profiles.
7. Platforms play a more involved role in credit risk evaluations and setting interest rates.

{bold}Evolution{reset}:
- Initially, lending involved a simple bidding process.
- Platforms now conduct their own credit risk evaluations and set interest rates.
- Investors decide participation based on the platform's evaluation.
""",

    "3-3-4": f"""
{bold}Student Loan Debt Evolution{reset}

{bold}2018-2019{reset}:
- Uniform interest rate of 6.6% for all.
- Income-Driven Programs available for distressed borrowers.
- Variation in rates based on perceived risk, e.g., SoFi offering 4% for low-risk borrowers.

{bold}Challenges in Refinancing Business{reset}:
- Treasury rates and student loan rates increasing since 2016.
- Tough for lenders like SoFi to undercut due to the rise in rates.

{bold}SoFi's Business Transition{reset}:
- Originally focused on refinancing but transitioning to original lending.
- Bigger risks, dealing with students who didn't borrow federally.
- Shifting from refinancing to original lending comes with uncertainties about graduation and job prospects.
""",

    "3-3-5": f"""

{bold}1. Merchant Cash Advance: Advantages{reset}
- Payment Aggregators analyze every sale, tip, and card usage, potentially even cash payments.
- Utilizes big data to make judgments about future cash flow: forming the basis for loan offers.
- Repayment structure linked to the merchant's cash flow (percentage of daily sales till repaid)

{bold}2. Square Capital{reset}
- Capital for loans provided by external investors.
- Small businesses benefit from informed lending decisions based on transaction information.
- Repayment directly tied to cash flow, ensuring a smoother repayment process.
""",

    "3-4-1": f"""
{bold}Problem Solving with Mobile Card Readers{reset}

- {bold}Challenge:{reset} Small businesses unable to accept credit cards, potentially losing sales.
- {bold}Solution:{reset} Utilizing mobile card readers, businesses can accept credit cards through mobile devices.
- {bold}Implementation:{reset} Connect a dongle into the headphone jack, enabling credit card transactions and ensuring sales opportunities are not missed.
""",

    "3-4-2": f"""
{bold}Utilizing Fintech at CommonBond{reset}

- {bold}High Tech Implementation:{reset}
  - Utilizes developers and code to enhance the end-user experience.
  - Implements a loan origination system for efficient processing.

- {bold}Application Experience Automation:{reset}
  - Streamlines the application process, providing a faster experience for users.
  - Automates verification of graduation status and outstanding payments, ensuring accuracy.
  - Offers automated income information for customers.

- {bold}Financial Structures:{reset}
  - Operates on a two-sided market, connecting capital providers with customers at a lower cost.

- {bold}Customer Treatment:{reset}
  - Designs products with a focus on simplicity and speed for an enhanced customer experience.
""",

    "4-1-1": f"""
{bold}Backbone of Fintech Today (Purpose){reset}
- Dimension reduction
- Efficiency
- Seeing patterns in data 

{bold}Background Definition{reset}
- Expressed as a concept in 1940
- Turing test: Standard set for sentient machine intelligence (AI Intelligent if evaluator can't differentiate between AI & Human)

{bold}Big Data in Finance{reset}
- Finance invented big data
- Financial firms evolved computer tech
- Stock ticker in 1867
- Computational arms race today with AI, Neural Networks, Big Data Analytics
- 25 years ago, dedicated terminals cost tens of thousands

{bold}Today{reset}
- Areas of finance remain human-centric in terms of trust and relationships
- Computers simulate humans in routine tasks.

{bold}Core Definitions{reset}
- Oxford: Computer systems performing tasks normally needing human intelligence
- Merriam-Webster: Branch of CS dealing with the simulation of computer/capability of machine to imitate human behavior

- Aiming to understand tasks towards self-directed learning (problem-solving, perception like humans)
""",

    "4-1-2": f"""
{bold}1. Assistants / Personal Finance{reset}
- B2C markets
- Wealth management
- Financial advice

{bold}2. Quantitative & Asset Management{reset}
- Trading/general portfolio allocation level

{bold}3. Insurance{reset}
- Credit risk management
- Claims integrity

{bold}4. Market Research / Market Analysis{reset}
- Investment
- Product development
- Structured/unstructured numerical data 
- News streams in multiple languages delivered to desktop 

{bold}5. Debt Collection{reset}
- Follow people prone to/with debts across geographical areas

{bold}6. Expense Reporting{reset}
- AI can improve outcomes

{bold}7. Predictive Analytics{reset}
- Unseen possibilities
- Financial crises could've been better identified with this

{bold}8. Regulatory, Compliance, Fraud Detection{reset}
- Gray area of aggressiveness in disclosure, statements
- C-suite executive behavior detectable with levels of testosterone

{bold}9. Credit Scoring / Direct Lending{reset}
- Combine multiple sources of data (especially in different formats)
""",

    "4-1-3": f"""
{bold}1. Superhuman Accuracy in Decision Making{reset}
- Lower cost, ability to operate at scale
- Utilizes algorithms to overcome human biases, emotions, and moods
- Less error-prone

{bold}2. Automated Customer Support{reset}
- Chatbots, conversation simulation
- Provides 24/7 availability

{bold}3. Wealth Management{reset}
- Robo-advisory
- Potential future disintermediation of human involvement, although unlikely due to legal/compliance issues (e.g., ERISA law)
""",

    "4-1-4": f"""
{bold}Robo-Advisors: Evolution and Overview{reset}

- {bold}Old Definition:{reset}
  - Aimed to reduce the cost of client service by disintermediating humans.
  
- {bold}Today's Definition:{reset}
  - Algorithms used to build customer allocation.
  - Examples: Wealthfront and Betterment.

- {bold}Current State:{reset}
  - Both Wealthfront and Betterment still have client service representatives, not achieving the pure vision of robo advice.
  - The robo model remains a useful cost-based competitor against the human-only model.

- {bold}Future Focus - AUM (Assets Under Management):{reset}
  - Vanguard Personal Advisor Services, rebranded as robo in 2015, had $21.2 million AUM by June.
  - Wealthfront has $11.4 billion AUM, with 90% invested in Vanguard funds.
  - Betterment has $16.4 billion AUM, emphasizing Defined Contribution retirement plan sales to small companies.

- {bold}Traditional Brokerage Firms:{reset}
  - Schwab, Merrill Lynch, Fidelity have acquired robo-type offerings.
""",

    "4-1-5":  f"""
{bold}Machine Learning{reset}

- {bold}Definition:{reset}
  - Learning over time through algorithms and mathematical models.
  - Acquiring knowledge by extracting patterns in data rather than following explicit instructions.

- {bold}Leverage in Insurtech Companies:{reset}
  - National Association of Insurance Commissioners: insurers only use 10-15% of data.
  - ML can extract more information from this data.

- {bold}Applications in Insurtech:{reset}
  - Risk modeling: Analyzing claims data.
  - Demand modeling: Using math models to predict demand for products.
  - Fraud detection: Identifying odd patterns of behavior.
  - Claims processing: Automating claim reporting.
  - Underwriting: Analyzing collected data, flagging errors, and estimating risk.

- {bold}Usage in Hedge Funds:{reset}
  - BarclayHedge states that over 50% of hedge funds use AI/ML for investment decisions.
  - A quarter of money managers use AI/ML for trade execution.

- {bold}Public Perception:{reset}
  - Responses to public surveys may mask the depth of AI in finance.
  - Sparse details are provided about AI/ML usage in hedge funds.

- {bold}Textual Analysis in Trading:{reset}
  - Hedge funds exploit technology and strategy but often hide it.
  - Textual analysis involves using news stories and financial releases to influence trading signals.

- {bold}IBM Watson:{reset}
  - Beat humans in Jeopardy.
  - Capable of collecting, curating, and analyzing data.
  - Natural language processing allows AI to answer questions.
  - Deployed in various industries, including healthcare, consumer retail, tax preparation, and academia.
""",

    "4-2-1": f"""
{bold}Artificial Intelligence in Insurtech{reset}

- {bold}Artificial Intelligence:{reset}
  - Software associated with human reasoning, including iterative learning.
  - Features self-awareness and emotions.
  - Utilized in chatbots, such as Allstate's Allstate Business Insurance Expert (ABIE), answering questions.
  - Similar AI systems are employed by other insurers.

- {bold}Machine Learning:{reset}
  - Involves computers learning over time using algorithms to simulate human brain networks.
  - Focuses on extracting patterns from raw data, especially with deep learning techniques for large datasets.
  - Notably, insurers currently use only 10-15% of available data.

- {bold}Applications in Insurtech Using Machine Learning:{reset}
  - {bold}Risk Modeling:{reset} Predicting future losses.
  - {bold}Demand Modeling:{reset} Predicting future demand and estimating premiums.
  - {bold}Detecting Fraud:{reset} Identifying patterns of malicious behavior.
  - {bold}Processing Claims:{reset} Automating claim reporting and processing.
  - {bold}Underwriting:{reset} Assisting underwriters in analyzing applicant data, flagging risks, aiding decision-making, and checking external sources for accuracy (e.g., social media).
""",

    "4-2-2": f"""
{bold}Redefining 5 Aspects in Insurtech{reset}

1. {bold}Product Design:{reset}
   - Learning from customer experiences.
   - Customization based on individual needs.
   - Adjusting product offerings in real-time.

2. {bold}Front Office (Selling & Marketing):{reset}
   - Omnichannel management for seamless client interactions.
   - Real-time updates and client interaction.
   - Client satisfaction levels.
   - Information availability and price transparency.

3. {bold}Underwriting (Risk Assessment):{reset}
   - Capturing feedback 
   - Implementing risk-based pricing models.
   - Providing promotions and discounts.
   - Less reliance on mandatory data.

4. {bold}Policy Administration:{reset}
   - Proactive client engagement based on servicing desires.
   - Implementing automated systems for efficient processing.
   - Timely renewal and premium reminders.
   - Easy access to policy details.

5. {bold}Claims Management:{reset}
   - Streamlining claims for reduced waiting time.
   - Real-time claims monitoring.
   - Analytics for fraud detection.
""",

    "4-2-3": f"""
{bold}Traditional View{reset}

1. {bold}Full Stack:{reset}
   - Platforms underwriting policies.
   - Assuming risk and managing the process end-to-end.

2. {bold}Agent:{reset}
   - Platforms acting on behalf of carriers.
   - Acting as an extension of an incumbent carrier.

3. {bold}Brokers:{reset}
   - Platforms providing customers with policies.
   - Involving incumbent carriers and insurance platforms.
   - May include commissions.
   - Customers may scroll through policies or connect to preferred policies through algorithms.

{bold}Nuanced View{reset}

1. {bold}Full Carriers:{reset}
   - Digital, P2P, Micro-Insurers.
   - On-Demand with customization options.
   - Usage-Based insurance models.

2. {bold}Enablers:{reset}
   - Addressing front office solutions.
   - Handling policy management, claims management, and data & tech specialties.

3. {bold}Distributors:{reset}
   - Online architecture.
   - Digital brokers customized to demand.
   - B2B distribution channels.
""",

    "4-2-4": f"""
{bold}Insurtech Statistics{reset}

- Startup Count:
  - 2015: 50
  - 2017: 1200

- Market Size:
  - 2018 Revenue: $0.5 billion
  - 2023 Expected Revenue: $1.2 billion (16% CAGR)
  - Highest Regional CAGR in Asia-Pacific (Singapore, Hong Kong, India)

- Areas of Disruption (Insurtech):
  1. Mobile Platforms (Product Distribution)
  2. Connected Home Office (Information, Property, Casualty)
  3. P2P/Sharing Economy
  4. Connected Health (Isolate bodily functions, state of being)
  5. Connected Car (Reroute traffic, drive safety)
  6. Blockchain (Data integrity)
""",

    "4-2-5": f"""
{bold}Micro Insurance Players{reset}

1. {bold}Omidyar Network{reset}:
   - Non-profit Profit Model
   - $1.5 billion committed since inception
   - $800 million in grants
   - Micro-insurance, micro-finance, infrastructure, tech-enabled activities based on the pyramid
   - Targets low-income individuals with limited access to insurance, facing challenging geopolitical and harsh physical environments
   - Product Types: Individual/group coverage, term life, health/accidental/disability, casualty (crop, livestock, theft), savings plans

2. {bold}BIMA{reset}:
   - Insurance Disrupter (Insurtech Leader)
   - Offers mobile insurance with accident, life, and health products to 26 million low-income individuals across 15 countries, including Sri Lanka
   - Lower prices via cellphone, pay-as-you-go (as little as 60 cents), and streamlined 3-minute process
   - Acquiring 550,000 new customers per month
   - 93% of customers live on <$10 a day, and 75% have never had insurance
   - Valuation: $300 million (as of December 2018)
""",

    "4-3-1": f"""
{bold}Real Estate Investment Overview{reset}

- Vast Industry: $873 billion in 2017
- US Commercial Properties Sales: $375.6 billion
- US Residential: 5.3 million existing homes, 667,000 new homes sold in 2018

{bold}Definition{reset}
- Expected to expand with democratized allocation of real assets
- Positive Rate of Return (ROR)

{bold}Real Estate Returns{reset}
- Equivalent to US equities
- Positive cash flow and price appreciation at 10%, with industrial sector having the highest returns
- Positive across all sectors

{bold}Cap Rate - Capitalization Rate{reset}
- Rate of cash flows (property scaled by value)
- Compared to dividend/bond yields
- Above US treasuries
""", 

    "4-3-2": f""" {bold}ReTech{reset}
- Application of tech and innovative solutions to enhance and transform aspects of the traditional real estate industry. 
- Disruption / Additive to Real Estate industry

{bold}Examples:{reset}
1. Zillow
- Online portal and listing aggregator
- Emerged during the late 90s dot-com boom
- Leveraged relationships with brokers
- Expanded data access to become a market leader
- Democratized view into regions and properties

2. WeWork
- Leading real estate company in shared workspaces
- Transforming office space through tech and social values
- Positioned as a leader in real estate leasing
""",

    "4-3-3": f"""
{bold}Innovative Real Estate Tech Companies{reset}

1. Blend
- Cloud-based platform facilitating the sharing of financial data between lenders and mortgage seekers.
- Cuts down on the cost of approval with real-time financial insights.

2. LendingHome
- Robo-lending platform providing bridge loans to active participants.
- Loans underwritten by accredited investors and institutions.
- Over $3.5 billion in loans and $160 million in VC funding.

3. Opendoor
- Utilizes algorithms, big data, and AI to value and purchase homes.
- Renovates and resells homes.
- Recently expanded to 20 cities, charging sellers a 7% fee.

{bold}Trends in Real Estate Tech:{reset}

1. Affordability
- Millennials spending a significant share of income on rent.
- Increasing trend of millennials living with parents.

2. Desire for Community
- Real estate tech trends aim to facilitate community involvement.
- Challenges arise due to longer work hours.

3. Flexibility
- Gig economy, enabled by tech, highlights the importance of flexibility.
- Rise in furniture rentals to meet flexible living needs.
""",

    "4-3-4": f"""
{bold}Investment in Commercial Real Estate (CRE) Tech{reset}

- $9.6 billion investment in CRE tech (beyond apps and algorithms)
- Tools related to real estate, including IoT (Internet of Things).
- Examples include Nest tags, key fobs, and smart home technologies.
- Innovative solutions like photovoltaic glass for energy savings.

{bold}Key Insights:{reset}

- Doubling of institutional capital in CRE tech, boosting innovative business models.
- From 2009 to 2017: CRE tech capital doubled from $400 billion to $800 billion.
""",

    "4-3-5": f"""
{bold}Data in Commercial Real Estate (CRE) Tech{reset}

1. Data-Driven Commercial Sector:
   - Property management, deal sourcing, and due diligence 
   - Reliant on data and detailed information.

2. CRE Tech Startups:
   - CRE Tech startups serve as industry-optimized versions of online applications.
   - Examples include:
     - Workframe: A tenant relationships portal and transaction data aggregator.
     - WeSmartPark: Often dubbed as the 'Airbnb for garage space.'
     - Bowery: Specializing in automating the CRE appraisal process.
""",

    "4-4-1": f"""
{bold}Vanguard: Exciting Trends in FinTech:{reset}

1. {bold}Disruption and Evolution:{reset}
   - Rethinking fundamentals of money and banking.
   - Challenge established players, building a dynamic industry.

2. {bold}Democratization:{reset}
   - Expanding access beyond traditional limits.
   - Moving beyond mutual funds to include diverse asset classes.
   - Breaking down barriers for non-affluent individuals.

3. {bold}Tokenization:{reset}
   - Converting physical assets into digital forms using blockchain.
   - Example: Tokenizing credit card numbers for secure transactions.

4. {bold}User Empowerment:{reset}
   - Putting more financial power in the hands of end-users.
   - Addressing liquidity challenges for increased financial flexibility.

5. {bold}Overcoming Regulation Challenges:{reset}
   - Navigating regulatory hurdles to foster growth.
   - Striking a balance between innovation and compliance.

6. {bold}Vanguard in Digital Advice:{reset}
   - Digitizing advisory services for a seamless user experience.
   - Setting the pace for advancements in financial advice.

"""

}


# Function to display options
def display_options(options, back_option=True):
    for idx, option in enumerate(options, start=1):
      4
      print(f"{idx}. {option}")
    if back_option:
        print("0. Back")

# display menu titles (specializations, topics, and segments)
def display_menu(title, items, back_option=True, specialization_name=None):
    # ANSI gold
    golden = "\033[93m"
    reset_colour = "\033[0m"

    if specialization_name:
        print(f"\n{golden}Topic - {specialization_name}:{reset_colour}")
    else:
        print(f"\n{golden}{title}:{reset_colour}")

    display_options(items, back_option=back_option)



# headings for material display
def display_material(topic_name, segment_name, material):
    orange = "\033[38;2;255;165;0m"
    reset_colour = "\033[0m"

    print(f"\n{orange}Topic:{reset_colour} {topic_name}")
    print(f"{orange}Segment:{reset_colour} {segment_name}")
    print("-" * 50)  # Line of dashes
    print(f"{material}")


# navigation functions
def navigate_course():
    red = "\033[91m"
    cyan = "\033[96m"
    reset_colour = "\033[0m"
    
    #display course name
    print(f"{red}Welcome to Applications and Foundations of Fintech by Upenn{reset_colour}")
    #loop specializations
    while True:
        display_menu("Specializations", [value['name'] for key, value in course_data.items()], back_option=False)
        specialization_index = int(input(f"{cyan}Select a specialization (1-4): {reset_colour}"))
        
        if specialization_index not in course_data:
            print("⛔️Invalid specialization index. Please try again.")
            continue

        #loop topics
        while True:
            display_menu("Topics", [value['name'] for key, value in course_data[specialization_index]['topics'].items()], specialization_name=course_data[specialization_index]['name'])
            topic_index = int(input(f"{cyan}Select a topic (1-4, 0 to go back): {reset_colour}"))

            if topic_index == 0:
                break  # Go back to selecting specializations

            if topic_index not in course_data[specialization_index]['topics']:
                print("⛔️Invalid topic index. Please try again.")
                continue

            topic_name = course_data[specialization_index]['topics'][topic_index]['name']
            #loop segments
            while True:
                segment_options = course_data[specialization_index]['topics'][topic_index]['segments']
                display_menu(f"Segments - {topic_name}", segment_options) #show respective topic
                segment_index = int(input(f"{cyan}Select a segment (1-{len(segment_options)}, 0 to go back): {reset_colour}")) #allow for dynamic index range

                if segment_index == 0:
                    break  # go back to selecting topics

                if segment_index not in range(1, len(segment_options) + 1):
                    print("⛔️Invalid segment index. Please try again.")
                    continue
                
                #retrieve segment, generate unique key from material storage
                segment_name = segment_options[segment_index - 1]
                segment_key = f"{specialization_index}-{topic_index}-{segment_index}" #Numeric navigator 1-1-1
                material = material_storage.get(segment_key, "No material available.")
                display_material(topic_name, segment_name, material)

                #Enter to return to Segments
                input(f"\n{cyan}Press Enter to return to the Segments menu...{reset_colour}")

            # Break to go back to specializations
            if topic_index == 0:
                break

# Run the navigation function
if __name__ == "__main__":
    navigate_course()

# Print the stored material after navigating through the course
print("\nStored Course Material:")
for segment_key, material in material_storage.items():
    print(f"{segment_key}: {material}")
