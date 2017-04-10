'''
train = [('I love this sandwich.', 'pos'),
('This is an amazing place!', 'pos'),
('I feel very good about these beers.', 'pos'),
('This is my best work.', 'pos'),
("What an awesome view", 'pos'),
('I do not like this restaurant', 'neg'),
('I am tired of this stuff.', 'neg'),
("I can't deal with this", 'neg'),
('He is my sworn enemy!', 'neg'),
('My boss is horrible.', 'neg'),
('France to invest euro 2 bn in India','pos'),
('India, France may soon sign deal for 60 Rafale fighter jets','pos'),
('HDFC to raise up to USD 500 million from ECB','pos'),
('Tax: Losing out on short term capital assets','neg'),
('India may fall way short of 2014-15 exports target','neg'),
('Hindustan Copper jumps over 3% on JV with Chhattisgarh govt','pos'),
('Sensex snaps 5-day rally but mid, smallcap run continues','neg'),
('Alibaba forms automotive, smart living business units','pos'),
('Harley-Davidson India now offers extended warranty on its motorcycles','pos'),
         ('Fadnavis announces closure of 12 toll plazas in Maharashtra','neg'),
         ('Transgression by China into Indian territory has reduced','pos'),
         ('Airbus supports Modi Make in India initiative','pos'),
         ('Long-term bullish on India; see recovery in Q1: Chandgothia','pos'),
         ('UP govt releases 1st instalment of compensation for farmers','pos'),
         ('HDFC Mutual Fund buys 17 lakh shares of Sanghvi Movers','pos'),
         ('Gold regains Rs 27K level on global cues','pos'),
         ('SBI cuts home loan interest rate by up to 0.25%','pos'),
         ('80% of acquired land will be used for irrigation: Gadkari','pos'),
         ('Modi Germany visit to open new avenues: Baba Kalyani','pos'),
         ('Ban on diesel vehicles: NGT stays order for two weeks','neg'),
         ('Food prices drive March CPI lower to 5.17%','neg'),
         ('Sensex ends above 29000, up 165 pts ahead of Q4 earnings','pos'),
         ('Modi invites global partnership in manufacturing sector','pos'),
         ('Gold prices up in Asia despite disappointing China trade data','neg'),
         ('March consumer inflation likely edged up for fourth month','neg'),
         ('Housing finance firm DHFL too lowered its home loan rate','pos'),
         ('Petrol up Rs 1.34 a litre, diesel by Rs 2.37','neg'),
         ('Fortis Healthcare completes 51% acquisition in Fortis Hospotel','pos'),
         ('Russia Gazprom sees new LNG deal with India Gail in 6 months','pos'),
         ('T-Hub,Uber launch program to connect startups','pos'),
         ('Den Networks to raise Rs 142 cr via preferential allotment','pos'),
         ('Rosneft entry to put pressure on giants like IOC, BPCL: Expert','neg'),
         ('Indian ADRs: Infosys slips 6%, ICICI Bank, ','neg'),
         ('Tata Motors up','pos'),
         ('Positive on chemical space: S Krishna Kumar','pos'),
         ('India, Russia seal big ticket defence deals','pos'),
         ('Gold imports drop 10.3% to $1.8 bn in September','neg'),
         ('RBI cancels certificate of registration of NBFC','neg'),
         ('Govt bans Samsung Galaxy Note 7 phones from airliners','neg'),
         ('Everything is going right for Indian economy, says KV Kamath','pos'),
         ('Scandal-hit Wells Fargo quarterly profit falls 3.7%','neg'),
         ('India loses up to $100 bn annually to corrosion: Hindustan Zinc','neg'),
         ('Coal import declines 6% to 16 million tonnes in September','neg'),
         ('Govt grants BP Plc licence to set up petrol pumps in India','pos'),
         ('Pharma cos may report subdued performance in Q2 FY17: Report','neg'),
         ('Top seven cos lose Rs 46,108 crore in market valuation','neg'),
         ('Consumer demand to rise 40% this festive season: Report','pos'),
         ('Tata Motors eyes more market share in south India in CV segment','pos'),
         ('Ford, GM lead India car export growth in H1 FY17','pos'),
         ('NIIT Tech shares tank 6.5% on Q2 profit fall','neg'),
         ('HDFC Life net profit up 12% at Rs 464 cr in Apr-Sep','pos'),
         ('See more investments into Indian oil & gas space: GE Agrawala','pos'),
         ('Mahindra & Mahindra Q2 PAT seen up 9.5% to Rs 950.2 cr: Centrum','pos'),
         ('Maruti Suzuki Q2 PAT seen up 21.8% to Rs 1810.2 cr: Centrum','pos'),
         ('Atul Auto Q2 PAT seen up 142.5% to Rs 12.1 cr: Centrum','neg'),
         ('Buy IndusInd Bank; target of Rs 1500: KR Choksey','pos'),
         ('Mercedes sees flat sales on uncertainty over diesel cars, GST','neg'),
         ('Global cues drag Sensex 144pts; RIL & HDFC Bank dip ','neg'),
         ('ICICI up 7%','pos'),
         ('Stay invested in DHFL, says Avinash Gorakshakar','pos'),
         ('India solar sector outlook positive: Report','pos'),
         ('Wall Street slips as energy, consumer stocks drag','neg'),
         ('LG eyes 30% rise in home entertainment products sale this yr','pos'),
         ('Asian stocks edge higher amid low risk appetite; oil firm','neg'),
         ('CanFin Homes net grows 56% to Rs 55 cr in Jul-Sep','pos'),
         ('Niti Aayog moots independent regulators for steel, mines sector','pos'),
         ('Govt approves Rs 234 cr project for ferry services in Gujarat','pos'),
         ('India may sign pact with Nigeria to invest in oil, gas sector','pos'),
         ('Tata AIA Life launches three new products','pos'),
         ('Shriram EPC surges 14% on Rs 61 crore order win','pos'),
         ('No loss to customers from cyber attack: Axis Bank','pos'),
         ('Tata Coffee Q2 net profit up 62% at Rs 44.65 cr','pos'),
         ('KPIT Q2 net dips 23.8% to Rs 56.1 cr','neg'),
         ('Tata Coffee Q2 net profit up 62% at Rs 44.65 cr','pos'),
         ('Bayer CropScience Q2 net profit sees marginal rise at Rs 159cr','pos'),
         ('Greenlam Industries Q2 net profit down 2.7% at Rs 8.97 cr','neg'),
         ('RBL Bank Q2 profit jumps 34% to Rs 90 cr on robust biz growth','pos'),
         ('Monsoon ends this week, record food output likely','pos'),
         ('Tata Steel bags sustainable manufacturing award','pos'),
         ('Hindustan Zinc Q2 net declines 15% to Rs 1,901.87 cr','neg'),
         ('Lupin Q2 PAT seen down 28.6% to Rs 630 cr: Centrum','neg'),
         ('Granules India Q2 PAT seen up 34% to Rs 52.2 cr: Centrum','pos'),
         ('Titan ties up with Swiss watch maker Raymond Weil','pos'),
         ('Rooftop solar power capacity crosses 1 GW mark: Report','pos'),
         ('Buy Hindustan Zinc, Voltas: Sandeep Wagle','pos'),
         ('Gold marginally down in futures trade on global cues','neg'),
         ('Hindustan Zinc Q2 profit seen down 35%, volumes may be lower','neg'),
         ('India can play major role to strengthen global economy: PM Modi','pos'),
         ('Sensex, Nifty flat; BHEL climbs 4%, ICICI & ITC laggards','pos'),
         ('Payments banks struggle to take off; Cos lack solid biz plans','neg'),
         ('SIDBI launches Rs 60 cr corpus ASPIRE fund','pos'),
         ('US sees much potential for increase in trade with India','pos'),
         ('RBI releases framework for penalising on payment issues','neg'),
         ('RBI permits 100% FDI in more financial services','pos'),
         ('RIL blockbuster numbers to continue into H2; stock to gain: Pros','pos'),
         ('HCL Tech Q2 net may drop 3.5%, margins seen lower by 100 bps','neg'),
         ('Discom losses to halve by FY19 on reforms, says Crisil','neg'),
         ('Exit Mindtree, says Rajat Bose','neg'),
         ('Sell United Breweries, Tata Motors','neg'),
         ('Expect 40% revenue growth in FY17 & FY18: Cosyn','pos'),
         ('India mfg sector in trouble, needs to take on China: Geete','neg'),
         ('Rupee opens lower at 66.68 per dollar','neg'),
         ('IT penetration very low in India: Microsoft India','neg'),
         ('Mindtree Q2 net slides 37% to Rs 95 cr','neg'),
         ('Jio unlikely to gain 2% revenue market share in 2017: Fitch','neg'),
         ('Avoid ACC as Q3 too disappointing, stock to decline: Experts','neg'),
         ('Sensex, Nifty end lower amid volatility; metals weak,Wipro up 1%','neg'),
         ('Sell ACC, Asian Paints: Sandeep Wagle','neg'),
         ('Nifty holds 8650 amid pressure, Sensex loses over 100 pts','neg'),
         ('CBI registers FIR against UK-based arms dealer in Embraer deal','neg'),
         ('Rupee falls further, opens 8 paise lower at 66.89 per dollar','neg'),
         ('FCNR redemptions to keep rupee under pressure: Raina','neg'),
         ('Verizon revenue drops as subscriber additions disappoint','neg'),
         ('Wall Street dips as telecoms slump; AmEx surges','neg'),
         ('Ramdev says was denied US visa','neg'),
         ('CBI raids residences of top FACT officials, including CMD','neg'),
         ('Bharti Infra Q2 profit seen down 9%, tenancy growth may be muted','neg'),
         ('Sunil Capital & Securities sells 3 lakh shares of E-Land Apparel','neg'),
         ('Persistent Q2 profit seen down 8%, dollar revenue may grow 3%','neg'),
         ('Foreign funded group wants to stop Adani project in Aus:Report','neg'),
         ('PE investments decline 53% to $2.5 bn in Sep qtr: Report','neg'),
         ('COAI dismayed over fine on telcos, takes hands-off approach','neg'),
         ('Idea net plunges to a trickle on Jio, spectrum impacts','neg'),
         ('IDBI Bank unions threaten strike over wage revision','neg'),
         ('Petcoke penchant lands Rs 3,800 cr punch on coal miners: Crisil','pos'),
         ('Idea, Airtel down up to 4% as TRAI asks DoT to impose fine','neg'),
         ('Mahindra launches new platform for vehicle auction','pos'),
         ('Gold go down','neg')





         ]
         '''

