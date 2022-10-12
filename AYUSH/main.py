import discord
from matplotlib.pyplot import eventplot

client = discord.Client()

@client.event
async def on_ready():
    a=client.get_channel(1029621300261572621)
    g=["Namaskar🙏🙏","Namaste🙏🙏","Hello✋","Hi🖐🖐","What's Up 🤘🤘"]
    import random
    
    a_e = discord.Embed(title="Introduction", description=random.choice(g)+"\nThis is Ayush-Bot" , color=0x233067)
    a_e.add_field(name="About Me", value="I am designed to interact with the users on discord and tell them about health related stuffs.")
    a_e.add_field(name="My Motto", value="Everybody should be safe and healthy even in the toughest situations")
    a_e.add_field(name="My advice",value="You can take advices related to health from me but you should consult a doctor also")
    a_e.add_field(name="__________________________________________",value='''Try typing:
    1.Type "AYUSH" for knowing about AYUSH\n
    2.Type "A" for knowing about Ayurveda\n
    3.Type "Y" for knowing about Yoga\n
    4.Type "U" for knowing about Unani\n
    5.Type "S" for knowing about Siddha\n
    6.Type "H" for knowing about Homeopathy\n 
    7.Type "R" for Remedies for commom health issues.\n
     ''')
    a_e.set_footer(text="""Stay Safe and Stay Tuned\n
            Regards, Ayush Bot😀""")
    await a.send(embed=a_e)

@client.event
async def on_disconnect():
    c=client.get_channel(1029621300261572621)
    await c.send('''The greatest wealth is health , So take care and \n
    Good Bye\n        
    (●'◡'●)  ''')

