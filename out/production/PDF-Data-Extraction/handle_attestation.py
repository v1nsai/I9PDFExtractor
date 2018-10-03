from wand.image import Image
import sys
import io
import PIL
import pytesseract
import re
import json
import numpy as np
from fuzzywuzzy import process

def findFormNumber(file):
    """
    @@file - the file to find the form number of
    This function takes in a file and spits out the form number associated with it
    """
    image = file
    im = PIL.Image.open(image)
    width, height = im.size

    # list of possible form choices
    choices = ['11-21-91(R)', '05/31/05', '07/17/17', '08/07/09',
               '11/14/2016', '02/02/09', '03/08/13', '05/07/87',
               '11-21-91(L)', '06/05/07']


    try:
        # Combine text from spots the form version is found into a blob, then search for form versions
        swap = crop(image, (.04 * width, .954 * height, .95 * width, .98 * height))
        text = pytesseract.image_to_string(PIL.Image.open(swap))

        swap = crop(image, (.04 * width, .945 * height, .95 * width, .97 * height))
        text = text + '\n' + pytesseract.image_to_string(PIL.Image.open(swap))

        swap = crop(image, (.04 * width, .925 * height, .95 * width, .955 * height))
        text = text + '\n' + pytesseract.image_to_string(PIL.Image.open(swap))

        swap = crop(image, (.04 * width, .907 * height, .95 * width, .925 * height))
        text = text + '\n' + pytesseract.image_to_string(PIL.Image.open(swap))

        swap = crop(image, (.04 * width, .925 * height, .955 * width, .955 * height))
        text = text + '\n' + pytesseract.image_to_string(PIL.Image.open(swap))

        swap = crop(image, (.04 * width, .80 * height, .955 * width, .83 * height))
        text = text + '\n' + pytesseract.image_to_string(PIL.Image.open(swap))

        swap = crop(image, (.04 * width, .955 * height, .95 * width, .98 * height))
        text = text + '\n' + pytesseract.image_to_string(PIL.Image.open(swap))

        match = process.extractOne(text, choices)[0]
        return match
    except IOError:
        return -1



def findPageNumber(file):
    """
    @@file file to determine page number of
    This function intakes a file and spits out the page number based on
    cropping the file to find a page number
    """
    # crop bottom of image
    image = file
    im = PIL.Image.open(image)
    width, height = im.size

    # list of possible page numbers (can't be page 0 and there is no form that has a page 1o)
    choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    while True:
        try:
            swap = crop(image, (.04 * width, .955 * height, .95 * width, .98 * height))
            # run tesseract on crop
            text = pytesseract.image_to_string(PIL.Image.open(swap))
            # clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
            matches = re.findall('Page (\d+)', text)
            # return output
            if matches:
                for match in matches:
                    query = match[0]
                    # get the top match ordered by score
                    return (int(process.extractOne(query, choices)[0]))
                    break

            elif not matches:
                swap = crop(image, (.04 * width, .945 * height, .95 * width, .97 * height))

                # run tesseract on crop
                text = pytesseract.image_to_string(PIL.Image.open(swap))

                # clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
                matches = re.findall('Page (\d+)', text)

                # output answer
                for match in matches:
                    query = match[0]
                    # get the top match ordered by score
                    return (int(process.extractOne(query, choices)[0]))
                    break

            elif not matches:
                swap = crop(image, (.04 * width, .925 * height, .95 * width, .955 * height))

                # run tesseract on crop
                text = pytesseract.image_to_string(PIL.Image.open(swap))

                # clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
                matches = re.findall('Page (\d+)', text)

                # output answer
                for match in matches:
                    query = match[0]
                    # get the top match ordered by score
                    return (int(process.extractOne(query, choices)[0]))
                    break

            if not matches:
                swap = crop(image, (.04 * width, .907 * height, .95 * width, .925 * height))

                # run tesseract on crop
                text = pytesseract.image_to_string(PIL.Image.open(swap))

                # clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
                matches = re.findall('Page (\d+)', text)

                # output answer
                for match in matches:
                    query = match[0]
                    # get the top match ordered by score
                    return (int(process.extractOne(query, choices)[0]))
                    break

            if not matches:
                swap = crop(image, (.04 * width, .925 * height, .95 * width, .955 * height))

                # run tesseract on crop
                text = pytesseract.image_to_string(PIL.Image.open(swap))

                # clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
                matches = re.findall('Page (\d+)', text)

                # output answer
                for match in matches:
                    query = match[0]
                    # get the top match ordered by score
                    return (int(process.extractOne(query, choices)[0]))
                    break

            if not matches:
                swap = crop(image, (.04 * width, .80 * height, .95 * width, .83 * height))

                # run tesseract on crop
                text = pytesseract.image_to_string(PIL.Image.open(swap))

                # clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
                matches = re.findall('Page (\d+)', text)

                # output answer
                for match in matches:
                    query = match[0]
                    # get the top match ordered by score
                    return (int(process.extractOne(query, choices)[0]))
                    break

            if not matches:
                swap = crop(image, (.04 * width, .955 * height, .95 * width, .98 * height))

                # run tesseract on crop
                text = pytesseract.image_to_string(PIL.Image.open(swap))

                # clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
                matches = re.findall('Page (\d+)', text)

                # output answer
                for match in matches:
                    query = match[0]
                    # get the top match ordered by score
                    return (int(process.extractOne(query, choices)[0]))
                    break

            if not matches:
                return ('not found')
                break

        except IOError:
            return ("image file is truncated")
            break


