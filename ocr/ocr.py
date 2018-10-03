# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:13:29 2018

@author: Brandon Croarkin
"""

from wand.image import Image
import numpy as np
import pandas as pd
#import sys
import io
import PIL
import pytesseract
import re
#import json
import os
import matplotlib.pyplot as plt
from fuzzywuzzy import process
#from fuzzywuzzy import fuzz

image_coords_020209 = {}
image_coords_050787 = {}
image_coords_060507 = {}
image_coords_080709 = {}
image_coords_053105 = {}
image_coords_030813_pg7 = {}
image_coords_030813_pg8 = {}
image_coords_071717_pg1 = {} 
image_coords_071717_pg2 = {}
image_coords_111416_pg1 = {} 
image_coords_111416_pg2 = {}
image_coords_112191_L = {}
image_coords_112191_R = {}

def findFileName(file):
    """
    Removes all .* endings from a file to get just the filename
    """
    (name, ext) = os.path.splitext(file)
    return(name)


def findFormNumber(file):
    """
    @@file - the file to find the form number of
    This function takes in a file and spits out the form number associated with it
    """        
    image = file
    im = PIL.Image.open(image)
    width, height = im.size
    
    #list of possible form choices
    choices = ['11-21-91(R)', '05/31/05', '07/17/17', '08/07/09',
               '11/14/2016', '02/02/09', '03/08/13','05/07/87', 
               '11-21-91(L)', '06/05/07']
    
    while True:
        try:    
            swap = crop(image, (.04*width,.954*height,.95*width,.98*height))
            #run tesseract on crop
            text = pytesseract.image_to_string(PIL.Image.open(swap))
            #clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
            matches = re.findall('(\d{2}[\/ ](\d{2}|January|Jan|February|Feb|March|Mar|April|Apr|May|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)[\/ ]\d{2,4})'
                     , text)
            #return output
            if matches:
                for match in matches:
                    query = match[0]
                    #get a list of matches ordered by score
                    return(process.extractOne(query, choices)[0])
                    break
                
            elif not matches:
                swap = crop(image, (.04*width,.945*height,.95*width,.97*height))
    
                #run tesseract on crop
                text = pytesseract.image_to_string(PIL.Image.open(swap))
    
                #clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
                matches = re.findall('(\d{2}[\/ ](\d{2}|January|Jan|February|Feb|March|Mar|April|Apr|May|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)[\/ ]\d{2,4})'
                     , text)
        
                #output answer
                for match in matches:
                    query = match[0]
                    #get a list of matches ordered by score
                    return(process.extractOne(query, choices)[0])
                    break
                
            elif not matches:
                swap = crop(image, (.04*width,.925*height,.95*width,.955*height))

                #run tesseract on crop
                text = pytesseract.image_to_string(PIL.Image.open(swap))
    
                #clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
                matches = re.findall('(\d{2}[\/ ](\d{2}|January|Jan|February|Feb|March|Mar|April|Apr|May|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)[\/ ]\d{2,4})'
                     , text)
        
                #output answer
                for match in matches:
                    query = match[0]
                    #get a list of matches ordered by score
                    return(process.extractOne(query, choices)[0])
                    break
    
            if not matches:
                swap = crop(image, (.04*width,.907*height,.95*width,.925*height))
            
                #run tesseract on crop
                text = pytesseract.image_to_string(PIL.Image.open(swap))
            
                #clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
                matches = re.findall('(\d{2}[\/ ](\d{2}|January|Jan|February|Feb|March|Mar|April|Apr|May|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)[\/ ]\d{2,4})'
                             , text)
                
                #output answer
                for match in matches:
                    query = match[0]
                    #get a list of matches ordered by score
                    return(process.extractOne(query, choices)[0])
                    break
            
            if not matches:
                swap = crop(image, (.04*width,.925*height,.955*width,.955*height))
            
                #run tesseract on crop
                text = pytesseract.image_to_string(PIL.Image.open(swap))
            
                #clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
                matches = re.findall('(\d{2}[\- ](\d{2}|January|Jan|February|Feb|March|Mar|April|Apr|May|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)[\- ]\d{2,4})'
                             , text)
                
                #output answer
                for match in matches:
                    query = match[0]+'(R)'
                    #get a list of matches ordered by score
                    return(process.extractOne(query, choices)[0])
                    break
                    
            if not matches:
                swap = crop(image, (.04*width,.80*height,.955*width,.83*height))
            
                #run tesseract on crop
                text = pytesseract.image_to_string(PIL.Image.open(swap))
            
                #clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
                matches = re.findall('(\d{2}[\- ](\d{2}|January|Jan|February|Feb|March|Mar|April|Apr|May|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)[\- ]\d{2,4})'
                             , text)
                
                #output answer
                for match in matches:
                    query = match[0]+'(L)'
                    #get a list of matches ordered by score
                    return(process.extractOne(query, choices)[0])
                    break
            
            if not matches: 
                swap = crop(image, (.04*width,.955*height,.95*width,.98*height))
            
                #run tesseract on crop
                text = pytesseract.image_to_string(PIL.Image.open(swap))
            
                #clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
                matches = re.findall('(\d{2}[\- ](\d{2}|January|Jan|February|Feb|March|Mar|April|Apr|May|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)[\- ]\d{2,4})'
                             , text)
                
                #output answer
                for match in matches:
                    query = match[0]+'(R)'
                    #get a list of matches ordered by score
                    return(process.extractOne(query, choices)[0])
                    break
                    
            if not matches:
                return('not found')
                break
        
        except IOError:
            return('image file is truncated')
            break
        
def findPageNumber(file):
    """
    @@file file to determine page number of
    This function intakes a file and spits out the page number based on
    cropping the file to find a page number
    """        
    #crop bottom of image
    image = file
    im = PIL.Image.open(image)
    width, height = im.size
    
    #list of possible page numbers (can't be page 0 and there is no form that has a page 1o)
    choices = ['1','2','3','4','5','6','7','8','9']
    
    while True:
        try:    
            swap = crop(image, (.04*width,.955*height,.95*width,.98*height))
            #run tesseract on crop
            text = pytesseract.image_to_string(PIL.Image.open(swap))
            #clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
            matches = re.findall('Page (\d+)', text)
            #return output
            if matches:
                for match in matches:
                    query = match[0]
                    #get the top match ordered by score
                    return(int(process.extractOne(query, choices)[0]))
                    break
                
            elif not matches:
                swap = crop(image, (.04*width,.945*height,.95*width,.97*height))
    
                #run tesseract on crop
                text = pytesseract.image_to_string(PIL.Image.open(swap))
    
                #clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
                matches = re.findall('Page (\d+)', text)
        
                #output answer
                for match in matches:
                    query = match[0]
                    #get the top match ordered by score
                    return(int(process.extractOne(query, choices)[0]))                
                    break
                
            elif not matches:
                swap = crop(image, (.04*width,.925*height,.95*width,.955*height))
    
                #run tesseract on crop
                text = pytesseract.image_to_string(PIL.Image.open(swap))
    
                #clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
                matches = re.findall('Page (\d+)', text)
        
                #output answer
                for match in matches:
                    query = match[0]
                    #get the top match ordered by score
                    return(int(process.extractOne(query, choices)[0]))
                    break
    
            if not matches:
                swap = crop(image, (.04*width,.907*height,.95*width,.925*height))
            
                #run tesseract on crop
                text = pytesseract.image_to_string(PIL.Image.open(swap))
            
                #clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
                matches = re.findall('Page (\d+)', text)
                
                #output answer
                for match in matches:
                    query = match[0]
                    #get the top match ordered by score
                    return(int(process.extractOne(query, choices)[0]))
                    break
            
            if not matches:
                swap = crop(image, (.04*width,.925*height,.95*width,.955*height))
            
                #run tesseract on crop
                text = pytesseract.image_to_string(PIL.Image.open(swap))
            
                #clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
                matches = re.findall('Page (\d+)', text)
                
                #output answer
                for match in matches:
                    query = match[0]
                    #get the top match ordered by score
                    return(int(process.extractOne(query, choices)[0]))               
                    break
                    
            if not matches:
                swap = crop(image, (.04*width,.80*height,.95*width,.83*height))
            
                #run tesseract on crop
                text = pytesseract.image_to_string(PIL.Image.open(swap))
            
                #clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
                matches = re.findall('Page (\d+)', text)
                
                #output answer
                for match in matches:
                    query = match[0]
                    #get the top match ordered by score
                    return(int(process.extractOne(query, choices)[0]))
                    break
            
            if not matches: 
                swap = crop(image, (.04*width,.955*height,.95*width,.98*height))
            
                #run tesseract on crop
                text = pytesseract.image_to_string(PIL.Image.open(swap))
            
                #clean output to just pull revision date with either dd/mm/yy or dd-mm-yy format
                matches = re.findall('Page (\d+)', text)
                
                #output answer
                for match in matches:
                    query = match[0]
                    #get the top match ordered by score
                    return(int(process.extractOne(query, choices)[0]))
                    break
                    
            if not matches:
                return('not found')
                break
        
        except IOError:
            return("image file is truncated")
            break

def setImageCoords(file, formNumber, page_number):
    image = file
    im = PIL.Image.open(image)
    width, height = im.size
    
    if formNumber == '02/02/09':
        #listing out the (x1, y1, x2, y2) coordinates of information on each of 
        #the different forms
        global image_coords_020209
        image_coords_020209 = {'LastName':(.055*width,.180*height,.37*width,.204*height),
                        'FirstName': (.368*width,.180*height,.61*width,.205*height), 
                        'MiddleInitial': (.610*width,.180*height,.686*width,.205*height),
                        'MaidenName': (.69*width,.18*height,.94*width,.205*height),
                        'StreetAddress': (.055*width,.217*height,.58*width,.240*height),
                        'City': (.055*width,.252*height,.35*width,.275*height),
                        'DateOfBirth': (.688*width,.217*height,.95*width,.240*height),
                        'SocialSecurity': (.688*width,.253*height,.9*width,.275*height),
                        'State': (.345*width,.252*height,.58*width,.275*height),
                        'Zip': (.58*width,.252*height,.688*width,.275*height),
                        'EmailAddress': (),
                        'Telephone': (),
                        'Attestation': (.49*width,.292*height,.515*width,.365*height),
                        'Alien # for Permanent Residence': (.722*width,.325*height,.94*width,.345*height),
                        'Date Expiration of Work Authorization': (.805*width,.362*height,.955*width,.377*height),
                        'Alien # for Work Authorization': (.81*width,.346*height,.955*width,.365*height),
                        'I-94 Admission Number': (),
                        'Foreign Passport': (),
                        'Country of Issuance': (),
                        'TranslatorName': (.513*width,.443*height,.94*width,.469*height),
                        'TranslatorAddress': (.104*width,.482*height,.67*width,.505*height),
                        'TranslatorDateOfSignature': (.68*width,.482*height,.94*width,.505*height),
                        'List A - DocumentTitle': (.145*width,.564*height,.363*width,.586*height),
                        'List A - IssuingAuthority': (.15*width,.586*height,.363*width,.605*height),
                        'List A - DocumentNumber': (.126*width,.606*height,.363*width,.625*height),
                        'List A - DocumentExpirationDate': (.215*width,.625*height,.363*width,.644*height),
                        'List A - DocumentTitle - Second Section': (),
                        'List A - IssuingAuthority - Second Section': (),
                        'List A - DocumentNumber - Second Section': (.13*width,.644*height,.363*width,.662*height),
                        'List A - DocumentExpirationDate - Second Section': (.215*width,.662*height,.363*width,.682*height),
                        'List B - DocumentTitle': (.38*width,.561*height,.64*width,.585*height),
                        'List B - IssuingAuthority': (.38*width,.585*height,.64*width,.605*height),
                        'List B - DocumentNumber': (.38*width,.6052*height,.64*width,.6245*height),
                        'List B - DocumentExpirationDate': (.38*width,.6245*height,.64*width,.6445*height),
                        'List C - DocumentTitle': (.7*width,.561*height,.95*width,.585*height),
                        'List C - IssuingAuthority': (.7*width,.585*height,.95*width,.605*height),
                        'List C - DocumentNumber': (.7*width,.6052*height,.95*width,.6245*height),
                        'List C - DocumentExpirationDate': (.7*width,.6245*height,.95*width,.6445*height),
                        'DateOfHire': (.16*width,.711*height,.278*width,.726*height),
                        'Name of Employee Representative': (.394*width,.752*height,.698*width,.777*height),
                        'Title': (.698*width,.752*height,.95*width,.777*height),
                        'EmployerBusinessName': (.05*width,.7875*height,.698*width,.808*height),
                        'EmployerStreetAddress': (),
                        'Date Signed by Employer': (.698*width,.7875*height,.95*width,.808*height),
                        'List A - DocumentTitle - Third Section': (),
                        'List A - IssuingAuthority - Third Section': (),
                        'List A - DocumentNumber - Third Section': (),
                        'List A - DocumentExpirationDate - Third Section': (),
                        'Employee Info from Section 1': ()}
     
    elif formNumber == '08/07/09':
        global image_coords_080709
        image_coords_080709 = {'LastName':(.055*width,.18*height,.37*width,.205*height),
                        'FirstName': (.37*width,.18*height,.61*width,.205*height), 
                        'MiddleInitial': (.61*width,.18*height,.685*width,.205*height),
                        'MaidenName': (),
                        'StreetAddress': (.055*width,.215*height,.58*width,.24*height),
                        'City': (.055*width,.251*height,.34*width,.277*height),
                        'State': (.34*width,.251*height,.58*width,.277*height),
                        'Zip': (.58*width,.251*height,.68*width,.275*height),
                        'DateOfBirth': (.693*width,.205*height,.94*width,.239*height),
                        'SocialSecurity': (.692*width,.2525*height,.9*width,.276*height),
                        'Attestation': (.492*width,.29*height,.517*width,.367*height),
                        'Alien # for Permanent Residence': (.727*width,.325*height,.945*width,.345*height),
                        'Date Expiration of Work Authorization': (),
                        'I-94 Admission Number': (),
                        'ForeignPassport': (),
                        'Country of Issuance': (),
                        'Alien # for Work Authorization': (.81*width,.345*height,.94*width,.363*height),
                        'TranslatorName': (.515*width,.445*height,.88*width,.467*height),
                        'TranslatorAddress': (),
                        'TranslatorDateOfSignature': (),
                        'List A - DocumentTitle': (.143*width,.561*height,.36*width,.586*height),
                        'List A - IssuingAuthority': (.153*width,.586*height,.358*width,.6*height),
                        'List A - DocumentNumber': (.133*width,.606*height,.358*width,.62*height),
                        'List A - DocumentExpirationDate': (.225*width,.625*height,.351*width,.64*height),
                        'List B - DocumentTitle': (.393*width,.561*height,.625*width,.583*height),
                        'List B - IssuingAuthority': (.393*width,.586*height,.625*width,.6*height),
                        'List B - DocumentNumber': (.393*width,.606*height,.625*width,.62*height),
                        'List B - DocumentExpirationDate': (.393*width,.625*height,.625*width,.64*height),
                        'List C - DocumentTitle': (.713*width,.561*height,.945*width,.586*height),
                        'List C - IssuingAuthority': (.713*width,.586*height,.945*width,.6*height),
                        'List C - DocumentNumber': (.713*width,.606*height,.945*width,.625*height),
                        'List C - DocumentExpirationDate': (.713*width,.625*height,.945*width,.64*height),
                        'List A - DocumentNumber - Second Section': (.133*width,.645*height,.358*width,.663*height),                
                        'List A - DocumentExpirationDate -  Second Section': (.223*width,.6624*height,.358*width,.68*height),
                        'DateOfHire': (),
                        #'ApartmentNo': (.57*width,.205*height,.66*width,.241*height)
                        }
        
    elif formNumber == '05/07/87':   
        global image_coords_050787
        image_coords_050787 = {'LastName':(.075*width,.133*height,.38*width,.1525*height),
                'FirstName': (.38*width,.133*height,.56*width,.1525*height), 
                'MiddleInitial': (.56*width,.133*height,.74*width,.1525*height),
                'MaidenName': (.74*width,.133*height,.95*width,.1525*height),
                'StreetAddress': (.08*width,.1612*height,.38*width,.182*height),
                'City': (.38*width,.1612*height,.56*width,.182*height),
                'State': (.56*width,.1612*height,.735*width,.182*height),
                'Zip': (.735*width,.1612*height,.92*width,.182*height),
                'DateOfBirth': (.07*width,.1923*height,.41*width,.211*height),
                'SocialSecurity': (.51*width,.194*height,.8*width,.211*height),
                'EmailAddress': (),
                'Telephone': (),
                'Attestation': (.085*width,.228*height,.12*width,.275*height),
                'Alien # for Permanent Residence': (.503*width,.24*height,.655*width,.26*height),
                'Date Expiration of Work Authorization': (.62*width,.2735*height,.78*width,.29*height),
                'Alien # for Work Authorization': (.732*width,.26*height,.911*width,.276*height),
                'Admission # for Work Authorization': (.235*width,.2735*height,.369*width,.29*height),
                'I-94 Admission Number': (),
                'ForeignPassport': (),
                'Country of Issuance': (),
                'TranslatorName': (.51*width,.406*height,.833*width,.424*height),
                'TranslatorAddress': (),
                'TranslatorDateOfSignature': (),
                'List A - DocumentTitle': (.06*width,.632*height,.09*width,.72*height),
                'List A - IssuingAuthority': (),
                'List A - DocumentNumber': (.076*width,.782*height,.315*width,.8*height),
                'List A - DocumentExpirationDate': (.067*width,.827*height,.315*width,.845*height),
                'List B - DocumentTitle': (.38*width,.61*height,.4*width,.73*height),
                'List B - IssuingAuthority': (),
                'List B - DocumentNumber': (.3913*width,.782*height,.63*width,.8*height),
                'List B - DocumentExpirationDate': (.3913*width,.827*height,.63*width,.845*height),
                'List C - DocumentTitle': (.7*width,.61*height,.72*width,.73*height),
                'List C - IssuingAuthority': (),
                'List C - DocumentNumber': (.712*width,.782*height,.95*width,.8*height),
                'List C - DocumentExpirationDate': (.712*width,.827*height,.95*width,.845*height),
                'DateOfHire': (),
                'Name of Employee Representative': (.42*width,.905*height,.8*width,.924*height),
                'Title': (.8*width,.905*height,.95*width,.924*height),
                'EmployerBusinessName': (.07*width,.936*height,.4*width,.954*height),
                'EmployerStreetAddress': (.42*width,.935*height,.80*width,.954*height),
                'Date Signed by Employer': (.785*width,.925*height,.95*width,.953*height),
                'List A - DocumentTitle - Third Section': (),
                'List A - IssuingAuthority - Third Section': (),
                'List A - DocumentNumber - Third Section': (),
                'List A - DocumentExpirationDate - Third Section': (),
                'Employee Info from Section 1': ()}
        
    elif formNumber == '05/31/05':
        global image_coords_053105
        image_coords_053105 = {'LastName':(.05*width,.168*height,.37*width,.189*height),
                'FirstName': (.37*width,.168*height,.57*width,.189*height), 
                'MiddleInitial': (.57*width,.168*height,.67*width,.189*height),
                'MaidenName': (.68*width,.168*height,.95*width,.189*height),
                'StreetAddress': (.05*width,.202*height,.67*width,.22*height),
                'City': (.05*width,.233*height,.34*width,.251*height),
                'State': (.34*width,.233*height,.57*width,.251*height),
                'Zip': (.57*width,.233*height,.67*width,.251*height),
                'DateOfBirth': (.68*width,.203*height,.95*width,.22*height),
                'SocialSecurity': (.68*width,.233*height,.90*width,.251*height),
                'EmailAddress': (),
                'Telephone': (),
                'Attestation': (.515*width,.263*height,.538*width,.32*height),
                'Alien # for Permanent Residence': (.782*width,.285*height,.97*width,.305*height),
                'Date Expiration of Work Authorization': (.73*width,.3026*height,.815*width,.32*height),
                'Alien # for Work Authorization': (.682*width,.3152*height,.97*width,.331*height),
                'Admission # for Work Authorization': (),
                'I-94 Admission Number': (),
                'ForeignPassport': (),
                'Country of Issuance': (),
                'TranslatorName': ((.513*width,.41*height,.88*width,.423*height)),
                'TranslatorAddress': (.1*width,.436*height,.67*width,.454*height),
                'TranslatorDateOfSignature': (.68*width,.436*height,.88*width,.454*height),
                'List A - DocumentTitle': (.14*width,.513*height,.34*width,.534*height),
                'List A - IssuingAuthority': (.15*width,.533*height,.34*width,.558*height),
                'List A - DocumentNumber': (.14*width,.558*height,.34*width,.579*height),
                'List A - DocumentExpirationDate': (.22*width,.581*height,.34*width,.605*height),
                'List B - DocumentTitle': (.38*width,.513*height,.618*width,.534*height),
                'List B - IssuingAuthority': (.38*width,.533*height,.618*width,.558*height),
                'List B - DocumentNumber': (.38*width,.558*height,.618*width,.579*height),
                'List B - DocumentExpirationDate': (.38*width,.581*height,.618*width,.605*height),
                'List C - DocumentTitle': (.7*width,.513*height,.96*width,.534*height),
                'List C - IssuingAuthority': (.7*width,.533*height,.96*width,.558*height),
                'List C - DocumentNumber': (.7*width,.558*height,.96*width,.579*height),
                'List C - DocumentExpirationDate': (.7*width,.581*height,.96*width,.605*height),
                'DateOfHire': (.398*width,.686*height,.491*width,.7*height),
                'Name of Employee Representative': (.394*width,.739*height,.68*width,.758*height),
                'Title': (.69*width,.739*height,.96*width,.758*height),
                'EmployerBusinessName': (.04*width,.772*height,.305*width,.797*height),
                'EmployerStreetAddress': (.307*width,.772*height,.685*width,.797*height),
                'Date Signed by Employer': (.688*width,.772*height,.96*width,.797*height),
                'List A - DocumentTitle - Third Section': (.13*width,.605*height,.34*width,.627*height),
                'List A - IssuingAuthority - Third Section': (),
                'List A - DocumentNumber - Third Section': (),
                'List A - DocumentExpirationDate - Third Section': (.22*width,.63*height,.34*width,.656*height),
                'Employee Info from Section 1 - LastName': (),
                'Employee Info from Section 1 - FirstName': (), 
                'Employee Info from Section 1 - Middle Initial': ()
                }
        
    elif formNumber == '06/05/07': 
        global image_coords_060507
        image_coords_060507 = {'LastName':(.055*width,.197*height,.36*width,.221*height),
                'FirstName': (.36*width,.197*height,.58*width,.221*height), 
                'MiddleInitial': (.58*width,.197*height,.685*width,.221*height),
                'MaidenName': (.688*width,.197*height,.95*width,.221*height),
                'StreetAddress': (.055*width,.233*height,.57*width,.257*height),
                'City': (.055*width,.257*height,.35*width,.291*height),
                'State': (.35*width,.257*height,.57*width,.291*height),
                'Zip': (.58*width,.257*height,.685*width,.291*height),
                'DateOfBirth': (.69*width,.233*height,.95*width,.25*height),
                'SocialSecurity': (.688*width,.2685*height,.88*width,.291*height),
                'Attestation': (.45*width,.306*height,.4752*width,.355*height),
                'Alien # for Permanent Residence': (.71*width,.318*height,.95*width,.332*height),
                'Date Expiration of Work Authorization': (.652*width,.332*height,.95*width,.349*height),
                'Alien # for Work Authorization': (.61*width,.349*height,.95*width,.368*height),
                'Admission # for Work Authorization': (),
                'I-94 Admission Number': (),
                'ForeignPassport': (),
                'Country of Issuance': (),
                'TranslatorName': (.515*width,.433*height,.88*width,.469*height),
                'TranslatorAddress': (.1*width,.47*height,.677*width,.497*height),
                'TranslatorDateOfSignature': (.678*width,.47*height,.9*width,.497*height),
                'List A - DocumentTitle': (.14*width,.561*height,.36*width,.59*height),
                'List A - IssuingAuthority': (.15*width,.586*height,.358*width,.607*height),
                'List A - DocumentNumber': (.13*width,.606*height,.358*width,.625*height),
                'List A - DocumentExpirationDate': (.225*width,.625*height,.351*width,.645*height),
                'List B - DocumentTitle': (.39*width,.561*height,.625*width,.586*height),
                'List B - IssuingAuthority': (.39*width,.586*height,.625*width,.607*height),
                'List B - DocumentNumber': (.39*width,.606*height,.625*width,.625*height),
                'List B - DocumentExpirationDate': (.39*width,.625*height,.625*width,.645*height),
                'List C - DocumentTitle': (.71*width,.561*height,.945*width,.586*height),
                'List C - IssuingAuthority': (.71*width,.586*height,.945*width,.607*height),
                'List C - DocumentNumber': (.71*width,.606*height,.945*width,.625*height),                
                'List C - DocumentExpirationDate': (.71*width,.625*height,.945*width,.645*height),
                'List A - DocumentTitle - Second Section': (),
                'List A - IssuingAuthority - Second Section': (),
                'List A - DocumentNumber - Second Section': (.13*width,.645*height,.358*width,.663*height),
                'List A - DocumentExpirationDate - Second Section': (.22*width,.6624*height,.358*width,.683*height),
                'DateOfHire': (.162*width,.711*height,.273*width,.726*height),
                #'ApartmentNo': (.58*width,.233*height,.685*width,.2454*height)
                }
        
    elif (formNumber == '03/08/13') & (page_number == 7):
        global image_coords_030813_pg7
        image_coords_030813_pg7 = {'LastName':(.063*width,.225*height,.345*width,.246*height),
                'FirstName': (.346*width,.226*height,.58*width,.246*height), 
                'MiddleInitial': (.58*width,.225*height,.66*width,.246*height),
                'MaidenName': (.665*width,.225*height,.94*width,.246*height),
                'StreetAddress': (.06*width,.263*height,.39*width,.287*height),
                'City': (.501*width,.263*height,.72*width,.287*height),
                'State': (.73*width,.263*height,.803*width,.287*height),
                'Zip': (.804*width,.263*height,.93*width,.287*height),
                'DateOfBirth': (.063*width,.301*height,.23*width,.325*height),
                'SocialSecurity': (.23*width,.301*height,.405*width,.325*height),
                'EmailAddress': (.408*width,.301*height,.75*width,.325*height),
                'Telephone': (.755*width,.301*height,.94*width,.325*height),
                'Attestation': (.057*width,.385*height,.087*width,.48*height),
                'Alien # for Permanent Residence': (.567*width,.42*height,.81*width,.445*height),
                'Date Expiration of Work Authorization': (.535*width,.447*height,.662*width,.475*height),
                'Alien # for Work Authorization': (.387*width,.505*height,.62*width,.53*height),
                'I-94 Admission Number': (.299*width,.53*height,.62*width,.57*height),
                'Foreign Passport': (.295*width,.6*height,.72*width,.63*height),
                'Country of Issuance': (.256*width,.628*height,.72*width,.656*height),
                'TranslatorName': (.063*width,.857*height,.94*width,.88*height),
                'TranslatorAddress': (.063*width,.892*height,.94*width,.915*height),
                'TranslatorDateOfSignature': (.75*width,.822*height,.94*width,.834*height)}
    
    elif (formNumber == '03/08/13') & (page_number == 8):
        global image_coords_030813_pg8
        image_coords_030813_pg8 = {'List A - DocumentTitle': (.063*width,.205*height,.344*width,.221*height),
                'List A - IssuingAuthority': (.063*width,.233*height,.344*width,.248*height),
                'List A - DocumentNumber': (.063*width,.259*height,.344*width,.276*height),
                'List A - DocumentExpirationDate': (.063*width,.2905*height,.344*width,.308*height),
                'List A - DocumentTitle - Second Section': (.063*width,.32*height,.344*width,.337*height),
                'List A - IssuingAuthority - Second Section': (.063*width,.3475*height,.344*width,.3632*height),
                'List A - DocumentNumber - Second Section': (.063*width,.3738*height,.344*width,.390*height),
                'List A - DocumentExpirationDate - Second Section': (.063*width,.4005*height,.344*width,.4165*height),
                'List B - DocumentTitle': (.361*width,.205*height,.65*width,.22*height),
                'List B - IssuingAuthority': (.361*width,.233*height,.65*width,.247*height),                
                'List B - DocumentNumber': (.361*width,.257*height,.65*width,.275*height),
                'List B - DocumentExpirationDate': (.361*width,.2905*height,.65*width,.308*height),
                'List C - DocumentTitle': (.655*width,.205*height,.94*width,.222*height),
                'List C - IssuingAuthority': (.655*width,.233*height,.94*width,.249*height),
                'List C - DocumentNumber': (.655*width,.259*height,.94*width,.277*height),
                'List C - DocumentExpirationDate': (.655*width,.2905*height,.94*width,.308*height),
                'DateOfHire': (.448*width,.60*height,.59*width,.62*height),
                'Name of Employee Representative': (.065*width,.677*height,.55*width,.7*height),
                'Title': (.61*width,.64*height,.9*width,.66*height),
                'EmployerBusinessName': (.58*width,.6775*height,.94*width,.702*height),
                'EmployerStreetAddress': (.06*width,.7135*height,.496*width,.739*height),
                'Date Signed by Employer': (.452*width,.641*height,.604*width,.665*height),
                'List A - DocumentTitle - Third Section': (.063*width,.43*height,.345*width,.447*height),
                'List A - IssuingAuthority - Third Section': (.063*width,.46*height,.345*width,.475*height),
                'List A - DocumentNumber - Third Section': (.063*width,.487*height,.345*width,.506*height),
                'List A - DocumentExpirationDate - Third Section': (.063*width,.5188*height,.345*width,.537*height),
                'Employee Info from Section 1': ()}

    elif (formNumber == '11/14/2016') & (page_number == 1):
        global image_coords_111416_pg1
        image_coords_111416_pg1 = {'LastName':(.06*width,.242*height,.335*width,.265*height),
                        'FirstName': (.34*width,.242*height,.582*width,.265*height), 
                        'MiddleInitial': (.586*width,.242*height,.689*width,.265*height),
                        'MaidenName': (.69*width,.242*height,.93*width,.265*height),
                        'StreetAddress': (.06*width,.279*height,.39*width,.303*height),
                        #'AptNo': (.395*width,.279*height,.493*width,.303*height),
                        'City': (.494*width,.279*height,.738*width,.303*height),
                        'State': (.74*width,.279*height,.802*width,.303*height),
                        'Zip': (.804*width,.279*height,.93*width,.303*height),
                        'DateOfBirth': (.06*width,.318*height,.241*width,.346*height),
                        'SocialSecurity': (.243*width,.319*height,.438*width,.346*height),
                        'EmailAddress': (.439*width,.319*height,.72*width,.346*height),
                        'Telephone': (.721*width,.318*height,.93*width,.346*height),
                        'Attestation': (.06*width,.407*height,.085*width,.492*height),
                        'Alien # for Permanent Residence': (.573*width,.45*height,.775*width,.468*height),
                        'Date Expiration of Work Authorization': (.573*width,.472*height,.705*width,.49*height),
                        'Alien # for Work Authorization': (.36*width,.534*height,.61*width,.559*height),
                        'Admission # for Work Authorization': (),
                        'I-94 Admission Number': (.265*width,.56*height,.61*width,.593*height),
                        'ForeignPassport': (.25*width,.592*height,.61*width,.622*height),
                        'Country of Issuance': (.225*width,.622*height,.61*width,.645*height),
                        'TranslatorName': (),
                        'TranslatorAddress': (.06*width,.865*height,.48*width,.886*height),
                        'TranslatorDateOfSignature': (.68*width,.789*height,.93*width,.808*height)}
   
    elif (formNumber == '11/14/2016') & (page_number == 2):
        global image_coords_111416_pg2
        image_coords_111416_pg2 = {'List A - DocumentTitle': (.06*width,.232*height,.335*width,.25*height),
                        'List A - IssuingAuthority': (.06*width,.264*height,.335*width,.278*height),
                        'List A - DocumentNumber': (.06*width,.29*height,.335*width,.306*height),
                        'List A - DocumentExpirationDate': (.06*width,.32*height,.335*width,.334*height),
                        'List A - DocumentTitle - Second Section': (.06*width,.35*height,.335*width,.366*height),
                        'List A - IssuingAuthority - Second Section': (.06*width,.381*height,.335*width,.394*height),
                        'List A - DocumentNumber - Second Section': (.06*width,.405*height,.335*width,.421*height),
                        'List A - DocumentExpirationDate - Second Section': (.06*width,.434*height,.335*width,.45*height),
                        'List B - DocumentTitle': (.361*width,.232*height,.65*width,.25*height),
                        'List B - IssuingAuthority': (.361*width,.264*height,.65*width,.278*height),
                        'List B - DocumentNumber': (.361*width,.29*height,.65*width,.306*height),
                        'List B - DocumentExpirationDate': (.361*width,.32*height,.65*width,.334*height),
                        'List C - DocumentTitle': (.658*width,.232*height,.94*width,.25*height),
                        'List C - IssuingAuthority': (.658*width,.264*height,.94*width,.278*height),
                        'List C - DocumentNumber': (.658*width,.29*height,.94*width,.306*height),
                        'List C - DocumentExpirationDate': (.658*width,.32*height,.94*width,.334*height),
                        'DateOfHire': (.462*width,.61*height,.6*width,.63*height),
                        'Name of Employee Representative': (.06*width,.686*height,.64*width,.706*height),
                        'Title': (.62*width,.652*height,.942*width,.672*height),
                        'EmployerBusinessName': (.662*width,.687*height,.942*width,.706*height),
                        'EmployerStreetAddress': (.06*width,.72*height,.5*width,.741*height),
                        'Date Signed by Employer': (.44*width,.652*height,.62*width,.672*height),
                        'List A - DocumentTitle - Third Section': (.06*width,.465*height,.335*width,.481*height),
                        'List A - IssuingAuthority - Third Section': (.06*width,.495*height,.335*width,.509*height),
                        'List A - DocumentNumber - Third Section': (.06*width,.521*height,.335*width,.535*height),
                        'List A - DocumentExpirationDate - Third Section': (.06*width,.549*height,.335*width,.565*height),
                        'Employee Info from Section 1 - LastName': (.27*width,.177*height,.51*width,.193*height),
                        'Employee Info from Section 1 - FirstName':(.514*width,.177*height,.705*width,.193*height), 
                        'Employee Info from Section 1 - Middle Initial': (.706*width,.177*height,.746*width,.193*height)
                        }

    elif (formNumber == '07/17/17') & (page_number == 1):
        global image_coords_071717_pg1 
        image_coords_071717_pg1 = {'LastName':(.065*width,.241*height,.347*width,.265*height),
                        'FirstName': (.35*width,.241*height,.592*width,.265*height), 
                        'MiddleInitial': (.596*width,.241*height,.694*width,.265*height),
                        'MaidenName': (.695*width,.241*height,.945*width,.265*height),
                        'StreetAddress': (.065*width,.279*height,.39*width,.302*height),
                        #'AptNo': (.405*width,.279*height,.495*width,.302*height),
                        'City': (.5*width,.279*height,.74*width,.302*height),
                        'State': (.746*width,.279*height,.805*width,.302*height),
                        'Zip': (.808*width,.279*height,.945*width,.302*height),
                        'DateOfBirth': (.066*width,.318*height,.25*width,.346*height),
                        'SocialSecurity': (.252*width,.318*height,.444*width,.345*height),
                        'EmailAddress': (.447*width,.318*height,.725*width,.345*height),
                        'Telephone': (.727*width,.318*height,.945*width,.344*height),
                        'Attestation': (.066*width,.407*height,.094*width,.49*height),
                        'Alien # for Permanent Residence': (.57*width,.449*height,.78*width,.466*height),
                        'Date Expiration of Work Authorization': (.57*width,.47*height,.72*width,.488*height),
                        'Alien # for Work Authorization': (.35*width,.537*height,.62*width,.557*height),
                        'Admission # for Work Authorization': (),
                        'I-94 Admission Number': (.28*width,.56*height,.62*width,.592*height),
                        'ForeignPassport': (.26*width,.593*height,.62*width,.621*height),
                        'Country of Issuance': (.23*width,.622*height,.62*width,.642*height),
                        'TranslatorName': (.53*width,.82*height,.945*width,.84*height),
                        'TranslatorAddress': (.068*width,.86*height,.46*width,.88*height),
                        'TranslatorDateOfSignature': (.688*width,.785*height,.945*width,.805*height)}

    elif (formNumber == '07/17/17') & (page_number == 2):
        global image_coords_071717_pg2 
        image_coords_071717_pg2 = {'List A - DocumentTitle': (.068*width,.231*height,.34*width,.249*height),
                        'List A - IssuingAuthority': (.068*width,.261*height,.34*width,.277*height),
                        'List A - DocumentNumber': (.068*width,.287*height,.34*width,.304*height),
                        'List A - DocumentExpirationDate': (.068*width,.317*height,.34*width,.333*height),
                        'List A - DocumentTitle - Second Section': (.068*width,.348*height,.34*width,.365*height),
                        'List A - IssuingAuthority - Second Section': (.068*width,.377*height,.34*width,.393*height),
                        'List A - DocumentNumber - Second Section': (.068*width,.402*height,.34*width,.419*height),
                        'List A - DocumentExpirationDate - Second Section': (.068*width,.432*height,.34*width,.448*height),
                        'List B - DocumentTitle': (.365*width,.233*height,.655*width,.25*height),
                        'List B - IssuingAuthority': (.365*width,.261*height,.655*width,.277*height),
                        'List B - DocumentNumber': (.365*width,.287*height,.655*width,.304*height),
                        'List B - DocumentExpirationDate': (.365*width,.317*height,.655*width,.333*height),
                        'List C - DocumentTitle': (.658*width,.233*height,.94*width,.25*height),
                        'List C - IssuingAuthority': (.658*width,.262*height,.94*width,.277*height),
                        'List C - DocumentNumber': (.658*width,.287*height,.94*width,.304*height),
                        'List C - DocumentExpirationDate': (.658*width,.317*height,.94*width,.333*height),
                        'DateOfHire': (.464*width,.61*height,.61*width,.628*height),
                        'Name of Employee Representative': (.068*width,.684*height,.64*width,.703*height),
                        'Title': (.625*width,.649*height,.945*width,.669*height),
                        'EmployerBusinessName': (.666*width,.684*height,.945*width,.703*height),
                        'EmployerStreetAddress': (.068*width,.713*height,.5*width,.737*height),
                        'Date Signed by Employer': (.443*width,.649*height,.623*width,.669*height),
                        'List A - DocumentTitle - Third Section': (.068*width,.462*height,.34*width,.479*height),
                        'List A - IssuingAuthority - Third Section': (.068*width,.492*height,.34*width,.506*height),
                        'List A - DocumentNumber - Third Section': (.068*width,.517*height,.34*width,.532*height),
                        'List A - DocumentExpirationDate - Third Section': (.068*width,.546*height,.34*width,.562*height),
                        'Employee Info from Section 1 - LastName': (.274*width,.175*height,.514*width,.192*height),
                        'Employee Info from Section 1 - FirstName':(.516*width,.175*height,.708*width,.192*height), 
                        'Employee Info from Section 1 - Middle Initial': (.71*width,.177*height,.748*width,.192*height)
                        }
        
    elif (formNumber == '11-21-91(L)'):
        global image_coords_112191_L
        image_coords_112191_L = {'LastName':(.09*width,.155*height,.36*width,.173*height),
                'FirstName': (.37*width,.155*height,.53*width,.173*height), 
                'MiddleInitial': (.54*width,.155*height,.64*width,.173*height),
                'MaidenName': (.645*width,.155*height,.9*width,.173*height),
                'StreetAddress': (.09*width,.182*height,.52*width,.198*height),
                'City': (.09*width,.208*height,.345*width,.222*height),
                'State': (.346*width,.208*height,.53*width,.222*height),
                'Zip': (.54*width,.208*height,.64*width,.222*height),
                'DateOfBirth': (.645*width,.182*height,.9*width,.198*height),
                'SocialSecurity': (.645*width,.208*height,.8*width,.222*height),
                'Attestation': (.495*width,.233*height,.512*width,.264*height),
                'Alien # for Permanent Residence': (.722*width,.242*height,.89*width,.254*height),
                'Date Expiration of Work Authorization': (.679*width,.254*height,.79*width,.265*height),
                'Alien # for Work Authorization': (.637*width,.264*height,.89*width,.273*height),
                'Admission # for Work Authorization': (),
                'I-94 Admission Number': (),
                'ForeignPassport': (),
                'Country of Issuance': (),
                'TranslatorName': (.501*width,.343*height,.78*width,.355*height),
                'TranslatorAddress': (.15*width,.365*height,.62*width,.379*height),
                'TranslatorDateOfSignature': (.64*width,.365*height,.8*width,.379*height),
                'List A - DocumentTitle': (.171*width,.433*height,.328*width,.448*height),
                'List A - IssuingAuthority': (.181*width,.452*height,.328*width,.468*height),
                'List A - DocumentNumber': (.17*width,.469*height,.328*width,.486*height),
                'List A - DocumentExpirationDate': (.24*width,.49*height,.329*width,.507*height),
                'List B - DocumentTitle': (.375*width,.433*height,.595*width,.448*height),
                'List B - IssuingAuthority': (.375*width,.452*height,.595*width,.468*height),
                'List B - DocumentNumber': (.375*width,.469*height,.595*width,.486*height),
                'List B - DocumentExpirationDate': (.405*width,.49*height,.49*width,.507*height),
                'List C - DocumentTitle': (.63*width,.433*height,.87*width,.448*height),
                'List C - IssuingAuthority': (.63*width,.452*height,.87*width,.468*height),
                'List C - DocumentNumber': (.63*width,.469*height,.87*width,.486*height),                
                'List C - DocumentExpirationDate': (.66*width,.49*height,.765*width,.506*height),
                'List A - DocumentTitle - Second Section': (),
                'List A - IssuingAuthority - Second Section': (),
                'List A - DocumentNumber - Second Section': (.17*width,.507*height,.328*width,.525*height),
                'List A - DocumentExpirationDate - Second Section': (.24*width,.528*height,.329*width,.545*height),
                'DateOfHire': (.401*width,.574*height,.526*width,.585*height)
                #'ApartmentNo': ()
                }
   
    elif (formNumber == '11-21-91(R)'):
        global image_coords_112191_R
        image_coords_112191_R = {'LastName':(.048*width,.167*height,.36*width,.189*height),
                'FirstName': (.361*width,.167*height,.564*width,.189*height), 
                'MiddleInitial': (.57*width,.167*height,.676*width,.189*height),
                'MaidenName': (.68*width,.167*height,.96*width,.189*height),
                'StreetAddress': (.048*width,.202*height,.565*width,.221*height),
                'City': (.048*width,.23*height,.33*width,.251*height),
                'State': (.33*width,.23*height,.565*width,.251*height),
                'Zip': (.57*width,.23*height,.676*width,.251*height),
                'DateOfBirth': (.68*width,.202*height,.96*width,.221*height),
                'SocialSecurity': (.68*width,.232*height,.9*width,.25*height),
                'Attestation': (.515*width,.262*height,.535*width,.306*height),
                'Alien # for Permanent Residence': (.779*width,.274*height,.9*width,.288*height),
                'Date Expiration of Work Authorization': (.733*width,.289*height,.83*width,.302*height),
                'Alien # for Work Authorization': (.682*width,.302*height,.836*width,.315*height),
                'Admission # for Work Authorization': (),
                'I-94 Admission Number': (),
                'ForeignPassport': (),
                'Country of Issuance': (),
                'TranslatorName': (.515*width,.395*height,.87*width,.41*height),
                'TranslatorAddress': (.1*width,.4213*height,.66*width,.439*height),
                'TranslatorDateOfSignature': (.68*width,.4213*height,.87*width,.439*height),
                'List A - DocumentTitle': (.14*width,.498*height,.32*width,.518*height),
                'List A - IssuingAuthority': (.15*width,.52*height,.32*width,.54*height),
                'List A - DocumentNumber': (.14*width,.547*height,.32*width,.562*height),
                'List A - DocumentExpirationDate': (.22*width,.573*height,.32*width,.588*height),
                'List B - DocumentTitle': (.375*width,.498*height,.63*width,.518*height),
                'List B - IssuingAuthority': (.375*width,.52*height,.63*width,.54*height),
                'List B - DocumentNumber': (.375*width,.547*height,.63*width,.562*height),
                'List B - DocumentExpirationDate': (.395*width,.573*height,.505*width,.588*height),
                'List C - DocumentTitle': (.67*width,.498*height,.93*width,.518*height),
                'List C - IssuingAuthority': (.67*width,.52*height,.93*width,.54*height),
                'List C - DocumentNumber': (.67*width,.547*height,.93*width,.562*height),                
                'List C - DocumentExpirationDate': (.705*width,.573*height,.81*width,.588*height),
                'List A - DocumentTitle - Second Section': (),
                'List A - IssuingAuthority - Second Section': (),
                'List A - DocumentNumber - Second Section': (),
                'List A - DocumentExpirationDate - Second Section': (.22*width,.618*height,.32*width,.635*height),
                'DateOfHire': (.396*width,.671*height,.492*width,.683*height)
                #'ApartmentNo': (.566*width,.20*height,.676*width,.221*height)
                }
    
    else:
        print("Dimensions not found for form number " + formNumber)

def resize(item, width, height):
    im = PIL.Image.open(item)
    im = im.resize((width,height), PIL.Image.ANTIALIAS)
    swap = io.BytesIO()
    im.save(swap, 'png')
    return swap

###make a function to put an array on a 0 to 1 scale
def scale(array):
    max = array.max()
    return(array/max)
    
###some image inverted the black and white pixels, function to tranform back
def invert(array):
    return(abs(1-array))

def SStesseract(image):
    #resize    
    swap = resize(image, 300, 60)
    #convert image to data array
    data = np.asarray(PIL.Image.open(swap))
    #set data property WRITEABLE to TRUE so we can make changes
    data.setflags(write = 1)
    #scale image
    data = scale(data)
    #if 3 dimensional...
    ##just choosing the 3rd dimension of the image, which is a 2 dimensional array
    if len(data.shape) > 2:
        data = data[:,:,2]
    #getting the height and width
    height, width = data.shape
    
    #set threshold
    threshold = 0.5
    
    #get column and row sums and change to 1 if value below threshold
    for i in range(height):
        row_average = data[i,].mean()
        if row_average < threshold:
            data[i,] = 1
        
    for i in range(width):
        col_average = data[:,i].mean()
        if col_average < threshold:
            data[:,i] = 1
    
    #convert back to an array
    im = PIL.Image.fromarray(np.uint8(data*255))
    
    #test tesseract output
    text = pytesseract.image_to_string(im)
    return(text)
    
def SStesseract2(image):
    #resize    
    swap = resize(image, 300, 60)
    #convert image to data array
    data = np.asarray(PIL.Image.open(swap))
    #set data property WRITEABLE to TRUE so we can make changes
    data.setflags(write = 1)
    #scale image
    data = scale(data)
    ##just choosing the 3rd dimension of the image, which is a 2 dimensional array
    if len(data.shape) > 2:
        data = data[:,:,2]
    height, width = data.shape
    
    threshold = 0.85
    #iterate over the rows and get the max number of consecutive dark pixels
    row_counts= []
    max_row_counts = []
    for i in range(height):
        count = 0
        for j in range(width):
            val = data[i,j]
            if (j + 1 == width):
                if len(row_counts) > 0:
                    max_no = max(row_counts)
                    max_row_counts.append(max_no)
                    row_counts = []
                    if max_no > 50:
                        data[i,] = 1
                else:
                    continue
            else:
                if (val < threshold):
                    count = count + 1
                elif (val >= threshold) & (count > 0):
                    row_counts.append(count)
                    count = 0
                else:
                    continue
    
    #iterate over the columns and get the max number of consecutive dark pixels
    col_counts= []
    max_col_counts = []
    for i in range(width):
        count = 0
        for j in range(height):
            val = data[j,i]
            if (j + 1 == height):
                max_val = max(col_counts)
                col_counts = []
                max_col_counts.append(max_val)
            else:
                if (val < .95):
                    count = count + 1
                    col_counts.append(count)
                else:
                    count = 0
                    col_counts.append(0)
            
    for i in range(len(max_col_counts)):
        if max_col_counts[i] > (.4 * height):
            data[:,i] = 1
            
    #convert back to an array
    im = PIL.Image.fromarray(np.uint8(data*255))

    #test tesseract output
    text = pytesseract.image_to_string(im) 
    return(text)

def SStesseract4(image, threshold = 0.95, leeway = 5, window = 3):
    """
    @@image the image to extract the text from
    @@threshold the pixel value below which is flagged as having a pixel
    @@leeway the number of missing pixels allowed in a column before stopping
    taking the count. Used to reduce the impact of random missing pixels. 
    @@window the window of columns to look at when determing whether there is a
    line in a column or row. Used to reduce the impact of random missing pixels.
    This function intakes an image with the Social Security information in boxes
    for each number and outputs the numbers within it. Before running the 
    pytesseract function to output the numbers, the image needs to be cleaned
    to remove the boxes and other random pixel distortions. Utilizes numerous
    box cleaning methods and outputs whichever performs the best.
    """   
    #resize    
    swap = resize(image, 300, 60)
    #convert image to data array
    data = np.asarray(PIL.Image.open(swap))
    #set data property WRITEABLE to TRUE so we can make changes
    data.setflags(write = 1)
    #scale image
    data = scale(data)
    #if color scheme is inverted, convert it back
    if np.mean(data) < 0.5:
        data = invert(data)
    #convert to 2-dimensions if it is a 3-dimensional image
    if len(data.shape) > 2:
        data = data[:,:,2]
    height, width = data.shape
    
    #iterate over the rows and get the max number of consecutive dark pixels
    row_counts= []
    max_row_counts = []
    for i in range(height):
        count = 0
        miss = 0
        for j in range(width):
            val = data[i,j]
            if (j + 1 == width):
                if len(row_counts) > 0:
                    max_no = max(row_counts)
                    max_row_counts.append(max_no)
                    row_counts = []
                    if max_no > 50:
                        data[i,] = 1
                else:
                    continue
            else:
                if (val < threshold):
                    count = count + 1
                    miss = 0
                    row_counts.append(count)
                elif (val >= threshold) & (miss < leeway):
                    count = count + 1
                    miss = miss + 1
                    row_counts.append(0)
                else:
                    count = 0
                    miss = miss + 1
                    row_counts.append(0)
    
    for i in range(len(max_row_counts)):
        if max_row_counts[i] > (.4 * height):
            data[:,i] = 1
    
    #iterate over the columns and get the max number of consecutive dark pixels
    col_counts= []
    max_col_counts = []
    for i in range(width):
        count = 0
        miss = 0
        for j in range(height):
            val = min(data[j,i:i+window])
            if (j + 1 == height):
                max_val = max(col_counts)
                col_counts = []
                max_col_counts.append(max_val)
            else:
                if (val < threshold):
                    count = count + 1
                    miss = 0
                    col_counts.append(count)
                elif (val >= threshold) & (miss < leeway):
                    count = count + 1
                    miss = miss + 1
                    col_counts.append(0)
                else:
                    count = 0
                    miss = miss + 1
                    col_counts.append(0)
            
    for i in range(len(max_col_counts)):
        if max_col_counts[i] > (.4 * height):
            data[:,i] = 1
    
    #try to clean up the data output for random pixels 
    #ROWS -- loop with 3 window, if only middle column has pixels, convert to 1
    for i in range(width-2):
        data_crop = data[:,i:i+3]
        col_1 = sum(data_crop[:,0] < 1)
        col_2 = sum(data_crop[:,1] < 1)
        col_3 = sum(data_crop[:,2] < 1)
        if (col_2 > 0) & (col_1 < 3) & (col_3 < 3):
            data[:,i+1] = 1
    
    #COLS -- loop with 3 window, if only middle column has pixels, convert to 1
    for i in range(height-2):
        data_crop = data[i:i+3]
        col_1 = sum(data_crop[0] < 1)
        col_2 = sum(data_crop[1] < 1)
        col_3 = sum(data_crop[2] < 1)
        if (col_2 > 0) & (col_1 < 2) & (col_3 < 2):
            data[i+1] = 1
                
    #convert back to an array
    im = PIL.Image.fromarray(np.uint8(data*255))
    
    #test tesseract output
    text = pytesseract.image_to_string(im).replace('\n','')
    if sum(c.isdigit() for c in text) < 9:
        text = SStesseract(image).replace('\n','')
        if sum(c.isdigit() for c in text) < 9:
            return(SStesseract2(image).replace('\n',''))
        else:
            return(text)
    elif sum(c.isdigit() for c in text) > 9:
        return(SStesseract2(image).replace('\n',''))
    else:
        return(text)

def Tesseract(image):
    """
    @@image the image to extract the text from
    This function intakes an image and spits out the text within it. Before
    running the pytesseract function the image is cleaned to remove lines in
    the image to improve performance. 
    """   
    #open image
    im = PIL.Image.open(image)
    width, height = im.size
    #resize image according to size for proper pixel format   
    swap = resize(image, width, height)
    #convert image to data array
    data = np.asarray(PIL.Image.open(swap))
    #set data property WRITEABLE to TRUE so we can make changes
    data.setflags(write = 1)
    #scale image
    data = scale(data)
    #if color scheme is inverted, convert it back
    if np.mean(data) < 0.5:
        data = invert(data)
    #if 3 dimensional...
    ##just choosing the 3rd dimension of the image, which is a 2 dimensional array
    if len(data.shape) > 2:
        data = data[:,:,2]
    #getting the height and width
    height, width = data.shape
    
    #set threshold
    threshold = 0.5
    
    #get column and row sums and change to 1 if value below threshold
    for i in range(height):
        row_average = data[i,].mean()
        if row_average < threshold:
            data[i,] = 1
        
    for i in range(width):
        col_average = data[:,i].mean()
        if col_average < threshold:
            data[:,i] = 1
    
    #convert back to an array
    image = PIL.Image.fromarray(np.uint8(data*255))
    
    #test tesseract output
    text = pytesseract.image_to_string(image) 
    return(text)

def Tesseract2(image, window = 3):
    """
    @@image the image to extract the text from
    This function intakes an image and spits out the text within it. Before
    running the pytesseract function the image is cleaned to remove lines in
    the image to improve performance. 
    """   
    #open image
    im = PIL.Image.open(image)
    width, height = im.size
    #resize image according to size for proper pixel format   
    swap = resize(image, width, height)
    #convert image to data array
    data = np.asarray(PIL.Image.open(swap))
    #set data property WRITEABLE to TRUE so we can make changes
    data.setflags(write = 1)
    #scale image
    data = scale(data)
    #if color scheme is inverted, convert it back
    if np.mean(data) < 0.5:
        data = invert(data)
    #if 3 dimensional...
    ##just choosing the 3rd dimension of the image, which is a 2 dimensional array
    if len(data.shape) > 2:
        data = data[:,:,2]
    #getting the height and width
    height, width = data.shape
    
    #set threshold
    threshold = 0.5
    
    #get column sums and change to 1 if value below threshold
    for i in range(width-(window - 1)):
        data_crop = data[:,i:i+window]
        row_average = data_crop.mean()
        if row_average < threshold:
            data[:,i:i+window] = 1
    
    #get row sums and change to 1 if value below threshold    
    #for i in range(height-(window-1)):
    #    data_crop = data[i:i+window]
    #    col_average = data_crop.mean()
    #    if col_average < threshold:
    #        data[i:i+window] = 1
    
    #convert back to an array
    image = PIL.Image.fromarray(np.uint8(data*255))
    
    #test tesseract output
    text = pytesseract.image_to_string(image) 
    return(text)

def findCheckBox(image, form_number):
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
        
def switchCoords(form_number, page_number):
    if form_number == '03/08/13':
        if page_number == 7:
            coords = image_coords_030813_pg7
            return(coords)
        elif page_number == 8:
            coords = image_coords_030813_pg8
            return(coords)
        else:
            print("This page does not contain data")
    elif form_number == '07/17/17':
        if page_number == 1:
            coords = image_coords_071717_pg1
            return(coords)
        elif page_number == 2:
            coords = image_coords_071717_pg2
            return(coords)
        else:
            print("This page does not contain data")        
    elif form_number == '11/14/2016':
        if page_number == 1:
            coords = image_coords_111416_pg1
            return(coords)
        elif page_number == 2:
            coords = image_coords_111416_pg2
            return(coords)
        else:
            print("This page does not contain data")  
    else:
        switcher = {
                '02/02/09': image_coords_020209,
                '05/07/87': image_coords_050787,
                '06/05/07': image_coords_060507,
                '08/07/09': image_coords_080709,
                '05/31/05': image_coords_053105,
                '11-21-91(L)': image_coords_112191_L,
                '11-21-91(R)': image_coords_112191_R
        }
        coords = switcher.get(form_number, "Invalid form number")
        return(coords)

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

######################################
########## main thread ###############
######################################

folder_location = 'C:\\Users\\Brandon Croarkin\\Documents\\GreenZone\\OCR\\NiFiTesting'

#Make a vector of PNG files in the image directory so it can repeat 
#process on all images in directory
PDFs = []
os.chdir(folder_location)
for image in os.listdir(folder_location):
    if image.endswith(".pdf"):
        PDFs.append(image)

# flowFile = open(r'C:\Users\Andrew Riffle\PycharmProjects\PDF-Data-Extraction\ocr\TestDataFiles\i-9_03-08-13.pdf', 'rb')
# flowFile = open(r'C:\Users\Andrew Riffle\PycharmProjects\PDF-Data-Extraction\ocr\TestDataFiles\i-9_08-07-09.pdf', 'rb')

# Declare the empty list of images
images = []

#loop through PDF files and convert them to PNG
for i in range(len(PDFs)):
    with Image(filename=PDFs[i], resolution = 300) as img:
        #find the filename
        filename = findFileName(PDFs[i])
        
        #loop through pages of PDF
        for i, page in enumerate(img.sequence):
            with Image(page) as im:
                im.alpha_channel = False
                im.format = 'png'
        
                swapPNG = io.BytesIO()
                im.save(swapPNG)
                images.append(tuple((filename, i, swapPNG)))

#make an empty dict to add the crops to
crops = {}

#create empty lists to add data to after cropped
file = []
field = []
text = []

#TESTING
#form_numbers = []
#page_numbers = []
#sub_images = images[20:50]


for i in range(len(images)):
    #the filename is the 1st object in the tuple
    filename = images[i][0]

    #the PDF page is the 3rd object in the tuple
    page = images[i][2]

    #find the form number for the image
    form_number = findFormNumber(page)
    
    # check if form_number found. If not, continue to next image.
    if (form_number == 'image file is truncated') or (form_number == 'not found'):
        continue

    # The pages number is the second item in the tuple
    page_number = images[i][1]
    page_number2 = findPageNumber(page)
    if (page_number2 == 'image file is truncated') or (page_number2 == 'not found'):
        page_number2 = page_number + 1
    
    # Set the global vars to the correct coordinates
    setImageCoords(page, form_number, page_number2)

    # Get coords for given form and page number
    coords = switchCoords(form_number, page_number2)
    
    #list which forms have the page number on their data page
    has_page_number = ['11-21-91(R)', '05/31/05', '07/17/17', '08/07/09',
                       '11/14/2016', '02/02/09', '03/08/13']
    
    #list which forms do not have the page number on their data page
    no_page_number = ['05/07/87', '11-21-91(L)', '06/05/07']

    page_info = {'05/07/87': 0,
                 '11-21-91(L)': 0,
                 '11-21-91(R)': 2,
                 '05/31/05': 2,
                 '06/05/07': 3,
                 '02/02/09': 4,
                 '08/07/09': 4,
                 '03/08/13': (7,8),
                 '11/14/2016': (1,2),
                 '07/17/17': (1,2)
                 }

    # determine if this file contains data based on page_info lookup table and then
    # crop the image if it does
    if isinstance(page_info[form_number], int):
        if form_number in no_page_number:
            if page_info[form_number] == page_number:
                # loop through the coordinates for each attribute and create a new image
                for key, value in coords.items():
                    # only do the crop if there is the correct number of dimensions
                    if len(value) != 4:
                        if len(value) == 0:
                            # print(key, " has no coords yet.")
                            continue
                        else:
                            # print(key, "has an incorrect number of dimensions.")
                            continue
                    else:
                        # print(key + ' : ' + str(value))
                        swap = crop(page, value)
                        crops[key] = tuple((swap, form_number, filename))
            # else:
            # print("Not a data form")
        else:
            if page_info[form_number] == page_number2:
                # loop through the coordinates for each attribute and create a new image
                for key, value in coords.items():
                    # only do the crop if there is the correct number of dimensions
                    if len(value) != 4:
                        if len(value) == 0:
                            # print(key, " has no coords yet.")
                            continue
                        else:
                            # print(key, "has an incorrect number of dimensions.")
                            continue
                    else:
                        # # print(key + ' : ' + str(value))
                        swap = crop(page, value)
                        crops[key] = tuple((swap, form_number, filename))
            # else:
            # print("Not a data form")
    else:
        if form_number in no_page_number:
            if (page_info[form_number][0] == page_number) or (page_info[form_number][1] == page_number):
                # loop through the coordinates for each attribute and create a new image
                for key, value in coords.items():
                    # only do the crop if there is the correct number of dimensions
                    if len(value) != 4:
                        if len(value) == 0:
                            # print(key, " has no coords yet.")
                            continue
                        else:
                            # print(key, "has an incorrect number of dimensions.")
                            continue
                    else:
                        # print(key + ' : ' + str(value))
                        swap = crop(page, value)
                        crops[key] = tuple((swap, form_number, filename))
            # else:
            # print("Not a data form")
        else:
            if (page_info[form_number][0] == page_number2) or (page_info[form_number][1] == page_number2):
                # loop through the coordinates for each attribute and create a new image
                for key, value in coords.items():
                    # only do the crop if there is the correct number of dimensions
                    if len(value) != 4:
                        if len(value) == 0:
                            # print(key, " has no coords yet.")
                            continue
                        else:
                            # print(key, "has an incorrect number of dimensions.")
                            continue
                    else:
                        # print(key + ' : ' + str(value))
                        swap = crop(page, value)
                        crops[key] = tuple((swap, form_number, filename))
            # else:
            # print("Not a data form")
    
    for key, value in crops.items():
        file.append(filename)
        field.append(key)
        if key == "Attestation":
            text.append(findCheckBox(crops[key][0], crops[key][1]))
        elif key == "SocialSecurity":
            text.append(SStesseract4(crops[key][0]))
        else:
            text.append(Tesseract2(crops[key][0]))
    
    crops = {}

#########################################
##########CLEANING THE OUTPUT############
#########################################

#make empty list to put cleaned text
cleaned_text = []
#pulling all the information after the heading
for i in range(len(text)):
    if len(text[i]) > 0:
        cleaned_text.append(re.search(r'[^\n]+$',text[i]).group())
    #add in a "no value found" if empty    
    else:
        cleaned_text.append(" ")

#create dataframe of the values
df = pd.DataFrame({'File': file, 
                   'Field': field, 
                   'Text': cleaned_text})

#format dataframe to have file as row and fields as columns
df_formatted = df.reset_index().pivot(index = 'File', columns = 'Field', values = 'Text')  

#fill the na's with 'no value found'
df_formatted = df_formatted.fillna(" ")

#make an array of leters to remove them when needed
letters = '[abcdefghijklmnopqrstuvwxyz]'
numbers = '[1234567890]'
date_symbols_to_remove = '[().?|,`_~!:;>—<*&§^%$‘»-]'
symbols_to_remove = '[().?|,`_~!:;><*&/—\^%$§‘»-]'

#create a dictionary to get the text value needed 
attestation_dict = {'box1': 'A citizen of the United States',
                    'box2': 'A noncitizen of the United States',
                    'box3': 'A lawful permanent resident (Alien #)',
                    'box4': 'An alien authorized to work',
                    'no box': 'Attestation not filled in!'
        }

#clean dataframe values
for i in range(len(df_formatted)):
    #REPLACE ATTESTATION: fill in the actual attestation based on the box that is checked
    if (df_formatted['Attestation'][i] != None) and (df_formatted['Attestation'][i] != ' '):
        df_formatted['Attestation'][i] = attestation_dict[df_formatted['Attestation'][i]]
    
    #CLEAN CITY: remove symbols and numbers
    if (df_formatted['City'][i] != None) and (df_formatted['City'][i] != ' '):
        df_formatted['City'][i] = re.sub(symbols_to_remove, "", df_formatted['City'][i])
        df_formatted['City'][i] = re.sub(numbers, "", df_formatted['City'][i])

    #CLEAN STATE: remove symbols and numbers
    if (df_formatted['State'][i] != None) and (df_formatted['State'][i] != ' '):
        df_formatted['State'][i] = re.sub(symbols_to_remove, "", df_formatted['State'][i])
        df_formatted['State'][i] = re.sub(numbers, "", df_formatted['State'][i])
        
    #CLEAN ADMISSION #: remove spaces, parenthesis, and other random values
    if (df_formatted['Admission # for Work Authorization'][i] != None) and (df_formatted['Admission # for Work Authorization'][i] != ' '):
        df_formatted['Admission # for Work Authorization'][i] = re.sub(symbols_to_remove, "", df_formatted['Admission # for Work Authorization'][i])
                     
    #CLEAN ALIEN # FOR PERMANENT RESIDENCE: remove spaces, parenthesis, and other random values
    if (df_formatted['Alien # for Permanent Residence'][i] != None) and (df_formatted['Alien # for Permanent Residence'][i] != ' '):
        df_formatted['Alien # for Permanent Residence'][i] = df_formatted['Alien # for Permanent Residence'][i].replace('O','0').replace(" ", "").replace("l","1").replace("'","").replace('"',"")
        df_formatted['Alien # for Permanent Residence'][i] = re.sub(symbols_to_remove, "", df_formatted['Alien # for Permanent Residence'][i])
    
    #CLEAN ALIEN # FOR WORK AUTHORIZATION: remove spaces, parenthesis, and other random values
    if (df_formatted['Alien # for Work Authorization'][i] != None) and (df_formatted['Alien # for Work Authorization'][i] != ' '):
        df_formatted['Alien # for Work Authorization'][i] = df_formatted['Alien # for Work Authorization'][i].replace('O','0').replace(" ", "").replace("l","1").replace("'","").replace('"',"")      
        df_formatted['Alien # for Work Authorization'][i] = re.sub(symbols_to_remove, "", df_formatted['Alien # for Work Authorization'][i])
                     
    #CLEAN TELEPHONE: remove parenthesis, spaces, and dashes from telephone if field is collected
    if (df_formatted['Telephone'][i] != None) and (df_formatted['Telephone'][i] != ' '):
        df_formatted['Telephone'][i] = re.sub(symbols_to_remove, "", df_formatted['Telephone'][i])
        df_formatted['Telephone'][i] = re.sub(letters, "", df_formatted['Telephone'][i])
        '{}-{}-{}'.format(df_formatted['Telephone'][i][0:3],df_formatted['Telephone'][i][3:6],df_formatted['Telephone'][i][6:])

    #CLEAN ZIP CODE: remove spaces and replaces any O's with 0's and L's with 1's
    if (df_formatted['Zip'][i] != None) and (df_formatted['Zip'][i] != ' '):
        df_formatted['Zip'][i] = df_formatted['Zip'][i].replace('O','0').replace(" ", "").replace("l","1").replace("'","").replace('"',"")
        df_formatted['Zip'][i] = re.sub(symbols_to_remove, "", df_formatted['Zip'][i])
        df_formatted['Zip'][i] = re.sub(letters, "", df_formatted['Zip'][i])
        
    #CLEAN EMAIL ADDRESS: remove spaces
    if (df_formatted['EmailAddress'][i] != None) and (df_formatted['EmailAddress'][i] != ' '):
        df_formatted['EmailAddress'][i] = df_formatted['EmailAddress'][i].replace(" ", "")
        
    #CLEAN DATE OF BIRTH: remove spaces, double slashes, and quotes and replaces any O's with 0's and L's with 1's and then removes any remaining letters
    if (df_formatted['DateOfBirth'][i] != None) and (df_formatted['DateOfBirth'][i] != ' '):
        df_formatted['DateOfBirth'][i] = df_formatted['DateOfBirth'][i].replace('O','0').replace(" ", "").replace("l","1").replace("I","1").replace("'","").replace('"',"")
        df_formatted['DateOfBirth'][i] = re.sub(date_symbols_to_remove, "", df_formatted['DateOfBirth'][i])
        df_formatted['DateOfBirth'][i] = re.sub(letters, "", df_formatted['DateOfBirth'][i])
        df_formatted['DateOfBirth'][i] = df_formatted['DateOfBirth'][i].strip("/")
    
    #CLEAN DATE OF HIRE: remove spaces, double slashes, and quotes and replaces any O's with 0's and L's with 1's and then removes any remaining letters
    if (df_formatted['DateOfHire'][i] != None) and (df_formatted['DateOfHire'][i] != ' '):
        df_formatted['DateOfHire'][i] = df_formatted['DateOfHire'][i].replace('O','0').replace(" ", "").replace("l","1").replace("I","1").replace("'","").replace('"',"")
        df_formatted['DateOfHire'][i] = re.sub(date_symbols_to_remove, "", df_formatted['DateOfHire'][i])
        df_formatted['DateOfHire'][i] = re.sub(letters, "", df_formatted['DateOfHire'][i])
        df_formatted['DateOfHire'][i] = df_formatted['DateOfHire'][i].strip("/")
    
    #CLEAN SOCIAL SECURITY: remove spaces, periods, quotes, replaces any O's with 0's and L's with 1's, and then removes any remaining letters. Remove slashes and then re-insert. 
    if (df_formatted['SocialSecurity'][i] != None) and (df_formatted['SocialSecurity'][i] != ' '):
        df_formatted['SocialSecurity'][i] = df_formatted['SocialSecurity'][i].replace('O','0').replace(" ", "").replace("l","1").replace("'","").replace('"',"")
        df_formatted['SocialSecurity'][i] = re.sub(symbols_to_remove, "", df_formatted['SocialSecurity'][i])
        df_formatted['SocialSecurity'][i] = re.sub(letters, "", df_formatted['SocialSecurity'][i])
        df_formatted['SocialSecurity'][i] = '{}-{}-{}'.format(df_formatted['SocialSecurity'][i][0:3],df_formatted['SocialSecurity'][i][3:5],df_formatted['SocialSecurity'][i][5:])
        
    #CLEAN DATE SIGNED BY EMPLOYER: remove spaces, double slashes, and quotes and replaces any O's with 0's and L's with 1's and then removes any remaining letters
    if (df_formatted['Date Signed by Employer'][i] != None) and (df_formatted['Date Signed by Employer'][i] != ' '):
        df_formatted['Date Signed by Employer'][i] = df_formatted['Date Signed by Employer'][i].replace('O','0').replace(" ", "").replace("l","1").replace("'","").replace('"',"")
        df_formatted['Date Signed by Employer'][i] = re.sub(date_symbols_to_remove, "", df_formatted['Date Signed by Employer'][i])
        df_formatted['Date Signed by Employer'][i] = re.sub(letters, "", df_formatted['Date Signed by Employer'][i])
        df_formatted['Date Signed by Employer'][i] = df_formatted['Date Signed by Employer'][i].strip("/")
        
    #CLEAN DATE EXPIRATION OF WORK AUTHORIZATION: remove spaces, double slashes, and quotes and replaces any O's with 0's and L's with 1's and then removes any remaining letters
    if (df_formatted['Date Expiration of Work Authorization'][i] != None) and (df_formatted['Date Expiration of Work Authorization'][i] != ' '):
        df_formatted['Date Expiration of Work Authorization'][i] = df_formatted['Date Expiration of Work Authorization'][i].replace('O','0').replace(" ", "").replace("I","1").replace("l","1").replace("'","").replace('"',"")
        df_formatted['Date Expiration of Work Authorization'][i] = re.sub(date_symbols_to_remove, "", df_formatted['Date Expiration of Work Authorization'][i])
        df_formatted['Date Expiration of Work Authorization'][i] = re.sub(letters, "", df_formatted['Date Expiration of Work Authorization'][i])
        df_formatted['Date Expiration of Work Authorization'][i] = df_formatted['Date Expiration of Work Authorization'][i].strip("/")
        
    #CLEAN LIST A - DOCUMENTEXPIRATIONDATE: remove spaces, double slashes, and quotes and replaces any O's with 0's and L's with 1's and then removes any remaining letters
    if (df_formatted['List A - DocumentExpirationDate'][i] != None) and (df_formatted['List A - DocumentExpirationDate'][i] != ' '):
        df_formatted['List A - DocumentExpirationDate'][i] = df_formatted['List A - DocumentExpirationDate'][i].replace('O','0').replace(" ", "").replace("I","1").replace("l","1").replace("'","").replace('"',"")
        df_formatted['List A - DocumentExpirationDate'][i] = re.sub(letters, "", df_formatted['List A - DocumentExpirationDate'][i])
        df_formatted['List A - DocumentExpirationDate'][i] = re.sub(date_symbols_to_remove, "", df_formatted['List A - DocumentExpirationDate'][i])
        
    #CLEAN LIST B - DOCUMENTEXPIRATIONDATE: remove spaces, double slashes, and quotes and replaces any O's with 0's and L's with 1's and then removes any remaining letters
    if (df_formatted['List B - DocumentExpirationDate'][i] != None) and (df_formatted['List B - DocumentExpirationDate'][i] != ' '):
        df_formatted['List B - DocumentExpirationDate'][i] = df_formatted['List B - DocumentExpirationDate'][i].replace('O','0').replace(" ", "").replace("\\","").replace("I","1").replace("l","1").replace("'","").replace('"',"")
        df_formatted['List B - DocumentExpirationDate'][i] = re.sub(letters, "", df_formatted['List B - DocumentExpirationDate'][i])
        df_formatted['List B - DocumentExpirationDate'][i] = re.sub(date_symbols_to_remove, "", df_formatted['List B - DocumentExpirationDate'][i])
        
    #CLEAN LIST C - DOCUMENTEXPIRATIONDATE: remove spaces, double slashes, and quotes and replaces any O's with 0's and L's with 1's and then removes any remaining letters
    if (df_formatted['List C - DocumentExpirationDate'][i] != None) and (df_formatted['List C - DocumentExpirationDate'][i] != ' '):
        df_formatted['List C - DocumentExpirationDate'][i] = df_formatted['List C - DocumentExpirationDate'][i].replace('O','0').replace(" ", "").replace("\\","").replace("I","1").replace("l","1").replace("'","").replace('"',"")
        df_formatted['List C - DocumentExpirationDate'][i] = re.sub(date_symbols_to_remove, "", df_formatted['List C - DocumentExpirationDate'][i])
        df_formatted['List C - DocumentExpirationDate'][i] = re.sub(letters, "", df_formatted['List C - DocumentExpirationDate'][i])
    
###########################################################
##############CREATE SUBSET DATAFRAME######################
###########################################################
        
#make the list of columns to grab
columns = ['LastName','FirstName', 'DateOfBirth', 'SocialSecurity', 'Attestation',
           'Alien # for Permanent Residence', 'Alien # for Work Authorization', 
           'StreetAddress', 'City', 'State', 'Zip', 'TranslatorName', 
           'List A - DocumentTitle', 'List A - DocumentNumber', 
           'List B - DocumentTitle', 'List B - DocumentNumber', 
           'List C - DocumentTitle', 'List C - DocumentNumber', 
           'DateOfHire']

#create a dictionary to get the text value needed 
attestation_dict = {'box 1': 'A citizen of the United States',
                    'box 2': 'A noncitizen of the United States',
                    'box 3': 'A lawful permanent resident (Alien #)',
                    'box 4': 'An alien authorized to work',
                    'no box': 'Attestation not filled in!'
        }

#choose the selected columns from df_clean
df_clean = df_formatted.loc[:,columns]

#create columns to add to df_clean
AlienAdmissionNumber = []
DocumentTitle = []
DocumentNumber = []

for i in range(len(df_formatted)):
    #set A# or Admission# value depending on Attestation
    if df_clean['Attestation'][i] == 'A citizen of the United States':
        AlienAdmissionNumber.append('NA')
    elif (df_clean['Attestation'][i] == 'A lawful permanent resident (Alien #)'):
        AlienAdmissionNumber.append(df_clean['Alien # for Permanent Residence'][i])            
    elif (df_clean['Attestation'][i] == 'An alien authorized to work'):
        AlienAdmissionNumber.append(df_clean['Alien # for Work Authorization'][i])  
    else:
        AlienAdmissionNumber.append('NA')
          
    #set document title
    if (df_clean['List A - DocumentTitle'][i] != ' ') and (df_clean['List A - DocumentTitle'][i] is not None):
        DocumentTitle.append(df_clean['List A - DocumentTitle'][i])
    else:
        if (df_clean['List B - DocumentTitle'][i] is not None) & (df_clean['List C - DocumentTitle'][i] is not None):
            DocumentTitle.append(df_clean['List B - DocumentTitle'][i] + " and " + df_clean['List C - DocumentTitle'][i])
        else:
            DocumentTitle.append("NA")
    
    #set document number
    if (df_clean['List A - DocumentNumber'][i] != ' ') and (df_clean['List A - DocumentNumber'][i] is not None):
        DocumentNumber.append(df_clean['List A - DocumentNumber'][i])
    else:
        if (df_clean['List B - DocumentNumber'][i] is not None) & (df_clean['List C - DocumentNumber'][i] is not None):
            DocumentNumber.append(df_clean['List B - DocumentNumber'][i] + " and " + df_clean['List C - DocumentNumber'][i])
        else:
            DocumentNumber.append("NA")

#create new columns from the lists
df_clean['A# or Admission#'] = AlienAdmissionNumber
df_clean['DocumentTitle'] = DocumentTitle
df_clean['DocumentNumber'] = DocumentNumber
                 
#delete uneeded columns
cols_to_delete = ['Alien # for Permanent Residence', 'Alien # for Work Authorization',
                  'List A - DocumentTitle', 'List B - DocumentTitle', 'List A - DocumentNumber',
                  'List B - DocumentNumber', 'List C - DocumentTitle', 'List C - DocumentNumber']

df_clean.drop(cols_to_delete, axis = 1, inplace = True)  

#order columns
cols = ['LastName', 'FirstName', 'DateOfBirth', 'SocialSecurity', 'Attestation', 
        'A# or Admission#', 'StreetAddress', 'City', 'State', 'Zip', 'TranslatorName',
        'DocumentTitle', 'DocumentNumber', 'DateOfHire']

df_clean = df_clean[cols]
        
#output = json.dumps(ocrs)
#sys.stdout.write(output)