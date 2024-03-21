import logging
import os
import boto3
from botocore.exceptions import ClientError
import constants


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

    score = matrix[len(str1)][len(str2)]
    # Normalize the distance by dividing by the maximum length of the strings
    max_length = max(len(str1), len(str2))
    normalized_distance = score / max_length
    # Return the normalized  Levenshtein distance
    return normalized_distance


def calculate_distance(actual, array_values):
    # calculate the distance score for every array value wtr the actual string
    scores = [levenshtein_distance(actual, value) for value in array_values]
    # Zip the arrays together
    combined = list(zip(scores, array_values))
    # Sort the zipped array based on scores (in ascending order - from the closer(0))
    combined.sort(reverse=False)
    # Unzip the sorted array into: sorted_scores, sorted_values
    sorted_scores, sorted_values = zip(*combined)
    return sorted_values, sorted_scores


def get_closer_name(actual, array_values, treshold=0.6):
    values, scores = calculate_distance(actual, array_values)
    # return only if the name is real, cant be another complitely different one.
    return values[0] if scores[0]>treshold else None


def get_info_from_anime(serched_anime):
    for anime in constants.AIRING_ANIME:
        if anime["name"] == serched_anime:
            return anime
    return None


def get_anime_feed(rating, follower):
    max_rating = max([anime['rating'] for anime in constants.AIRING_ANIME])
    max_follower = max([anime['follower'] for anime in constants.AIRING_ANIME])
    result = ((rating*100)/max_rating) + ((follower*100)/max_follower)
    if result>=90:
        return "Mi sa che è molto figo"
    elif result>=70 and result<90:
        return "Anime tra i top!"
    elif result>=40 and result<70:
        return "buono, si può vedere!"
    else:
        return "Lascia stare è una merda!"
    
    
    
    