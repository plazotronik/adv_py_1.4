#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class PhoneBook:
    def __init__(self, name):
        self.name = name
        self.list_contacts = []

    def add_contact(self, contact):
        self.list_contacts.append(contact)

    def view_all(self):
        for index, contact in enumerate(self.list_contacts):
            print(f'{index+1}. {contact.fio}')

    def del_contact(self, phonenumber):
        for contact in self.list_contacts:
            if phonenumber in [contact.phonenumber, contact.addinfo]:
                self.list_contacts.remove(contact)
            else:
                continue

    def all_favorite(self):
        for contact in self.list_contacts:
            if contact.favorite:
                print(f'{contact.fio}')

    def search(self, name, surname):
        for contact in self.list_contacts:
            if contact.name == name and contact.surname == surname:
                print(contact)
