import gzip  # Библиотека для работы с gz
import json
from datetime import datetime
from pathlib import Path
import time
from time import gmtime, strftime
# Подключение к БД по:
import mysql.connector

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

columns = ", ".join(column_for_insert)
placeholders = ", ".join(["%s"] * len(column_for_insert))

print(columns)
print(placeholders)
#
# def db_insert(host_name: str,user_name: str,password_name: str,database_name: str,raise_exception_name: str,table_name: str, columns_name: str, values: str):
#     print(host_name,user_name,password_name,database_name,raise_exception_name,table_name,columns_name,values)
#     """
#     db_insert(host, user, password, database, raise_exception, table_name from db, columns_name db, values for input)
#
#     create connection to db using input parametrs
#     create cursor
#     create str to execute sql with columns_name and values
#     insert str to cursor and commit
#     close cursor and close connection
#     1 sec to new commit
#     if exception print DB error with error message and time
#
#     """
#     try:
#         cnx = mysql.connector.connect(host = host_name, user = user_name, password = password_name, database = database_name, raise_on_warnings = raise_exception_name)
#         cursor = cnx.cursor()
#         print(f"INSERT INTO `{table_name}`({columns_name}) VALUES ({values});")
#         cursor.execute(f"INSERT INTO `{table_name}`({columns_name}) VALUES ({values});") # TODO регэскп чтобы собрать нужную строку в колумн и вэлью
#         cnx.commit()
#         cursor.close()
#         cnx.close()
#         time.sleep(1)
#     except Exception as e:
#         print("DB error", datetime.now(), e)
#     return None
#
#
# print(db_insert('*.beget.tech','*_recruti','r3Cr7t1',
#                           '*_recruti',True, 'results','`id`,`linkedin_username`,`industry`,`job_title`',f'{str_to_commit[:-2]}'))
#                 db_insert('*.beget.tech','*_recruti','r3Cr7t1',
#                           '*_recruti',True, 'results','`id`,`linkedin_username`,`industry`,`job_title`',f'{str_to_commit[:-2]}')
