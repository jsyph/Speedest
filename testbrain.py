import json
import random
import datetime as dt
import math


class TestBrain:
    def __init__(self):
        with open("paragraphs.json", encoding="utf8") as file:
            self.paragraph_data = json.load(file)
        self.chosen_text = str(random.choice(self.paragraph_data)["text"])
        self.splitted_text = self.chosen_text.split(" ")
        self.words_left = len(self.splitted_text)
        self.total_words = len(self.splitted_text)
        self.start_time = 0
        self.stop_time = 0
        self.time_taken = 0
        self.index = 0
        self.difficulty_time = 0
        self.scentence = None
        self.is_test_complete = {"state": False, "message": ""}
        self.user_score = {
            "errors": 0,
            "typing_speed": 0
        }

    def refresh_paragraph_data(self):
        with open("paragraphs.json", encoding="utf8") as file:
            self.paragraph_data = json.load(file)
        self.chosen_text = str(random.choice(self.paragraph_data)["text"])
        self.splitted_text = self.chosen_text.split(" ")
        self.words_left = len(self.splitted_text)

    def get_scentence(self):
        if self.index == 0:
            word0 = " "
            word1 = " "
            word2 = self.splitted_text[0]
            word3 = self.splitted_text[1]
            word4 = self.splitted_text[2]
            word5 = self.splitted_text[3]
            word6 = self.splitted_text[4]
            word7 = self.splitted_text[5]
            word8 = self.splitted_text[6]
        else:
            word0 = self.splitted_text[self.index - 2]

            word1 = self.splitted_text[self.index - 1]

            try:
                word2 = self.splitted_text[self.index]
            except IndexError:
                word0 = " "
                word1 = " "
                word2 = " "
                self.is_test_complete["state"] = True
                self.is_test_complete["message"] = "Test is complete, 0 words left."

            try:
                word3 = self.splitted_text[self.index + 1]
            except IndexError:
                word3 = " "

            try:
                word4 = self.splitted_text[self.index + 2]
            except IndexError:
                word4 = " "

            try:
                word5 = self.splitted_text[self.index + 3]
            except IndexError:
                word5 = " "

            try:
                word6 = self.splitted_text[self.index + 4]
            except IndexError:
                word6 = " "

            try:
                word7 = self.splitted_text[self.index + 5]
            except IndexError:
                word7 = " "

            try:
                word8 = self.splitted_text[self.index + 6]
            except IndexError:
                word8 = " "

        self.scentence = f"{word0} {word1} {word2} {word3} {word4} {word5} {word6} {word7} {word8}"

    def check_answer(self, test_result: str):
        self.check_timer()
        result_list = test_result.split(" ")
        wrong_answers = 0
        for right, wrong in zip(self.splitted_text, result_list):
            if right != wrong:
                wrong_answers += 1
        self.user_score["errors"] = wrong_answers
        self.user_score["typing_speed"] = math.ceil(len(result_list) / self.time_taken)
        print(self.user_score)

    def start_timer(self):
        self.start_time = dt.datetime.now().second

    def end_timer(self):
        self.stop_time = dt.datetime.now().second

    def check_timer(self):
        self.end_timer()
        self.time_taken = self.stop_time - self.start_time
        print(self.time_taken)
        if self.time_taken >= self.difficulty_time:
            print("Fuuuuuuuuuuuuuuuuuuuuuuuuuuuuck")
            self.is_test_complete["state"] = True
            self.is_test_complete["message"] = "Time Over!"
