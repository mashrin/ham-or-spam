# -*- coding: utf-8 -*-
# @Author: Inderpartap Cheema
# @Date:   2017-02-10
# @Last Modified by:   Inderpartap Cheema
# @Last Modified time: 2017-04-16 19:30:00
# @GPLv3 License

import os

import bs4
import dill

APP = os.path.abspath(__file__)
APP_DIR, APP_NAME = os.path.split(APP)

classifier_file_path = os.path.join(APP_DIR, 'saved_classifiers', 'spam_classifier.pickle')
classifier_file = open(classifier_file_path, 'rb')
classifier_object = dill.load(classifier_file)
classifier_file.close()

trainer_file_path = os.path.join(APP_DIR, 'saved_classifiers', 'trainer.pickle')
trainer_file = open(trainer_file_path, 'rb')
trainer_object = dill.load(trainer_file)
trainer_file.close()

def ham_or_spam(email_text):
    """
    :param email_text: the passed email text to be classified
    :returns: Whether the passed email is a spam, ham or giving
              UnicodeEncodeError
    """
    try:
        # === Preprocessing ==== #
        email_text = bs4.UnicodeDammit.detwingle(
            email_text).decode('utf-8')
        email_text = email_text.encode('ascii', 'ignore')
        # ====================== #

        hamorspam = classifier_object.classify(
                        trainer_object.extract_features(email_text)
                    )
        response = {'category': hamorspam, 'status': 'ok'}

        # anything printed to the STDOUT will be stored in heroku's logs
        print "TEXT: '{0}' :: RESPONSE : '{1}'".format(     
                    email_text.replace("\n", " ").replace("\r", " "),     
                    hamorspam
                )

        return response
    except UnicodeEncodeError:
        hamorspam = 'UnicodeEncodeError'
        response = {'category': hamorspam, 'status': 'error'}
        return response
