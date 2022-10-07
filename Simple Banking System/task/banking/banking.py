# Write your code here
import random
import textwrap
import sqlite3


class Luha:
    def __init__(self):
        pass

    def cal_check_sum(self, card_bin):
        # card_bin
        odd_multiply_2 = [value * 2 if index % 2 == 0 else value for index, value in enumerate(card_bin.copy())]
        odd_multiply_2 = [value - 9 if value >= 10 else value for value in odd_multiply_2]
        # checksum
        digit_sum = sum(odd_multiply_2)
        check_sum = 0
        for i in range(1, 10):
            if (digit_sum + i) % 10 == 0:
                check_sum = i
                break
        return check_sum

    def check_number(self, number):
        card_bin = [int(x) for index, x in enumerate(number) if index < len(number) - 1]
        check_sum = self.cal_check_sum(card_bin)
        return check_sum == int(number[-1])


class DbHelper:
    def __init__(self):
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.__start()

    def __start(self):
        # self.cur.execute("""
        # DROP TABLE card;
        # """)
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS card 
        (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            number  TEXT,
            pin     TEXT,
            balance INTEGER DEFAULT 0
        );
        """)
        self.conn.commit()

    def save_card(self, card):
        self.cur.execute(f"""
        INSERT INTO card(number, pin, balance)
        VALUES ({card.number}, {card.pin}, {card.balance});
        """)
        self.conn.commit()

    def query_card(self, number):
        self.cur.execute(f"""
        SELECT number, pin, balance
        FROM card WHERE number = {number};
        """)
        res = self.cur.fetchone()
        if res is None or len(res) == 0:
            return None
        return Card(res[0], res[1], res[2])

    def update_card(self, card):
        self.cur.execute(f"""
        UPDATE card SET balance = {card.balance}
        WHERE number = {card.number}
        """)
        self.conn.commit()

    def do_trans(self, number, trans_money, remote_number):
        self.cur.execute(f"""
        UPDATE card SET balance = balance - {trans_money} WHERE number = {number};
        """)
        self.cur.execute(f"""
        UPDATE card SET balance = balance + {trans_money} WHERE number = {remote_number};
        """)
        self.conn.commit()

    def remove_card(self, number):
        self.cur.execute(f"""
        DELETE FROM card WHERE number = {number};
        """)
        self.conn.commit()


class Card:
    def __init__(self, number, pin, balance):
        self.number = number
        self.pin = pin
        self.balance = balance


class Bank:

    def __init__(self):
        self.db = DbHelper()
        self.luha = Luha()

    def generate_card(self):
        while True:
            # card_bin
            card_bin = [4, 0, 0, 0, 0, 0]
            card_bin.extend([random.randint(0, 9) for _ in range(9)])
            check_sum = self.luha.cal_check_sum(card_bin)
            card_bin.append(check_sum)
            # card_number
            card_number = "".join([str(value) for value in card_bin])
            if self.db.query_card(card_number):
                continue
            card = Card(card_number, "".join([str(random.randint(0, 9)) for _ in range(4)]), 0)
            self.db.save_card(card)
            return card

    def main_menu(self):
        while True:
            # choice == 0
            should_exit = False
            choice = int(input(
                textwrap.dedent("""
                1. Create an account
                2. Log into account
                0. Exit
                """)))
            if choice == 0:
                should_exit = True
            elif choice == 1:
                card = self.generate_card()
                print(
                    textwrap.dedent(f"""
                    Your card has been created
                    Your card number:
                    {card.number}
                    Your card PIN:
                    {card.pin}
                    """))
            else:
                should_exit = self.__second_menu()
            if should_exit:
                print("Bye!")
                break

    def __second_menu(self):
        card_number = input("Enter your card number:")
        pin = input("Enter your PIN:")
        card = self.db.query_card(card_number)
        if not card or card.pin != pin:
            print("Wrong card number or PIN!")
        else:
            print("You have successfully logged in!")
            while True:
                second_choice = int(input(textwrap.dedent("""
                1. Balance
                2. Add income
                3. Do transfer
                4. Close account
                5. Log out
                0. Exit
                """)))
                if second_choice == 0:
                    return True
                elif second_choice == 5:
                    print("You have successfully logged out!")
                    return False
                elif second_choice == 1:
                    print(f'Balance: {card.balance}')
                elif second_choice == 2:
                    income = int(input("Enter income:"))
                    card.balance += income
                    self.db.update_card(card)
                    print("Income was added!")
                elif second_choice == 3:
                    remote_number = input(textwrap.dedent("""
                    Transfer
                    Enter card number:
                    """))
                    if remote_number == card.number:
                        print("You can't transfer money to the same account!")
                        continue
                    if not self.luha.check_number(remote_number):
                        print("Probably you made a mistake in the card number. Please try again!")
                        continue
                    remote_card = self.db.query_card(remote_number)
                    if not remote_card:
                        print("Such a card does not exist.")
                        continue
                    trans_money = int(input("Enter how much money you want to transfer:"))
                    if trans_money > card.balance:
                        print("Not enough money!")
                        continue
                    card.balance -= trans_money
                    self.db.do_trans(card.number, trans_money, remote_number)
                    print("Success!")
                elif second_choice == 4:
                    self.db.remove_card(card.number)
                    print("The account has been closed!")
                    return False


bank = Bank()
bank.main_menu()
