#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from contact import Contact
from phonebook import PhoneBook


if __name__ == '__main__':
    jhon = Contact('Jhon', 'Doe', '+79001234567', work='+78001234567', telega='jhondoe', vk='vk.com/jhondoe')
    maxim = Contact('Maxim', 'Maximus', '+79007654321', True, telega='maxim', vk='vk.com/maxim', fb='MaximMaximus')
    print(jhon, maxim, sep='\n')

    my_contacts = PhoneBook('My Phonebook')
    my_contacts.add_contact(jhon)
    my_contacts.add_contact(maxim)

    my_contacts.view_all()

    my_contacts.search('Jhon', 'Doe')

    my_contacts.all_favorite()

    my_contacts.del_contact('+79001234567')
    my_contacts.view_all()
