# Generated by Django 4.2.9 on 2024-01-21 22:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('phone_number', models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message='Номер телефона должен быть в формате 7XXXXXXXXXX', regex='^7\\d{10}$')], verbose_name='Номер телефона')),
                ('operator_code', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Код мобильного оператора должен начинаться с символа "+"', regex='^\\+\\d{1,5}$')], verbose_name='Код мобильного оператора')),
                ('timezone', models.CharField(choices=[('Asia/Khandyga', 'Asia/Khandyga'), ('America/Monterrey', 'America/Monterrey'), ('Egypt', 'Egypt'), ('Asia/Chita', 'Asia/Chita'), ('Europe/Malta', 'Europe/Malta'), ('Etc/GMT-14', 'Etc/GMT-14'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Brazil/West', 'Brazil/West'), ('Asia/Kuching', 'Asia/Kuching'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('America/Godthab', 'America/Godthab'), ('Australia/Eucla', 'Australia/Eucla'), ('Asia/Makassar', 'Asia/Makassar'), ('Australia/Melbourne', 'Australia/Melbourne'), ('Canada/Pacific', 'Canada/Pacific'), ('America/Cayenne', 'America/Cayenne'), ('Etc/GMT-8', 'Etc/GMT-8'), ('Africa/Monrovia', 'Africa/Monrovia'), ('GB-Eire', 'GB-Eire'), ('Australia/Canberra', 'Australia/Canberra'), ('America/St_Kitts', 'America/St_Kitts'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Pacific/Yap', 'Pacific/Yap'), ('America/Rainy_River', 'America/Rainy_River'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('America/Dominica', 'America/Dominica'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('America/Halifax', 'America/Halifax'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Europe/Vilnius', 'Europe/Vilnius'), ('America/Louisville', 'America/Louisville'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Pacific/Wake', 'Pacific/Wake'), ('America/Tortola', 'America/Tortola'), ('Asia/Singapore', 'Asia/Singapore'), ('America/Noronha', 'America/Noronha'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Australia/Darwin', 'Australia/Darwin'), ('Africa/Conakry', 'Africa/Conakry'), ('Europe/Vaduz', 'Europe/Vaduz'), ('America/New_York', 'America/New_York'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Antarctica/Troll', 'Antarctica/Troll'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Pacific/Noumea', 'Pacific/Noumea'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('America/Recife', 'America/Recife'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Pacific/Efate', 'Pacific/Efate'), ('Australia/Lindeman', 'Australia/Lindeman'), ('America/Jamaica', 'America/Jamaica'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Australia/Sydney', 'Australia/Sydney'), ('Etc/GMT+8', 'Etc/GMT+8'), ('Greenwich', 'Greenwich'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('UTC', 'UTC'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('America/Mendoza', 'America/Mendoza'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Australia/LHI', 'Australia/LHI'), ('America/Adak', 'America/Adak'), ('Pacific/Midway', 'Pacific/Midway'), ('Indian/Mauritius', 'Indian/Mauritius'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Africa/Maputo', 'Africa/Maputo'), ('HST', 'HST'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('Asia/Omsk', 'Asia/Omsk'), ('Indian/Cocos', 'Indian/Cocos'), ('America/Whitehorse', 'America/Whitehorse'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Europe/Monaco', 'Europe/Monaco'), ('Europe/Minsk', 'Europe/Minsk'), ('America/Resolute', 'America/Resolute'), ('Asia/Kabul', 'Asia/Kabul'), ('Africa/Accra', 'Africa/Accra'), ('America/Havana', 'America/Havana'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('America/Caracas', 'America/Caracas'), ('US/Eastern', 'US/Eastern'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('America/Montreal', 'America/Montreal'), ('GMT0', 'GMT0'), ('US/Alaska', 'US/Alaska'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Africa/Djibouti', 'Africa/Djibouti'), ('CET', 'CET'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Africa/Juba', 'Africa/Juba'), ('America/Thule', 'America/Thule'), ('Europe/Oslo', 'Europe/Oslo'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('Asia/Hovd', 'Asia/Hovd'), ('Portugal', 'Portugal'), ('Europe/Rome', 'Europe/Rome'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('America/La_Paz', 'America/La_Paz'), ('Asia/Oral', 'Asia/Oral'), ('America/Manaus', 'America/Manaus'), ('Europe/Stockholm', 'Europe/Stockholm'), ('Asia/Amman', 'Asia/Amman'), ('Africa/Harare', 'Africa/Harare'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('Asia/Bahrain', 'Asia/Bahrain'), ('Asia/Magadan', 'Asia/Magadan'), ('America/Costa_Rica', 'America/Costa_Rica'), ('Africa/Tripoli', 'Africa/Tripoli'), ('Africa/Lagos', 'Africa/Lagos'), ('Pacific/Chatham', 'Pacific/Chatham'), ('America/Lima', 'America/Lima'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Europe/Zagreb', 'Europe/Zagreb'), ('America/Ojinaga', 'America/Ojinaga'), ('America/Belem', 'America/Belem'), ('Africa/Ceuta', 'Africa/Ceuta'), ('Pacific/Fiji', 'Pacific/Fiji'), ('America/Virgin', 'America/Virgin'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('Africa/Luanda', 'Africa/Luanda'), ('Asia/Almaty', 'Asia/Almaty'), ('America/Nassau', 'America/Nassau'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('Etc/GMT0', 'Etc/GMT0'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Asia/Chungking', 'Asia/Chungking'), ('America/Montevideo', 'America/Montevideo'), ('Asia/Colombo', 'Asia/Colombo'), ('Asia/Dubai', 'Asia/Dubai'), ('US/Central', 'US/Central'), ('America/Kralendijk', 'America/Kralendijk'), ('America/Santiago', 'America/Santiago'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('Europe/Chisinau', 'Europe/Chisinau'), ('MST7MDT', 'MST7MDT'), ('Australia/Currie', 'Australia/Currie'), ('ROC', 'ROC'), ('America/Grenada', 'America/Grenada'), ('Europe/Paris', 'Europe/Paris'), ('Asia/Macau', 'Asia/Macau'), ('Africa/Libreville', 'Africa/Libreville'), ('Factory', 'Factory'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('Zulu', 'Zulu'), ('Europe/Busingen', 'Europe/Busingen'), ('Australia/South', 'Australia/South'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('America/St_Lucia', 'America/St_Lucia'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('America/Creston', 'America/Creston'), ('America/Jujuy', 'America/Jujuy'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('Africa/Abidjan', 'Africa/Abidjan'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('Israel', 'Israel'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('Etc/GMT-4', 'Etc/GMT-4'), ('MST', 'MST'), ('Singapore', 'Singapore'), ('America/Atka', 'America/Atka'), ('Asia/Kashgar', 'Asia/Kashgar'), ('Asia/Riyadh', 'Asia/Riyadh'), ('America/Martinique', 'America/Martinique'), ('America/Guyana', 'America/Guyana'), ('Etc/GMT+11', 'Etc/GMT+11'), ('America/Guayaquil', 'America/Guayaquil'), ('Mexico/General', 'Mexico/General'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Asia/Harbin', 'Asia/Harbin'), ('Iran', 'Iran'), ('America/St_Vincent', 'America/St_Vincent'), ('Australia/Hobart', 'Australia/Hobart'), ('Asia/Jayapura', 'Asia/Jayapura'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Europe/Zurich', 'Europe/Zurich'), ('America/Winnipeg', 'America/Winnipeg'), ('America/Managua', 'America/Managua'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('America/Sitka', 'America/Sitka'), ('Europe/Bucharest', 'Europe/Bucharest'), ('America/Cancun', 'America/Cancun'), ('America/Montserrat', 'America/Montserrat'), ('Africa/Asmara', 'Africa/Asmara'), ('America/St_Thomas', 'America/St_Thomas'), ('GMT', 'GMT'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('Pacific/Truk', 'Pacific/Truk'), ('America/Toronto', 'America/Toronto'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('America/Detroit', 'America/Detroit'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Asia/Tashkent', 'Asia/Tashkent'), ('Etc/GMT', 'Etc/GMT'), ('US/Hawaii', 'US/Hawaii'), ('America/Fortaleza', 'America/Fortaleza'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Europe/Uzhgorod', 'Europe/Uzhgorod'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('NZ-CHAT', 'NZ-CHAT'), ('America/Antigua', 'America/Antigua'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('Asia/Qatar', 'Asia/Qatar'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('America/Asuncion', 'America/Asuncion'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('Africa/Malabo', 'Africa/Malabo'), ('UCT', 'UCT'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('Asia/Taipei', 'Asia/Taipei'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('America/Rio_Branco', 'America/Rio_Branco'), ('Pacific/Nauru', 'Pacific/Nauru'), ('Europe/Tallinn', 'Europe/Tallinn'), ('GB', 'GB'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Africa/Kampala', 'Africa/Kampala'), ('Asia/Gaza', 'Asia/Gaza'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Europe/Prague', 'Europe/Prague'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Europe/Athens', 'Europe/Athens'), ('Etc/GMT+6', 'Etc/GMT+6'), ('Asia/Seoul', 'Asia/Seoul'), ('Iceland', 'Iceland'), ('America/Ensenada', 'America/Ensenada'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Asia/Baku', 'Asia/Baku'), ('Hongkong', 'Hongkong'), ('Africa/Asmera', 'Africa/Asmera'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('Etc/GMT-11', 'Etc/GMT-11'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('America/Nipigon', 'America/Nipigon'), ('Etc/UTC', 'Etc/UTC'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('America/Eirunepe', 'America/Eirunepe'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Asia/Tomsk', 'Asia/Tomsk'), ('America/Iqaluit', 'America/Iqaluit'), ('Pacific/Niue', 'Pacific/Niue'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('America/Anguilla', 'America/Anguilla'), ('Pacific/Ponape', 'Pacific/Ponape'), ('W-SU', 'W-SU'), ('Europe/Dublin', 'Europe/Dublin'), ('Europe/Volgograd', 'Europe/Volgograd'), ('CST6CDT', 'CST6CDT'), ('America/Nome', 'America/Nome'), ('Eire', 'Eire'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('America/Cordoba', 'America/Cordoba'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('America/Goose_Bay', 'America/Goose_Bay'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Africa/Mbabane', 'Africa/Mbabane'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('Universal', 'Universal'), ('Etc/GMT+10', 'Etc/GMT+10'), ('America/Mexico_City', 'America/Mexico_City'), ('Europe/Kiev', 'Europe/Kiev'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Cuba', 'Cuba'), ('Asia/Tehran', 'Asia/Tehran'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('America/Menominee', 'America/Menominee'), ('Asia/Yerevan', 'Asia/Yerevan'), ('Europe/Brussels', 'Europe/Brussels'), ('Asia/Bishkek', 'Asia/Bishkek'), ('America/Chihuahua', 'America/Chihuahua'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('Etc/GMT-7', 'Etc/GMT-7'), ('America/Curacao', 'America/Curacao'), ('America/Regina', 'America/Regina'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('Canada/Mountain', 'Canada/Mountain'), ('Asia/Kolkata', 'Asia/Kolkata'), ('Australia/West', 'Australia/West'), ('America/Bahia', 'America/Bahia'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('Brazil/East', 'Brazil/East'), ('Asia/Shanghai', 'Asia/Shanghai'), ('Africa/Freetown', 'Africa/Freetown'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Pacific/Johnston', 'Pacific/Johnston'), ('America/Merida', 'America/Merida'), ('Etc/GMT+0', 'Etc/GMT+0'), ('Africa/Bangui', 'Africa/Bangui'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('America/El_Salvador', 'America/El_Salvador'), ('Africa/Niamey', 'Africa/Niamey'), ('America/Catamarca', 'America/Catamarca'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Navajo', 'Navajo'), ('Europe/London', 'Europe/London'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('Europe/Riga', 'Europe/Riga'), ('US/Mountain', 'US/Mountain'), ('Africa/Algiers', 'Africa/Algiers'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Pacific/Majuro', 'Pacific/Majuro'), ('EST', 'EST'), ('Africa/Douala', 'Africa/Douala'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('America/Belize', 'America/Belize'), ('Indian/Christmas', 'Indian/Christmas'), ('America/Yellowknife', 'America/Yellowknife'), ('Asia/Aden', 'Asia/Aden'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Asia/Karachi', 'Asia/Karachi'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Atlantic/Canary', 'Atlantic/Canary'), ('America/Vancouver', 'America/Vancouver'), ('Africa/Tunis', 'Africa/Tunis'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Asia/Damascus', 'Asia/Damascus'), ('US/Arizona', 'US/Arizona'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Pacific/Saipan', 'Pacific/Saipan'), ('Australia/Adelaide', 'Australia/Adelaide'), ('Europe/Helsinki', 'Europe/Helsinki'), ('America/St_Johns', 'America/St_Johns'), ('Canada/Yukon', 'Canada/Yukon'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Pacific/Kanton', 'Pacific/Kanton'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Etc/UCT', 'Etc/UCT'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('Europe/Berlin', 'Europe/Berlin'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('Asia/Katmandu', 'Asia/Katmandu'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Asia/Bangkok', 'Asia/Bangkok'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('Africa/Bamako', 'Africa/Bamako'), ('America/Edmonton', 'America/Edmonton'), ('Chile/Continental', 'Chile/Continental'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('Indian/Reunion', 'Indian/Reunion'), ('ROK', 'ROK'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('America/Scoresbysund', 'America/Scoresbysund'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('Australia/Victoria', 'Australia/Victoria'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('America/Boa_Vista', 'America/Boa_Vista'), ('Turkey', 'Turkey'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Asia/Urumqi', 'Asia/Urumqi'), ('America/Guadeloupe', 'America/Guadeloupe'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Pacific/Easter', 'Pacific/Easter'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Etc/GMT-13', 'Etc/GMT-13'), ('America/Maceio', 'America/Maceio'), ('America/Denver', 'America/Denver'), ('US/Samoa', 'US/Samoa'), ('Libya', 'Libya'), ('Etc/GMT+7', 'Etc/GMT+7'), ('EST5EDT', 'EST5EDT'), ('America/Mazatlan', 'America/Mazatlan'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Africa/Casablanca', 'Africa/Casablanca'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Asia/Muscat', 'Asia/Muscat'), ('GMT-0', 'GMT-0'), ('America/Miquelon', 'America/Miquelon'), ('Europe/Skopje', 'Europe/Skopje'), ('US/Pacific', 'US/Pacific'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Pacific/Samoa', 'Pacific/Samoa'), ('Africa/Dakar', 'Africa/Dakar'), ('America/Rosario', 'America/Rosario'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('Asia/Qostanay', 'Asia/Qostanay'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('Africa/Kigali', 'Africa/Kigali'), ('Asia/Tokyo', 'Asia/Tokyo'), ('Etc/GMT-2', 'Etc/GMT-2'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('America/Knox_IN', 'America/Knox_IN'), ('Etc/Universal', 'Etc/Universal'), ('America/Inuvik', 'America/Inuvik'), ('America/Guatemala', 'America/Guatemala'), ('America/Bogota', 'America/Bogota'), ('America/Indianapolis', 'America/Indianapolis'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Europe/Moscow', 'Europe/Moscow'), ('Brazil/Acre', 'Brazil/Acre'), ('PRC', 'PRC'), ('Etc/GMT-3', 'Etc/GMT-3'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('Pacific/Guam', 'Pacific/Guam'), ('Asia/Dhaka', 'Asia/Dhaka'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Etc/GMT+9', 'Etc/GMT+9'), ('Asia/Manila', 'Asia/Manila'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('America/Chicago', 'America/Chicago'), ('Indian/Chagos', 'Indian/Chagos'), ('Europe/Samara', 'Europe/Samara'), ('Asia/Dili', 'Asia/Dili'), ('Africa/Cairo', 'Africa/Cairo'), ('Australia/Perth', 'Australia/Perth'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Europe/Tirane', 'Europe/Tirane'), ('Europe/Simferopol', 'Europe/Simferopol'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('Japan', 'Japan'), ('Etc/GMT-5', 'Etc/GMT-5'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('America/Paramaribo', 'America/Paramaribo'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('America/Araguaina', 'America/Araguaina'), ('Poland', 'Poland'), ('Asia/Baghdad', 'Asia/Baghdad'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Africa/Maseru', 'Africa/Maseru'), ('America/Lower_Princes', 'America/Lower_Princes'), ('Africa/Banjul', 'Africa/Banjul'), ('Australia/North', 'Australia/North'), ('America/Nuuk', 'America/Nuuk'), ('Asia/Atyrau', 'Asia/Atyrau'), ('America/Barbados', 'America/Barbados'), ('Europe/Kyiv', 'Europe/Kyiv'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('Asia/Dacca', 'Asia/Dacca'), ('NZ', 'NZ'), ('America/Metlakatla', 'America/Metlakatla'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('America/Phoenix', 'America/Phoenix'), ('America/Cayman', 'America/Cayman'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('EET', 'EET'), ('Australia/Queensland', 'Australia/Queensland'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('America/Swift_Current', 'America/Swift_Current'), ('Africa/Lusaka', 'Africa/Lusaka'), ('Asia/Calcutta', 'Asia/Calcutta'), ('Etc/Greenwich', 'Etc/Greenwich'), ('PST8PDT', 'PST8PDT'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('Asia/Istanbul', 'Asia/Istanbul'), ('America/Juneau', 'America/Juneau'), ('GMT+0', 'GMT+0'), ('America/Dawson', 'America/Dawson'), ('US/Aleutian', 'US/Aleutian'), ('Europe/Andorra', 'Europe/Andorra'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('America/Panama', 'America/Panama'), ('Etc/GMT-1', 'Etc/GMT-1'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('America/Anchorage', 'America/Anchorage'), ('Europe/Vienna', 'Europe/Vienna'), ('US/East-Indiana', 'US/East-Indiana'), ('Africa/Lome', 'Africa/Lome'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('Asia/Brunei', 'Asia/Brunei'), ('Europe/Nicosia', 'Europe/Nicosia'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('America/Atikokan', 'America/Atikokan'), ('Pacific/Palau', 'Pacific/Palau'), ('Jamaica', 'Jamaica'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Europe/Sofia', 'Europe/Sofia'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('Europe/Vatican', 'Europe/Vatican'), ('Etc/GMT+5', 'Etc/GMT+5'), ('Asia/Beirut', 'Asia/Beirut'), ('Kwajalein', 'Kwajalein'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('America/Glace_Bay', 'America/Glace_Bay'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Asia/Macao', 'Asia/Macao'), ('America/Boise', 'America/Boise'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('Australia/ACT', 'Australia/ACT'), ('Australia/NSW', 'Australia/NSW'), ('Pacific/Apia', 'Pacific/Apia'), ('America/Yakutat', 'America/Yakutat'), ('America/Cuiaba', 'America/Cuiaba'), ('America/Marigot', 'America/Marigot'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Asia/Yangon', 'Asia/Yangon'), ('WET', 'WET'), ('US/Michigan', 'US/Michigan'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Asia/Rangoon', 'Asia/Rangoon'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Asia/Hebron', 'Asia/Hebron'), ('Canada/Atlantic', 'Canada/Atlantic'), ('Asia/Saigon', 'Asia/Saigon'), ('Indian/Comoro', 'Indian/Comoro'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('Pacific/Wallis', 'Pacific/Wallis'), ('Africa/Windhoek', 'Africa/Windhoek'), ('Europe/Madrid', 'Europe/Madrid'), ('Europe/Budapest', 'Europe/Budapest'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Africa/Bissau', 'Africa/Bissau'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Etc/GMT-0', 'Etc/GMT-0'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('America/Santarem', 'America/Santarem'), ('Europe/Saratov', 'Europe/Saratov'), ('Canada/Eastern', 'Canada/Eastern'), ('Indian/Mahe', 'Indian/Mahe'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Indian/Mayotte', 'Indian/Mayotte'), ('Australia/Tasmania', 'Australia/Tasmania'), ('Europe/Kirov', 'Europe/Kirov'), ('Europe/Belfast', 'Europe/Belfast'), ('America/Shiprock', 'America/Shiprock'), ('America/Hermosillo', 'America/Hermosillo'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Indian/Maldives', 'Indian/Maldives'), ('Asia/Barnaul', 'Asia/Barnaul'), ('America/Tijuana', 'America/Tijuana'), ('Asia/Jakarta', 'Asia/Jakarta'), ('America/Pangnirtung', 'America/Pangnirtung'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('Europe/Jersey', 'Europe/Jersey'), ('Etc/Zulu', 'Etc/Zulu'), ('America/Matamoros', 'America/Matamoros'), ('Etc/GMT-6', 'Etc/GMT-6'), ('America/Aruba', 'America/Aruba'), ('Canada/Central', 'Canada/Central'), ('America/Moncton', 'America/Moncton'), ('MET', 'MET'), ('America/Grand_Turk', 'America/Grand_Turk')], default='Europe/Moscow', verbose_name='Часовой пояс')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='ClientAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator_code', models.CharField(max_length=6)),
            ],
            options={
                'verbose_name': 'Атрибут клиента',
                'verbose_name_plural': 'Атрибуты клиентов',
            },
        ),
        migrations.CreateModel(
            name='MailingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Дата и время начала рассылки')),
                ('end_time', models.DateTimeField(verbose_name='Дата и время окончания рассылки')),
                ('message_text', models.TextField(verbose_name='Текст сообщения')),
                ('client_filter', models.ManyToManyField(related_name='mailing_settings', to='dto.clientattribute', verbose_name='Фильтр клиентов')),
            ],
            options={
                'verbose_name': 'Настройка рассылки',
                'verbose_name_plural': 'Настройки рассылок',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('status', models.CharField(choices=[('Sent', 'Отправлено'), ('Failed', 'Ошибка')], default='Sent', max_length=10, verbose_name='Статус')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dto.client', verbose_name='Клиент')),
                ('mailing_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dto.mailingsettings', verbose_name='Настройка рассылки')),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомления',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название тега')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='NotificationStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Sent', 'Отправлено'), ('Failed', 'Ошибка')], max_length=10, verbose_name='Статус')),
                ('sent_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время отправки')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dto.client', verbose_name='Клиент')),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dto.notification', verbose_name='Уведомление')),
            ],
            options={
                'verbose_name': 'Статистика уведомления',
                'verbose_name_plural': 'Статистика уведомлений',
            },
        ),
        migrations.AddField(
            model_name='clientattribute',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='dto.tag'),
        ),
        migrations.AddField(
            model_name='client',
            name='tags',
            field=models.ManyToManyField(to='dto.tag', verbose_name='Теги'),
        ),
    ]
