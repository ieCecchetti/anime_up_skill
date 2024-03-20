import logging
import os
import boto3
from botocore.exceptions import ClientError


def create_presigned_url(object_name):
    """Generate a presigned URL to share an S3 object with a capped expiration of 60 seconds

    :param object_name: string
    :return: Presigned URL as string. If error, returns None.
    """
    s3_client = boto3.client('s3',
                             region_name=os.environ.get('S3_PERSISTENCE_REGION'),
                             config=boto3.session.Config(signature_version='s3v4',s3={'addressing_style': 'path'}))
    try:
        bucket_name = os.environ.get('S3_PERSISTENCE_BUCKET')
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=60*1)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response


def levenshtein_distance(str1, str2):
    # Initialize a matrix to store distances
    matrix = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

    # Initialize the first row and column
    for i in range(len(str1) + 1):
        matrix[i][0] = i
    for j in range(len(str2) + 1):
        matrix[0][j] = j

    # Calculate distances
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            matrix[i][j] = min(matrix[i - 1][j] + 1,      # deletion
                               matrix[i][j - 1] + 1,      # insertion
                               matrix[i - 1][j - 1] + cost)  # substitution

    # Return the Levenshtein distance
    return matrix[len(str1)][len(str2)]


def calculate_distance(actual, array_values):
    # calculate the distance score for every array value wtr the actual string
    score = [levenshtein_distance(actual, value) for value in array_values]
    # Zip the arrays together
    combined = list(zip(scores, values))
    # Sort the zipped array based on scores (in descending order)
    combined.sort(reverse=True)
    # Unzip the sorted array
    sorted_scores, sorted_values = zip(*combined)
    #  return the sorted array from the closest distance string to the farest one
    return sorted_values
    