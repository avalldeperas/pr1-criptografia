#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

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
    print(f'message = {message}, shift {shift}')
    for i in range(len(message)):
        char = message[i]
        # get position of char in our alphabet
        current_position = ABC.index(char)
        # add shift to position with module of alphabet
        shifted_position = (current_position + shift) % len(ABC)
        # get shifted char in alphabet
        shifted_char = ABC[shifted_position]
        # append shifted char
        ciphertext += shifted_char
    print(f'ciphertext = {ciphertext}')
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
        shifted_char = message[i]
        shifted_position = ABC.index(shifted_char)
        # this time we extract shift value from current position with module of alphabet
        real_position = (shifted_position - shift) % len(ABC)
        shifted_char = ABC[real_position]
        plaintext += shifted_char
    print(f'plaintext = {plaintext}')
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
        # Set calculated value
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
    print(f'key = {key}, plaintext = {plaintext}')
    k = 0
    done = False
    # loop 1 until we have covered all plaintext chars
    while not done:
        # looping key array
        for i in range(len(key)):
            value = key[i]
            # if value is 1 AND we haven't covered all chars in plaintext, then add plaintext char
            if value > 0 & k < len(plaintext):
                char_chosen = plaintext[k]
                k += 1
            else:  # otherwise add a random char from our custom alphabet
                char_chosen = random.choice(ABC)
            ciphertext += char_chosen
            # if we have covered all chars in plaintext, then finish looping
            if k >= len(plaintext):
                done = True
                break
    print(f'ciphertext = {ciphertext}')
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

    #### IMPLEMENTATION GOES HERE ###
    print(f'key = {key}, ciphertext = {ciphertext}')
    for i in range(len(ciphertext)):
        # get position by position i with module of key length
        position = i % len(key)
        # get value from this position
        key_value = key[position]
        # if we find a 1 we append it as it's a char from the plaintext
        if key_value == 1:
            plaintext += ciphertext[i]
    print(f'plaintext = {plaintext}')
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
    # as per requirements of PR1, the sum of holes (ones inside the key array) is the shift value
    shift = sum(key)
    # we first shift the plaintext using the already built method from exercise 1
    shifted_text = uoc_rotative_encrypt(plaintext, shift)
    # we then cipher the text using the grille method built in exercise 4
    ciphertext = uoc_grille_encrypt(key, shifted_text)
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
    # we first decipher the text using the grille method built in exercise 5
    shifted_result = uoc_grille_decrypt(key, ciphertext)
    # as per requirements of PR1, the sum of holes (ones inside the key array) is the shift value
    shift = sum(key)
    # we then unshift the text using the already built method from exercise 2
    plaintext = uoc_rotative_decrypt(shifted_result, shift)
    # --------------------------------

    return plaintext
