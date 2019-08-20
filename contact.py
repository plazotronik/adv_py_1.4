#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Contact:
    def __init__(self, name, surname, phonenumber, favorite=False, **kwargs:'email, соц.сети, проч.'):
        self.name = name
        self.surname = surname
        self.phonenumber = phonenumber
        self.favorite = favorite
        self.addinfo = kwargs
        self.fio = self.name + " " + self.surname + " " + self.phonenumber

    def __list_addinfo(self):
        list_addinfo = []
        for k,v in self.addinfo.items():
            list_addinfo.append(f'{k}: {v}')
        return list_addinfo

    def __str__(self):
        sep = f'\n{" "*5}'
        return f'Имя: {self.name}\nФамилия: {self.surname}\nТелефон: {self.phonenumber}' \
               f'\nВ избранных: {str(self.favorite).replace("True", "да").replace("False", "нет")}' \
               f'\nДополнительная информация: {sep}{sep.join(self.__list_addinfo())}'
