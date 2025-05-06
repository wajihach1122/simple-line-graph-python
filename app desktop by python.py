# -*- coding: utf-8 -*-
"""
Created on Tue May  6 17:24:02 2025

@author: test
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit,
    QComboBox, QCheckBox, QRadioButton, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox
)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Large Form Example")
window.setGeometry(100, 100, 400, 500)

# --- Widgets ---
name_label = QLabel("Full Name:")
name_input = QLineEdit()

email_label = QLabel("Email:")
email_input = QLineEdit()

phone_label = QLabel("Phone Number:")
phone_input = QLineEdit()

gender_label = QLabel("Gender:")
gender_male = QRadioButton("Male")
gender_female = QRadioButton("Female")
gender_other = QRadioButton("Other")

country_label = QLabel("Country:")
country_combo = QComboBox()
country_combo.addItems(["Select", "USA", "UK", "Canada", "Pakistan", "India"])

subscribe_checkbox = QCheckBox("Subscribe to newsletter")
terms_checkbox = QCheckBox("I agree to the Terms and Conditions")

about_label = QLabel("About Yourself:")
about_input = QTextEdit()

submit_button = QPushButton("Submit")

# --- Submit action ---
submit_button.clicked.connect(lambda: QMessageBox.information(
    window,
    "Form Submitted",
    f"Name: {name_input.text()}\n"
    f"Email: {email_input.text()}\n"
    f"Phone: {phone_input.text()}\n"
    f"Gender: "
    f"{'Male' if gender_male.isChecked() else 'Female' if gender_female.isChecked() else 'Other' if gender_other.isChecked() else 'Not Selected'}\n"
    f"Country: {country_combo.currentText()}\n"
    f"Subscribed: {'Yes' if subscribe_checkbox.isChecked() else 'No'}\n"
    f"Agreed to Terms: {'Yes' if terms_checkbox.isChecked() else 'No'}\n"
    f"About: {about_input.toPlainText()}"
))

# --- Layout ---
layout = QVBoxLayout()
layout.addWidget(name_label)
layout.addWidget(name_input)
layout.addWidget(email_label)
layout.addWidget(email_input)
layout.addWidget(phone_label)
layout.addWidget(phone_input)

layout.addWidget(gender_label)
gender_layout = QHBoxLayout()
gender_layout.addWidget(gender_male)
gender_layout.addWidget(gender_female)
gender_layout.addWidget(gender_other)
layout.addLayout(gender_layout)

layout.addWidget(country_label)
layout.addWidget(country_combo)

layout.addWidget(subscribe_checkbox)
layout.addWidget(terms_checkbox)

layout.addWidget(about_label)
layout.addWidget(about_input)

layout.addWidget(submit_button)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())