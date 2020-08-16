#Author: Patrick McNeil
#Helper libraries from Tim Jarrett & Chris Campbell
import sys
import requests
from datetime import datetime
from optparse import OptionParser
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC
from helpers import api
from helpers.unicodecsv import create_csv

def get_user_api_expiration(expiry,credtype):
    
    usernames = api.VeracodeAPI().get_users()
    length=len(usernames)
    count=1
    for user in usernames:

        userdata = api.VeracodeAPI().get_user(user["user_id"])
        if ("api_credentials" in userdata) and ((credtype == "all") or (credtype in str(userdata))):
            date_time_str = datetime.strptime(userdata["api_credentials"]["expiration_ts"], "%Y-%m-%dT%H:%M:%S.000+0000")
            date_time = "{} {}".format(str(date_time_str.date()),str(date_time_str.time()))
            expiry.append((user["user_name"],user["email_address"],date_time))
        
        percent = ("{0:.0f}".format(100*(count/float(length))))
        filledLength=int(100*count // length)
        bar="*" * filledLength + '-' * (100-filledLength)
        print(f'\r{"Progress:"} |{bar}| {percent}% Complete', end="\r")
        count+=1

    print("\r\n")
    return expiry

def main():

    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage,version='Version 1.0')
    parser.add_option("-f", "--filename", dest="filename", help="The file name for user API expiry results")
    parser.add_option("-a", "--apiusers", dest="credtype", action="store_const", const="apiUser", help="Only retrieve API account data. Default is all account types.")
    parser.add_option("-u", "--humans", dest="credtype", action="store_const", const="humanUser", help="Only retrieve Human account data. Default is all account types.")

    options, args = parser.parse_args()
    credtype = options.credtype
    filename = options.filename
    if not filename:
        print("Please specify a file path/name using the -f option.")
        exit(0)

    if credtype=="apiUser":
        crednote="API"
    elif credtype=="humanUser":
        crednote="human"
    else:
        credtype="all"
        crednote="all"

    start_time = datetime.now()
    expiry = []

    print("Retrieving {} user information. Please be patient, this may take some time...".format(crednote))
    get_user_api_expiration(expiry,credtype)
    
    csv_header = ["User Name", "Email Address", "Expiry Date"]
    print("Writing to CSV file {}".format(filename))
    create_csv([csv_header] + expiry, filename)

    print("Total elapsed time (HH:MM:SS.us): {}".format(datetime.now() - start_time))
    print("Done.")
       
if __name__ == '__main__':
    main()
