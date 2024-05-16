import tkinter as tk
from tkinter import *


class App(tk.Tk):
	def __init__(self):
		super().__init__()
		# Создаем текстовое поле для ввода текста
		self.text_frame = tk.Frame(self)
		self.text_area = tk.Text(self.text_frame, height=10, width=50)
		self.text_area.pack()

		# Создаем кнопку для подсчета гласных
		self.button_frame = tk.Frame(self)
		self.count_button = tk.Button(self.button_frame, text="Подсчитать гласные", command=self.count_vowels)
		self.count_button.pack()

		# Создаем текстовое поле для вывода результатов
		self.result_frame = tk.Frame(self)
		self.result_text = tk.Text(self.result_frame, height=10, width=50)
		self.result_text.pack()

		# Располагаем фреймы в главном окне
		self.text_frame.pack()
		self.button_frame.pack()
		self.result_frame.pack()

	def count_vowels(self):
    	# Получаем текст из текстового поля
		text = self.text_area.get("1.0", tk.END)
    
    	# Подсчитываем количество гласных в тексте
		self.vowel_counts = {
			'а': 0, 'у': 0, 'о': 0, 'э': 0, 'ы': 0,
			'е': 0, 'и': 0, 'ю': 0, 'ё': 0, 'я': 0,
			'А': 0, 'У': 0, 'О': 0, 'Э': 0, 'Ы': 0,
			'Е': 0, 'И': 0, 'Ю': 0, 'Ё': 0, 'Я': 0
    	}
    
		for char in text:
			if char.lower() in 'ауэоыеиюёяАУЭОЫЕИЮЯ':
				self.vowel_counts[char] += 1
		
		# Выводим результаты в текстовое поле результата
		self.result_text.delete('1.0', tk.END)
		for key, value in self.vowel_counts.items():
			self.result_text.insert(tk.END, f"{key} - {value} шт.\n")
		
		# Добавляем итоговую строку
		self.result_text.insert(tk.END, "Всего гласных:  ")
		total_vowels = sum(self.vowel_counts.values())
		self.result_text.insert(tk.END, str(total_vowels))

if __name__ == "__main__":
    app = App()
    app.mainloop()
