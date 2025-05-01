"""
Main module for the application.

This module contains the main functionality of the application.
"""

import glob
import gzip
import json
import os
from datetime import datetime
from pathlib import Path
from time import gmtime, strftime

import mysql.connector
import logging

config = {
    'host': '*.beget.tech',
    'user': '*_recruti',
    'password': 'r3Cr7t1',
    'database': '*_recruti',
    'raise_on_warnings': True
}

formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

"""A class that serves as an example.

    This class demonstrates how to write proper docstrings
    that Sphinx can parse into documentation.

    Attributes:
        name (str): The name of the example.
        value (int): The value of the example.
    """


def db_insert(host_name: str, user_name: str, password_name: str, database_name: str, raise_exception_name: str,
              table_name: str, columns_name: str, values: str):
    logger.info(host_name, user_name, password_name, database_name, raise_exception_name, table_name, columns_name, values)
    logger.info("host_name: %s user_name: %s database_name: %s", host_name, user_name, database_name)
    """db_insert(host, user, password, database, raise_exception, table_name from db, columns_name db, values for input)

    create connection to db using input parametrs
    create cursor
    create str to execute sql with columns_name and values
    insert str to cursor and commit
    close cursor and close connection
    1 sec to new commit
    if exception print DB error with error message and time

    A class that serves as an example.
    
    This class demonstrates how to write proper docstrings
    that Sphinx can parse into documentation.
    
    Attributes:
        name (str): The name of the example.
        value (int): The value of the example.
    
    """
    try:
        cnx = mysql.connector.connect(host=host_name, user=user_name, password=password_name, database=database_name,
                                      raise_on_warnings=raise_exception_name)
        cursor = cnx.cursor()
        print(f"INSERT INTO `{table_name}`({columns_name}) VALUES ({values});")
        cursor.execute(
            f"INSERT INTO `{table_name}`({columns_name}) VALUES ({values});")  # TODO регэскп чтобы собрать нужную строку в колумн и вэлью
        cnx.commit()  # TODO добавить соответствие columns_names and values
        cursor.close()
        cnx.close()
        return True
    except Exception as e:
        print("DB error", datetime.now(), e)
        return False




directory_path = "K:\gz"  # TODO сделать функцию + описание
try:
    Path(directory_path).exists()  # Проверим папку
    print("Directory exists")
    gz_files = glob.glob(os.path.join(directory_path, "*.gz"))
    print(gz_files)
except:
    print("Directory does not exist")


def advanced_permission_check(file_path: str):
    return None
    # TODO навесить блокировку файла


# Создадим списки для проверки
check_region = ['Russia', 'Belarus', 'Kazakhstan', 'Armenia', 'Turkey', 'Cyprus', 'Dubai', 'Poland', 'Uzbekistan',
                'Georgia', 'russia', 'belarus', 'kazakhstan', 'armenia', 'turkey', 'cyprus', 'dubai', 'poland',
                'uzbekistan', 'georgia']
check_languages = ['Russian', 'Turkish', 'Polish', 'Uzbek', 'Georgian', 'Armenian', 'russian', 'turkish', 'polish',
                   'uzbek', 'georgian', 'armenian']
# формат для инсерта в БД
column_for_insert = ['id', 'full_name', 'first_name', 'middle_initial', 'middle_name', 'last_name', 'gender',
                     'birth_year',
                     'birth_date', 'linkedin_url', 'linkedin_username', 'linkedin_id', 'facebook_url',
                     'facebook_username',
                     'facebook_id', 'twitter_url', 'twitter_username', 'github_url', 'github_username', 'work_email',
                     'mobile_phone', 'industry', 'job_title', 'job_title_role', 'job_title_sub_role',
                     'job_title_levels',
                     'job_company_id', 'job_company_name', 'job_company_website', 'job_company_size',
                     'job_company_founded',
                     'job_company_industry', 'job_company_linkedin_url', 'job_company_linkedin_id',
                     'job_company_facebook_url',
                     'job_company_twitter_url', 'job_company_location_name', 'job_company_location_locality',
                     'job_company_location_metro', 'job_company_location_region', 'job_company_location_geo',
                     'job_company_location_street_address', 'job_company_location_address_line_2',
                     'job_company_location_postal_code', 'job_company_location_country',
                     'job_company_location_continent',
                     'job_last_updated', 'job_start_date', 'job_summary', 'location_name', 'location_locality',
                     'location_metro',
                     'location_region', 'location_country', 'location_continent', 'location_street_address',
                     'location_address_line_2', 'location_postal_code', 'location_geo', 'location_last_updated',
                     'linkedin_connections', 'inferred_salary', 'inferred_years_experience', 'summary', 'phone_numbers',
                     'emails',
                     'interests', 'skills', 'location_names', 'regions', 'countries', 'street_addresses', 'experience',
                     'education', 'profiles', 'certifications', 'languages', 'version_status']