def getImageCoords(file, formNumber, page_number):
    image = file
    im = PIL.Image.open(image)
    width, height = im.size

    swap_coords = {}

    if formNumber == '02/02/09':
        # listing out the (x1, y1, x2, y2) coordinates of information on each of
        # the different forms
        swap_coords = {'LastName': (.055 * width, .180 * height, .37 * width, .204 * height),
                               'FirstName': (.368 * width, .180 * height, .61 * width, .205 * height),
                               'MiddleInitial': (.610 * width, .180 * height, .686 * width, .205 * height),
                               'MaidenName': (.69 * width, .18 * height, .94 * width, .205 * height),
                               'StreetAddress': (.055 * width, .217 * height, .58 * width, .240 * height),
                               'City': (.055 * width, .252 * height, .35 * width, .275 * height),
                               'DateOfBirth': (.688 * width, .217 * height, .95 * width, .240 * height),
                               'SocialSecurity': (.688 * width, .253 * height, .9 * width, .275 * height),
                               'State': (.345 * width, .252 * height, .58 * width, .275 * height),
                               'Zip': (.58 * width, .252 * height, .688 * width, .275 * height),
                               'EmailAddress': (),
                               'Telephone': (),
                               'Attestation': (.49 * width, .292 * height, .515 * width, .365 * height),
                               'Alien # for Permanent Residence': (
                               .722 * width, .325 * height, .94 * width, .345 * height),
                               'Date Expiration of Work Authorization': (
                               .805 * width, .362 * height, .955 * width, .377 * height),
                               'Alien # for Work Authorization': (
                               .81 * width, .346 * height, .955 * width, .365 * height),
                               'I-94 Admission Number': (),
                               'Foreign Passport': (),
                               'Country of Issuance': (),
                               'TranslatorName': (.513 * width, .443 * height, .94 * width, .469 * height),
                               'TranslatorAddress': (.104 * width, .482 * height, .67 * width, .505 * height),
                               'TranslatorDateOfSignature': (.68 * width, .482 * height, .94 * width, .505 * height),
                               'List A - DocumentTitle': (.145 * width, .564 * height, .363 * width, .586 * height),
                               'List A - IssuingAuthority': (.15 * width, .586 * height, .363 * width, .605 * height),
                               'List A - DocumentNumber': (.126 * width, .606 * height, .363 * width, .625 * height),
                               'List A - DocumentExpirationDate': (
                               .215 * width, .625 * height, .363 * width, .644 * height),
                               'List A - DocumentTitle - Second Section': (),
                               'List A - IssuingAuthority - Second Section': (),
                               'List A - DocumentNumber - Second Section': (
                               .13 * width, .644 * height, .363 * width, .662 * height),
                               'List A - DocumentExpirationDate - Second Section': (
                               .215 * width, .662 * height, .363 * width, .682 * height),
                               'List B - DocumentTitle': (.38 * width, .561 * height, .64 * width, .585 * height),
                               'List B - IssuingAuthority': (.38 * width, .585 * height, .64 * width, .605 * height),
                               'List B - DocumentNumber': (.38 * width, .6052 * height, .64 * width, .6245 * height),
                               'List B - DocumentExpirationDate': (
                               .38 * width, .6245 * height, .64 * width, .6445 * height),
                               'List C - DocumentTitle': (.7 * width, .561 * height, .95 * width, .585 * height),
                               'List C - IssuingAuthority': (.7 * width, .585 * height, .95 * width, .605 * height),
                               'List C - DocumentNumber': (.7 * width, .6052 * height, .95 * width, .6245 * height),
                               'List C - DocumentExpirationDate': (
                               .7 * width, .6245 * height, .95 * width, .6445 * height),
                               'DateOfHire': (.16 * width, .711 * height, .278 * width, .726 * height),
                               'Name of Employee Representative': (
                               .394 * width, .752 * height, .698 * width, .777 * height),
                               'Title': (.698 * width, .752 * height, .95 * width, .777 * height),
                               'EmployerBusinessName': (.05 * width, .7875 * height, .698 * width, .808 * height),
                               'EmployerStreetAddress': (),
                               'Date Signed by Employer': (.698 * width, .7875 * height, .95 * width, .808 * height),
                               'List A - DocumentTitle - Third Section': (),
                               'List A - IssuingAuthority - Third Section': (),
                               'List A - DocumentNumber - Third Section': (),
                               'List A - DocumentExpirationDate - Third Section': (),
                               'Employee Info from Section 1': ()}

    elif formNumber == '08/07/09':
        swap_coords = {'LastName': (.055 * width, .18 * height, .37 * width, .205 * height),
                               'FirstName': (.37 * width, .18 * height, .61 * width, .205 * height),
                               'MiddleInitial': (.61 * width, .18 * height, .685 * width, .205 * height),
                               'MaidenName': (),
                               'StreetAddress': (.055 * width, .215 * height, .58 * width, .24 * height),
                               'City': (.055 * width, .251 * height, .34 * width, .277 * height),
                               'State': (.34 * width, .251 * height, .58 * width, .277 * height),
                               'Zip': (.58 * width, .251 * height, .68 * width, .275 * height),
                               'DateOfBirth': (.693 * width, .205 * height, .94 * width, .239 * height),
                               'SocialSecurity': (.692 * width, .2525 * height, .9 * width, .276 * height),
                               'Attestation': (.492 * width, .29 * height, .517 * width, .367 * height),
                               'Alien # for Permanent Residence': (
                               .727 * width, .325 * height, .945 * width, .345 * height),
                               'Date Expiration of Work Authorization': (),
                               'I-94 Admission Number': (),
                               'ForeignPassport': (),
                               'Country of Issuance': (),
                               'Alien # for Work Authorization': (
                               .81 * width, .345 * height, .94 * width, .363 * height),
                               'TranslatorName': (.515 * width, .445 * height, .88 * width, .467 * height),
                               'TranslatorAddress': (),
                               'TranslatorDateOfSignature': (),
                               'List A - DocumentTitle': (.143 * width, .561 * height, .36 * width, .586 * height),
                               'List A - IssuingAuthority': (.153 * width, .586 * height, .358 * width, .6 * height),
                               'List A - DocumentNumber': (.133 * width, .606 * height, .358 * width, .62 * height),
                               'List A - DocumentExpirationDate': (
                                   .225 * width, .625 * height, .351 * width, .64 * height),
                               'List B - DocumentTitle': (.393 * width, .561 * height, .625 * width, .583 * height),
                               'List B - IssuingAuthority': (.393 * width, .586 * height, .625 * width, .6 * height),
                               'List B - DocumentNumber': (.393 * width, .606 * height, .625 * width, .62 * height),
                               'List B - DocumentExpirationDate': (
                               .393 * width, .625 * height, .625 * width, .64 * height),
                               'List C - DocumentTitle': (.713 * width, .561 * height, .945 * width, .586 * height),
                               'List C - IssuingAuthority': (.713 * width, .586 * height, .945 * width, .6 * height),
                               'List C - DocumentNumber': (.713 * width, .606 * height, .945 * width, .625 * height),
                               'List C - DocumentExpirationDate': (
                               .713 * width, .625 * height, .945 * width, .64 * height),
                               'List A - DocumentNumber - Second Section': (
                               .133 * width, .645 * height, .358 * width, .663 * height),
                               'List A - DocumentExpirationDate -  Second Section': (
                               .223 * width, .6624 * height, .358 * width, .68 * height),
                               'DateOfHire': (),
                               # 'ApartmentNo': (.57*width,.205*height,.66*width,.241*height)
                               }

    elif formNumber == '05/07/87':
        swap_coords = {'LastName': (.075 * width, .133 * height, .38 * width, .1525 * height),
                               'FirstName': (.38 * width, .133 * height, .56 * width, .1525 * height),
                               'MiddleInitial': (.56 * width, .133 * height, .74 * width, .1525 * height),
                               'MaidenName': (.74 * width, .133 * height, .95 * width, .1525 * height),
                               'StreetAddress': (.08 * width, .1612 * height, .38 * width, .182 * height),
                               'City': (.38 * width, .1612 * height, .56 * width, .182 * height),
                               'State': (.56 * width, .1612 * height, .735 * width, .182 * height),
                               'Zip': (.735 * width, .1612 * height, .92 * width, .182 * height),
                               'DateOfBirth': (.07 * width, .1923 * height, .41 * width, .211 * height),
                               'SocialSecurity': (.51 * width, .194 * height, .8 * width, .211 * height),
                               'EmailAddress': (),
                               'Telephone': (),
                               'Attestation': (.085 * width, .228 * height, .12 * width, .275 * height),
                               'Alien # for Permanent Residence': (
                               .503 * width, .24 * height, .655 * width, .26 * height),
                               'Date Expiration of Work Authorization': (
                               .62 * width, .2735 * height, .78 * width, .29 * height),
                               'Alien # for Work Authorization': (
                               .732 * width, .26 * height, .911 * width, .276 * height),
                               'Admission # for Work Authorization': (
                               .235 * width, .2735 * height, .369 * width, .29 * height),
                               'I-94 Admission Number': (),
                               'ForeignPassport': (),
                               'Country of Issuance': (),
                               'TranslatorName': (.51 * width, .406 * height, .833 * width, .424 * height),
                               'TranslatorAddress': (),
                               'TranslatorDateOfSignature': (),
                               'List A - DocumentTitle': (.06 * width, .632 * height, .09 * width, .72 * height),
                               'List A - IssuingAuthority': (),
                               'List A - DocumentNumber': (.076 * width, .782 * height, .315 * width, .8 * height),
                               'List A - DocumentExpirationDate': (
                               .067 * width, .827 * height, .315 * width, .845 * height),
                               'List B - DocumentTitle': (.38 * width, .61 * height, .4 * width, .73 * height),
                               'List B - IssuingAuthority': (),
                               'List B - DocumentNumber': (.3913 * width, .782 * height, .63 * width, .8 * height),
                               'List B - DocumentExpirationDate': (
                               .3913 * width, .827 * height, .63 * width, .845 * height),
                               'List C - DocumentTitle': (.7 * width, .61 * height, .72 * width, .73 * height),
                               'List C - IssuingAuthority': (),
                               'List C - DocumentNumber': (.712 * width, .782 * height, .95 * width, .8 * height),
                               'List C - DocumentExpirationDate': (
                               .712 * width, .827 * height, .95 * width, .845 * height),
                               'DateOfHire': (),
                               'Name of Employee Representative': (
                               .42 * width, .905 * height, .8 * width, .924 * height),
                               'Title': (.8 * width, .905 * height, .95 * width, .924 * height),
                               'EmployerBusinessName': (.07 * width, .936 * height, .4 * width, .954 * height),
                               'EmployerStreetAddress': (.42 * width, .935 * height, .80 * width, .954 * height),
                               'Date Signed by Employer': (.785 * width, .925 * height, .95 * width, .953 * height),
                               'List A - DocumentTitle - Third Section': (),
                               'List A - IssuingAuthority - Third Section': (),
                               'List A - DocumentNumber - Third Section': (),
                               'List A - DocumentExpirationDate - Third Section': (),
                               'Employee Info from Section 1': ()}

    elif formNumber == '05/31/05':
        swap_coords = {'LastName': (.05 * width, .168 * height, .37 * width, .189 * height),
                               'FirstName': (.37 * width, .168 * height, .57 * width, .189 * height),
                               'MiddleInitial': (.57 * width, .168 * height, .67 * width, .189 * height),
                               'MaidenName': (.68 * width, .168 * height, .95 * width, .189 * height),
                               'StreetAddress': (.05 * width, .202 * height, .67 * width, .22 * height),
                               'City': (.05 * width, .233 * height, .34 * width, .251 * height),
                               'State': (.34 * width, .233 * height, .57 * width, .251 * height),
                               'Zip': (.57 * width, .233 * height, .67 * width, .251 * height),
                               'DateOfBirth': (.68 * width, .203 * height, .95 * width, .22 * height),
                               'SocialSecurity': (.68 * width, .233 * height, .90 * width, .251 * height),
                               'EmailAddress': (),
                               'Telephone': (),
                               'Attestation': (.515 * width, .263 * height, .538 * width, .32 * height),
                               'Alien # for Permanent Residence': (
                               .782 * width, .285 * height, .97 * width, .305 * height),
                               'Date Expiration of Work Authorization': (
                               .73 * width, .3026 * height, .815 * width, .32 * height),
                               'Alien # for Work Authorization': (
                               .682 * width, .3152 * height, .97 * width, .331 * height),
                               'Admission # for Work Authorization': (),
                               'I-94 Admission Number': (),
                               'ForeignPassport': (),
                               'Country of Issuance': (),
                               'TranslatorName': ((.513 * width, .41 * height, .88 * width, .423 * height)),
                               'TranslatorAddress': (.1 * width, .436 * height, .67 * width, .454 * height),
                               'TranslatorDateOfSignature': (.68 * width, .436 * height, .88 * width, .454 * height),
                               'List A - DocumentTitle': (.14 * width, .513 * height, .34 * width, .534 * height),
                               'List A - IssuingAuthority': (.15 * width, .533 * height, .34 * width, .558 * height),
                               'List A - DocumentNumber': (.14 * width, .558 * height, .34 * width, .579 * height),
                               'List A - DocumentExpirationDate': (
                               .22 * width, .581 * height, .34 * width, .605 * height),
                               'List B - DocumentTitle': (.38 * width, .513 * height, .618 * width, .534 * height),
                               'List B - IssuingAuthority': (.38 * width, .533 * height, .618 * width, .558 * height),
                               'List B - DocumentNumber': (.38 * width, .558 * height, .618 * width, .579 * height),
                               'List B - DocumentExpirationDate': (
                               .38 * width, .581 * height, .618 * width, .605 * height),
                               'List C - DocumentTitle': (.7 * width, .513 * height, .96 * width, .534 * height),
                               'List C - IssuingAuthority': (.7 * width, .533 * height, .96 * width, .558 * height),
                               'List C - DocumentNumber': (.7 * width, .558 * height, .96 * width, .579 * height),
                               'List C - DocumentExpirationDate': (
                               .7 * width, .581 * height, .96 * width, .605 * height),
                               'DateOfHire': (.398 * width, .686 * height, .491 * width, .7 * height),
                               'Name of Employee Representative': (
                               .394 * width, .739 * height, .68 * width, .758 * height),
                               'Title': (.69 * width, .739 * height, .96 * width, .758 * height),
                               'EmployerBusinessName': (.04 * width, .772 * height, .305 * width, .797 * height),
                               'EmployerStreetAddress': (.307 * width, .772 * height, .685 * width, .797 * height),
                               'Date Signed by Employer': (.688 * width, .772 * height, .96 * width, .797 * height),
                               'List A - DocumentTitle - Third Section': (
                               .13 * width, .605 * height, .34 * width, .627 * height),
                               'List A - IssuingAuthority - Third Section': (),
                               'List A - DocumentNumber - Third Section': (),
                               'List A - DocumentExpirationDate - Third Section': (
                               .22 * width, .63 * height, .34 * width, .656 * height),
                               'Employee Info from Section 1 - LastName': (),
                               'Employee Info from Section 1 - FirstName': (),
                               'Employee Info from Section 1 - Middle Initial': ()
                               }

    elif formNumber == '06/05/07':
        swap_coords = {'LastName': (.055 * width, .197 * height, .36 * width, .221 * height),
                               'FirstName': (.36 * width, .197 * height, .58 * width, .221 * height),
                               'MiddleInitial': (.58 * width, .197 * height, .685 * width, .221 * height),
                               'MaidenName': (.688 * width, .197 * height, .95 * width, .221 * height),
                               'StreetAddress': (.055 * width, .233 * height, .57 * width, .257 * height),
                               'City': (.055 * width, .257 * height, .35 * width, .291 * height),
                               'State': (.35 * width, .257 * height, .57 * width, .291 * height),
                               'Zip': (.58 * width, .257 * height, .685 * width, .291 * height),
                               'DateOfBirth': (.69 * width, .233 * height, .95 * width, .25 * height),
                               'SocialSecurity': (.688 * width, .2685 * height, .88 * width, .291 * height),
                               'Attestation': (.45 * width, .306 * height, .4752 * width, .355 * height),
                               'Alien # for Permanent Residence': (
                               .71 * width, .318 * height, .95 * width, .332 * height),
                               'Date Expiration of Work Authorization': (
                               .652 * width, .332 * height, .95 * width, .349 * height),
                               'Alien # for Work Authorization': (
                               .61 * width, .349 * height, .95 * width, .368 * height),
                               'Admission # for Work Authorization': (),
                               'I-94 Admission Number': (),
                               'ForeignPassport': (),
                               'Country of Issuance': (),
                               'TranslatorName': (.515 * width, .433 * height, .88 * width, .469 * height),
                               'TranslatorAddress': (.1 * width, .47 * height, .677 * width, .497 * height),
                               'TranslatorDateOfSignature': (.678 * width, .47 * height, .9 * width, .497 * height),
                               'List A - DocumentTitle': (.14 * width, .561 * height, .36 * width, .59 * height),
                               'List A - IssuingAuthority': (.15 * width, .586 * height, .358 * width, .607 * height),
                               'List A - DocumentNumber': (.13 * width, .606 * height, .358 * width, .625 * height),
                               'List A - DocumentExpirationDate': (
                               .225 * width, .625 * height, .351 * width, .645 * height),
                               'List B - DocumentTitle': (.39 * width, .561 * height, .625 * width, .586 * height),
                               'List B - IssuingAuthority': (.39 * width, .586 * height, .625 * width, .607 * height),
                               'List B - DocumentNumber': (.39 * width, .606 * height, .625 * width, .625 * height),
                               'List B - DocumentExpirationDate': (
                               .39 * width, .625 * height, .625 * width, .645 * height),
                               'List C - DocumentTitle': (.71 * width, .561 * height, .945 * width, .586 * height),
                               'List C - IssuingAuthority': (.71 * width, .586 * height, .945 * width, .607 * height),
                               'List C - DocumentNumber': (.71 * width, .606 * height, .945 * width, .625 * height),
                               'List C - DocumentExpirationDate': (
                               .71 * width, .625 * height, .945 * width, .645 * height),
                               'List A - DocumentTitle - Second Section': (),
                               'List A - IssuingAuthority - Second Section': (),
                               'List A - DocumentNumber - Second Section': (
                               .13 * width, .645 * height, .358 * width, .663 * height),
                               'List A - DocumentExpirationDate - Second Section': (
                               .22 * width, .6624 * height, .358 * width, .683 * height),
                               'DateOfHire': (.162 * width, .711 * height, .273 * width, .726 * height),
                               # 'ApartmentNo': (.58*width,.233*height,.685*width,.2454*height)
                               }

    elif (formNumber == '03/08/13') & (page_number == 7):
        swap_coords = {'LastName': (.063 * width, .225 * height, .345 * width, .246 * height),
                                   'FirstName': (.346 * width, .226 * height, .58 * width, .246 * height),
                                   'MiddleInitial': (.58 * width, .225 * height, .66 * width, .246 * height),
                                   'MaidenName': (.665 * width, .225 * height, .94 * width, .246 * height),
                                   'StreetAddress': (.06 * width, .263 * height, .39 * width, .287 * height),
                                   'City': (.501 * width, .263 * height, .72 * width, .287 * height),
                                   'State': (.73 * width, .263 * height, .803 * width, .287 * height),
                                   'Zip': (.804 * width, .263 * height, .93 * width, .287 * height),
                                   'DateOfBirth': (.063 * width, .301 * height, .23 * width, .325 * height),
                                   'SocialSecurity': (.23 * width, .301 * height, .405 * width, .325 * height),
                                   'EmailAddress': (.408 * width, .301 * height, .75 * width, .325 * height),
                                   'Telephone': (.755 * width, .301 * height, .94 * width, .325 * height),
                                   'Attestation': (.057 * width, .385 * height, .087 * width, .48 * height),
                                   'Alien # for Permanent Residence': (
                                   .567 * width, .42 * height, .81 * width, .445 * height),
                                   'Date Expiration of Work Authorization': (
                                   .535 * width, .447 * height, .662 * width, .475 * height),
                                   'Alien # for Work Authorization': (
                                   .387 * width, .505 * height, .62 * width, .53 * height),
                                   'I-94 Admission Number': (.299 * width, .53 * height, .62 * width, .57 * height),
                                   'Foreign Passport': (.295 * width, .6 * height, .72 * width, .63 * height),
                                   'Country of Issuance': (.256 * width, .628 * height, .72 * width, .656 * height),
                                   'TranslatorName': (.063 * width, .857 * height, .94 * width, .88 * height),
                                   'TranslatorAddress': (.063 * width, .892 * height, .94 * width, .915 * height),
                                   'TranslatorDateOfSignature': (
                                   .75 * width, .822 * height, .94 * width, .834 * height)}

    elif (formNumber == '03/08/13') & (page_number == 8):
        swap_coords = {'List A - DocumentTitle': (.063 * width, .205 * height, .344 * width, .221 * height),
                                   'List A - IssuingAuthority': (
                                   .063 * width, .233 * height, .344 * width, .248 * height),
                                   'List A - DocumentNumber': (
                                   .063 * width, .259 * height, .344 * width, .276 * height),
                                   'List A - DocumentExpirationDate': (
                                   .063 * width, .2905 * height, .344 * width, .308 * height),
                                   'List A - DocumentTitle - Second Section': (
                                   .063 * width, .32 * height, .344 * width, .337 * height),
                                   'List A - IssuingAuthority - Second Section': (
                                   .063 * width, .3475 * height, .344 * width, .3632 * height),
                                   'List A - DocumentNumber - Second Section': (
                                   .063 * width, .3738 * height, .344 * width, .390 * height),
                                   'List A - DocumentExpirationDate - Second Section': (
                                   .063 * width, .4005 * height, .344 * width, .4165 * height),
                                   'List B - DocumentTitle': (.361 * width, .205 * height, .65 * width, .22 * height),
                                   'List B - IssuingAuthority': (
                                   .361 * width, .233 * height, .65 * width, .247 * height),
                                   'List B - DocumentNumber': (.361 * width, .257 * height, .65 * width, .275 * height),
                                   'List B - DocumentExpirationDate': (
                                   .361 * width, .2905 * height, .65 * width, .308 * height),
                                   'List C - DocumentTitle': (.655 * width, .205 * height, .94 * width, .222 * height),
                                   'List C - IssuingAuthority': (
                                   .655 * width, .233 * height, .94 * width, .249 * height),
                                   'List C - DocumentNumber': (.655 * width, .259 * height, .94 * width, .277 * height),
                                   'List C - DocumentExpirationDate': (
                                   .655 * width, .2905 * height, .94 * width, .308 * height),
                                   'DateOfHire': (.448 * width, .60 * height, .59 * width, .62 * height),
                                   'Name of Employee Representative': (
                                   .065 * width, .677 * height, .55 * width, .7 * height),
                                   'Title': (.61 * width, .64 * height, .9 * width, .66 * height),
                                   'EmployerBusinessName': (.58 * width, .6775 * height, .94 * width, .702 * height),
                                   'EmployerStreetAddress': (.06 * width, .7135 * height, .496 * width, .739 * height),
                                   'Date Signed by Employer': (
                                   .452 * width, .641 * height, .604 * width, .665 * height),
                                   'List A - DocumentTitle - Third Section': (
                                   .063 * width, .43 * height, .345 * width, .447 * height),
                                   'List A - IssuingAuthority - Third Section': (
                                   .063 * width, .46 * height, .345 * width, .475 * height),
                                   'List A - DocumentNumber - Third Section': (
                                   .063 * width, .487 * height, .345 * width, .506 * height),
                                   'List A - DocumentExpirationDate - Third Section': (
                                   .063 * width, .5188 * height, .345 * width, .537 * height),
                                   'Employee Info from Section 1': ()}

    elif (formNumber == '11/14/2016') & (page_number == 1):
        swap_coords = {'LastName': (.06 * width, .242 * height, .335 * width, .265 * height),
                                   'FirstName': (.34 * width, .242 * height, .582 * width, .265 * height),
                                   'MiddleInitial': (.586 * width, .242 * height, .689 * width, .265 * height),
                                   'MaidenName': (.69 * width, .242 * height, .93 * width, .265 * height),
                                   'StreetAddress': (.06 * width, .279 * height, .39 * width, .303 * height),
                                   # 'AptNo': (.395*width,.279*height,.493*width,.303*height),
                                   'City': (.494 * width, .279 * height, .738 * width, .303 * height),
                                   'State': (.74 * width, .279 * height, .802 * width, .303 * height),
                                   'Zip': (.804 * width, .279 * height, .93 * width, .303 * height),
                                   'DateOfBirth': (.06 * width, .318 * height, .241 * width, .346 * height),
                                   'SocialSecurity': (.243 * width, .319 * height, .438 * width, .346 * height),
                                   'EmailAddress': (.439 * width, .319 * height, .72 * width, .346 * height),
                                   'Telephone': (.721 * width, .318 * height, .93 * width, .346 * height),
                                   'Attestation': (.06 * width, .407 * height, .085 * width, .492 * height),
                                   'Alien # for Permanent Residence': (
                                   .573 * width, .45 * height, .775 * width, .468 * height),
                                   'Date Expiration of Work Authorization': (
                                   .573 * width, .472 * height, .705 * width, .49 * height),
                                   'Alien # for Work Authorization': (
                                       .36 * width, .534 * height, .61 * width, .559 * height),
                                   'Admission # for Work Authorization': (),
                                   'I-94 Admission Number': (.265 * width, .56 * height, .61 * width, .593 * height),
                                   'ForeignPassport': (.25 * width, .592 * height, .61 * width, .622 * height),
                                   'Country of Issuance': (.225 * width, .622 * height, .61 * width, .645 * height),
                                   'TranslatorName': (),
                                   'TranslatorAddress': (.06 * width, .865 * height, .48 * width, .886 * height),
                                   'TranslatorDateOfSignature': (
                                   .68 * width, .789 * height, .93 * width, .808 * height)}

    elif (formNumber == '11/14/2016') & (page_number == 2):
        swap_coords = {'List A - DocumentTitle': (.06 * width, .232 * height, .335 * width, .25 * height),
                                   'List A - IssuingAuthority': (
                                   .06 * width, .264 * height, .335 * width, .278 * height),
                                   'List A - DocumentNumber': (.06 * width, .29 * height, .335 * width, .306 * height),
                                   'List A - DocumentExpirationDate': (
                                   .06 * width, .32 * height, .335 * width, .334 * height),
                                   'List A - DocumentTitle - Second Section': (
                                   .06 * width, .35 * height, .335 * width, .366 * height),
                                   'List A - IssuingAuthority - Second Section': (
                                   .06 * width, .381 * height, .335 * width, .394 * height),
                                   'List A - DocumentNumber - Second Section': (
                                   .06 * width, .405 * height, .335 * width, .421 * height),
                                   'List A - DocumentExpirationDate - Second Section': (
                                   .06 * width, .434 * height, .335 * width, .45 * height),
                                   'List B - DocumentTitle': (.361 * width, .232 * height, .65 * width, .25 * height),
                                   'List B - IssuingAuthority': (
                                   .361 * width, .264 * height, .65 * width, .278 * height),
                                   'List B - DocumentNumber': (.361 * width, .29 * height, .65 * width, .306 * height),
                                   'List B - DocumentExpirationDate': (
                                   .361 * width, .32 * height, .65 * width, .334 * height),
                                   'List C - DocumentTitle': (.658 * width, .232 * height, .94 * width, .25 * height),
                                   'List C - IssuingAuthority': (
                                   .658 * width, .264 * height, .94 * width, .278 * height),
                                   'List C - DocumentNumber': (.658 * width, .29 * height, .94 * width, .306 * height),
                                   'List C - DocumentExpirationDate': (
                                   .658 * width, .32 * height, .94 * width, .334 * height),
                                   'DateOfHire': (.462 * width, .61 * height, .6 * width, .63 * height),
                                   'Name of Employee Representative': (
                                   .06 * width, .686 * height, .64 * width, .706 * height),
                                   'Title': (.62 * width, .652 * height, .942 * width, .672 * height),
                                   'EmployerBusinessName': (.662 * width, .687 * height, .942 * width, .706 * height),
                                   'EmployerStreetAddress': (.06 * width, .72 * height, .5 * width, .741 * height),
                                   'Date Signed by Employer': (.44 * width, .652 * height, .62 * width, .672 * height),
                                   'List A - DocumentTitle - Third Section': (
                                   .06 * width, .465 * height, .335 * width, .481 * height),
                                   'List A - IssuingAuthority - Third Section': (
                                   .06 * width, .495 * height, .335 * width, .509 * height),
                                   'List A - DocumentNumber - Third Section': (
                                   .06 * width, .521 * height, .335 * width, .535 * height),
                                   'List A - DocumentExpirationDate - Third Section': (
                                   .06 * width, .549 * height, .335 * width, .565 * height),
                                   'Employee Info from Section 1 - LastName': (
                                   .27 * width, .177 * height, .51 * width, .193 * height),
                                   'Employee Info from Section 1 - FirstName': (
                                   .514 * width, .177 * height, .705 * width, .193 * height),
                                   'Employee Info from Section 1 - Middle Initial': (
                                   .706 * width, .177 * height, .746 * width, .193 * height)
                                   }

    elif (formNumber == '07/17/17') & (page_number == 1):
        swap_coords = {'LastName': (.065 * width, .241 * height, .347 * width, .265 * height),
                                   'FirstName': (.35 * width, .241 * height, .592 * width, .265 * height),
                                   'MiddleInitial': (.596 * width, .241 * height, .694 * width, .265 * height),
                                   'MaidenName': (.695 * width, .241 * height, .945 * width, .265 * height),
                                   'StreetAddress': (.065 * width, .279 * height, .39 * width, .302 * height),
                                   # 'AptNo': (.405*width,.279*height,.495*width,.302*height),
                                   'City': (.5 * width, .279 * height, .74 * width, .302 * height),
                                   'State': (.746 * width, .279 * height, .805 * width, .302 * height),
                                   'Zip': (.808 * width, .279 * height, .945 * width, .302 * height),
                                   'DateOfBirth': (.066 * width, .318 * height, .25 * width, .346 * height),
                                   'SocialSecurity': (.252 * width, .318 * height, .444 * width, .345 * height),
                                   'EmailAddress': (.447 * width, .318 * height, .725 * width, .345 * height),
                                   'Telephone': (.727 * width, .318 * height, .945 * width, .344 * height),
                                   'Attestation': (.066 * width, .407 * height, .094 * width, .49 * height),
                                   'Alien # for Permanent Residence': (
                                   .57 * width, .449 * height, .78 * width, .466 * height),
                                   'Date Expiration of Work Authorization': (
                                   .57 * width, .47 * height, .72 * width, .488 * height),
                                   'Alien # for Work Authorization': (
                                   .35 * width, .537 * height, .62 * width, .557 * height),
                                   'Admission # for Work Authorization': (),
                                   'I-94 Admission Number': (.28 * width, .56 * height, .62 * width, .592 * height),
                                   'ForeignPassport': (.26 * width, .593 * height, .62 * width, .621 * height),
                                   'Country of Issuance': (.23 * width, .622 * height, .62 * width, .642 * height),
                                   'TranslatorName': (.53 * width, .82 * height, .945 * width, .84 * height),
                                   'TranslatorAddress': (.068 * width, .86 * height, .46 * width, .88 * height),
                                   'TranslatorDateOfSignature': (
                                   .688 * width, .785 * height, .945 * width, .805 * height)}

    elif (formNumber == '07/17/17') & (page_number == 2):
        swap_coords = {'List A - DocumentTitle': (.068 * width, .231 * height, .34 * width, .249 * height),
                                   'List A - IssuingAuthority': (
                                   .068 * width, .261 * height, .34 * width, .277 * height),
                                   'List A - DocumentNumber': (.068 * width, .287 * height, .34 * width, .304 * height),
                                   'List A - DocumentExpirationDate': (
                                   .068 * width, .317 * height, .34 * width, .333 * height),
                                   'List A - DocumentTitle - Second Section': (
                                   .068 * width, .348 * height, .34 * width, .365 * height),
                                   'List A - IssuingAuthority - Second Section': (
                                   .068 * width, .377 * height, .34 * width, .393 * height),
                                   'List A - DocumentNumber - Second Section': (
                                       .068 * width, .402 * height, .34 * width, .419 * height),
                                   'List A - DocumentExpirationDate - Second Section': (
                                   .068 * width, .432 * height, .34 * width, .448 * height),
                                   'List B - DocumentTitle': (.365 * width, .233 * height, .655 * width, .25 * height),
                                   'List B - IssuingAuthority': (
                                   .365 * width, .261 * height, .655 * width, .277 * height),
                                   'List B - DocumentNumber': (
                                   .365 * width, .287 * height, .655 * width, .304 * height),
                                   'List B - DocumentExpirationDate': (
                                   .365 * width, .317 * height, .655 * width, .333 * height),
                                   'List C - DocumentTitle': (.658 * width, .233 * height, .94 * width, .25 * height),
                                   'List C - IssuingAuthority': (
                                   .658 * width, .262 * height, .94 * width, .277 * height),
                                   'List C - DocumentNumber': (.658 * width, .287 * height, .94 * width, .304 * height),
                                   'List C - DocumentExpirationDate': (
                                   .658 * width, .317 * height, .94 * width, .333 * height),
                                   'DateOfHire': (.464 * width, .61 * height, .61 * width, .628 * height),
                                   'Name of Employee Representative': (
                                   .068 * width, .684 * height, .64 * width, .703 * height),
                                   'Title': (.625 * width, .649 * height, .945 * width, .669 * height),
                                   'EmployerBusinessName': (.666 * width, .684 * height, .945 * width, .703 * height),
                                   'EmployerStreetAddress': (.068 * width, .713 * height, .5 * width, .737 * height),
                                   'Date Signed by Employer': (
                                   .443 * width, .649 * height, .623 * width, .669 * height),
                                   'List A - DocumentTitle - Third Section': (
                                   .068 * width, .462 * height, .34 * width, .479 * height),
                                   'List A - IssuingAuthority - Third Section': (
                                   .068 * width, .492 * height, .34 * width, .506 * height),
                                   'List A - DocumentNumber - Third Section': (
                                   .068 * width, .517 * height, .34 * width, .532 * height),
                                   'List A - DocumentExpirationDate - Third Section': (
                                   .068 * width, .546 * height, .34 * width, .562 * height),
                                   'Employee Info from Section 1 - LastName': (
                                   .274 * width, .175 * height, .514 * width, .192 * height),
                                   'Employee Info from Section 1 - FirstName': (
                                   .516 * width, .175 * height, .708 * width, .192 * height),
                                   'Employee Info from Section 1 - Middle Initial': (
                                   .71 * width, .177 * height, .748 * width, .192 * height)
                                   }

    elif (formNumber == '11-21-91(L)'):
        swap_coords = {'LastName': (.09 * width, .155 * height, .36 * width, .173 * height),
                                 'FirstName': (.37 * width, .155 * height, .53 * width, .173 * height),
                                 'MiddleInitial': (.54 * width, .155 * height, .64 * width, .173 * height),
                                 'MaidenName': (.645 * width, .155 * height, .9 * width, .173 * height),
                                 'StreetAddress': (.09 * width, .182 * height, .52 * width, .198 * height),
                                 'City': (.09 * width, .208 * height, .345 * width, .222 * height),
                                 'State': (.346 * width, .208 * height, .53 * width, .222 * height),
                                 'Zip': (.54 * width, .208 * height, .64 * width, .222 * height),
                                 'DateOfBirth': (.645 * width, .182 * height, .9 * width, .198 * height),
                                 'SocialSecurity': (.645 * width, .208 * height, .8 * width, .222 * height),
                                 'Attestation': (.495 * width, .233 * height, .512 * width, .264 * height),
                                 'Alien # for Permanent Residence': (
                                 .722 * width, .242 * height, .89 * width, .254 * height),
                                 'Date Expiration of Work Authorization': (
                                 .679 * width, .254 * height, .79 * width, .265 * height),
                                 'Alien # for Work Authorization': (
                                 .637 * width, .264 * height, .89 * width, .273 * height),
                                 'Admission # for Work Authorization': (),
                                 'I-94 Admission Number': (),
                                 'ForeignPassport': (),
                                 'Country of Issuance': (),
                                 'TranslatorName': (.501 * width, .343 * height, .78 * width, .355 * height),
                                 'TranslatorAddress': (.15 * width, .365 * height, .62 * width, .379 * height),
                                 'TranslatorDateOfSignature': (.64 * width, .365 * height, .8 * width, .379 * height),
                                 'List A - DocumentTitle': (.171 * width, .433 * height, .328 * width, .448 * height),
                                 'List A - IssuingAuthority': (
                                 .181 * width, .452 * height, .328 * width, .468 * height),
                                 'List A - DocumentNumber': (.17 * width, .469 * height, .328 * width, .486 * height),
                                 'List A - DocumentExpirationDate': (
                                 .24 * width, .49 * height, .329 * width, .507 * height),
                                 'List B - DocumentTitle': (.375 * width, .433 * height, .595 * width, .448 * height),
                                 'List B - IssuingAuthority': (
                                 .375 * width, .452 * height, .595 * width, .468 * height),
                                 'List B - DocumentNumber': (.375 * width, .469 * height, .595 * width, .486 * height),
                                 'List B - DocumentExpirationDate': (
                                 .405 * width, .49 * height, .49 * width, .507 * height),
                                 'List C - DocumentTitle': (.63 * width, .433 * height, .87 * width, .448 * height),
                                 'List C - IssuingAuthority': (.63 * width, .452 * height, .87 * width, .468 * height),
                                 'List C - DocumentNumber': (.63 * width, .469 * height, .87 * width, .486 * height),
                                 'List C - DocumentExpirationDate': (
                                 .66 * width, .49 * height, .765 * width, .506 * height),
                                 'List A - DocumentTitle - Second Section': (),
                                 'List A - IssuingAuthority - Second Section': (),
                                 'List A - DocumentNumber - Second Section': (
                                 .17 * width, .507 * height, .328 * width, .525 * height),
                                 'List A - DocumentExpirationDate - Second Section': (
                                 .24 * width, .528 * height, .329 * width, .545 * height),
                                 'DateOfHire': (.401 * width, .574 * height, .526 * width, .585 * height)
                                 # 'ApartmentNo': ()
                                 }

    elif (formNumber == '11-21-91(R)'):
        swap_coords = {'LastName': (.048 * width, .167 * height, .36 * width, .189 * height),
                                 'FirstName': (.361 * width, .167 * height, .564 * width, .189 * height),
                                 'MiddleInitial': (.57 * width, .167 * height, .676 * width, .189 * height),
                                 'MaidenName': (.68 * width, .167 * height, .96 * width, .189 * height),
                                 'StreetAddress': (.048 * width, .202 * height, .565 * width, .221 * height),
                                 'City': (.048 * width, .23 * height, .33 * width, .251 * height),
                                 'State': (.33 * width, .23 * height, .565 * width, .251 * height),
                                 'Zip': (.57 * width, .23 * height, .676 * width, .251 * height),
                                 'DateOfBirth': (.68 * width, .202 * height, .96 * width, .221 * height),
                                 'SocialSecurity': (.68 * width, .232 * height, .9 * width, .25 * height),
                                 'Attestation': (.515 * width, .262 * height, .535 * width, .306 * height),
                                 'Alien # for Permanent Residence': (
                                 .779 * width, .274 * height, .9 * width, .288 * height),
                                 'Date Expiration of Work Authorization': (
                                 .733 * width, .289 * height, .83 * width, .302 * height),
                                 'Alien # for Work Authorization': (
                                 .682 * width, .302 * height, .836 * width, .315 * height),
                                 'Admission # for Work Authorization': (),
                                 'I-94 Admission Number': (),
                                 'ForeignPassport': (),
                                 'Country of Issuance': (),
                                 'TranslatorName': (.515 * width, .395 * height, .87 * width, .41 * height),
                                 'TranslatorAddress': (.1 * width, .4213 * height, .66 * width, .439 * height),
                                 'TranslatorDateOfSignature': (.68 * width, .4213 * height, .87 * width, .439 * height),
                                 'List A - DocumentTitle': (.14 * width, .498 * height, .32 * width, .518 * height),
                                 'List A - IssuingAuthority': (.15 * width, .52 * height, .32 * width, .54 * height),
                                 'List A - DocumentNumber': (.14 * width, .547 * height, .32 * width, .562 * height),
                                 'List A - DocumentExpirationDate': (
                                 .22 * width, .573 * height, .32 * width, .588 * height),
                                 'List B - DocumentTitle': (.375 * width, .498 * height, .63 * width, .518 * height),
                                 'List B - IssuingAuthority': (.375 * width, .52 * height, .63 * width, .54 * height),
                                 'List B - DocumentNumber': (.375 * width, .547 * height, .63 * width, .562 * height),
                                 'List B - DocumentExpirationDate': (
                                 .395 * width, .573 * height, .505 * width, .588 * height),
                                 'List C - DocumentTitle': (.67 * width, .498 * height, .93 * width, .518 * height),
                                 'List C - IssuingAuthority': (.67 * width, .52 * height, .93 * width, .54 * height),
                                 'List C - DocumentNumber': (.67 * width, .547 * height, .93 * width, .562 * height),
                                 'List C - DocumentExpirationDate': (
                                 .705 * width, .573 * height, .81 * width, .588 * height),
                                 'List A - DocumentTitle - Second Section': (),
                                 'List A - IssuingAuthority - Second Section': (),
                                 'List A - DocumentNumber - Second Section': (),
                                 'List A - DocumentExpirationDate - Second Section': (
                                 .22 * width, .618 * height, .32 * width, .635 * height),
                                 'DateOfHire': (.396 * width, .671 * height, .492 * width, .683 * height)
                                 # 'ApartmentNo': (.566*width,.20*height,.676*width,.221*height)
                                 }

    if len(swap_coords) > 0:
        return swap_coords
    else:
        return -1

