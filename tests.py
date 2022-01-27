import test_fixtures as fixtures
import update_functions as app
import simplejson as json
import unittest
import unittest.mock as mock
import requests

class TestEventList(unittest.TestCase):
    # testing functions in app.py
    
    def test_format_meetup_events(self):
        #function should return a list of dictionaries
        output = app.format_meetup_events(fixtures.meetup_events_list)
        self.assertIsInstance(output, list)       #returns a list
        self.assertTrue(len(output) > 0)                #list is not empty
        self.assertIsInstance(output[0], dict)    #first item in list is dictionary
        self.assertTrue(len(list(output[0].keys())))    #first dictionary is not empty

    def test_format_eventbrite_events(self):
        #function should return a list of dictionaries
        output = app.format_eventbrite_events(fixtures.eventbrite_events_list, fixtures.eventbrite_venues_list, fixtures.group_list['Eventbrite'])
        self.assertIsInstance(output, list)       #returns a list
        self.assertTrue(len(output) > 0)                #list is not empty
        self.assertIsInstance(output[0], dict)    #first item in list is dictionary
        self.assertTrue(len(list(output[0].keys())))    #first dictionary is not empty

    @mock.patch('app.requests.get')
    def test_get_group_lists(self, mock_get):
        #function should return a dictionary of lists
        mock_response = mock.MagicMock()
        mock_response.text = fixtures.open_upstate_response_text
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        output = app.get_group_lists()
        self.assertIsInstance(output, dict)                     #returns a dictionary
        self.assertIsInstance(output['Meetup'], list)           #Meetup attribute returns a list
        self.assertIsInstance(output['Eventbrite'], list)       #Eventbrite attribute returns a list

    @mock.patch('app.requests.get')
    def test_get_meetup_events(self, mock_get):
        #function should return list of dictionaries
        mock_response = mock.MagicMock()
        mock_response.text = fixtures.meetup_events_list_text
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        output = app.get_meetup_events(fixtures.group_list['Meetup'])
        self.assertIsInstance(output, list)       #returns a list
        self.assertTrue(len(output) > 0)                #list is not empty
        self.assertIsInstance(output[0], dict)    #first item in list is dictionary
        self.assertTrue(len(list(output[0].keys())))    #first dictionary is not empty

    @mock.patch('app.requests.get')
    def test_get_eventbrite_events(self, mock_get):
        #function should return list of dictionaries
        mock_response = mock.MagicMock()
        mock_response.text = fixtures.eventbrite_events_list_text
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        output = app.get_eventbrite_events(fixtures.group_list['Eventbrite'])
        self.assertIsInstance(output, list)       #returns a list
        self.assertTrue(len(output) > 0)                #list is not empty
        self.assertIsInstance(output[0], dict)    #first item in list is dictionary
        self.assertTrue(len(list(output[0].keys())))    #first dictionary is not empty

    @mock.patch('app.requests.get')
    def test_get_eventbrite_venues(self, mock_get):
        #function should return list of dictionaries
        mock_response = mock.MagicMock()
        mock_response.text = fixtures.eventbrite_venues_list_text
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        output = app.get_eventbrite_venues(fixtures.eventbrite_events_list)
        self.assertIsInstance(output, list)       #returns a list
        self.assertTrue(len(output) > 0)                #list is not empty
        self.assertIsInstance(output[0], dict)    #first item in list is dictionary
        self.assertTrue(len(list(output[0].keys())))    #first dictionary is not empty


if __name__ == '__main__':
    unittest.main()
