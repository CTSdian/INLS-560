# I found these FAQs on https://www.government.is/ministries/ministry-for-foreign-affairs/faq/
import string
import re

def remove_punc_char(s):
    # this function is to remove all the characters and punctuations in the input
    for i in string.punctuation:
        s = s.replace(i,'')
    s = re.sub('[a-zA-Z]','',s)
    if s == "":
        # if there is no number in the input, return -1 to continue loop
        return -1
    else:
        return s

def user_input():
    print("""
Iceland FAQS list:
1: Visa to Iceland
2: What kind of identificaiton do I need to travel to Iceland?
3: Travelling to Iceland with a pet
4: What medicines can I bring with me to Iceland?
5: Is my driving licence valid in Iceland?
6: Travel safety in Iceland
7: Health insurance for tourists in Iceland
8: How to get married in Iceland
9: Working in Iceland
0: Quit
    """)
    tmp = int(remove_punc_char(input("Please enter number above to show Iceland FAQs:")))
    
    while tmp < 0 or tmp > 9:
        tmp = int(input("Invalid input, please reenter between(0-9):"))
    return tmp


user_option = user_input()
while user_option != 0:
    if user_option == 1:
        print("""
For information about visa requirements, please visit the website of the Icelandic Directorate of Immigration.

There you will find information about visa requirements, how to get a visa and how to apply, including fees and documents needed.
              """)
    elif user_option == 2:
        print("""
Iceland is a part of the Schengen Agreement and although travellers within the Schengen area are not to be asked to present a passport at borders, travellers are still advised to bring their passports. It is the obligation of everyone travelling within the area to be able to show a fully valid form of personal identification approved by other Schengen States. Also, airlines within the Schengen area may want to inspect the passports of their passengers. Three months passport validity is normally required for those intending to visit Iceland.

.For further information please visit our website
.Information about Passport Control at Keflavik International Airport              
              """)
    elif user_option == 3:
        print("""
Please contact the Icelandic Food and Veterinary Authority for information on travelling to Iceland with a pet. Information on importing live animals can be found on their website.

Icelandic Food and Veterinary Authority

Tel +354 530 4800
Fax +354 530 4801
mast@mast.is

www.mast.is/english
              """)
    elif user_option == 4:
        print("""
Information about medicines for those travelling to Iceland can be found on the website of the Icelandic Medicines Agency.
              """)
    elif user_option == 5:
        print("""
The driving licence will need to be held for at least one year and be from the holder's country of residence. If the licence is of non-roman alphabet (e.g. Japanese), then an International driving licence will be required.

An International Driver's Permit alone isn't sufficient for a rental - it may only be used in conjunction with a standard driving licence.

UK licence holders will need to take their ID card and its paper counterpart (old style licence still accepted).

Information on foreign driving licences in Iceland on the website of the Multicultural Information Centre.

 As driving conditions in Iceland can be pretty tough in the wintertime
https://guidetoiceland.is/travel-info/driving-in-iceland 
              """)
    elif user_option == 6:
        print("""
Please visit safetravel.is for information about travelling in Iceland.
              """)
    elif user_option == 7:
        print("""
General information about health services and health insurance for tourists in Iceland can be found on the website of Icelandic Health Insurance (IHI).

For futher information about health insurance please contact Icelandic Health Insurance:

Icelandic Health Insurance:
Address: Vínlandsleið 16, 105 Reykjavík.
Phone: +354 515-0000
E-mail: sjukra@sjukra.is
http://www.sjukra.is/
              """)
    elif user_option == 8:
        print("""
For civil ceremonies in Reykjavik, contact:
District Commissioner in Reykjavik (Syslumadurinn í Reykjavik)
Skogarhlid 6
IS-150 Reykjavík
Tel: +354 569 2400
Fax: +354 562 4870
Web: island.is/s/syslumenn

Information on required documents can be found on the website of the District Commissioners.

For details pertaining to a Church wedding you should also contact either of the following: The Dean of Reykjavík (East)
Rev. Gísli Jónason
Tel: + 354 864 7486
E-mail: gisli.jonasson@kirkjan.is


The Dean of Reykjavik (West)
Rev. Ása Laufey Sæmudsdóttir
Hallgrimskirkja, Skolavörduholti
IS-101 Reykjavík
Tel: +354 510 1000
Fax: + 354 510 1010
E-mail: hallgrimskirkja@hallgrimskirkja.is
              """)
    elif user_option == 9:
        print("""
The Ministry for Foreign Affairs of Iceland does not provide information about employment opportunities.

Useful information regarding work in Iceland. 
For information about work permits, please visit the website of the Icelandic Directorate of Immigration
              """)
    user_option = user_input()

