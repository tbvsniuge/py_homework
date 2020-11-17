import tkinter
import random


def generate_button_data():
    max = 25
    numbers = list(range(1, max + 1))
    random.shuffle(numbers)
    data_list = []
    for number in numbers:
        value = {"number": number, "button": None}
        data_list.append(value)
    return data_list


class ShuErTe:
    def __init__(self, size_x=300, size_y=500):
        self.top = tkinter.Tk()
        self.top.minsize(size_x, size_y)
        self.click_count = 1

    def button_command(self, index):
        button_number = self.button_data_list[index]['number']
        current_button = self.button_data_list[index]['button']
        if current_button['text'] == '':
            current_button['text'] = button_number
            if self.click_count == button_number:
                current_button['bg'] = 'green'
            else:
                current_button['bg'] = 'red'
            self.click_count += 1

    def generate_buttons(self):
        self.button_data_list = generate_button_data()

        for index, button_data_obj in enumerate(self.button_data_list):
            button_data_obj['button'] = tkinter.Button(
                self.top,
                text=button_data_obj['number'],
                command=lambda index=index: self.button_command(index))
            width = 60
            height = 60
            place_x = (index % 5) * width
            place_y = (index // 5) * height + 20

            button_data_obj['button'].place(x=place_x,
                                            y=place_y,
                                            width=width,
                                            height=height)

        # print(self.button_data_list)
    def start_gm(self):
        for button_data_list in self.button_data_list:
            current_button = button_data_list['button']
            current_button['text'] = ''

    def main_func(self):
        button_begin = tkinter.Button(self.top,
                                      text='GEN',
                                      command=self.generate_buttons)
        button_begin.place(x=40, y=380, width=80, height=40)

        self.button_begin = tkinter.Button(self.top,
                                           text='STA',
                                           command=self.start_gm)
        self.button_begin.place(x=170, y=380, width=80, height=40)
        self.top.mainloop()


if __name__ == "__main__":
    shu_er_te = ShuErTe()
    shu_er_te.main_func()
