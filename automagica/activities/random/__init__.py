

def generate_random_name(locale=None):
    """
	Generates a random name.

	:param locale: Add a locale to generate popular name for selected locale.
		ar_EG - Arabic (Egypt)
		ar_PS - Arabic (Palestine)
		ar_SA - Arabic (Saudi Arabia)
		bg_BG - Bulgarian
		bs_BA - Bosnian
		cs_CZ - Czech
		de_DE - German
		dk_DK - Danish
		el_GR - Greek
		en_AU - English (Australia)
		en_CA - English (Canada)
		en_GB - English (Great Britain)
		en_NZ - English (New Zealand)
		en_US - English (United States)
		es_ES - Spanish (Spain)
		es_MX - Spanish (Mexico)
		et_EE - Estonian
		fa_IR - Persian (Iran)
		fi_FI - Finnish
		fr_FR - French
		hi_IN - Hindi
		hr_HR - Croatian
		hu_HU - Hungarian
		hy_AM - Armenian
		it_IT - Italian
		ja_JP - Japanese
		ka_GE - Georgian (Georgia)
		ko_KR - Korean
		lt_LT - Lithuanian
		lv_LV - Latvian
		ne_NP - Nepali
		nl_NL - Dutch (Netherlands)
		no_NO - Norwegian
		pl_PL - Polish
		pt_BR - Portuguese (Brazil)
		pt_PT - Portuguese (Portugal)
		ro_RO - Romanian
		ru_RU - Russian
		sl_SI - Slovene
		sv_SE - Swedish
		tr_TR - Turkish
		uk_UA - Ukrainian
		zh_CN - Chinese (China)
		zh_TW - Chinese (Taiwan)
	"""
    from faker import Faker
    if locale:
        seed = Faker(locale)
    else:
        seed = Faker()
    return seed.name()

def generate_random_sentence(locale=None):
    """
	Generates a random sentence.

	:param locale: Add a locale to generate sentences for selected locale (language).
		ar_EG - Arabic (Egypt)
		ar_PS - Arabic (Palestine)
		ar_SA - Arabic (Saudi Arabia)
		bg_BG - Bulgarian
		bs_BA - Bosnian
		cs_CZ - Czech
		de_DE - German
		dk_DK - Danish
		el_GR - Greek
		en_AU - English (Australia)
		en_CA - English (Canada)
		en_GB - English (Great Britain)
		en_NZ - English (New Zealand)
		en_US - English (United States)
		es_ES - Spanish (Spain)
		es_MX - Spanish (Mexico)
		et_EE - Estonian
		fa_IR - Persian (Iran)
		fi_FI - Finnish
		fr_FR - French
		hi_IN - Hindi
		hr_HR - Croatian
		hu_HU - Hungarian
		hy_AM - Armenian
		it_IT - Italian
		ja_JP - Japanese
		ka_GE - Georgian (Georgia)
		ko_KR - Korean
		lt_LT - Lithuanian
		lv_LV - Latvian
		ne_NP - Nepali
		nl_NL - Dutch (Netherlands)
		no_NO - Norwegian
		pl_PL - Polish
		pt_BR - Portuguese (Brazil)
		pt_PT - Portuguese (Portugal)
		ro_RO - Romanian
		ru_RU - Russian
		sl_SI - Slovene
		sv_SE - Swedish
		tr_TR - Turkish
		uk_UA - Ukrainian
		zh_CN - Chinese (China)
		zh_TW - Chinese (Taiwan)
	"""
	from faker import Faker
	if locale:
		seed = Faker(locale)
	else:
		seed = Faker()
	return seed.sentence()