def findCheckBox(image, form_number):
    no_page_number = ['05/07/87', '11-21-91(L)', '06/05/07']

    if form_number in no_page_number:
        boxes = 3
    else:
        boxes = 4
    #resize image
    swap = resize(image, 50, 200)
    #convert image to data array
    data = np.asarray(PIL.Image.open(swap))
    #find the height of the image to divide it
    width = data.shape[0]
    #create empty dicts to store values
    crops = {}
    means = {}
    #add the crop arrays and their means
    for i in range(4):
        crops["box" + str(i + 1)] = data[int(width/boxes)*i:int(width/boxes)*(i+1),:]
        means["box" + str(i + 1)] = crops["box" + str(i + 1)].mean()
    #find the maximum and minimum value from the dict and the range
    key_max = max(means.keys(), key=(lambda k: means[k]))
    key_min = min(means.keys(), key=(lambda k: means[k]))
    value_max = means[key_max]
    value_min = means[key_min]
    value_range = value_max - value_min
    if value_range > 0.03:
        return(min(means, key = means.get))
    else:
        return("no box")

def resize(item, width, height):
    im = PIL.Image.open(item)
    im = im.resize((width,height), PIL.Image.ANTIALIAS)
    swap = io.BytesIO()
    im.save(swap, 'png')
    return swap

