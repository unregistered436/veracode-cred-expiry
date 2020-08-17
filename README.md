# Veracode API Credential Expiry Date Report
This tool will create a CSV report of Veracode platform API credential user names, emails, and their expiry dates. Output can be restricted to only "API" accounts used for CI/CD integrations, or "human" users which are typically developers.

## Requirements
* Python3.6 and above
* A valid API Key and ID for the Veracode platform with Administrator permissions (API service account or human user account)
* Local system permissions to install new Python3 libraries via pip

## Setup
Clone this repository:
```
    git clone https://github.com/unregistered436/veracode-cred-expiry
```
Install dependencies:
```
    cd veracode-cred-expiry
    sudo python3 -m pip install -r requirements.txt
```
(Recommended) Save Veracode API credentials in `~/.veracode/credentials`
```
    [default]
    veracode_api_key_id = <YOUR_API_KEY_ID>
    veracode_api_key_secret = <YOUR_API_KEY_SECRET>
```
Otherwise you will need to set environment variables before running:
``` 
    export VERACODE_API_KEY_ID=<YOUR_API_KEY_ID>
    export VERACODE_API_KEY_SECRET=<YOUR_API_KEY_SECRET>
```
    
The Veracode Identity API is described further here: https://help.veracode.com/go/c_identity_intro
    
## Run
If you have saved credentials as above you can run:
    `python3 cred-expiry.py -f <YOUR_FILE_NAME>`

## Usage
```Usage: python3 cred-expiry.py [options] arg1 arg2

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -f FILENAME, --filename=FILENAME
                        The file name for user API expiry results
  -a, --apiusers        Only retrieve API account data. Default is all account
                        types.
  -u, --humans          Only retrieve Human account data. Default is all
                        account types.
```
