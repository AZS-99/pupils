"""
Problem Description
Text messaging using a cell phone is popular among teenagers. The messages can appear peculiar because short forms and
symbols are used to abbreviate messages and hence reduce typing.
For example, “LOL” means “laughing out loud” and “:-)” is called an emoticon which looks like a happy face (on its side)
and it indicates chuckling. This is all quite a mystery to some adults.
Write a program that will continually input a short form and output the translation for an adult using the following
translation table:

                                        CU      see you
                                        :-)     I’m happy
                                        :-(     I'm sad
                                        ;-)     wink
                                        :-P     stick out the tongue
                                        (~.~)   sleepy
                                        TA      totally awesome
                                        CCC     Canadian Computation Competetion
                                        CUZ     because
                                        TY      thank you
                                        YW      you are welcome
                                        TTYL    talk to you later

Input Specifications
The user will be prompted to enter text to be translated one line at a time. When the short form “TTYL” is entered, the
program ends. Users may enter text that is found in the translation table, or they may enter other words. All entered
text will be symbols or upper case letters. There will be no spaces and no quotation marks.

Output Specifications
The program will output text immediately after each line of input. If the input is one of the phrases in the translation
table, the output will be the translation; if the input does not appear in the table, the output will be the original
word. The translation of the last short form entered “TTYL” should be output.

Sample Session(user input is in italics)
Enter phrase> CCC
Canadian Computing Competition
Enter phrase> :-)
I’m happy
Enter phrase> SQL
SQL
Enter phrase> TTYL
talk to you later
"""
def translation():
    text_dict = {
        "CU": "see you",
        ":-)": "I’m happy",
        ":-(": "I'm sad",
        ";-)": "wink",
        ":-P": "stick out the tongue",
        "(~.~)": "sleepy",
        "TA": "totally awesome",
        "CCC": "Canadian Computation Competetion",
        "CUZ": "because",
        "TY": "thank you",
        "YW": "you are welcome"

    }
    text_message = input("Enter phrase> ")
    while text_message != "TTYL":
        if text_message in text_dict:
            print(text_dict[text_message])
        else:
            print(text_message)
        text_message = input("Enter phrase> ")
    print("talk to you later")