def generate_random_address(locale=None):
	"""
	Generates a random address.

	:param locale: Add a locale to generate addresses for selected locale.
		ar_EG - Arabic (Egypt)
		ar_PS - Arabic (Palestine)
		ar_SA - Arabic (Saudi Arabia)
		bg_BG - Bulgarian
		bs_BA - Bosnian
		cs_CZ - Czech
		de_DE - German
		dk_DK - Danish
		el_GR - Greek
		en_AU - English (Australia)
		en_CA - English (Canada)
		en_GB - English (Great Britain)
		en_NZ - English (New Zealand)
		en_US - English (United States)
		es_ES - Spanish (Spain)
		es_MX - Spanish (Mexico)
		et_EE - Estonian
		fa_IR - Persian (Iran)
		fi_FI - Finnish
		fr_FR - French
		hi_IN - Hindi
		hr_HR - Croatian
		hu_HU - Hungarian
		hy_AM - Armenian
		it_IT - Italian
		ja_JP - Japanese
		ka_GE - Georgian (Georgia)
		ko_KR - Korean
		lt_LT - Lithuanian
		lv_LV - Latvian
		ne_NP - Nepali
		nl_NL - Dutch (Netherlands)
		no_NO - Norwegian
		pl_PL - Polish
		pt_BR - Portuguese (Brazil)
		pt_PT - Portuguese (Portugal)
		ro_RO - Romanian
		ru_RU - Russian
		sl_SI - Slovene
		sv_SE - Swedish
		tr_TR - Turkish
		uk_UA - Ukrainian
		zh_CN - Chinese (China)
		zh_TW - Chinese (Taiwan)
	"""
	from faker import Faker
	if locale:
		seed = Faker(locale)
	else:
		seed = Faker()
	return seed.address()

def generate_random_number(lower_limit=0,upper_limit=10, fractional=False):
	"""
	Generates a random number. Can be integers (not a fractional number) or a float (fractional number).

	:param lower_limit: Lower limit for random number
	:param upper_limit: Upper limit for random number
	:param fractional: Setting this to True will generate fractional number. Default value is False and only generates whole numbers.
	"""
	import random 
	if fractional:
		return random.uniform(lower_limit, upper_limit)
	else:
		return random.randrange(lower_limit,upper_limit,1)

def generate_random_boolean():
	"""
	Generates a random boolean (True or False)
	"""
	import random 
	return bool(random.getrandbits(1))

def generate_random_beep(max_duration=2000, max_frequency=5000):
	"""
	Generates a random beep, only works on Windows

	:param max_duration: Maximum random duration in miliseconds. Default value is 2 miliseconds
	:param max_frequency: Maximum random frequency in Hz. Default value is 5000 Hz.
	"""
	import winsound
	import random
	frequency = random.randrange(5000)
	duration = random.randrange(2000)
	winsound.Beep(frequency, duration)

def generate_random_date(format='%m/%d/%Y %I:%M', days_in_past=1000):
    """
	Generate a random date. 

    :param days_in_past: Days in the past for which oldest random date is generated, default is 1000 days
	:param format: Formatting of the dates, replace with 'None' to get raw datetime format. 
	e.g. format='Current month is %B' generates 'Current month is Januari' and format='%m/%d/%Y %I:%M' generates format 01/01/1900 00:00. 
	%a	Abbreviated weekday name.	 
	%A	Full weekday name.	 
	%b	Abbreviated month name.	 
	%B	Full month name.	 
	%c	Predefined date and time representation.	 
	%d	Day of the month as a decimal number [01,31].	 
	%H	Hour (24-hour clock) as a decimal number [00,23].	 
	%I	Hour (12-hour clock) as a decimal number [01,12].	 
	%j	Day of the year as a decimal number [001,366].	 
	%m	Month as a decimal number [01,12].	 
	%M	Minute as a decimal number [00,59].	 
	%p	AM or PM.
	%S	Second as a decimal number [00,61].	
	%U	Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.	(3)
	%w	Weekday as a decimal number [0(Sunday),6].	 
	%W	Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.	(3)
	%x	Predefined date representation.	 
	%X	Predefined time representation.	 
	%y	Year without century as a decimal number [00,99].	 
	%Y	Year with century as a decimal number.
	%Z	Time zone name (no characters if no time zone exists).
    """

	import random
	import datetime

	latest  = datetime.datetime.now()
	earliest = latest - datetime.timedelta(days=days_in_past)
	delta_seconds = (latest - earliest).total_seconds()

	random_date = earliest + datetime.timedelta(seconds = random.randrange(delta_seconds))

	if format:
		return random_date.strftime(format)
	else:
		return random_date