values_for_insert = [str('id'), str('full_name'), str('first_name'), str('middle_initial'), str('middle_name'),
                     str('last_name'), str('gender'), str('birth_year'),
                     str('birth_date'), 'linkedin_url ', str('linkedin_username'), str('linkedin_id'), 'facebook_url ',
                     str('facebook_username'),
                     str('facebook_id'), 'twitter_url ', str('twitter_username'), 'github_url ', str('github_username'),
                     str('work_email'),
                     str('mobile_phone'), str('industry'), str('job_title'), str('job_title_role'),
                     str('job_title_sub_role'), 'job_title_levels ',
                     str('job_company_id'), str('job_company_name'), 'job_company_website ', str('job_company_size'),
                     str('job_company_founded'),
                     str('job_company_industry'), 'job_company_linkedin_url ', str('job_company_linkedin_id'),
                     'job_company_facebook_url ',
                     'job_company_twitter_url', str('job_company_location_name'), str('job_company_location_locality'),
                     str('job_company_location_metro'), str('job_company_location_region'),
                     str('job_company_location_geo'),
                     str('job_company_location_street_address'), str('job_company_location_address_line_2'),
                     str('job_company_location_postal_code'), str('job_company_location_country'),
                     str('job_company_location_continent'),
                     str('job_last_updated'), str('job_start_date'), str('job_summary'), str('location_name'),
                     str('location_locality'), str('location_metro'),
                     str('location_region'), str('location_country'), str('location_continent'),
                     str('location_street_address'),
                     str('location_address_line_2'), str('location_postal_code'), str('location_geo'),
                     str('location_last_updated'),
                     'linkedin_connections ', str('inferred_salary'), 'inferred_years_experience ', str('summary'),
                     'phone_numbers ', 'emails ',
                     'interests ', 'skills ', 'location_names ', 'regions ', 'countries ', 'street_addresses ',
                     'experience ',
                     'education ', 'profiles ', 'certifications ', 'languages ', 'version_status ']

