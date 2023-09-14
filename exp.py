
import csv

final = """1. "Mary, witnessed your proactive approach towards modernizing verification at DHS; how about embracing another for your employees’ meals at Okendo?"
2. "Viviana, streamline corporate wellness with our meal boxes at Latin American Agribusiness Development Corporation."
3. "Celebrating 10 years at haku, Samary? Let’s make it memorable with our Indian cuisine."
4. "Jennifer, unbox a world of flavor at itopia with our corporate meal boxes."
5. "Yani, enhance your office atmosphere at OpenStore with our authentic Indian Cuisine.”
6. "Tatiana, join us in forging flavorsome bonds at Vozzcom with our Indian meal boxes."
7. "Eda, let’s celebrate HackerOne's success and the launch of SAS with our Indian meal boxes."
8. "Lenore, make mealtimes memorable at Blue Stream Fiber with our vibrant Indian cuisine."
9. "Tatiana, bring the warmth of Indian spices to Corporate HR at Faraway with our meal boxes."
10. "Yor, congratulate Nate at Arctic Industries on his new role with a touch of Indian flavor."
11. "Utkirbek, let's celebrate Jafton's success in app development with a savory Indian feast." 
12. "Spice up your office meals, Kayla, just as you do at EdgeUno."
13. "Krystal, add a creative mix to your team at Paper Street Media with our flavorful Indian cuisine."
14. "Lucie, let the VeEX team savor the fine elements of Indian cuisine with our meals."
15. "Liah, experiment with taste beyond technology at Wide Cloud Communications with us."
16. "Nallely, reward the FlexOffers team's dedication with our aromatic Indian meal boxes."
17. "Zulie, give your work family at DigitalEra Group a Lunchbox full of love from India."
18. "Damaris, boost morale at Backpack with culinary delights from our kitchen."
19. "Maggie, experience the joy of designer food at ComRes with our diverse Indian meal boxes."
20. "Bruno, let our curated meal boxes complement your human resource management expertise at Phygtl."
21. "Luisa, bring the zest of Indian cuisine to Adistec’s offices for a change."
22. "Camila, let's celebrate Walmart's tech evolution at Teikametrics over Indian cuisine."
23. "Saya, add a dash of spiciness to OpenSea with our Indian meal boxes."
24. "Matthew, join us in discovering the taste of unity at OpenStore via our Indian meals."
25. "Angie, let's nourish your team at Stash with our flavorful Indian meal boxes."
26. "Stephanie, provide a culinary break to your Flex team with our Indian cuisine."
27. "Catherine, celebrate Bucket Listers’ inclusion in 2023 Inc. 5000 with our meal boxes."
28. "Karla, transform office meals at Nextech Systems with our savory Indian dishes."
29. "Victoria, explore Indian culinary arts at OpenStore with our meal box service."
30. "Yaddyra, fuel your creative writing at Florida International University with our flavorful Indian meals."
31. "Jill, spice up calculations at Metabase with our diverse Indian cuisine."
32. "Hayley, explore Indian flavors at Getaround for your next team outing."
33. "Diego, enjoy our Indian meal boxes designed with precision like your HR strategy at Deal Engine."
34. "Alejandro, take a break from Blockchain.com’s digital world with our Indian delights."
35. "LauraLee, bring cultural diversity to Novo with our Indian meal boxes."
36. "Adrian, treat your team at Arionkoder with our tasty Indian meal box delights."
37. "Philippe, enjoy the harmony of diverse Indian flavors at Aptum as you promote workplace harmony."
38. "Mary, leverage the art of Indian culinary expertise at Codelitt."
39. "Lilya, reward Calculator’s performance at Careerist with our Indian meal box service."
40. "Luisana, turn lunchtime at haku into another moment of pure enjoyment with our Indian meal boxes."
41. "Gabriela, introduce your team at Accelirate Inc. to Indian culinary delights."
42. "Joy, let's bring some Indian warmth to your upcoming trip at Connex One."
43. "Hila, let Cyolo's HR team explore the diversity of Indian flavors with our meal boxes."
44. "Ashton, introduce Indian culinary wisdom to your HR initiatives at Capital Analytics."
45. "Eber, serve your team at SMX Services & Consulting with our delicious Indian meal boxes."
46. "Dolores, celebrate Carina Edwards' new role at Kipu Health with our Indian delicacies."
47. "Erika, discover a perfect blend of spices in our meal boxes just like your team at Intellitech."
48. "Christina, a delightful box of Indian cuisine to brighten up your day at Ortega Construction."
49. "Gabriela, let's introduce DACAS to our delightful Indian meal boxes."
50. "Federico, get ready to relish the finest Indian flavors with our meal boxes at GroupM."
51. "Maria, take your colleagues at Sealance on a flavorful Indian culinary journey."
52. "Rebeca, celebrate your Magna Cum Laude status with exciting Indian flavors at HD House LLC."
53. "Ivette, give your team at Picsart a taste of our vibrant Indian cuisine."
54. "Sandra, add an Indian touch to your office meals at Foundever."
55. "Sanny, savor the taste of our unique Indian meal boxes at America On Tech."
56. "Yvette, inspire your team at Millicom (Tigo) with our delicious Indian meal boxes."
57. "Amanda, resolve conflicts over a fulfilling Indian meal box at FICO."
58. "Silvia, connect the Sonnedix team with Indian culture through our meal boxes."
59. "Ken, enjoy our meal boxes at eMed Digital Healthcare, crafted with the same precision as your MBA expertise."
60. "Allison, nourish your team at Datadog with our refreshing Indian meal boxes."
61. "Jessica, welcome your new joiners at OpenStore with our delightful Indian meal boxes."
62. "Nargiza, enhance team spirit at Pipe with our unique and flavorful Indian meal boxes."
63. "Lin, commemorate your whirlwind trip to Orlando at Wizeline with our warm Indian meal boxes."
64. "Yadira, reward your team at ACI Worldwide with our tempting Indian meal boxes."
65. "Joel, spice up your meetings at Kaseya with our exciting Indian meal boxes."

66. "Empathy and curiosity are no soft skills, Sheena! Power up your team at Amplitude with our authentic Indian meals to spark compassionate conversations."
67. "Hi Marcela at Atlas Renewable Energy, our Indian cuisine will fuel your people and communications with the delicacy of spices."
68. "Hey Caroline! Add a little spice to your HR coordination at Kaseya with our Indian meal boxes."
69. "Hi Teobaldo, let's communicate the language of Indian cuisine together to your team at Factorial."
70. "Hey Dana! Add a little 'environmental-friendly' Indian cuisine to Decon Environmental's HR menu."
71. "Hi Glenda, ready to spice up the general HR tasks at OJO with our Indian meal boxes?"
72. "Hello Zsolt! At PairSoft, adding our Indian meal boxes might just be your next best HR strategy!"
73. "Hi Sabela, let's take customer success at Factorial to the next level with our mouth-watering Indian cuisine"
74. "Hi Shawn! Excited to add a dash of Indian spice to the HR functions at Red Violet Inc."
75. "Hey Ana, imagine Intelepeer's leadership relishing our authentic Indian meal boxes. Ready to spice things up?"
76. "Hi Karen, we're as thrilled to provide our Indian meal boxes to the team at Udemy as you are in welcoming your new CPO."
77. "Hello Alyssa, Inceptra deserves a CATIA consultant and your team deserves our top-notch Indian meal boxes!"
78. "Hi Macarena, our Indian meal boxes are exactly what your LATAM HR team at Provenir needs."
79. "Hello Lourdes, bring the spice of India to Black Dragon Capital with our delicious corporate meal boxes."
80. "Vivian, allow us to honor the HR team at Honorlock with our delectable home-like Indian meals."
81. "Hi Renee, at Project44, your people are your project. So let's perfect it with our Indian meal boxes."
82. "Hi Scott, let's bring some Indian flavor to the HR desk at DeliverLogic."
83. "Hello Marcelo, spice up HR discussions at Crawford and Company with our delectable Indian cuisine."
84. "Hi Ngoc! Add a dash of Indian variety to Anju Software's HR conversations."
85. "Hey Kelli-Anne! Let's add a spicy Indian twist to the HR management at GreenLight.ai."
86. "Hi Orlando, whether it's sports or food, variety matters. Let's bring that variety to Fanatics with our Indian meals."
87. "Hello Tarrah, at It's Just Lunch, enjoy actual lunch with our Indian meal boxes."
88. "Hi Vivian, our Indian meal boxes are worth the discovery at Veeva Systems."
89. "Hey Paula! Let's give Awesome Motive to your HR team with our delicious Indian cuisine."
90. "Hello Kristin! Finance is serious. But lunch? Let's spice that up with our Indian meal boxes at Corellium."
91. "Hi Melissa, adding bloom with our Indian cuisine at Bloom Growth sounds like a delightful plan!"
92. "Hello Shanikwa, let's add some Indian spices to your HR discussions at Axela Technologies."
93. "Hi Alyson! UKG stands for Ultimate Kronos Group, but let it also stand for Ultimate Kitchen Gourmet with our Indian meal boxes."
94. "Hello Rhonda, no words needed when our Indian meal boxes can speak volumes at SPACE GROUND SYSTEM SOLUTIONS, INC."
95. "Hi Nicole! Looking for a spicy twist for Financeit's HR? Our Indian cuisine has just the right mixture."
96. "Hello Cynthia, let's talk AI and Indian food at the Partnership on AI."
97. "Hey Jessica, ready for a logical return to authentic food? Try our Indian meal boxes at ReturnLogic."
98. "Hello Pascale, spice up your HR communications at Allvue Systems with our delightful Indian cuisine."
99. "Hi Victor, get your sales rolling at US Army with the exotic flavors of our Indian meal boxes."
100. "Hello Lisa, Let's replace the hassles of billing and coding at Element Medical Billing with our delightful Indian meal boxes."
101. "Hi Neil, smarter commerce deserves smarter food choices. Try our Indian meal boxes at SmarterCommerce."
102. "Hey Shannon, add a 'GTG' rating to your HR platter at GTG Networks with our Indian meal boxes."
103. "Hello Andrea, let's replace 'not found' with 'found the best' - namely, our Indian meal boxes."
104. "Hi Foster, Unjected is the wellness company and our Indian meal boxes offer the wellness of authentic Indian food."
105. "Hello Solamon, let's grow together with Creceras and our Indian cuisine for an ideal culinary experience."
106. "Hi Gabriela, while you're providing psychological support at Ecomfy Lead, let us provide culinary support with our Indian meal boxes."
107. "Hello Nina, let's enhance your marketing strategies at Regie.ai with the exciting flavors of our Indian Meals."
108. "Hi Scott, we thought you might appreciate the instruction manual for our Indian meal boxes at Regie.ai."
109. "Hello Cara, from fashion designing at Prescient AI to taste designing, our Indian meal boxes are surely a hit."
110. "Hey Jim, let’s inspire your business development operations at Ispire with our flavorful Indian meal boxes."

111. "Hi David, Speed up your sales with our speedy Indian meal deliveries at Ookla."
112. "Hello Danny, elevate your sales at Metadata with the intriguing flavors of our Indian meal boxes."
113. "Hi Asher, get a taste of Indian culture while managing HR at LaCalle Group."
114. "Hey Justin, get ready to divert the business development at HUMAN towards our Indian meal boxes."
115. "Hello Laura, think our Indian meal boxes can lighten up your remote meetings at Userlytics?"
116. "Hey Anna, add a flavorful investment to your wealthtech roundtable at CapIntel with our Indian meal boxes."
117. "Hi Herber, align your IT goals at Simera with our scrumptious Indian meal boxes."
118. "Hello Lisa, insert a delectable drive to Pure Storage HR with our mouth-watering Indian meals."
119. "Hi Trinity, ready to treasure the Indian culinary gems with UserGems?"
120. "Hello Travers, looking to modernize your menu at Thought Machine? Our Indian meal boxes could be the solution."
121. "Hey Chris, add our trending Indian meal boxes to your next meeting at Ispire."
122. "Hi Victor, enhance your business development operations at EdgeUno with the flavors of our Indian cuisine."
123. "Hello Daniel, let's innovate your sales strategy at CIENCE with an exotic Indian rising."
124. "Hey Alexey, ready to add some Indian techno-flavor to your network labs at Mercury Development, LLC?"
125. "Hello Lara, keen to make Teal's operations more delicious with our Indian meal boxes?"
126. "Hi Thorsten, let our Indian meal boxes be the saving byte of your group development at 1NCE."
127. "Hello William, let’s add a spicy touch to your business development operations with our authentic Indian meal boxes at Manusis4."
128. "Hey Lourenco, spice up the All-Optical Industry Summit 2023 with the exquisite flavors of our Indian cuisine."
129. "Hi Michael, let Ethereum team enjoy the ethereal flavors of our Indian meal boxes."
130. "Hello Younes, excited to redefine IoT connectivity with the exotic flavors of our Indian cuisine at 1NCE."
131. "Hi Sabine, missing the spices in your marketing endeavors at 1NCE? Our Indian meal boxes are here to rescue!"
132. Hello Lakshmi, Just like you master organizational politics at Metadata, we master recipes at our Indian restaurant in Miami. Experience our corporate meal boxes and boost collaboration over a sumptuous meal!
133. Hi Andrey, At FinConecta you optimize systems and we optimize flavors. How about experiencing our Indian delicacies made for tech gurus?
134. Greetings Christian, We've seen your proficiency with Lean Six Sigma at Fiplex! Our approach to Indian cuisine mirrors your efficiency - precise, optimized, and delicious.
135. Sunita, just as you head Human Resources at IT Convergence, we head the kitchen with zeal and expertise. Taste the leadership in our Indian corporate meal boxes!
136. Greetings, Melanie, like you, we at our restaurant know the importance of good management. Let us pitch in with our well-managed Indian corporate meal boxes for Canela Media!
137. Roshni, while you're shaping Allvue Systems in India, consider bringing a taste of India to Miami with our corporate meal boxes. 
138. Hello Karyn, we'd love to share our mastery in Indian cuisine, just like your mastery in HR at Thought Machine. Excited to serve you our flavorful corporate meal boxes!
139. Olivier, like you strategize at CAST AI, we strategize perfect meals for our valued patrons. Allow us to plan your next corporate meal!
140. Hi Jason! As you recently discovered while reading the HR Masterclass at Pure Storage, great things come to those venture out. Venture into Indian food with us?
141. Alison, at Square, you understand the importance of international relations. We deliver internationally-renowned Indian cuisine right to your office!
142. Hey Shri, it's time to develop India's most loved recipes here at NewPage Solutions. Our corporate meal boxes will redefine your lunch time.
143. Matt, we took a page out of your book and found the essential ‘One to One’ in our Indian cuisine. Let’s explore this together through our corporate meal boxes for Shaped?
144. Hola Tomás, you run global operations at Entravision, we would like to run a great global cuisine experience for you. Let's start with our Indian corporate meal boxes.
145. Gabby, like a good HR strategy, our menu at HUMAN is diverse, enriching, and unique. We'd love to cater for your team.
146. Hi Kori, let us bring a taste of India to Placer.ai. We promise an explosion of flavors that you'll adore!
147. Hi Steve, to complement your wide-ranging focus at Placer.ai, our corporate meal box offers a range of flavors that span the length and breadth of India.
148. Hola María, you organize data at Infobae. We curate flavors at our restaurant. Let's orchestrate a corporate feast for your team!
149. Hi Jeff, Managing is a skill, just like good cooking. Let's swap expertise over Indian corporate meal boxes for Valenta. 
150. Decker, Congratulations on your recent success at Backpack. Celebrate this achievement with our Indian corporate meal boxes!
151. Hi Brenna, Like your pulse on global HR at ORBCOMM, we have a pulse on global Indian flavors. Ready to give them a try?
152. Hi Beckett, don't cringe over misused SEO, relish our well-used spices in our Indian corporate meal boxes for Wrk. 
153. Louis, at HUBX you deliver seamless management solutions. We deliver seamless flavors from Indian cuisine right to your desk!
154. Aaron, while you manage operations at Healthcare.com, let us manage your lunch with our Indian corporate meal boxes.
155. Zahra, let us be a beneficial part of Vimeo's employee perks with our delightful Indian corporate meal boxes.
156. Hi Bill, it can be hard to manage systems at ACAMS, but it's easy to enjoy good food. Try our Indian corporate meal boxes to simplify things!
157. Olivier, you aim for a prosperous future at Extend, we aim for satisfied customers. Experience the prosperity of Indian flavors!
158. Janice, let us add some delectable flavors to your taxing role at MainStreet - one bite at a time.
159. Santiago, our Indian cuisine is as innovative as the entrepreneurial solutions at Ontop. Let's mix business with food, shall we?
160. Hi Will, we have a great pitch for you at PerformYard. Have you tried our irresistible Indian corporate meal boxes?
161. Hi Justin, following the trend of teams/leagues at Misfits Gaming Group, we encourage you to try our winning team of Indian dishes.
162. Hey Rachel, your strategic analysis at Callsign inspires us. Let us inspire you back with our strategic selection of Indian delicacies.
163. Hi Cathy, join us for a delicious discussion over our Indian corporate meal boxes at Ncontracts.
164. Karee, let us bring diversity to your lunch hour at Semper Laser just the way you diversify operations and sales!
165. Hi Erwin, managing daily operations must be exhausting at Inktel! Refuel with our Indian corporate meal boxes - packed with flavor and freshness!
166. Daniel, leading HR at Samsung calls for a prudent mind and a satisfied tummy. Let us cater to the latter one with our corporate meal boxes.
167. Hi Efrat, you added a new role at Nexar Inc, we add new Indian flavors in every meal box. Let's exchange notes?
168. Kevin, our flavors at TiVo are as unique as your sales strategies. Don't believe us? Try our corporate meal boxes!
169. Pritish, we code our recipes with as much precision as you code software at Pipe. Enjoy a coded meal with us?
170. Layla, enjoy a taste of India's vibrant culture through your palate, all from the comfort of your office at Pure Storage. Does that sound exciting?
171. Hola Daniela! At Torre, you design products; we design flavors. Enhance your artistic eye with a taste of our Indian corporate meal boxes.
172. Heather, we too believe in loyalty like your mom, we're loyal to our traditional Indian culinary practices. Experience loyalty in our corporate meal boxes at Nearpod!
173. Michael, boosting sales at Sure requires energy, let us fuel you with our authentic Indian meal boxes!
174. Hi Michael, need to strategize your meals for your Global Team Project at When I Work? We'll take care of it!
175. Hey Alice, allow us to be the perfect HR partner to your taste buds - serving a taste of India's rich food heritage at Checkout.com!
176. Hi Rauf, lead your team to taste victory with our Indian corporate meal boxes at CareScout.
177. Ezgi, we understand how HR works according to your post at Freshworks! Support your HR events with our tantalizing corporate meal boxes. 
178. Monica, the team at Westminster Christian School is doing a wonderful job. Reward them with a delicious Indian meal box prepared by us.
179. Nick, like sharing admiration for a colleague's journey, sharing our Indian corporate meal boxes with your team at PulsePoint will be equally splendid!
180. Hi Elyse, big news awaits Aleph Group, Inc. Celebrate with our big flavors in our Indian corporate meal boxes!
181. Hi Anthon, we share your passion for business at Belong. Let's fuel our ambitions together with our Indian corporate meal boxes!
182. Giacomo, engineering operations at Inktel Contact Center Solutions must be a challenging task! Energize with our Indian meal boxes.
183. Sonia, recharge your HR strategy at Lennar with a savoury spice up from our Indian cuisine!
184. Hola Ivan, let's infuse some Indian flavors into your sales strategy at Crystal Lagoons. Ready to explore?
185. Hi Asaf, bid adieu to boring meals and say hello to our authentic Indian meal boxes at Promon.
186. James, aren't big opportunities exciting? Try our Indian corporate meal box and experience the thrill of flavors at Crunchtime!
187. Hi Todd, implementing strategies at PayCargo builds up an appetite. Take a break with our Indian corporate meal boxes, you've earned it!
188. Michelle, at Chief you've been a leader. Allow us to lead the flavor revolution in your meals with our Indian corporate meal boxes.
189. Hi Jim! Being a technology officer, you appreciate good systems. Our Indian recipes have been systematically delicious for years!
190. Hi Ryan, as CCO at Starship Technologies, you're always flying high. Let us elevate your culinary experiences as well with our corporate meal boxes!
191. Hey Mark, at Funday co-founder work must be fun. Spice up your fun quotient with our delightful Indian meal boxes!
192. Hi James, Axonius is a sample vendor at the Gartner Hype Cycle, we're a sample of Indian authenticity delivered to your office!
193. Ahmed, you've got an eye for detail at Kira Floorings. Catch a glance of Indian culinary finesse in our corporate meal boxes!
194. Hello Ariel, add a tasteful experience to your long list of accomplishments at CareScout with our Indian corporate meal boxes!
195. Sergio, your innovation at Kiwibot keeps the world moving. Our innovative Indian recipes inspire us to deliver amazing meals!
196. Hi Henry, The CEO of his own name deserves a meal fit for a king. Enjoy a royal Indian feast with us!
197. Hi Tim, as Director at Nybble Group, your oversight is impeccable. Enjoy our Indian meal boxes with equal discernment!
198. Hi Jennifer, our restaurant is just like a successful subway - always delivering on time. Try our Indian corporate meal boxes!
199. Hola Tomas, at Workana, you create workspaces. Let's create a lunchtime experience with our corporate meal boxes!
"""

# Split the variable into individual lines
lines = final.strip().split('\n')

# Remove the numbering at the beginning of each sentence
one_liners = [line.split(". ", 1)[1] for line in lines]
print(len(one_liners))
# Load the existing CSV file into a list of dictionaries
csv_file_path = 'One-liner details ( Tech Companies) - Sheet1.csv'
existing_data = []

with open(csv_file_path, mode='r', encoding='utf-8-sig', errors='replace') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        existing_data.append(row)


print(existing_data)
# Add the new "One Liners" to the existing data
for i, row in enumerate(existing_data):
    row['One Liners'] = one_liners[i]

# Write the updated data back to the CSV file
with open(csv_file_path, mode='w', newline='', encoding='utf-8-sig', errors='replace') as csv_file:
    fieldnames = existing_data[0].keys()
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    csv_writer.writeheader()
    csv_writer.writerows(existing_data)

print(f"The new 'One Liners' have been added to the existing CSV file '{csv_file_path}'.")