train = [('Wipro Joins LoRa Alliance to Accelerate IoT Deployments','pos'),
 ('IT services firm stocks dip after government suspends fast tech visas','neg'),
 ('Wipro Recognized as Best in Class Technology Provider for 2017 by Consumer Goods Technology Readers','pos'),
 ('Wipro Positioned as a Leader in Gartner Magic Quadrant for SAP Application Services, EMEA','pos'),
 ('Wipro Positioned in Winner Circle of HfS Blueprint Report on Product Lifecycle Management Services','pos'),
 ('Wipro new IoT-based solution to power wind parks','pos'),
 ('Trump Immigration Plans Still Major Headwind For India IT Outsourcers','neg'),
 ('Wipro Builds Industry-Focused Big Data Analytics-as-a-Service Platform on IBM Bluemix','pos'),
 ('Wipro Rated as a Top Digital Service Provider in Retail by Zinnov','pos'),
 ('Wipro Partners with and Invests in Tradeshift to Increase Digitalization and Automation across Source-to-Pay Processes','pos')





 ]


from nltk.tokenize import word_tokenize # or use some other tokenizer
all_words = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in train]

#importing the csv file containing the testing sentences

f1=open("F:\FinanceProject\code\NewsAnalytics/WIPRO.NS.csv",'rb')
nega=0
posi=0

import nltk
classifier = nltk.NaiveBayesClassifier.train(t)
classifier.show_most_informative_features()
test_sentence = "HDFC Bank (HDB) Earnings Up Y/Y in Q4, Stock Rises 1%"
test_sent_features = {word.lower(): (word in word_tokenize(test_sentence.lower())) for word in all_words}
print("The sentiment of the sentence is "+classifier.classify(test_sent_features))


for line in f1.readlines():

    test_sent_features = {word.lower(): (word in word_tokenize(line.lower())) for word in all_words}
    print line, classifier.classify(test_sent_features)
    if (classifier.classify(test_sent_features)) == 'neg':
        nega=nega+1
    if (classifier.classify(test_sent_features)) == 'pos':
        posi=posi+1





print "No. of negative=",nega
print "No. of positive=", posi
total = nega + posi
print "Total",total