line_number = 0
result = []
for gz_file in gz_files:
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()), gz_file)
    with (gzip.open(gz_file, 'r') as file_input):
        for line in file_input:
            python_obj = json.loads(line)
            line_number += 1
            # print(line)
            count_for_pop = 0  # Счетчик по которому будем удалять
            # Проверяем есть ли упоминания нужных стран и языков
            if python_obj['location_name'] in check_region:  # TODO регэксп будет тут
                count_for_pop = count_for_pop + 1
            if python_obj['location_region'] in check_region:
                count_for_pop = count_for_pop + 1
            if python_obj['location_country'] in check_region:
                count_for_pop = count_for_pop + 1
            if python_obj['location_names'] in check_region:
                count_for_pop = count_for_pop + 1
            if python_obj['regions'] in check_region:
                count_for_pop = count_for_pop + 1
            if python_obj['countries'] in check_region:
                count_for_pop = count_for_pop + 1
            if python_obj['languages'] in check_languages:
                count_for_pop = count_for_pop + 1
            # Если нашли - записали в переменную
            if count_for_pop > 0:
                result.append(str(line_number) + ' ' + str(python_obj))
                str_to_commit = ''
                for name_column in column_for_insert:
                    # print(name_column, type(python_obj[f'{name_column}']))
                    # TODO
                    # Заменить values_for_insert c листа на str и append на +
                    if name_column == 'id':
                        str_to_commit = str_to_commit + "'" + str(python_obj[name_column]) + "', "
                    elif name_column == 'linkedin_username':
                        str_to_commit = str_to_commit + "'" + str(python_obj[name_column]) + "', "
                    elif name_column == 'industry':
                        str_to_commit = str_to_commit + "'" + str(python_obj[name_column]) + "', "
                    elif name_column == 'job_title':
                        str_to_commit = str_to_commit + "'" + str(python_obj[name_column]).replace(',', '').replace("'",
                                                                                                                    '') + "', "
                        """
                    elif name_column == 'job_title_role':
                        str_to_commit = str_to_commit + "'" + str(python_obj[name_column]).replace(',','').replace('None','[]') + "', "
                    elif name_column == 'job_title_sub_role':
                        str_to_commit = str_to_commit + "'" + str(python_obj[name_column]).replace(',','').replace('None','[]') + "', "
                        """
                print(db_insert('*.beget.tech', '*_recruti', 'r3Cr7t1',
                                '*_recruti', True, 'results', '`id`,`linkedin_username`,`industry`,`job_title`',
                                f'{str_to_commit[:-2]}'))
                db_insert('*.beget.tech', '*_recruti', 'r3Cr7t1',
                          '*_recruti', True, 'results', '`id`,`linkedin_username`,`industry`,`job_title`',
                          f'{str_to_commit[:-2]}')

                """
                try:
                    cnx = mysql.connector.connect(**config)
                    cursor = cnx.cursor()
                    sql = f"INSERT INTO `results`(`id`,`linkedin_username`,`industry`,`job_title`) VALUES ({str_to_commit[:-2]});"
                    # sql = f"INSERT INTO `results`(`{columns_str}`) VALUES ({values_str.replace('"',"'").replace("\\","")});"
                    cursor.execute(sql)

                        # Закрываем подключение
                    cnx.commit()
                    cursor.close()
                    cnx.close()
                    time.sleep(1)
                except Exception as e:
                    print("DB error", datetime.now(), e)
                    
                    special_characters = ["!", "#", "$", "%", "&", "*"]
                    for final_str_without_special_characters in special_characters:
                        str_to_commit = str_to_commit[:-2].replace(final_str_without_special_characters,'')
                    cnx = mysql.connector.connect(**config)
                    cursor = cnx.cursor()
                    sql = f"INSERT INTO `results`(`id`,`linkedin_username`,`industry`,`job_title`) VALUES ({str_to_commit[:-2]});"
                    # sql = f"INSERT INTO `results`(`{columns_str}`) VALUES ({values_str.replace('"',"'").replace("\\","")});"
                    print(sql)
                    cursor.execute(sql)

                    # Закрываем подключение
                    cnx.commit()
                    cursor.close()
                    cnx.close()
                    time.sleep(1)
                   
                    if type(python_obj[f'{name_column}']) != 'str':
                        values_for_insert.append(json.dumps(python_obj[f'{name_column}']) )
                    elif type(python_obj[f'{name_column}']) == 'int':
                        values_for_insert.append(int(python_obj[f'{name_column}']))
                    else:
                        values_for_insert.append(python_obj[f'{name_column}'])
                    print(values_for_insert)
                    # values_for_insert.append(python_obj[f'{name_column}'])
                    columns_str = '`, `'.join(column_for_insert)
                    values_str = ', '.join(values_for_insert)
                try:
                    cnx = mysql.connector.connect(**config)
                    cursor = cnx.cursor()
                    sql = f"INSERT INTO `results`(`{columns_str}`) VALUES ({values_str});"
                    #sql = f"INSERT INTO `results`(`{columns_str}`) VALUES ({values_str.replace('"',"'").replace("\\","")});"
                    print(sql)
                    cursor.execute(sql)

                    # Закрываем подключение
                    cnx.commit()
                    cursor.close()
                    cnx.close()
                except Exception as e:
                    print("DB error", datetime.now(), e)
                

    # name_gz_file = str(gz_file)[6:16]

            #line.values()

# Продолжаем подключение к БД
try :
    cnx = mysql.connector.connect(**config)
except Exception as e:
    print("DB error", datetime.now(), e)

cursor = cnx.cursor()
sql = "SELECT * FROM linkedin_profiles"

cursor.execute(sql)
res = cursor.fetchall()
print(res)
cnx.commit()
cursor.close()
cnx.close()


with open(f"result_{name_gz_file}", 'w', encoding="utf-8") as file_output:
    file_output.write(str(result))
"""