@client.event
async def on_message(message):
    if message.content == 'A':
        b = client.get_channel(1029621300261572621)
        b_e = discord.Embed(title = "Ayurveda" , descripition = "Ayurveda is attributed to Dhanvantari, the physician to the gods in Hindu mythology, who received it from Brahma", color=0x00ff00)
        b_e.add_field(name="Origin of Ayurveda",value="Ayurveda is attributed to Dhanvantari, the physician to the gods in Hindu mythology, who received it from Brahma")
        b_e.add_field(name="Benefits of Ayurveda", value="Ayurveda looks at your body as a whole")
        b_e.add_field(name="___________" ,value="It cures the root of the problem not the symptoms alone.")
        b_e.set_footer(text="Regards, Ayush Bot😃")
        await b.send(embed =b_e)
        await b.send(file=discord.File('AYUR.jpg'))

    elif message.content== "version":
        b=client.get_channel(1029621300261572621)
        b_e = discord.Embed(title = "Version" , descripition = "This is Version 2.0 of Ayush Bot", color=0xff0000)
        b_e.add_field(name="Version", value="This is Version 2.0 of Ayush Bot")
        b_e.set_footer(text="Regards, Team Ayush Bot😃")
        await b.send(embed =b_e)

    elif message.content== "Y":
        b=client.get_channel(1029621300261572621)
        b_e = discord.Embed(title = "Yoga" , descripition = "The word Yoga means ‘unity’ or ‘oneness’.", color=0xff0000)
        b_e.add_field(name="Benefits of Yoga", value='''
        In practical level yoga is to integrate body
        mind and spirit to unfold our higher potential
        in life through the practice of asana, pranayama
        and meditation.\n
        ''')
        b_e.set_footer(text="Regards, Ayush Bot😃")
        await b.send(embed =b_e)
        await b.send(file=discord.File('YOGA.jpg'))

    elif message.content =="AYUSH":
        b=client.get_channel(1029621300261572621)
        b_e = discord.Embed(title = "AYUSH" , descripition = "AYUSH stands for Ayurveda, Yoga & Naturopathy, Unani, Siddha and Homeopathy.", color=0x0000ff)
        b_e.add_field(name="Role of AYUSH", value='''
        AYUSH is the acronym of the medical systems that are being practiced in India.
        these systems are based on definite medical philosophies and represent a way of healthy living with established concepts on prevention of diseases and promotion of health.
        ''')
        b_e.set_footer(text="Regards, Ayush Bot😃")
        await b.send(embed = b_e)
        await b.send(file = discord.File("AYUSH_1.png"))

    elif message.content =="U":
        b=client.get_channel(1029621300261572621)
        b_e = discord.Embed(title = "Unani" , descripition = "Unani or Yunani medicine is Perso-Arabic traditional medicine as practiced in Muslim culture in South Asia and modern day Central Asia. Unani medicine is pseudoscientific. ", color=0xffff00)
        b_e.add_field(name="Role of Unani", value='''
        Unani system of medicine is a great healing art as well as science. It treats a person as a whole not as a group of individual parts. It is aimed at treating body, mind and soul. This system is based on hippocratic theory of four 
        humors viz. blood, phlegm, yellow bile and black bile
        ''')
        b_e.set_footer(text="Regards, Ayush Bot😃")
        await b.send(embed = b_e)
        await b.send(file = discord.File("UNANI.jpg"))

    elif message.content =="S":
        b=client.get_channel(1029621300261572621)
        b_e = discord.Embed(title = "Siddha" , descripition = "Siddha medicine is a traditional medicine originating in South India. It is one of the oldest systems of medicine in India. ", color=0xffc0cb)
        b_e.add_field(name="Role of Siddha", value='''
        The word Siddha means established truth. The persons who were associated with establishing such a Siddha school of thought were known as Siddhars. They recorded their mystic findings in medicine, yoga, and astrology in Tamil. Fundamental
         Principles of Siddha include theories of Five Elements (Aimpootham), and Three Forces/Faults (Mukkuttram). The Eight Methods of Examination (Envakai Thervukal) is used to determine diagnosis, etiology, treatment and prognosis. 
        ''')
        b_e.set_footer(text="Regards, Ayush Bot😃")
        await b.send(embed = b_e)
        await b.send(file = discord.File("SIDDHA.jpg"))

    elif message.content =="H":
        b=client.get_channel(1029621300261572621)
        b_e = discord.Embed(title = "Homeopathy" , descripition = "Homeopathy or homoeopathy is a pseudoscientific system of alternative medicine. It was conceived in 1796 by the German physician Samuel Hahnemann ", color=0x00ffff)
        b_e.add_field(name="Role of Homeopathy", value='''
        Homeopathy is an alternative medicine based on the theory of treating 'like with like'. Homeopathy claims to stimulate healing responses to diseases by administering substances that mimic the symptoms of those diseases in healthy people.
        The effectiveness of homeopathic preparations is disputed within medical science.
        ''')
        b_e.set_footer(text="Regards, Ayush Bot😃")
        await b.send(embed = b_e)
        await b.send(file = discord.File("HOMO.jpg"))

    elif message.content =="R":
        b=client.get_channel(1029621300261572621)
        b_e = discord.Embed(title = "Remedies for Common Health Issues" , descripition = "You can follow them in case of basic health diseases,but supervised consultation is strictly adviced.", color=0x00ffff)
        b_e.add_field(name="Type :", value='''
        1.Type "1" for Injury
        2.Type "2" for Immunization
        3.Type "3" for Tooth Ache
        4.Type "4" for Head Ache
        5.Type "5" for Fever{Normal Fever}
        6.Type "6" for Stomach Ache
        7.Type "7" for Cough & Cold
        8.Type "8" for Blood Pressure
        ''')
        b_e.set_footer(text="Regards, Ayush Bot😃")
        await b.send(embed = b_e)
        await b.send(file = discord.File("AYU-MED.jpg"))
        #Remedies 
        @client.event
        async def on_message(message):
            if message.content == "1":
                A = client.get_channel(1029621300261572621)
                A_e = discord.Embed(title="Injury",color=0xffa500)
                A_e.add_field(name="Turmeric", value='''
                It's an inlammatory agent, taken internal and often applied external to reduce swelling. \n
                Directions to use:\n
	            You can take with a glass of milk if any internal injury especially for bones and apply it externally mixing along with oil.
                ''')
                A_e.add_field(name="Ginger", value='''
                It's also a strong anti-inflammatory benefints. It is effective pain reliever for human muscle pain resulting from 	an exercise-induced injury.\n
                Direction for use:\n
	            Ingest two grams of either raw ginger or heated ginge experienced reduced pain and inflammation.
                ''')
                await A.send(embed =A_e)
                await A.send(file = discord.File("TG.jpg"))
            elif message.content =="2":
                B = client.get_channel(1029621300261572621)
                B_e = discord.Embed(title="Immunization", color=0xaef359)
                B_e.add_field(name="Tulsi & Pippali",value="Start the day with Tulsi, Pippali (fruit of long pepper) and ginger tea to strengthen and cleanse the upper respiratory tract.")
                B_e.add_field(name="Amla",value="Take 15 ml of Amla juice daily.")
                B_e.add_field(name="Turmeric and Black pepper ", value="Use turmeric and black pepper in the meals daily, to boost immunity and reduce ama (toxins).")
                await B.send(embed = B_e)
                await B.send(file = discord.File("TC.jpg"))
            elif message.content =="3":
                C = client.get_channel(1029621300261572621)
                C_e = discord.Embed(title = "Tooth Ache", color=0xffffff)
                C_e.add_field(name="Remedy:",value="Ginger and cayenne pepper when 	mixed together work magic on toothaches")
                C_e.add_field(name="Method:", value='''
                Take half a teaspoon of ginger paste and mix with equal amounts of cayenne pepper \n
	            Mix two to three drops of olive oil in 	it and apply the mix on the affected tooth area\n
	            Keep the mixture on for 10-15 minutes\n
	            Thereafter, rinse mouth with warm water\n
	            Repeat the process once or twice a 	week\n
                ''')
                await C.send(embed = C_e)
                await C.send(file = discord.File("GC.jpg"))
            elif message.content=="4":
                D = client.get_channel(1029621300261572621)
                D_e = discord.Embed(title="Head Ache", color=0x800020)
                D_e.add_field(name="Remedy:", value="Chanda or Snadalwood: Chandan is the best remedy to soothe headache.")
                D_e.add_field(name="Method:", value='''Apply paste of sandalwood on your forehead and lit it sir for 20 minutes.
                ''')
                await D.send(embed = D_e)
                await D.send(file = discord.File("CN.jpg"))
            elif message.content=="5":
                E = client.get_channel(1029621300261572621)
                E_e = discord.Embed(title="Fever[Normal Fever]", color=0x808080)
                E_e.add_field(name="Remedy:", value="Crushed Garlic")
                E_e.add_field(name="Method:", value='''It is one of the widely used remedy 	for fever, cough and cold. Garlic has antibacterial properties and hence it has great healing power for fever, 	cough and cold. You can take 4-6 
                crushed garlic cloves and consume it directly. If you are not very comfortable with the strong flavour and smell then you can also take it with curd.
                ''')
                await E.send(embed = E_e)
                await E.send(file = discord.File("CG.jpg"))
            elif message.content=="6":
                F = client.get_channel(1029621300261572621)
                F_e = discord.Embed(title="Stomach Ache", color=0x008080)
                F_e.add_field(name="Remedy:", value="Pomegranate Seed")
                F_e.add_field(name="Method:", value='''Take Anardana (Pomegranate seed in English) and apply some black salt and Kali Mirch (Peppercorns) powder on seeds. Finally, use these seeds in a stomach ache natural treatment.
                ''')
                await F.send(embed = F_e)
                await F.send(file = discord.File("PM.jpg"))
            elif message.content=="7":
                G = client.get_channel(1029621300261572621)
                G_e = discord.Embed(title="Cough & Cold", color=0xd2691e)
                G_e.add_field(name="Remedy:", value="Cinnamon")
                G_e.add_field(name="Method:", value='''This aromatic spice can give you great relief in throat infection, cough and cold. It is an antibiotic which has the 	capacity to prevent any flu. You can consume it in your
                tea. It will give flavour, aroma and taste to your beverage and you will also enjoy its benefit.
                ''')
                await G.send(embed = G_e)
                await G.send(file = discord.File("CM.jpg"))
            elif message.content=="8":
                G = client.get_channel(1029621300261572621)
                G_e = discord.Embed(title="Blood Pressure", color=0x2ECC71)
                G_e.add_field(name="Remedy:", value="Amla or Indian Gooseberry")
                G_e.add_field(name="Method:", value='''Amla or Indian Gooseberry is an effective ayurvedic medicine for blood pressure. It has Vitamin C which helps reduce blood cholesterol levels and widens blood vessels.
                ''')
                await G.send(file = discord.File("AM.jpg"))
                G_e.add_field(name="Remedy:", value="Ashwagandha")
                G_e.add_field(name="Method:", value='''Ashwagandha or Indian Ginseng is a natural herb that you can add to your evening tea in small quantities. It has been proven to lower blood pressure along with acupressure points for blood pressure.
                ''')
                await G.send(embed = G_e)
              
                await G.send(file = discord.File("AW.jpg"))
    
client.run('MTAyOTU5NDIyNzQzODUzMDYwMg.GFXS8o.1Uiq4JcQHDBa5zGnQcDZfZda4Ynfd3KPzZSnms')
