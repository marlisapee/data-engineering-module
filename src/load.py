import pandas
from auth import auth
from s3_operations import upload_file

def upload(object_key):
  chances = pandas.read_csv('./data/input/admission_chances.csv')
  scores = pandas.read_csv('./data/input/admission_scores.csv')

  chances_dataframe = pandas.DataFrame(chances)
  scores_dataframe = pandas.DataFrame(scores)

  merged_data = chances_dataframe.merge(scores_dataframe, how='inner', on='Serial_Number')
  cleaned_data = merged_data.dropna()
  print(cleaned_data)
  cleaned_data.to_csv('./data/input/final_cleaned_data.csv')
  upload_file(object_key, 'final_cleaned_data.csv')


response = upload('mpeemv2')
print(response)