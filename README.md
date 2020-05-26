## WIP --currently adding to this repo

Simple script to visualize your facebook ad data. (Requires requesting data download from FB)

## Data Download Steps:
Log in to your Facebook Page.

Settings --> 

Your Facebook Information --> 

Download Your Information --> 

Make sure the box for "Ads and Business" is checked. You can uncheck the other boxes if you wish. <h5>IMPORTANT:</h5> Click dropdown menu for "Format" change to "JSON". --> "Create File"

You will have to wait a few days for Facebook to process your information and send it.

## Using this script
<h2> Wordcloud <h2>
  
Fork and clone into this repo. Run `./init.sh` to install requirements.

<h4>Option 1:</h4> Download your facebook zip. Unzip. Move this file into the repo: "advertisers_who_uploaded_a_contact_list_with_your_information.json"

(`mv advertisers_who_uploaded_a_contact_list_with_your_information.json /path/to/facebook_advertiser_viz`)

Run: `python3 generate.py` 



<h4>Option 2:</h4> Download your facebook zip. Unzip. Find the path to this file:
"advertisers_who_uploaded_a_contact_list_with_your_information.json"


Run `python3 generate.py --path "/path/to/advertisers_who_uploaded_a_contact_list_with_your_information.json"`



_Why Don't I see that file?_
It is possible that you did not check "Ads and Business" when you requested your data download.



<h3> Geomap </h3>
  <i>Coming soon</i>
  
  
<h3>Which Famous People does Facebook think I want to see ads about?</h3>
 <i>Coming soon</i>

