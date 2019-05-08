#!/bin/python


template = """location ~ ^<PATH>$ {
        autoindex on;
        auth_basic           'LVL<INT>';
        auth_basic_user_file /var/www/levels/level<INT>;
    }"""


levels = 10
start_path = "\/\w*\/"

aggregated_locations = []

for r in range(2,levels+1):

    # Put PATH into template
    prepared_template = template.replace("<PATH>",start_path)

    # Change level number
    prepared_template = prepared_template.replace("<INT>", str(r))

    aggregated_locations.append(prepared_template + '\n')

    start_path += '\w*\/'


with open('data/sezaam.conf.tmp') as file:
    nginx_template = file.read()

    final_config = nginx_template.replace("<LOCATIONS>", ''.join(reversed(aggregated_locations)))


with open('sezaam.conf','w') as file:
    file.write(final_config)

