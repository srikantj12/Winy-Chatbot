from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import sqlite3 as lite


class ActionHelp(Action):
    def name(self):
        return 'action_help'

    def run(self, dispatcher, tracker, domain):
        """Prints a help message when the user types 'help'. It tells
        the user what he/she can ask the chatbot

        Parameters
        ----------
        dispatcher : object
            Invokes the utter_message function which allows us to send a
            message to the inputChannel
        tracker : state
            Keeps track of the state in the conversation. In our case it is
            slot(entity): 'Variety'
        domain : yml file
            Domain file - wine_domain.yml

        Returns
        -------
        Nothing

        """
        dispatcher.utter_template("utter_help")


class ActionVariety(Action):
    def name(self):
        return 'action_variety'

    def run(self, dispatcher, tracker, domain):
        """Gets a description of the wine from the database.

        Parameters
        ----------
        dispatcher : object
            Invokes the utter_message function which allows us to send a
            message to the inputChannel
        tracker : state
            Keeps track of the state in the conversation. In our case it is
            slot(entity): 'Variety'
        domain : yml file
            Domain file - wine_domain.yml

        Returns
        -------
        Nothing


        """
        variety = tracker.get_slot('Variety')
        conn = lite.connect('wine.db')
        sql = (" SELECT description FROM reviews WHERE description IS NOT NULL"
               " AND variety like (?) limit 1")
        args = ("%"+variety+"%",)
        cur = conn.execute(sql, args)
        response = cur.fetchall()
        for row in response:
            row = row[0]
            dispatcher.utter_message("{}".format(row))
        conn.close()
        return [SlotSet('Variety', variety)]


class ActionPrice(Action):
    def name(self):
        return 'action_price'

    def run(self, dispatcher, tracker, domain):
        """Gets the price of a wine from the database

        Parameters
        ----------
        dispatcher : object
            Invokes the utter_message function which allows us to send a
            message to the inputChannel
        tracker : state
            Keeps track of the state in the conversation. In our case it is
            slot(entity): 'Variety'
        domain : yml file
            Domain file - wine_domain.yml

        Returns
        -------
        Nothing

        """
        variety = tracker.get_slot('Variety')
        conn = lite.connect('wine.db')
        sql = ("SELECT price FROM reviews WHERE variety like (?) "
               "ORDER BY points DESC limit 5 ")
        args = ("%"+variety+"%",)
        cur = conn.execute(sql, args)
        price_response = cur.fetchall()
        dispatcher.utter_message("Here are the top 5 prices"
                                 " for {}:".format(variety))
        for row in price_response:
            row = row[0]
            dispatcher.utter_message("${}".format(row))
        conn.close()
        return [SlotSet('Variety', variety)]


class ActionCountry(Action):
    def name(self):
        return 'action_country'

    def run(self, dispatcher, tracker, domain):
        """Gets the country in which the wine is made from the database.

        Parameters
        ----------
        dispatcher : object
            Invokes the utter_message function which allows us to send a
            message to the inputChannel
        tracker : state
            Keeps track of the state in the conversation. In our case it is
            slot(entity): 'Variety'
        domain : yml file
            Domain file - wine_domain.yml

        Returns
        -------
        Nothing

        """
        variety = tracker.get_slot('Variety')
        conn = lite.connect('wine.db')
        sql = ("SELECT country FROM reviews WHERE country IS NOT NULL"
               " AND variety like (?) "
               "ORDER BY points DESC limit 1")
        args = ("%"+variety+"%",)
        cur = conn.execute(sql, args)
        country_response = cur.fetchall()
        dispatcher.utter_message("{} is from: \n".format(variety))
        dispatcher.utter_message("{}".format(country_response))
        conn.close()
        return [SlotSet('Variety', variety)]


class ActionRating(Action):
    def name(self):
        return 'action_rating'

    def run(self, dispatcher, tracker, domain):
        """Gets the rating of the wine from the database.

        Parameters
        ----------
        dispatcher : object
            Invokes the utter_message function which allows us to send a
            message to the inputChannel
        tracker : state
            Keeps track of the state in the conversation. In our case it is
            slot(entity): 'Variety'
        domain : yml file
            Domain file - wine_domain.yml

        Returns
        -------
        Nothing

        """
        variety = tracker.get_slot('Variety')
        conn = lite.connect('wine.db')
        sql = ("SELECT DISTINCT points FROM reviews WHERE points IS NOT NULL "
               "AND variety like (?) limit 1")
        args = ("%"+variety+"%",)
        cur = conn.execute(sql, args)
        rating = cur.fetchall()
        for row in rating:
            row = row[0]
            dispatcher.utter_message("{} has a rating"
                                     " of {}".format(variety, row))
        conn.close()
        return [SlotSet('Variety', variety)]
