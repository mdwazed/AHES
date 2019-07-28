
def read_text():
    """
        this module accomplish all text reading related activities
        using google cloud vision api
    """

    from google.cloud import vision
    import os
    import io

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="ahes-google-credential.json"
    client = vision.ImageAnnotatorClient()

    path = 'grader/google_cloud_vision/tanvir_text.jpg'
    with io.open(path, 'rb') as image_file:
            content = image_file.read()

    image = vision.types.Image(content=content)
    resp = client.text_detection(image=image)
    resp_text = resp.text_annotations[0].description
    resp_text = resp_text.replace('\n', '')
    resp_text = resp_text.replace('\t', '')
    return resp_text
    # print('\n'.join([d.description for d in resp.text_annotations]))
    # print([d.description for d in resp.text_annotations[0]])


if __name__ == "__main__":
    text = read_text()
    print(text)