def crop(image, coords):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = PIL.Image.open(image)
    cropped_image = image_obj.crop(coords)
    swap = io.BytesIO()
    cropped_image.save(swap, 'png')
    return swap

# Put the incoming FlowFile into a dataframe
flowFile = sys.stdin.buffer.read()
flowFile = io.BytesIO(flowFile)

# flowFile = open('../ocr/TestDataFiles/james_bond.pdf', 'rb')

# Declare the empty list of PNGs
PNGs = []

# convert multipage pdf to a list of images
with Image(file=flowFile, resolution=200) as img:
    # loop through pages of PDF and convert each into a separate PNG
    for i, page in enumerate(img.sequence):
        with Image(page) as im:
            im.alpha_channel = False
            im.format = 'png'

            swapPNG = io.BytesIO()
            im.save(swapPNG)
            PNGs.append(swapPNG)

for page in PNGs:
    form_number = findFormNumber(page)
    page_number = findPageNumber(page)

    coords = getImageCoords(page, form_number, page_number)
    if coords != -1:
        if 'Attestation' in coords.keys():
            att_box_image = crop(page, coords['Attestation'])
            att_box = findCheckBox(page, form_number)
            break
    else:
        att_box = 'Form or page number not found'

if att_box in 'box1':
    attestation = 'Citizen'
elif att_box in 'box2':
    attestation = 'Non-citizen national'
elif att_box in 'box3':
    attestation = 'Lawful permanent resident'
elif att_box in 'box4':
    attestation = 'Alien authorized to work'
else:
    attestation = 'Not Found'

sys.stdout.write(attestation)