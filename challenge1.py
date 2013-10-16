from lxml import etree
import sys

def parse_xml():
	apartments = etree.parse("test.xml").getroot()

	highest_monthly_rent = -1
	lowest_monthly_rent = -1
	av_1_bdrm_sqft_ca = 0
	highest_price_per_sqft = -1
	num_apart_sfca = 0
	num_2_bthrm_nyny = 0

	total_1_bdrm_ca_count = 0
	total_1_bdrm_ca_sqft = 0

	total_1_bdrm_sfca_laca_count = 0
	total_1_bdrm_sfca_laca_rent = 0
	
	for apartment in apartments:

		attr = {}
		for child in apartment.getchildren():
			attr[child.tag] = child.text

		if float(attr["Rent"]) > highest_monthly_rent or \
				highest_monthly_rent == -1:
			highest_monthly_rent = float(attr["Rent"])
		if float(attr["Rent"]) < lowest_monthly_rent or \
				lowest_monthly_rent == -1:
			lowest_monthly_rent = float(attr["Rent"])
		if attr["State"] == "CA" and attr["Beds"] == "1":
			total_1_bdrm_ca_sqft += float(attr["SquareFoot"])
			total_1_bdrm_ca_count += 1.0
		if float(attr["Rent"]) / float(attr["SquareFoot"]) > \
				highest_price_per_sqft:
			highest_price_per_sqft = float(attr["Rent"]) / \
					float(attr["SquareFoot"])
		if attr["City"] == "San Francisco" and attr["State"] == "CA":
			num_apart_sfca += 1.0
		if attr["City"] == "New York" and attr["State"] == "NY" and \
				attr["Bathrooms"] == "2":
			num_2_bthrm_nyny += 1.0
		if (attr["City"] == "San Francisco" or \
				attr["City"] == "Los Angeles") and attr["State"] == "CA" and \
				attr["Beds"] == "1":
			total_1_bdrm_sfca_laca_rent += float(attr["Rent"])
			total_1_bdrm_sfca_laca_count += 1.0

	if highest_monthly_rent == -1:
		highest_monthly_rent = "N/A"
	if lowest_monthly_rent == -1:
		lowest_monthly_rent = "N/A"
	if highest_price_per_sqft == -1:
		highest_price_per_sqft = "N/A"

	print "Highest Rent: $" + str(highest_monthly_rent)
	print "Lowest Rent: $" + str(lowest_monthly_rent)
	print "Average Square Footage 1 Bedroom in CA: " + \
			str(total_1_bdrm_ca_sqft / total_1_bdrm_ca_count)
	print "Highest Price Per Square Foot: $" + str(highest_price_per_sqft)
	print "Number of Apartments in SF: " + str(num_apart_sfca)
	print "Number of Apartments 2 Bathrooms: " + str(num_2_bthrm_nyny)
	print "Average Rent 1 Bedroom in SF or LA: $" + \
			str(total_1_bdrm_sfca_laca_rent / total_1_bdrm_sfca_laca_count)

parse_xml()
