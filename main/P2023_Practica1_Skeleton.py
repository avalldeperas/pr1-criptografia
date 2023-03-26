#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import string

ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:?"


# --- IMPLEMENTATION GOES HERE -----------------------------------------------
#  Student helpers (functions, constants, etc.) can be defined here, if needed


# ----------------------------------------------------------------------------


def uoc_rotative_encrypt(message, shift):
    """
    EXERCISE 1: Simple substitution cipher
    :message: message to cipher (plaintext)
    :shift: offset or displacement
    :return: ciphered text
    """

    ciphertext = ""

    #### IMPLEMENTATION GOES HERE ####
    for i in range(len(message)):
        char = message[i]
        position = ABC.index(char)
        shifted_position = (position + shift) % len(ABC)
        shifted_char = ABC[shifted_position]
        print(f'{char} ({position}) + {shift} --> {shifted_char} ({shifted_position})')
        ciphertext += shifted_char

    print(f'ciphertext {ciphertext}')
    # --------------------------------

    return ciphertext


def uoc_rotative_decrypt(message, shift):
    """
    EXERCISE 2: Simple substitution decipher
    :message: message to cipher (plaintext)
    :shift: offset or displacement
    :return: ciphered text
    """

    plaintext = ""

    #### IMPLEMENTATION GOES HERE ####
    for i in range(len(message)):
        char = message[i]
        position = ABC.index(char)
        shifted_position = (position - shift) % len(ABC)
        shifted_char = ABC[shifted_position]
        print(f'{char} ({position}) + {shift} --> {shifted_char} ({shifted_position})')
        plaintext += shifted_char

    print(f'plaintext {plaintext}')
    # --------------------------------

    return plaintext


def uoc_grille_genkey(grille_len, num_holes):
    """
    EXERCISE 3: Key generation
    :gruille_len: total grille length in symbols
    :num_holes: Number of holes in the grille
    :return: key as list of 0 and 1
    """

    key = []

    #### IMPLEMENTATION GOES HERE ####
    for i in range(grille_len):
        value = random.randint(0, 1)
        if value == 1:
            # If we already set more 1 than needed, just fill with 0.
            if sum(key) >= num_holes:
                value = 0
        else:  # 0
            # If there's 1 pending to be set BUT reaching the end of array, fill with 1.
            pending_iterations = grille_len - i
            pending_num_holes = num_holes - sum(key)
            if pending_iterations <= pending_num_holes:
                value = 1
        # Set whatever value
        key.append(value)
    print(f'key = {key}')
    # --------------------------------

    return key


def uoc_grille_encrypt(key, plaintext):
    """
    EXERCISE 4: Encrypt a text using the key
    :message: message to grille_encrypt
    :shift: offset or displacement
    :return: ciphered text
    """

    ciphertext = ""

    #### IMPLEMENTATION GOES HERE ####

    # --------------------------------

    return ciphertext


def uoc_grille_decrypt(key, ciphertext):
    """
    EXERCISE 5: Decrypt a text using the key
    :message: message to grille_decrypt
    :subs_alphabet: substitution alphabet
    :return: ciphered text
    """

    plaintext = ""

    #### IMPLEMENTATION GOES HERE ####

    # --------------------------------

    return plaintext


def uoc_encrypt(key, plaintext):
    """
    EXERCISE 6: Complete cryptosystem (encrypt)
    :key: grille key
    :plaintext: message to encrypt
    :return: encrypted text
    """

    ciphertext = ""

    #### IMPLEMENTATION GOES HERE ####

    # --------------------------------

    return ciphertext


def uoc_decrypt(key, ciphertext):
    """
    EXERCISE 6: Complete cryptosystem (decrypt)
    :key: grille key
    :ciphertext: message to decrypt
    :return: plaintext
    """

    plaintext = ""

    #### IMPLEMENTATION GOES HERE ####

    # --------------------------------

    return plaintext
