import json
import random
import datetime as dt


class TestBrain:
    def __init__(self):
        with open("paragraphs.json", encoding="utf8") as file:
            self.paragraph_data = json.load(file)
        self.chosen_text = str(random.choice(self.paragraph_data)["text"])
        self.splitted_text = self.chosen_text.split(" ")
        self.start_time = None
        self.stop_time = None
        self.index = 0
        self.scentence = None

    def get_scentence(self):
        if self.index == 0:
            word1 = " "
            word2 = self.splitted_text[0]
            word3 = self.splitted_text[1]
            word4 = self.splitted_text[2]
            word5 = self.splitted_text[3]
            word6 = self.splitted_text[4]
            word7 = self.splitted_text[5]
            word8 = self.splitted_text[6]
        else:
            word1 = self.splitted_text[self.index-1]
            word2 = self.splitted_text[self.index]
            word3 = self.splitted_text[self.index+1]
            word4 = self.splitted_text[self.index+2]
            word5 = self.splitted_text[self.index+3]
            word6 = self.splitted_text[self.index+4]
            word7 = self.splitted_text[self.index+5]
            word8 = self.splitted_text[self.index+6]
        self.scentence = f"{word1} {word2} {word3} {word4} {word5} {word6} {word7} {word8}"

    def check_answer(self, test_result):
        pass

    def start_timer(self):
        pass

    def check_timer(self):
        pass
