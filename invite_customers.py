"""
"""
import json
import operator
from geopy.distance import vincenty



OFFICE = (53.3393, -6.2576841)
CUSTOMERS_FILE = 'customers.json'



def customers_invitation(customers_file, office_position):
    """Use this function to create a list of customers close
    to the office.

    Args:
        customers_file: json file with a customers.
        office_position: for latitude and longitude of our office.

    Returns:
        The return cointain the list with all user_id and name of customers ordened.

    """
    customers_invite = {}

    for line in open(customers_file, 'r'):
        customer_latitude = (json.loads(line))['latitude']
        customer_longitude = (json.loads(line))['longitude']
        customer_user_id = (json.loads(line))['user_id']
        customer_name = (json.loads(line))['name']

        if vincenty(office_position, (customer_latitude, customer_longitude)).kilometers < 100:
            customers_invite[customer_user_id] = customer_name

    return sorted(customers_invite.items(), key=operator.itemgetter(0))



if __name__ == '__main__':
    print customers_invitation(customers_file=CUSTOMERS_FILE, office_position=OFFICE)[0][1]
